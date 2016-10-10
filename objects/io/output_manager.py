from time import gmtime, strftime

import falcon

from objects.io.response_codes import ResponseCodes


class OutputManager(object):
    def __init__(self):
        self.status = ResponseCodes.INTERNAL_SERVER_ERROR['internalError']
        self.data = {}
        self.__update_timestamp()

    def output(self, **kwargs):
        r"""Builds the output and returns a valid JSON

        :param \**kwargs:
            See below

        :Keyword Arguments:
            * *status* (``int``) --
              Status code to return. Appropriate status message is picked automatically.
            * *data* (``dict``) --
              Output body as dictionary.

        """
        if 'status' in kwargs:
            self.__set_status(kwargs['status'])

        if 'data' in kwargs:
            self.__set_data(kwargs['data'])

        self.__update_timestamp()

        _response = {
            'status': self.status,
            'data': self.data,
            'timestamp': self.timestamp
        }

        return _response

    def __set_status(self, pointer):
        self.status = {
            'code': getattr(falcon, 'HTTP_' + str(pointer[0])),
            'description': pointer[1]
        }

    def __set_data(self, data):
        self.data = data

    def __update_timestamp(self):
        self.timestamp = strftime("%Y-%m-%d %H:%M:%S %Z", gmtime())
