import phonenumbers
from test import number

from phonenumbers import geocoder

ch_number = phonenumbers.parse(number, "CH")
print("Name of the Country where Your Number are Activatred ---->")
print(geocoder.description_for_number(ch_number,"en"))

from phonenumbers import carrier
service_number = phonenumbers.parse(number,"RO")
print("Nmae of the Service Provider------>")
print(carrier.name_for_number(service_number, "en"))