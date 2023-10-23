import phonenumbers
from phonenumbers import geocoder
#from test import number
import folium

Key = "0ab0e4cdbd2e4935a37d013bf12cc65b"

number = input("Enter phone number along with country code: ")
check_num = phonenumbers.parse(number)
number_loc = geocoder.description_for_number(check_num,"en")
print(number_loc)


from phonenumbers import carrier
service_prov = phonenumbers.parse(number)
print(carrier.name_for_number(service_prov,"en"))


from opencage.geocoder import OpenCageGeocode
geocoder = OpenCageGeocode(Key)

query = str(number_loc)
result = geocoder.geocode(query)
lat = result[0]['geometry']['lat']
lng = result[0]['geometry']['lng']
print(lat,lng)

map_loc = folium.Map(location = [lat,lng],zoom_start=9)
folium.Marker([lat,lng],popup=number_loc).add_to(map_loc) 
map_loc.save("mylocation.html")