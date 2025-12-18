code = """import pandas as pd
import json
import re

businesses_with_wifi = []

# The result from query_db is a list of strings, where each string is a JSON representation of a list of business records.
# We need to parse each string into a list, and then iterate through the business records within that list.
for json_list_str in locals()['var_function-call-10940338859333470323'][0].get('query_db_response', {}).get('results', []):
    business_records = json.loads(json_list_str)
    for business_data in business_records:
        wifi_attribute = business_data.get('attributes', {}).get('WiFi')
        
        # Filter for businesses that actually offer WiFi (not 'no' or u'no')
        if wifi_attribute and wifi_attribute not in ["u'no'", "no"]:
            description = business_data.get('description', '')
            state = None
            
            # Regex to find the pattern "in City, ST" or similar
            # This looks for 'in ' followed by any characters (not comma), then a comma, then space, then two uppercase letters
            match = re.search(r'in [^,]+,\s*([A-Z]{2})(?:,|$|\s)', description)
            if match:
                state = match.group(1)
            
            if state:
                businesses_with_wifi.append({'business_id': business_data['business_id'], 'state': state})

df_businesses_with_wifi = pd.DataFrame(businesses_with_wifi)

if not df_businesses_with_wifi.empty:
    state_counts = df_businesses_with_wifi['state'].value_counts()
    most_common_state = state_counts.index[0]
    most_common_state_count = state_counts.iloc[0]

    filtered_businesses = df_businesses_with_wifi[df_businesses_with_wifi['state'] == most_common_state]
    business_ids_in_state = filtered_businesses['business_id'].tolist()
    
    # Convert business_id to business_ref format for the review database
    business_refs_in_state = [bid.replace("businessid_", "businessref_") for bid in business_ids_in_state]

    print('__RESULT__:')
    print(json.dumps({'most_common_state': most_common_state, 
                      'most_common_state_count': int(most_common_state_count), 
                      'business_ids_in_state': business_ids_in_state,
                      'business_refs_in_state': business_refs_in_state}))
else:
    print('__RESULT__:')
    print(json.dumps({'most_common_state': None, 'most_common_state_count': 0, 'business_ids_in_state': [], 'business_refs_in_state': []}))"""

