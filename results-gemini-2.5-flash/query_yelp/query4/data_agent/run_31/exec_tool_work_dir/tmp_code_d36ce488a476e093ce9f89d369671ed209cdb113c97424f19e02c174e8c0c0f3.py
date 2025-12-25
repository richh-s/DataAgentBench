code = """import pandas as pd
import re
import json

# Access the full output of the query_db call, which is a dictionary
full_query_db_output = locals()['var_function-call-16253449884847113815']

# The actual list of results is under 'results' key within 'query_db_response'
# This 'results' is a list where each element is a string containing JSON data.
raw_json_strings = full_query_db_output['query_db_response']['results']

parsed_business_data = []
for json_string_with_metadata in raw_json_strings:
    # Use regex to extract the actual JSON array from the string
    match = re.search(r'\[.+\]', json_string_with_metadata, re.DOTALL)
    if match:
        json_array_str = match.group(0)
        try:
            # Load the JSON array string into a Python list of dictionaries
            parsed_business_data.extend(json.loads(json_array_str))
        except json.JSONDecodeError as e:
            print(f"Error decoding JSON from string: {e}")
            print(f"Problematic string excerpt: {json_array_str[:200]}...")

df_business = pd.DataFrame(parsed_business_data)

# Function to extract categories from description
def extract_categories(description):
    match = re.search(r'(?:providing a range of services in|offers a wide range of services, including|offers a range of services including|offers enthusiasts a premier destination for|offers a diverse range of services and products in the fields of) (.*)', description)
    if match:
        categories_str = match.group(1).strip()
        if categories_str.endswith('.'):
            categories_str = categories_str[:-1]
        return [cat.strip() for cat in categories_str.split(',')] if categories_str else []
    return []

df_business['categories'] = df_business['description'].apply(extract_categories)

# Explode categories to have one row per category
df_exploded = df_business.explode('categories')

# Convert business_id to business_ref format
df_exploded['business_ref'] = df_exploded['business_id'].str.replace('businessid_', 'businessref_')

# Filter out any empty categories that might have resulted from parsing issues
df_final_business = df_exploded[df_exploded['categories'] != ''].copy()

print('__RESULT__:')
print(df_final_business.to_json(orient='records'))"""

env_args = {'var_function-call-16277713404362704611': [{'_id': '6859a000fe8b31cd7362e2ab', 'business_id': 'businessid_49', 'name': 'Steps to Learning Montessori Preschool', 'review_count': '8', 'is_open': '1', 'attributes': {'BusinessAcceptsCreditCards': 'True', 'WiFi': "u'no'", 'BusinessAcceptsBitcoin': 'False'}, 'hours': {'Monday': '0:0-0:0', 'Tuesday': '8:0-17:0', 'Wednesday': '8:0-17:0', 'Thursday': '8:0-17:0', 'Friday': '8:0-17:0'}, 'description': 'Located at 6901 Phelps Rd in Goleta, CA, this facility offers a nurturing environment for young learners, providing a range of services in Education, Elementary Schools, Child Care & Day Care, Local Services, Preschools, and Montessori Schools.'}], 'var_function-call-6086026484184560441': [{'_id': '6859a000fe8b31cd7362e2ab', 'business_id': 'businessid_49', 'description': 'Located at 6901 Phelps Rd in Goleta, CA, this facility offers a nurturing environment for young learners, providing a range of services in Education, Elementary Schools, Child Care & Day Care, Local Services, Preschools, and Montessori Schools.'}, {'_id': '6859a000fe8b31cd7362e2ac', 'business_id': 'businessid_47', 'description': 'Located at 9916 Clayton Rd in St. Louis, MO, this establishment offers a wide range of services, including Hair Salons, Beauty & Spas, Hair Stylists, Skin Care, Blow Dry/Out Services, and Makeup Artists.'}, {'_id': '6859a000fe8b31cd7362e2ad', 'business_id': 'businessid_88', 'description': 'Located at 11655 W Executive Dr in Boise, ID, this facility offers enthusiasts a premier destination for Gun/Rifle Ranges, Active Life.'}, {'_id': '6859a000fe8b31cd7362e2af', 'business_id': 'businessid_33', 'description': 'Located at 9655 E US Hwy 36, Unit H in Avon, IN, this establishment offers a range of services including Nail Salons, Hair Removal, Beauty & Spas, and Waxing.'}, {'_id': '6859a000fe8b31cd7362e2b1', 'business_id': 'businessid_92', 'description': 'Located at 690 W Dekalb Pike in King of Prussia, PA, this business offers a diverse range of services and products in the fields of Cosmetics & Beauty Supply, Cosmetic Dentists, Tanning, Teeth Whitening, Beauty & Spas, Dentists, Shopping, Blow Dry/Out Services, Health & Medical, Spray Tanning, and Hair Salons.'}], 'var_function-call-16253449884847113815': [{'_id': '6859a000fe8b31cd7362e2ab', 'business_id': 'businessid_49', 'description': 'Located at 6901 Phelps Rd in Goleta, CA, this facility offers a nurturing environment for young learners, providing a range of services in Education, Elementary Schools, Child Care & Day Care, Local Services, Preschools, and Montessori Schools.'}, {'_id': '6859a000fe8b31cd7362e2ac', 'business_id': 'businessid_47', 'description': 'Located at 9916 Clayton Rd in St. Louis, MO, this establishment offers a wide range of services, including Hair Salons, Beauty & Spas, Hair Stylists, Skin Care, Blow Dry/Out Services, and Makeup Artists.'}, {'_id': '6859a000fe8b31cd7362e2ad', 'business_id': 'businessid_88', 'description': 'Located at 11655 W Executive Dr in Boise, ID, this facility offers enthusiasts a premier destination for Gun/Rifle Ranges, Active Life.'}, {'_id': '6859a000fe8b31cd7362e2af', 'business_id': 'businessid_33', 'description': 'Located at 9655 E US Hwy 36, Unit H in Avon, IN, this establishment offers a range of services including Nail Salons, Hair Removal, Beauty & Spas, and Waxing.'}, {'_id': '6859a000fe8b31cd7362e2b1', 'business_id': 'businessid_92', 'description': 'Located at 690 W Dekalb Pike in King of Prussia, PA, this business offers a diverse range of services and products in the fields of Cosmetics & Beauty Supply, Cosmetic Dentists, Tanning, Teeth Whitening, Beauty & Spas, Dentists, Shopping, Blow Dry/Out Services, Health & Medical, Spray Tanning, and Hair Salons.'}]}

exec(code, env_args)
