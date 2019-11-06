from sys import maxsize

class Contact:

    def __init__(self, id = None, firstname=None, middlename=None, lastname=None, nickname=None, title=None,
                 company=None, address=None, home=None, mobile=None, work=None, email=None, email2=None, email3=None,
                 homepage=None, bday=None, bmonth=None, byear=None, address2=None, phone2=None, notes=None,
                 all_email_from_home_page=None, all_phones_from_home_page=None):

        self.id = id
        self.firstname = firstname
        self.middlename = middlename
        self.lastname = lastname
        self.nickname = nickname
        self.title = title
        self.company = company
        self.address = address
        self.home = home
        self.mobile = mobile
        self.work = work
        self.email = email
        self.email2 = email2
        self.email3 = email3
        self.homepage = homepage
        self.bday = bday
        self.bmonth = bmonth
        self.byear = byear
        self.address2 = address2
        self.phone2 = phone2
        self.notes = notes
        self.all_email_from_home_page=all_email_from_home_page
        self.all_phones_from_home_page=all_phones_from_home_page

    def __repr__(self):
        return "%s:%s:%s" % (self.id, self.firstname, self.lastname)

    def __eq__(self, other):
        return (self.id is None or other.id is None or self.id == other.id) and self.firstname == other.firstname and self.lastname == other.lastname

    def id_or_max(self):
        if self.id:
            return int(self.id)
        else:
            return maxsize