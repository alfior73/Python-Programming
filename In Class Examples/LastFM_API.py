import urllib.request
import json

apikey = "3723c1d2d8f4016621c25a8b52b05c95"
secret = "2718052e654e875f2e7fcb70c8a602eb"

hosturl= "http://ws.audioscrobbler.com"
artist = "Ghostface+Killah"

artist = input("enter an artist")
artist = artist.replace(" ", "+")

queryurl= "/2.0/?method=artist.getinfo&artist="+artist+"&api_key="+apikey+"&format=json"

url = hosturl+queryurl

data  = urllib.request.urlopen(url).read()

artistinfo = json.loads(data)

artist = artistinfo["artist"]

print("Name = ", artist["name"])
#print("bio = ", artist["bio"]["summary"])

ontour = int(artist["ontour"])
ontour = bool(ontour)
if ontour:
    print(artist["name"], " is on tour, go get robbed by ticketmaster")
else:
    print(artist["name"], " is probably at home")
