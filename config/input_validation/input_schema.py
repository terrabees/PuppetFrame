from voluptuous import Schema, Optional, Required, All, Length, Match

from config.input_validation.input_validators import InputValidators


class InputSchema(object):
    def __init__(self):
        # ## Account ## #

        self.create_account = Schema({
            Required('email'): InputValidators.email(),
            Required('first_name'): All(str, Length(min=2)),
            Required('last_name'): All(str, Length(min=2)),
            Required('password'): All(str, Length(min=8))
        })

        self.update_account = Schema({
            Optional('email'): InputValidators.email(),
            Optional('first_name'): All(str, Length(min=2)),
            Optional('last_name'): All(str, Length(min=2)),
            Optional('password'): All(str, Length(min=8))
        })

        # ## Session ## #

        self.create_session = Schema({
            Required('email'): InputValidators.email(),
            Required('password'): str
        })
