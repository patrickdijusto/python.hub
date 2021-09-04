import phonenumbers
from phonenumbers import carrier, timezone, geocoder
import sys

print(sys.argv[1])

numberNo = (sys.argv[1])

print(numberNo)

mobileNo = phonenumbers.parse(numberNo, "US")

print(mobileNo)

print("Timezone:", timezone.time_zones_for_number(mobileNo))

print("Carrier: ", carrier.name_for_number(mobileNo, "en"))

print("Geographic region: ", geocoder.description_for_number(mobileNo, "en"))



