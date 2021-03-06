import phonenumbers

from phonenumbers import geocoder, timezone, carrier

number = "+359898303089"
ch_number = phonenumbers.parse(number, "CH")
print(geocoder.description_for_number(ch_number, "en"))

ch_number = phonenumbers.parse(number, "RO")
print(carrier.name_for_number(ch_number, "en"))

ch_number = phonenumbers.parse(number)
print(timezone.time_zones_for_number(ch_number))