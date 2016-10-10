import re

from voluptuous import Invalid


class InputValidators:
    @staticmethod
    def email(msg=None):
        def f(v):
            if re.match("[\w\.\-\+]*@[\w\.\-]*\.\w+", str(v)):
                return str(v)
            else:
                raise Invalid(msg or "Incorrect email address")

        return f
