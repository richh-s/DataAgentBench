code = """import pandas as pd
import json

# The full system output of the query_db tool is stored as a dictionary in locals().
# The actual tool result is a dictionary, not a string that needs json.loads itself.
full_tool_output = locals()['var_function-call-14540983208523752576']

# The actual business data is embedded as a string within 'query_db_response' -> 'results' list.
# The 'results' list contains a single string, which has verbose text and the JSON array.
data_string_with_verbose_text = full_tool_output['query_db_response']['results'][0]

# Extract the pure JSON array string from the verbose output.
json_start_index = data_string_with_verbose_text.find('[')
json_end_index = data_string_with_verbose_text.rfind(']') + 1

business_list = []
if json_start_index != -1 and json_end_index != -1:
    clean_json_str = data_string_with_verbose_text[json_start_index:json_end_index]
    try:
        business_list = json.loads(clean_json_str)
    except json.JSONDecodeError as e:
        # If JSON decoding fails, business_list remains empty, and we can print the error for debugging.
        print(f"JSONDecodeError: {e}")
        pass

df_business = pd.DataFrame(business_list)

highest_state_name = None
business_ids_in_highest_state = []

if not df_business.empty:
    # Function to extract state from description
    def get_state(description):
        if description and " in " in description:
            parts = description.split(" in ")
            if len(parts) > 1:
                location_parts = parts[-1].split(", ")
                if len(location_parts) > 1:
                    state_city_parts = location_parts[1].strip().split(" ")
                    if state_city_parts and len(state_city_parts[0]) == 2:
                        return state_city_parts[0]
        return None

    df_business["state"] = df_business["description"].apply(get_state)

    # Filter for businesses with WiFi, explicitly handling common string representations of 'no'/'None'
    df_wifi_businesses = df_business[
        df_business["attributes"].apply(
            lambda x: x and 'WiFi' in x and str(x['WiFi']).lower() not in ["u'no'", "'no'", "none", "false", "no"]
        )
    ].copy()

    df_wifi_businesses.dropna(subset=['state'], inplace=True)

    if not df_wifi_businesses.empty:
        state_counts = df_wifi_businesses["state"].value_counts().reset_index()
        state_counts.columns = ["state", "business_count"]

        if not state_counts.empty:
            highest_state = state_counts.loc[state_counts["business_count"].idxmax()]
            highest_state_name = highest_state["state"]

            business_ids_in_highest_state = df_wifi_businesses[
                df_wifi_businesses["state"] == highest_state_name
            ]['business_id'].tolist()

print("__RESULT__:")
print(json.dumps({
    "highest_state_name": highest_state_name,
    "business_ids_in_highest_state": business_ids_in_highest_state
}))"""

env_args = {'var_function-call-14540983208523752576': [{'_id': '6859a000fe8b31cd7362e2ab', 'business_id': 'businessid_49', 'attributes': {'BusinessAcceptsCreditCards': 'True', 'WiFi': "u'no'", 'BusinessAcceptsBitcoin': 'False'}, 'description': 'Located at 6901 Phelps Rd in Goleta, CA, this facility offers a nurturing environment for young learners, providing a range of services in Education, Elementary Schools, Child Care & Day Care, Local Services, Preschools, and Montessori Schools.'}, {'_id': '6859a000fe8b31cd7362e2b1', 'business_id': 'businessid_92', 'attributes': {'ByAppointmentOnly': 'False', 'BusinessAcceptsCreditCards': 'True', 'BusinessParking': "{'garage': True, 'street': False, 'validated': False, 'lot': False, 'valet': False}", 'RestaurantsPriceRange2': '2', 'WheelchairAccessible': 'True', 'BikeParking': 'True', 'NoiseLevel': "u'quiet'", 'WiFi': "u'no'"}, 'description': 'Located at 690 W Dekalb Pike in King of Prussia, PA, this business offers a diverse range of services and products in the fields of Cosmetics & Beauty Supply, Cosmetic Dentists, Tanning, Teeth Whitening, Beauty & Spas, Dentists, Shopping, Blow Dry/Out Services, Health & Medical, Spray Tanning, and Hair Salons.'}, {'_id': '6859a000fe8b31cd7362e2b2', 'business_id': 'businessid_64', 'attributes': {'BusinessParking': "{'garage': True, 'street': False, 'validated': False, 'lot': True, 'valet': False}", 'ByAppointmentOnly': 'False', 'BusinessAcceptsCreditCards': 'True', 'RestaurantsPriceRange2': '2', 'BikeParking': 'True', 'WiFi': "u'free'"}, 'description': 'Located at 12337 Olive Blvd in Creve Coeur, MO, this establishment offers a range of services in Nail Salons, Beauty & Spas.'}, {'_id': '6859a000fe8b31cd7362e2b7', 'business_id': 'businessid_54', 'attributes': {'BusinessParking': "{'garage': False, 'street': False, 'validated': False, 'lot': False, 'valet': False}", 'BusinessAcceptsCreditCards': 'True', 'WheelchairAccessible': 'True', 'RestaurantsDelivery': 'True', 'RestaurantsTakeOut': 'True', 'RestaurantsPriceRange2': '1', 'WiFi': "u'free'"}, 'description': 'Located at 13151 Race Track Rd in Tampa, FL, this establishment offers a variety of services including Service Stations, Coffee & Tea, Gas Stations, Automotive, Gas Stations, Food, and Convenience Stores.'}, {'_id': '6859a000fe8b31cd7362e2ba', 'business_id': 'businessid_91', 'attributes': {'BusinessParking': "{'garage': False, 'street': True, 'validated': False, 'lot': False, 'valet': False}", 'WiFi': "u'free'", 'WheelchairAccessible': 'True', 'Caters': 'True', 'HasTV': 'True', 'HappyHour': 'False', 'Ambience': "{'touristy': None, 'hipster': None, 'romantic': None, 'divey': None, 'intimate': True, 'trendy': None, 'upscale': None, 'classy': True, 'casual': True}", 'RestaurantsDelivery': 'True', 'RestaurantsPriceRange2': '2', 'GoodForKids': 'True', 'RestaurantsAttire': "u'casual'", 'BikeParking': 'True', 'OutdoorSeating': 'True', 'NoiseLevel': "u'quiet'", 'RestaurantsGoodForGroups': 'True', 'RestaurantsTakeOut': 'True', 'BusinessAcceptsCreditCards': 'True', 'RestaurantsReservations': 'False', 'GoodForMeal': "{'dessert': None, 'latenight': None, 'lunch': True, 'dinner': None, 'brunch': True, 'breakfast': True}", 'Alcohol': "u'beer_and_wine'", 'RestaurantsTableService': 'True', 'Corkage': 'False', 'BYOB': 'True'}, 'description': 'Located at 1625 Baronne St in New Orleans, LA, this vibrant establishment offers a delightful array of options ranging from Food, Shaved Ice, Cajun/Creole, Breakfast & Brunch, Party & Event Planning, Comfort Food, Cafes, Restaurants, to Event Planning & Services, making it a perfect spot for any occasion.'}]}

exec(code, env_args)
