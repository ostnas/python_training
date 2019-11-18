from model.contact import Contact
from model.group import Group
import random

def test_delete_contact_from_group(app, orm):
    if len(orm.get_contact_list()) == 0:
        app.contact.create(Contact(firstname = "NameName"))
    if len(orm.get_group_list()) == 0:
        app.group.create(Group(name = "groupname"))
    group = random.choice(orm.get_group_list())
    contacts_in_group = orm.get_contacts_in_group(group)
    if len(contacts_in_group) == 0:
        contact = random.choice(orm.get_contact_list())
        app.contact.add_contact_to_group(contact.id, group.id)
        contacts_in_group.append(contact)
    contact_to_delete_from_group = random.choice(contacts_in_group)
    app.contact.delete_contact_from_group(contact_to_delete_from_group.id, group.id)
    assert orm.contact_is_in_group(contact_to_delete_from_group, group) == False