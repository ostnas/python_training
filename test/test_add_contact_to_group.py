from model.contact import Contact
from model.group import Group
import random

def test_add_contact_to_group(app, orm):
    if len(orm.get_contact_list()) == 0:
        app.contact.create(Contact(firstname = "NameName"))
    if len(orm.get_group_list()) == 0:
        app.group.create(Group(name = "groupname"))
    group = random.choice(orm.get_group_list())
    contacts_not_in_group = orm.get_contacts_not_in_group(group)
    if len(contacts_not_in_group) == 0:
        contacts_not_in_group.append(app.contact.create(Contact(firstname="NameName")))
    contact_to_add_in_group = random.choice(contacts_not_in_group)
    app.contact.add_contact_to_group(contact_to_add_in_group.id, group.id)
    assert orm.contact_is_in_group(contact_to_add_in_group, group) == True