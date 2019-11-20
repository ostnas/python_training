from model.contact import Contact
from model.group import Group
import random

def test_delete_contact_from_group(app, orm):
    if len(orm.get_contact_list()) == 0:
        app.contact.create(Contact(firstname = "NameName"))
    if len(orm.get_group_list()) == 0:
        app.group.create(Group(name = "groupname"))
    all_groups = orm.get_group_list()
    group_with_contact = None
    contact_to_delete = None
    for i, group in enumerate(all_groups):
        contacts_in_group = orm.get_contacts_in_group(group)
        if len(contacts_in_group) > 0:
            contact_to_delete = random.choice(contacts_in_group)
            group_with_contact = group
            break
        # all groups are empty, add contact to last group
        elif i == len(all_groups) - 1:
            contact = random.choice(orm.get_contact_list())
            app.contact.add_contact_to_group(contact.id, group.id)
            contact_to_delete = contact
            group_with_contact = group
    app.contact.delete_contact_from_group(contact_to_delete.id, group_with_contact.id)
    assert orm.contact_is_in_group(contact_to_delete, group_with_contact) == False