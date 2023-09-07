#!/usr/bin/env python3
import json
# Let's use the module created in chapter 9
from print_n_structure_elements import print_first_n_values
# Read files into lists
def read_json_return_structure( file_name ):
    # We say this is a list that we return but the structure
    # is totally dependent on the file
    with open( file_name, encoding="utf8"  ) as fn:
        return json.load( fn )

countries_list = read_json_return_structure( "countries.json" )
countries_states_list = read_json_return_structure("countries_states_cities.json")

# Print the first 3 entries in each structure
# So we can explore the data in these files
# Let's assume we can't just browse the files themselves; we'll
# need to dump a part of the structs we loaded via json.load()
#
# Use the module print_n_structure_elements with function print_first_n_values
'''
print_first_n_values( countries_list, 5 )
print_first_n_values( countries_states_list, 5 )
print_first_n_values( countries_list[ 0 ], 10)
'''

# Inside of countries_list, the country ID is 'id'
# Inside of countries_states_list is 'country_id'

# Create a dictionary with a key of country name and
# values of a dictionary containing the key 'capital' and the country capital
# and the key 'states' and a list of the states/provinces/counties for this country
# We'll need to get the capital from the countries_list and the states from
# the countries_states_cities_list

# try one country first...then have a list of countries
# Start with country_id and id for a match
# Need a blank dictionary; we'll add to it each loop iteration
dict_extract_country_data = dict()
for country_id in [1, 2, 3, 4]:
    country_id_list_for_extract = [ c_info for c_info in countries_list if c_info['id'] == country_id ][0]
    # Get the name from the above extract
    country_name = country_id_list_for_extract[ 'name']
    # Now pull the states/counties for the same country code from countries_states_list
    # First, get everything for this country_id
    states_from_country_extract = [ c_info for c_info in countries_states_list if c_info['country_id'] == country_id ]
    # Now extract the states
    states_this_country = [item['name'] for item in states_from_country_extract]

    # Create a dictionary entry that looks like:
    #  Key - Country name (from country_id_list_for_extract)
    #  Value - Dictionary {key = 'capital' value=country_id_list_for_extract,
    #                      key = 'states', value = List of states/counties from states_from_country_extract
    dict_extract_country_data[ country_name ]  = { 'capital'   : country_name,
                                                   'states'    : states_this_country,
                                                 }
# OK - Write this out to a file:
with open( "extract.json", "w", encoding="utf8") as je:
    json.dump( dict_extract_country_data, je, indent=4 )

