class UserProvider:

    @staticmethod
    def fake_user():
        return {
            'username': 'some_name',
            'id': 'some_id'
        }

    @staticmethod
    def existing_user():
        return {
            'username': 'defunkt',
            'id': 2,
        }