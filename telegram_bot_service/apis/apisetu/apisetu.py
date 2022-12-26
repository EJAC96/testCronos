import requests

from config import STATE_URL


class ApisSetu:
    def __init__(self):
        pass

    def get_state(self):
        #Return the list of states from Apisetu.org
        response = requests.get(STATE_URL)
        print(response)

    def get_districts(self,state_id):
        pass

    def get_appointments_by_district(self,district_id, date):
        pass

    def get_appointments_by_pincode(self, pincode, date):
        pass


obj = ApisSetu()
obj.get_state()