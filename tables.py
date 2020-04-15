from flask_table import Table, Col


class UserResults(Table):
    user_id = Col('Id', show=False)
    username = Col('Username')
    alert = Col('Status')
