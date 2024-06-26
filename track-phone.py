import phonenumbers
from phonenumbers import geocoder

phone_number1 = phonenumbers.parse("+33 6 12 34 56 78")
phone_number2 = phonenumbers.parse("+44 20 7123 4567")
phone_number3 = phonenumbers.parse("+1 212-555-1234")
phone_number4 = phonenumbers.parse("+81 3 1234 5678")

print(geocoder.description_for_number(phone_number1, 'en'))
print(geocoder.description_for_number(phone_number2, 'en'))
print(geocoder.description_for_number(phone_number3, 'en'))
print(geocoder.description_for_number(phone_number4, 'en'))