from ..service.ContactService import ContactService

class ContactApp:

    def __init__(self):
        pass

    contactService = ContactService()

    def add(self, contact):
        self.contactService.add(contact)

