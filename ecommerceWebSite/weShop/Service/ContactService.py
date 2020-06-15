from weShop.Models.models import Contact

class ContactService:

    def __init__(self):
        self.contact = Contact()

    def add(self, contactObj):

        fname = contactObj.get('firstname')
        lname = contactObj.get('lastname')
        email = contactObj.get('email')
        subject = contactObj.get('subject')
        message = contactObj.get('message')

        self.contact.fname = fname
        self.contact.lname = lname
        self.contact.email = email
        self.contact.subject = subject
        self.contact.message = message

        self.contact.save()
