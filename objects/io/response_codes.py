class ResponseCodes(object):
    OK = {
        'success': [200, 'success']
    }

    MOVED_PERMANENTLY = {
        'movedPermanently': [301, 'movedPermanently']
    }

    SEE_OTHER = {
        'seeOther': [303, 'seeOther'],
        'mediaDownloadRedirect': [303, 'mediaDownloadRedirect']
    }

    NOT_MODIFIED = {
        'notModified': [304, 'notModified']
    }

    TEMPORARY_REDIRECT = {
        'temporaryRedirect': [307, 'temporaryRedirect']
    }

    BAD_REQUEST = {
        'badRequest': [400, 'badRequest'],
        'badBinaryDomainRequest': [400, 'badBinaryDomainRequest'],
        'badContent': [400, 'badContent'],
        'badLockedDomainRequest': [400, 'badLockedDomainRequest'],
        'corsRequestWithXOrigin': [400, 'corsRequestWithXOrigin'],
        'endpointConstraintMismatch': [400, 'endpointConstraintMismatch'],
        'invalid': [400, 'invalid'],
        'invalidAltValue': [400, 'invalidAltValue'],
        'invalidHeader': [400, 'invalidHeader'],
        'invalidParameter': [400, 'invalidParameter'],
        'invalidQuery': [400, 'invalidQuery'],
        'keyExpired': [400, 'keyExpired'],
        'keyInvalid': [400, 'keyInvalid'],
        'lockedDomainCreationFailure': [400, 'lockedDomainCreationFailure'],
        'notDownload': [400, 'notDownload'],
        'notUpload': [400, 'notUpload'],
        'parseError': [400, 'parseError'],
        'required': [400, 'required'],
        'tooManyParts': [400, 'tooManyParts'],
        'unknownApi': [400, 'unknownApi'],
        'unsupportedMediaProtocol': [400, 'unsupportedMediaProtocol'],
        'unsupportedOutputFormat': [400, 'unsupportedOutputFormat'],
        'wrongUrlForUpload': [400, 'wrongUrlForUpload']
    }

    UNAUTHORIZED = {
        'unauthorized': [401, 'unauthorized'],
        'authError': [401, 'authError'],
        'expired': [401, 'expired'],
        'lockedDomainExpired': [401, 'lockedDomainExpired'],
        'required': [401, 'required']
    }

    PAYMENT_REQUIRED = {
        'dailyLimitExceeded402': [402, 'dailyLimitExceeded402'],
        'quotaExceeded402': [402, 'quotaExceeded402'],
        'user402': [402, 'user402']
    }

    FORBIDDEN = {
        'forbidden': [403, 'forbidden'],
        'accessNotConfigured': [403, 'accessNotConfigured'],
        'accountExists': [403, 'accountExists'],
        'accountDeleted': [403, 'accountDeleted'],
        'accountDisabled': [403, 'accountDisabled'],
        'accountUnverified': [403, 'accountUnverified'],
        'concurrentLimitExceeded': [403, 'concurrentLimitExceeded'],
        'dailyLimitExceeded': [403, 'dailyLimitExceeded'],
        'dailyLimitExceededUnreg': [403, 'dailyLimitExceededUnreg'],
        'downloadServiceForbidden': [403, 'downloadServiceForbidden'],
        'insufficientAudience': [403, 'insufficientAudience'],
        'insufficientAuthorizedParty': [403, 'insufficientAuthorizedParty'],
        'insufficientPermissions': [403, 'insufficientPermissions'],
        'limitExceeded': [403, 'limitExceeded'],
        'lockedDomainForbidden': [403, 'lockedDomainForbidden'],
        'quotaExceeded': [403, 'quotaExceeded'],
        'rateLimitExceeded': [403, 'rateLimitExceeded'],
        'rateLimitExceededUnreg': [403, 'rateLimitExceededUnreg'],
        'responseTooLarge': [403, 'responseTooLarge'],
        'servingLimitExceeded': [403, 'servingLimitExceeded'],
        'sslRequired': [403, 'sslRequired'],
        'unknownAuth': [403, 'unknownAuth'],
        'userRateLimitExceeded': [403, 'userRateLimitExceeded'],
        'userRateLimitExceededUnreg': [403, 'userRateLimitExceededUnreg'],
        'variableTermExpiredDailyExceeded': [403, 'variableTermExpiredDailyExceeded'],
        'variableTermLimitExceeded': [403, 'variableTermLimitExceeded']
    }

    NOT_FOUND = {
        'notFound': [404, 'notFound'],
        'unsupportedProtocol': [404, 'unsupportedProtocol']
    }

    METHOD_NOT_ALLOWED = {
        'httpMethodNotAllowed': [405, 'httpMethodNotAllowed']
    }

    CONFLICT = {
        'conflict': [409, 'conflict'],
        'duplicate': [409, 'duplicate']
    }

    GONE = {
        'deleted': [410, 'deleted']
    }

    PRECONDITION_FAILED = {
        'conditionNotMet': [412, 'conditionNotMet']
    }

    REQUEST_ENTITY_TOO_LARGE = {
        'backendRequestTooLarge': [413, 'backendRequestTooLarge'],
        'batchSizeTooLarge': [413, 'batchSizeTooLarge'],
        'uploadTooLarge': [413, 'uploadTooLarge']
    }

    REQUESTED_RANGE_NOT_SATISFIABLE = {
        'requestedRangeNotSatisfiable': [416, 'requestedRangeNotSatisfiable']
    }

    EXPECTATION_FAILED = {
        'expectationFailed': [417, 'expectationFailed']
    }

    PRECONDITION_REQUIRED = {
        'preconditionRequired': [428, 'preconditionRequired']
    }

    TOO_MANY_REQUESTS = {
        'rateLimitExceeded': [429, 'rateLimitExceeded']
    }

    INTERNAL_SERVER_ERROR = {
        'internalError': [500, 'internalError']
    }

    NOT_IMPLEMENTED = {
        'notImplemented': [501, 'notImplemented'],
        'unsupportedMethod': [501, 'unsupportedMethod']
    }

    SERVICE_UNAVAILABLE = {
        'backendError': [503, 'backendError'],
        'backendNotConnected': [503, 'backendNotConnected'],
        'notReady': [503, 'notReady']
    }
