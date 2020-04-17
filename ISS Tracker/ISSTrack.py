import json, turtle, urllib.request, time, webbrowser
import geocoder # need to pip install geocoder for your lat/long to work.


#Retrieve the names of all the astronauts currently on board the ISS, and own lat/long - write to a file and display
url = "http://api.open-notify.org/astros.json"
response = urllib.request.urlopen(url)
result = json.loads(response.read())
a=open("iss.txt","w")
a.write("There are currently " + str(result["number"]) + " astronauts on the ISS:\n\n")

people = result["people"]

for p in people:
  a.write(p["name"] + " - on board" + "\n")

g=geocoder.ip('me') # need to pip install geocoder, and import as in the headers above
a.write("\nYour current Lat/Long is: " + str(g.latlng)) # prints your current lat/long in the text file.
a.close()
webbrowser.open("iss.txt")



#Setup world map in Turtle
screen = turtle.Screen()
screen.setup(1280, 720)
screen.setworldcoordinates(-180, -90, 180, 90)
#Load the world map image
screen.bgpic("map.gif")
  
screen.register_shape("iss.gif")
iss = turtle.Turtle()
iss.shape("iss.gif")
iss.setheading(45)
iss.penup()

while True:
  #Load the current status of the ISS in real-time  
  url = "http://api.open-notify.org/iss-now.json"
  response = urllib.request.urlopen(url)
  result = json.loads(response.read())
    
  #Extract the ISS location
  location = result["iss_position"]
  lat = location["latitude"]
  lon = location["longitude"]
    
  #Output Latitude and Longitude to the console
  lat = float(lat)
  lon = float(lon)
  print("\nLatitude: " + str(lat))
  print("Longitude: " + str(lon))

  #Update the ISS location on the map  
  iss.goto(lon, lat)
  #refresh every 5 seconds
  time.sleep(5)
  

