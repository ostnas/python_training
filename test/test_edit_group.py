from model.group import Group
import random


def test_edit_some_group(app, db, check_ui):
    if len(db.get_group_list()) == 0:
        app.group.create(Group(name = "Test"))
    old_groups = db.get_group_list()
    random_group = random.choice(old_groups)
    group = Group(name = "New_group_name")
    app.group.edit_group_by_id(random_group.id, group)
    new_groups = db.get_group_list()
    assert len(old_groups) == len(new_groups)
    group.id = random_group.id
    old_groups.remove(random_group)
    old_groups.append(group)
    assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)
    if check_ui:
        new_groups = map(Group.clean, db.get_group_list())
        assert sorted(new_groups, key=Group.id_or_max) == sorted(app.group.get_group_list(), key=Group.id_or_max)