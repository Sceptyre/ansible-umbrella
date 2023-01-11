from .base import _BaseAPI

class DestinationListAPI(_BaseAPI):
    # Destination List interactions
    def get_destination_list(self, destination_list_id: str):
        r = self._uc._s.get(
            'https://api.umbrella.com/policies/v2/destinationlists/' + destination_list_id
        )
        r.raise_for_status()

        return r.json()
    
    def get_destination_lists(self):
        r = self._uc._s.get(
            'https://api.umbrella.com/policies/v2/destinationlists'
        )
        r.raise_for_status()

        return r.json()


    # Destination interactions
    def add_destination_list_destination(self, destination_list_id: str, destination: str, type: str='DOMAIN', comment: str='Added By Automation'):
        r = self._uc._s.post(
            'https://api.umbrella.com/policies/v2/destinationlists/' + destination_list_id + '/destinations',
            json=[
                {
                    'destination': destination,
                    'comment': comment
                }
            ]
        )
        r.raise_for_status()

        return r.json()

    def get_destination_list_destinations(self, destination_list_id: str, page: int=1, limit: int=100):
        r = self._uc._s.get(
            'https://api.umbrella.com/policies/v2/destinationlists/' + destination_list_id + '/destinations',
            params={
                'page':page,
                'limit':limit
            }
        )
        r.raise_for_status()

        return r.json()
