from model.group import Group

def test_edit_first_group(app):
    app.group.edit_first_group(Group(name="New name of group", header="New header of group", footer="New footer of group"))