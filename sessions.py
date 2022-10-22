import requests
from datetime import datetime as dt
import os

class Pixela:

    def __init__(self):
        self.pixela_username = os.environ.get("PIXELA_USER")
        self.pixela_pass = os.environ.get("PIXELA_PASS")
        self.pixela_endpoint = "https://pixe.la/v1/users"
        self.header = {
            "X-USER-TOKEN": self.pixela_pass
        }


    def create_graph(self, id, name):
        graph_endpoint = f"{self.pixela_endpoint}/{self.pixela_username}/graphs"
        graph_params = {
            "id": id,
            "name": name,
            "unit": "sessions",
            "type": "int",
            "color": "ajisai"
        }

        response = requests.post(url=graph_endpoint, json=graph_params, headers=self.header)
        print(response.text)

    def delete_graph(self, graph_id: str):
        del_graph_endpoint = f"{self.pixela_endpoint}/{self.pixela_username}/graphs/{graph_id}"
        response = requests.delete(url=del_graph_endpoint, headers=self.header)
        print(response.text)

    def add_pixel(self, quantity, graph_id, date=dt.today().strftime('%Y%m%d')):
        pixel_endpoint = f"{self.pixela_endpoint}/{self.pixela_username}/graphs/{graph_id}/"
        pixel_params = {
            "date": date,
            "quantity": quantity
        }
        response = {"isSuccess": "false"}
        while response["isSuccess"] != True:
            response = requests.post(url=pixel_endpoint, json=pixel_params, headers=self.header)
            response = response.json()
            print(response)

    def del_pixel(self, graph_id, date=dt.today().strftime('%Y%m%d')):
        del_pixel_endpoint = f"{self.pixela_endpoint}/{self.pixela_username}/graphs/{graph_id}/{date}/"
        response = requests.delete(url=del_pixel_endpoint, headers=self.header)
        print("hmm")
        print(response.status_code)

        print("whuu")



nathan = Pixela()
nathan.add_pixel("3", "graph01")

