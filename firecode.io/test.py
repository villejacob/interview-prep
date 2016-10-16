

from_name = "Jacob"
from_address_1 = "Addr 1"
from_address_2 = "Addr 2"
from_city = "City"
from_state = "State"
from_zip = "ZIP"

from_address = collections.OrderedDict()

from_address['name'] = from_name
from_address['address_line1'] = from_address_1
from_address['address_line2'] = from_address_2
from_address['address_city'] = from_city
from_address['address_state'] = from_state
from_address['address_zip'] = from_zip

address_string = ""

for name, info in from_address.items():
    address_string += info

print address_string