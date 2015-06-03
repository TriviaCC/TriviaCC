import requests
import json
import unirest

class Trivia:
    def __init__(self):
        pass

    # Use this one for jservice.io
    def get_question(self):
        url = 'http://jservice.io/api/random'
        response = requests.get(url).json()
        data = json.dumps(response)

        headers = {'Content-type': 'application/json'}
        requests.post("http://127.0.0.1:8001/add_question/", data=data, headers=headers)
        trivia_json = open('trivia_json.txt', 'w')
        trivia_json.write(data)

    # Use this one for mashape Trivia
    # def get_question(self):
    #     # These code snippets use an open-source library. http://unirest.io/python
    #     response = unirest.get("https://pareshchouhan-trivia-v1.p.mashape.com/v1/getRandomQuestion",
    #       headers={
    #         "X-Mashape-Key": "5QG19uOAA6mshcwTHetgc3bz7XDnp1FZE7DjsnLD1gDl3T4hGx",
    #         "Accept": "application/json"
    #       }
    #     )
    #
    #     print json.dumps(response.body)
    #     url = "http://127.0.0.1:8001/add_question/"
    #     headers = {"Accept": "application/json"}
    #     params = json.dumps(response.body)
    #     callback = None
    #     unirest.post(url=url, headers=headers, params=params, callback=callback)
    #     trivia_json = open('trivia_json.txt', 'w')
    #     trivia_json.write(json.dumps(response.body))




def main():
    Trivia().get_question()


if __name__ == "__main__":
    main()



# These code snippets use an open-source library. http://unirest.io/python
# response = unirest.get("https://pareshchouhan-trivia-v1.p.mashape.com/v1/getRandomQuestion",
#   headers={
#     "X-Mashape-Key": "5QG19uOAA6mshcwTHetgc3bz7XDnp1FZE7DjsnLD1gDl3T4hGx",
#     "Accept": "application/json"
#   }
# )
