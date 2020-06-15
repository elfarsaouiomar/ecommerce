from weShop.Service.ContactService import ContactService
from weShop.Dto.ContactDto import ContactDto

class ContactApp:

    def __init__(self):
        pass

    @staticmethod
    def add(contactDto):

        data = {}
        contactService = ContactService()

        contactDto.validate()

        if len(contactDto.errors) != 0:
            return contactDto

        contactService.add(contactDto.data)
        data['response'] = "thank you for your message"
        data['status'] = "201"

        return data





