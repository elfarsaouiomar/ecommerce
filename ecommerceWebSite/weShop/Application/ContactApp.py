from weShop.Service.ContactService import ContactService
from weShop.Dto.ContactDto import ContactDto
from logging import ERROR

class ContactApp:

    def __init__(self):
        pass

    @staticmethod
    def add(contactDto):
        try:
            data = {}
            contactService = ContactService()
            contactDto.validate()
            if len(contactDto.errors) != 0:
                data['errors'] = contactDto.errors
                data['statusCode'] = 422
                return data

            contactService.add(contactDto.data)
            data['response'] = "thank you for your message"
            data['statusCode'] = 201

        except Exception as e:
            ERROR(e)

        finally:
            return data






