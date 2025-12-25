code = """import pandas as pd
import re
import json

# Access the raw output from the first query_db call
business_data_raw_output = locals()['var_function-call-16253449884847113815']

# The actual list of results is directly under the key (not nested under 'query_db_response')
# This 'results' is a list where the first element is a string containing JSON data along with other text.
raw_string_from_db = business_data_raw_output['results'][0]

# Use regex to extract the actual JSON array from the string
# This regex should correctly find the outermost JSON array.
match = re.search(r'(\[.*?\])', raw_string_from_db, re.DOTALL)
json_array_str = match.group(1) if match else "[]"

parsed_business_data = []
try:
    # Load the JSON array string into a Python list of dictionaries
    parsed_business_data = json.loads(json_array_str)
except json.JSONDecodeError as e:
    # This print statement will help debug if there's a JSON parsing issue
    print(f"Error decoding JSON from string: {e}")
    print(f"Problematic string excerpt: {json_array_str[:500]}...")

df_business_credit_cards = pd.DataFrame(parsed_business_data)

# Function to extract categories from description
def extract_categories(description):
    match = re.search(r'(?:providing a range of services in|offers a wide range of services, including|offers a range of services including|offers enthusiasts a premier destination for|offers a diverse range of services and products in the fields of) (.*)', description)
    if match:
        categories_str = match.group(1).strip()
        if categories_str.endswith('.'):
            categories_str = categories_str[:-1]
        return [cat.strip() for cat in categories_str.split(',')] if categories_str else []
    return []

df_business_credit_cards['categories'] = df_business_credit_cards['description'].apply(extract_categories)

# Explode categories to have one row per category
df_exploded_categories = df_business_credit_cards.explode('categories')

# Convert business_id to business_ref format
df_exploded_categories['business_ref'] = df_exploded_categories['business_id'].str.replace('businessid_', 'businessref_')

# Filter out any empty categories that might have resulted from parsing issues
df_final_business_categories = df_exploded_categories[df_exploded_categories['categories'] != ''].copy()

print('__RESULT__:')
print(df_final_business_categories.to_json(orient='records'))"""

env_args = {'var_function-call-16277713404362704611': [{'_id': '6859a000fe8b31cd7362e2ab', 'business_id': 'businessid_49', 'name': 'Steps to Learning Montessori Preschool', 'review_count': '8', 'is_open': '1', 'attributes': {'BusinessAcceptsCreditCards': 'True', 'WiFi': "u'no'", 'BusinessAcceptsBitcoin': 'False'}, 'hours': {'Monday': '0:0-0:0', 'Tuesday': '8:0-17:0', 'Wednesday': '8:0-17:0', 'Thursday': '8:0-17:0', 'Friday': '8:0-17:0'}, 'description': 'Located at 6901 Phelps Rd in Goleta, CA, this facility offers a nurturing environment for young learners, providing a range of services in Education, Elementary Schools, Child Care & Day Care, Local Services, Preschools, and Montessori Schools.'}], 'var_function-call-6086026484184560441': [{'_id': '6859a000fe8b31cd7362e2ab', 'business_id': 'businessid_49', 'description': 'Located at 6901 Phelps Rd in Goleta, CA, this facility offers a nurturing environment for young learners, providing a range of services in Education, Elementary Schools, Child Care & Day Care, Local Services, Preschools, and Montessori Schools.'}, {'_id': '6859a000fe8b31cd7362e2ac', 'business_id': 'businessid_47', 'description': 'Located at 9916 Clayton Rd in St. Louis, MO, this establishment offers a wide range of services, including Hair Salons, Beauty & Spas, Hair Stylists, Skin Care, Blow Dry/Out Services, and Makeup Artists.'}, {'_id': '6859a000fe8b31cd7362e2ad', 'business_id': 'businessid_88', 'description': 'Located at 11655 W Executive Dr in Boise, ID, this facility offers enthusiasts a premier destination for Gun/Rifle Ranges, Active Life.'}, {'_id': '6859a000fe8b31cd7362e2af', 'business_id': 'businessid_33', 'description': 'Located at 9655 E US Hwy 36, Unit H in Avon, IN, this establishment offers a range of services including Nail Salons, Hair Removal, Beauty & Spas, and Waxing.'}, {'_id': '6859a000fe8b31cd7362e2b1', 'business_id': 'businessid_92', 'description': 'Located at 690 W Dekalb Pike in King of Prussia, PA, this business offers a diverse range of services and products in the fields of Cosmetics & Beauty Supply, Cosmetic Dentists, Tanning, Teeth Whitening, Beauty & Spas, Dentists, Shopping, Blow Dry/Out Services, Health & Medical, Spray Tanning, and Hair Salons.'}], 'var_function-call-16253449884847113815': [{'_id': '6859a000fe8b31cd7362e2ab', 'business_id': 'businessid_49', 'description': 'Located at 6901 Phelps Rd in Goleta, CA, this facility offers a nurturing environment for young learners, providing a range of services in Education, Elementary Schools, Child Care & Day Care, Local Services, Preschools, and Montessori Schools.'}, {'_id': '6859a000fe8b31cd7362e2ac', 'business_id': 'businessid_47', 'description': 'Located at 9916 Clayton Rd in St. Louis, MO, this establishment offers a wide range of services, including Hair Salons, Beauty & Spas, Hair Stylists, Skin Care, Blow Dry/Out Services, and Makeup Artists.'}, {'_id': '6859a000fe8b31cd7362e2ad', 'business_id': 'businessid_88', 'description': 'Located at 11655 W Executive Dr in Boise, ID, this facility offers enthusiasts a premier destination for Gun/Rifle Ranges, Active Life.'}, {'_id': '6859a000fe8b31cd7362e2af', 'business_id': 'businessid_33', 'description': 'Located at 9655 E US Hwy 36, Unit H in Avon, IN, this establishment offers a range of services including Nail Salons, Hair Removal, Beauty & Spas, and Waxing.'}, {'_id': '6859a000fe8b31cd7362e2b1', 'business_id': 'businessid_92', 'description': 'Located at 690 W Dekalb Pike in King of Prussia, PA, this business offers a diverse range of services and products in the fields of Cosmetics & Beauty Supply, Cosmetic Dentists, Tanning, Teeth Whitening, Beauty & Spas, Dentists, Shopping, Blow Dry/Out Services, Health & Medical, Spray Tanning, and Hair Salons.'}], 'var_function-call-2203831416668818230': 'file_storage/function-call-2203831416668818230.json'}

exec(code, env_args)
