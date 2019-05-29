import requests

def zip2latlong(zip):
    response = requests.get("https://www.zipcodeapi.com/rest/OyuA5nnRd28hAzIdPTGB66oOcNCpjQeqHOwn31oAkyX0X8HZ252hLTck4Ya072Te/info.json/{}/degrees".format(zip)).json()
    # print(response)
    return response['lat'], response['lng']


print(zip2latlong("94112"))