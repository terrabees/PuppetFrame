from voluptuous import MultipleInvalid

from config.input_validation.input_schema import InputSchema


class InputValidator(object):
    def __init__(self, schema_name):
        _input_schema = InputSchema()
        self.schema = getattr(_input_schema, schema_name)

    def validate(self, payload):
        """
        Validates given inputs against predefined schema.

        :param payload: User inputs
        :return: Boolean
        """
        try:
            self.schema(payload)
            return True

        except MultipleInvalid as error:
            raise error
