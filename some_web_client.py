import requests
import json
from datetime import datetime


class SomeResourceClient:
    def __init__(self, url):
        self.url = url

    def __user_get_status(self, user_id):
        resp = requests.get(f"{self.url}/web/2/user/get-status/{user_id}")
        json_data = json.loads(resp.text)
        return json_data

    def get_user_last_action_time(self, user_id):
        json_data = self.__user_get_status(user_id)
        last_action_time = json_data["lastActionTime"]
        time_diff = json_data["timeDiff"]
        return datetime.fromtimestamp(last_action_time - time_diff)

    def get_card_info(self, product_id):
        resp = requests.get(f"{self.url}//vol995/part99532/{product_id}/info/ru/card.json")
        json_data = json.loads(resp.text)
        return json_data


some_recource_client = SomeResourceClient("https://www.avito.ru/")
print(
    some_recource_client.get_user_last_action_time("43e99f0389907ec95262e6f7e929c70e6b6848a45f77ae7d8a3971bafdd4a79c"))
recource_client = SomeResourceClient("https://basket-05.wb.ru/")
print(recource_client.get_card_info(99532155))