env_args = {'var_function-call-16459610088306211483': [{'_id': '6859a000fe8b31cd7362e2ab', 'business_id': 'businessid_49', 'attributes': {'WiFi': "u'no'"}, 'description': 'Located at 6901 Phelps Rd in Goleta, CA, this facility offers a nurturing environment for young learners, providing a range of services in Education, Elementary Schools, Child Care & Day Care, Local Services, Preschools, and Montessori Schools.'}, {'_id': '6859a000fe8b31cd7362e2b1', 'business_id': 'businessid_92', 'attributes': {'WiFi': "u'no'"}, 'description': 'Located at 690 W Dekalb Pike in King of Prussia, PA, this business offers a diverse range of services and products in the fields of Cosmetics & Beauty Supply, Cosmetic Dentists, Tanning, Teeth Whitening, Beauty & Spas, Dentists, Shopping, Blow Dry/Out Services, Health & Medical, Spray Tanning, and Hair Salons.'}, {'_id': '6859a000fe8b31cd7362e2b2', 'business_id': 'businessid_64', 'attributes': {'WiFi': "u'free'"}, 'description': 'Located at 12337 Olive Blvd in Creve Coeur, MO, this establishment offers a range of services in Nail Salons, Beauty & Spas.'}, {'_id': '6859a000fe8b31cd7362e2b7', 'business_id': 'businessid_54', 'attributes': {'WiFi': "u'free'"}, 'description': 'Located at 13151 Race Track Rd in Tampa, FL, this establishment offers a variety of services including Service Stations, Coffee & Tea, Gas Stations, Automotive, Gas Stations, Food, and Convenience Stores.'}, {'_id': '6859a000fe8b31cd7362e2ba', 'business_id': 'businessid_91', 'attributes': {'WiFi': "u'free'"}, 'description': 'Located at 1625 Baronne St in New Orleans, LA, this vibrant establishment offers a delightful array of options ranging from Food, Shaved Ice, Cajun/Creole, Breakfast & Brunch, Party & Event Planning, Comfort Food, Cafes, Restaurants, to Event Planning & Services, making it a perfect spot for any occasion.'}], 'var_function-call-13209304622312942091': {'most_common_state': None, 'most_common_state_count': 0, 'business_ids_in_state': []}, 'var_function-call-10940338859333470323': [{'_id': '6859a000fe8b31cd7362e2ab', 'business_id': 'businessid_49', 'attributes': {'WiFi': "u'no'"}, 'description': 'Located at 6901 Phelps Rd in Goleta, CA, this facility offers a nurturing environment for young learners, providing a range of services in Education, Elementary Schools, Child Care & Day Care, Local Services, Preschools, and Montessori Schools.'}, {'_id': '6859a000fe8b31cd7362e2b1', 'business_id': 'businessid_92', 'attributes': {'WiFi': "u'no'"}, 'description': 'Located at 690 W Dekalb Pike in King of Prussia, PA, this business offers a diverse range of services and products in the fields of Cosmetics & Beauty Supply, Cosmetic Dentists, Tanning, Teeth Whitening, Beauty & Spas, Dentists, Shopping, Blow Dry/Out Services, Health & Medical, Spray Tanning, and Hair Salons.'}, {'_id': '6859a000fe8b31cd7362e2b2', 'business_id': 'businessid_64', 'attributes': {'WiFi': "u'free'"}, 'description': 'Located at 12337 Olive Blvd in Creve Coeur, MO, this establishment offers a range of services in Nail Salons, Beauty & Spas.'}, {'_id': '6859a000fe8b31cd7362e2b7', 'business_id': 'businessid_54', 'attributes': {'WiFi': "u'free'"}, 'description': 'Located at 13151 Race Track Rd in Tampa, FL, this establishment offers a variety of services including Service Stations, Coffee & Tea, Gas Stations, Automotive, Gas Stations, Food, and Convenience Stores.'}, {'_id': '6859a000fe8b31cd7362e2ba', 'business_id': 'businessid_91', 'attributes': {'WiFi': "u'free'"}, 'description': 'Located at 1625 Baronne St in New Orleans, LA, this vibrant establishment offers a delightful array of options ranging from Food, Shaved Ice, Cajun/Creole, Breakfast & Brunch, Party & Event Planning, Comfort Food, Cafes, Restaurants, to Event Planning & Services, making it a perfect spot for any occasion.'}], 'var_function-call-2171371082411261723': {'most_common_state': None, 'most_common_state_count': 0, 'business_ids_in_state': []}, 'var_function-call-16837304070296463667': {'most_common_state': None, 'most_common_state_count': 0, 'business_ids_in_state': [], 'business_refs_in_state': []}, 'var_function-call-1781243808930433701': {'most_common_state': None, 'most_common_state_count': 0, 'business_ids_in_state': [], 'business_refs_in_state': []}, 'var_function-call-14983487006339177246': {'most_common_state': None, 'most_common_state_count': 0, 'business_ids_in_state': [], 'business_refs_in_state': []}, 'var_function-call-7669751082835840629': {'most_common_state': None, 'most_common_state_count': 0, 'business_ids_in_state': [], 'business_refs_in_state': []}, 'var_function-call-14920764576787354622': {'most_common_state': None, 'most_common_state_count': 0, 'business_ids_in_state': [], 'business_refs_in_state': []}, 'var_function-call-15445155587090315162': {'most_common_state': None, 'most_common_state_count': 0, 'business_ids_in_state': [], 'business_refs_in_state': []}, 'var_function-call-15317122708512539741': {'most_common_state': None, 'most_common_state_count': 0, 'business_ids_in_state': [], 'business_refs_in_state': []}, 'var_function-call-9917076592845081378': {'most_common_state': None, 'most_common_state_count': 0, 'business_ids_in_state': [], 'business_refs_in_state': []}}

exec(code, env_args)
