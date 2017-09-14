import re


class Transformer(object):
    def __init__(self, template):
        self.template = template

    def has_placeholders(self, template_str):
        """Return true if the template's string has placeholders in the format ${attr}"""
        # import pdb; pdb.set_trace()
        matches = re.findall(r"\$\{\w+\}", template_str)
        if matches:
            return matches
        return False

    def replace_with_attrs(self, matched_placeholders, key, source):
        compiled_key = key
        for placeholder in matched_placeholders:
            compiled_key = compiled_key.replace(placeholder, "source.%s" % placeholder[2:-1])
        try:
            result = eval(compiled_key)
        except AttributeError:
            raise Exception('Invalid template %s' % key)
        except SyntaxError:
            raise Exception('Failed While running template %s' % key)

        return result

    def __call__(self, source):
        target = dict()
        for key in self.template:
            key_formatter = self.template[key]
            matched_placeholders = False
            if type(key_formatter) is str:
                matched_placeholders = self.has_placeholders(key_formatter)
            if matched_placeholders:
                target[key] = self.replace_with_attrs(matched_placeholders, key_formatter, source)
            else:
                target[key] = key_formatter
        return target
