
class Response(object):

    def __init__(self, details=None, status='ok'):
        self.details = details
        self.status = status

    def json(self):
        default_response = {'status': self.status}
        if self.details is not None:
            default_response.update(self.details)
        return default_response
