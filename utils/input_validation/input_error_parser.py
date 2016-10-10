from config.input_validation.error_messages import ErrorMessages


class InputErrorParser(object):
    def __init__(self):
        self.default_messages = ErrorMessages.default
        self.result = {}

    @staticmethod
    def __get_type(error):
        t = str(type(error))
        return t[t.find(".") + 1:t.find("'>")]

    @staticmethod
    def __get_field(error):
        error = str(error)
        return error[error.find("['"):]

    @staticmethod
    def __get_message(error):
        error = str(error).split(' @ ')
        return error[0]

    def build_message(self, error):
        if self.__get_type(error) in self.default_messages:
            return {
                self.__get_field(error): self.default_messages[self.__get_type(error)]
            }
        else:
            return {
                self.__get_field(error): self.__get_message(error)
            }

    def translate_errors(self, errors):
        for error in errors.errors:
            self.result.update(self.build_message(error))

        return self.result
