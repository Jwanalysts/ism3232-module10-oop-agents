
class ServiceLookup:
    """A tool for looking up business services."""

    def __init__(self, services):
        self.services = services

    def find_service(self, message):
        text = message.lower()

        for service in self.services:
            if service.lower() in text:
                return service

        return None

    def find_price(self, service):
        return self.services.get(service)
