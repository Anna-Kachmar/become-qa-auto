class RepositoriesProvider:


    @staticmethod
    def existing_repository():
        return {
            'name': 'become-qa-auto',
            'total_count': 1,
            'items_count': 1,
        }

    @staticmethod
    def non_existing_repository():
        return {
            'name': 'dnfnfcnedndnndcnednnedne',
            'total_count': 0,
            'items_count': 0,
        }