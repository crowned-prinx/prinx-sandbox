
r"""
@author: Prinx

Geocoding and Reverse Geocoding Tool

This program allows users to convert addresses into geographic coordinates (latitude and longitude) 
and vice versa using the Nominatim geocoding service. It supports:
- Address to coordinates conversion.
- Coordinates to address conversion (reverse geocoding).
- Input validation for addresses and coordinates.
- Default location based on the user's local timezone.

The program is built using the `geopy` library and is designed to handle user input errors gracefully, 
providing informative feedback for invalid inputs or geocoding failures.

"""


from utils.functions import convert_address, get_user_input

# address = [35.6768601, 139.7638947]

def main():
    user_input = get_user_input()
    response = convert_address(user_input)
    if isinstance(response, list):
        print(f'\nThe cordinates for {user_input} is:\n')
        print(f'Latitude: {response[0]}\nLongitude: {response[1]}')
    else:
        print(f'\nThe corresponding address to your input {user_input} is: ')
        print(response)


if __name__ == "__main__":
    main()
