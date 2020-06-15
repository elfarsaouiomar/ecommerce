from validate_email import validate_email
from logging import ERROR

class ContactDto:
    postParams = ['fname', 'lname', 'email', 'subject', 'message']

    def __init__(self, params):

        self.data = {}
        self.errors = {}

        for singleParam in self.postParams:
            param = params.get(singleParam)
            self.data[singleParam] = param

    def validate(self):
        try:
            fname = self.data.get('fname')
            lname = self.data.get('lname')
            email = self.data.get('email')
            subject = self.data.get('subject')
            message = self.data.get('message')

            for para in self.postParams:
                paramsvalue = self.data.get(para)
                print("The parmas is {0} and the value is {1}".format(para, paramsvalue))
                if not self.paramsLenght(parms=paramsvalue):
                    self.errors['error'] = "{} is required".format(para)
                    return self.errors

            if len(fname) > 30:
                self.errors['fname'] = "max length for first name is 30"
            elif len(fname) < 2:
                self.errors['fname'] = "min length for fist name is 2"

            if len(lname) > 30:
                self.errors['lname'] = "max length for last name is 30"
            elif len(lname) < 2:
                self.errors['lname'] = "min length for last name is 2 "

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
            ERROR(er)

    @staticmethod
    def paramsLenght(parms):
        if len(parms) == 0:
            return False
        return True