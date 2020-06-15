from ecommerceWebSite.weShop.Models.models import Contact

class ContactDao:

    contact = Contact()

    def add(self, contactObj):
        # TODO // add raise here
        try:
            self.contact.save(contactObj)
        except Exception as e:
            print (e)
