code = """import pandas as pd
import re
import json

# Access the raw result from the storage variable.
# Based on previous errors and the output format, it seems locals()['var_function-call-8991307272850992448']
# directly contains the *list of strings* from the `query_db_response.results`.
# So we directly access the first element of that list.
raw_output_list_of_strings = locals()['var_function-call-8991307272850992448']
full_output_string = raw_output_list_of_strings[0] # This should be the single long string

# Extract the JSON array string by finding the first '[' and last ']' characters.
start_bracket = full_output_string.find('[')
end_bracket = full_output_string.rfind(']')

parsed_business_data = []
if start_bracket != -1 and end_bracket != -1 and end_bracket > start_bracket:
    json_array_string = full_output_string[start_bracket : end_bracket + 1]

    # Replace Python-style string literals (u'...') and ('...') inside JSON string
    # with standard JSON double-quoted strings.
    # This specifically targets values that are themselves strings enclosed in "u'...'".
    # Example: "WiFi": "u'no'" should become "WiFi": "no"
    # We need to be careful with quotes within the regex and replacement strings
    json_array_string = re.sub(r'"u\'([^\']*)\'"', r'"\1"', json_array_string)
    json_array_string = re.sub(r'"\'([^\']*)\'"', r'"\1"', json_array_string) # Also handle just single quotes

    try:
        parsed_business_data = json.loads(json_array_string)
    except json.JSONDecodeError as e:
        raise ValueError(f"Failed to parse JSON from extracted string: {e}. String snippet: {json_array_string[:500]}...")
else:
    raise ValueError("Could not extract a valid JSON array from the raw string.")

df = pd.DataFrame(parsed_business_data)

# Filter for businesses with WiFi (not 'no')
def has_wifi(attributes):
    if isinstance(attributes, dict) and 'WiFi' in attributes:
        wifi_status = str(attributes['WiFi']).lower() # Ensure string for comparison
        return wifi_status not in ["no", "none"]
    return False

df_wifi = df[df['attributes'].apply(has_wifi)]

# Extract state from description using regex
def extract_state(description):
    match = re.search(r',\s*([A-Z]{2})\b', description)
    return match.group(1) if match else None

df_wifi['state'] = df_wifi['description'].apply(extract_state)

# Filter out rows where state could not be extracted (e.g., non-US businesses)
df_wifi = df_wifi.dropna(subset=['state'])

# Get business_ids for filtering reviews later
business_ids_with_wifi = df_wifi['business_id'].tolist()

# Count businesses per state
state_counts = df_wifi['state'].value_counts().reset_index()
state_counts.columns = ['state', 'business_count']

# Find the state with the highest number of businesses
if not state_counts.empty:
    highest_state = state_counts.loc[state_counts['business_count'].idxmax()]
else:
    highest_state = {'state': None, 'business_count': 0}

# Prepare business_ids for the next query (change prefix from 'businessid_' to 'businessref_')
business_refs_for_query = [bid.replace('businessid_', 'businessref_') for bid in business_ids_with_wifi]

# Store results for later use in a dictionary and then convert to JSON string
result = {
    'highest_state': highest_state.to_dict() if isinstance(highest_state, pd.Series) else highest_state,
    'business_refs_for_query': business_refs_for_query
}
print("__RESULT__:")
print(json.dumps(result))"""

env_args = {'var_function-call-14800440221700262084': [{'_id': '6859a000fe8b31cd7362e2ab', 'business_id': 'businessid_49', 'attributes': {'WiFi': "u'no'"}, 'description': 'Located at 6901 Phelps Rd in Goleta, CA, this facility offers a nurturing environment for young learners, providing a range of services in Education, Elementary Schools, Child Care & Day Care, Local Services, Preschools, and Montessori Schools.'}, {'_id': '6859a000fe8b31cd7362e2b1', 'business_id': 'businessid_92', 'attributes': {'WiFi': "u'no'"}, 'description': 'Located at 690 W Dekalb Pike in King of Prussia, PA, this business offers a diverse range of services and products in the fields of Cosmetics & Beauty Supply, Cosmetic Dentists, Tanning, Teeth Whitening, Beauty & Spas, Dentists, Shopping, Blow Dry/Out Services, Health & Medical, Spray Tanning, and Hair Salons.'}, {'_id': '6859a000fe8b31cd7362e2b2', 'business_id': 'businessid_64', 'attributes': {'WiFi': "u'free'"}, 'description': 'Located at 12337 Olive Blvd in Creve Coeur, MO, this establishment offers a range of services in Nail Salons, Beauty & Spas.'}, {'_id': '6859a000fe8b31cd7362e2b7', 'business_id': 'businessid_54', 'attributes': {'WiFi': "u'free'"}, 'description': 'Located at 13151 Race Track Rd in Tampa, FL, this establishment offers a variety of services including Service Stations, Coffee & Tea, Gas Stations, Automotive, Gas Stations, Food, and Convenience Stores.'}, {'_id': '6859a000fe8b31cd7362e2ba', 'business_id': 'businessid_91', 'attributes': {'WiFi': "u'free'"}, 'description': 'Located at 1625 Baronne St in New Orleans, LA, this vibrant establishment offers a delightful array of options ranging from Food, Shaved Ice, Cajun/Creole, Breakfast & Brunch, Party & Event Planning, Comfort Food, Cafes, Restaurants, to Event Planning & Services, making it a perfect spot for any occasion.'}], 'var_function-call-8991307272850992448': [{'_id': '6859a000fe8b31cd7362e2ab', 'business_id': 'businessid_49', 'attributes': {'WiFi': "u'no'"}, 'description': 'Located at 6901 Phelps Rd in Goleta, CA, this facility offers a nurturing environment for young learners, providing a range of services in Education, Elementary Schools, Child Care & Day Care, Local Services, Preschools, and Montessori Schools.'}, {'_id': '6859a000fe8b31cd7362e2b1', 'business_id': 'businessid_92', 'attributes': {'WiFi': "u'no'"}, 'description': 'Located at 690 W Dekalb Pike in King of Prussia, PA, this business offers a diverse range of services and products in the fields of Cosmetics & Beauty Supply, Cosmetic Dentists, Tanning, Teeth Whitening, Beauty & Spas, Dentists, Shopping, Blow Dry/Out Services, Health & Medical, Spray Tanning, and Hair Salons.'}, {'_id': '6859a000fe8b31cd7362e2b2', 'business_id': 'businessid_64', 'attributes': {'WiFi': "u'free'"}, 'description': 'Located at 12337 Olive Blvd in Creve Coeur, MO, this establishment offers a range of services in Nail Salons, Beauty & Spas.'}, {'_id': '6859a000fe8b31cd7362e2b7', 'business_id': 'businessid_54', 'attributes': {'WiFi': "u'free'"}, 'description': 'Located at 13151 Race Track Rd in Tampa, FL, this establishment offers a variety of services including Service Stations, Coffee & Tea, Gas Stations, Automotive, Gas Stations, Food, and Convenience Stores.'}, {'_id': '6859a000fe8b31cd7362e2ba', 'business_id': 'businessid_91', 'attributes': {'WiFi': "u'free'"}, 'description': 'Located at 1625 Baronne St in New Orleans, LA, this vibrant establishment offers a delightful array of options ranging from Food, Shaved Ice, Cajun/Creole, Breakfast & Brunch, Party & Event Planning, Comfort Food, Cafes, Restaurants, to Event Planning & Services, making it a perfect spot for any occasion.'}]}

exec(code, env_args)
