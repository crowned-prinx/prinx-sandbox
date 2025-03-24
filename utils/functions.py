r"""
@author: Prinx

"""

from geopy.geocoders import Nominatim
from tzlocal import get_localzone

# Initialize geocoder and default address
geo_coder = Nominatim(user_agent="my_geocoder")
TIMEOUT = 10
default_addr = str(get_localzone()).split("/")[1]

def get_user_input():
    """Prompt the user for an address or coordinates and return the input."""
    while True:
        user_input = input("Please enter an address or [latitude, longitude] coordinates: ").strip()
        if user_input:
            if user_input.startswith("[") and user_input.endswith("]"):
                return user_input[1:-1].split(",")
            return user_input
        print("Input cannot be empty. Please try again.")

def validate_address(address):
    """
    Validate the address or coordinates.
    Returns True if valid, otherwise returns an error message.
    """
    if isinstance(address, list):
        if len(address) == 2 and all(coord.strip() for coord in address):
            return True
        return "Invalid coordinates. Format must be [latitude, longitude]."
    elif isinstance(address, str) and address.strip():
        return True
    return "Please enter a valid address or coordinates."

def convert_address(addr=default_addr):
    """
    Convert an address to coordinates or vice versa.
    Returns the result or an error message.
    """
    validation_result = validate_address(addr)
    if validation_result != True:
        return validation_result

    print("Fetching...")
    try:
        if isinstance(addr, list):
            location = geo_coder.reverse(addr, timeout=TIMEOUT)
            return location.address
        else:
            location = geo_coder.geocode(addr, timeout=TIMEOUT)
            if location:
                return [location.latitude, location.longitude]
            return "Address not found. Please check your input."
    except Exception as e:
        return f"There was an unknown error fetching address: {e}"