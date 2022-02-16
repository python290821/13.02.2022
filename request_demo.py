import requests
response = requests.get("https://jsonplaceholder.typicode.com/users/1")

class my_web():
    def __init__(self, json_val):
        self.__dict__ = json_val

    def __str__(self):
        return f'{self.__dict__}'


json_from_web = response.json()
print(json_from_web)
print(json_from_web["id"])
web_response_as_class = my_web(json_from_web)
print(web_response_as_class.__dict__)
print(web_response_as_class.id)
