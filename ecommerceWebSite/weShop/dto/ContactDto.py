from validate_email import validate_email


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

            if fname is None or lname is None or email is None or subject is None or message is None:
                errors['error'] = "All fields is required"

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

            if len(message) > 30:
                self.errors['message'] = "max length for message is 300"
            elif len(message) < 2:
                self.errors['message'] = "min length for message is 3"

            if not validate_email(email):
                errors['email'] = "invalid email"


        except Exception as er:
            print (er)

