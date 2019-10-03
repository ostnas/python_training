from model.group import Group

def test_edit_first_group(app):
    app.session.login(username="admin", password="secret")
    app.group.edit_first_group(Group(name="New name of group", header="New header of group", footer="New footer of group"))
    app.session.logout()