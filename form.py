from wtforms import Form, StringField, SelectField


class UserSearchForm(Form):
    choices = [('Username', 'Username')]
    select = SelectField('Search for user:', choices=choices)
    search = StringField('')
