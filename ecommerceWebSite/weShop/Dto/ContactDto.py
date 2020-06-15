from validate_email import validate_email
from logging import ERROR

class ContactDto:
    postParams = ['firstname', 'lastname', 'email', 'subject', 'message']

    def __init__(self, params):

        self.data = {}
        self.errors = {}

        for singleParam in self.postParams:
            param = params.get(singleParam)
            self.data[singleParam] = param

    def validate(self):
        try:
            firstname = self.data.get('firstname')
            lastname = self.data.get('lastname')
            email = self.data.get('email')
            subject = self.data.get('subject')
            message = self.data.get('message')

            for para in self.postParams:
                paramsvalue = self.data.get(para)
                if not self.paramsLenght(parms=paramsvalue):
                    self.errors['error'] = "{} is required".format(para)
                    return self.errors

            if len(firstname) > 30:
                self.errors['firstname'] = "max length for first name is 30"
            elif len(firstname) < 2:
                self.errors['firstname'] = "min length for fist name is 2"

            if len(lastname) > 30:
                self.errors['lastname'] = "max length for last name is 30"
            elif len(lastname) < 2:
                self.errors['lastname'] = "min length for last name is 2 "

            if len(subject) > 50:
                self.errors['subject'] = "max length for subject is 40"
            elif len(subject) < 2:
                self.errors['subject'] = "min length for subject is 3"

            if len(message) > 300:
                self.errors['message'] = "max length for message is 300"
            elif len(message) < 2:
                self.errors['message'] = "min length for message is 3"

            if not validate_email(email):
                self.errors['email'] = "invalid email"
                return self.errors

        except Exception as er:
            self.errors['error'] = "something is wrong !!"
            self.errors['statusCode'] = 500
            ERROR(er)

    @staticmethod
    def paramsLenght(parms):
        try:
            if len(parms) == 0:
                return False
            return True
        except Exception as e:
            return False