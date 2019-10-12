from model.group import Group

def test_edit_first_group(app):
    if app.group.count() == 0:
        app.group.create(Group(name = "Test"))
    app.group.edit_first_group(Group(name="New name of group", header="New header of group", footer="New footer of group"))