code = """import json
import re

def parse_description_for_categories(description_text):
    if not description_text:
        return []
    
    patterns = [
        r'(?:services in|fields of|including|offers a range of services|premier destination for|diverse range of services and products in the fields of)\s+([\w\s,&/\-]+(?:\band\b\s+[\w\s,&/\-]+)*)',
        r'\b(?:in|of)\s+([A-Z][a-zA-Z0-9\s,&/-]+(?:\s+and\s+[A-Z][a-zA-Z0-9\s,&/-]+)*)\s*\.'
    ]
    
    category_string = ""
    for pattern in patterns:
        match = re.search(pattern, description_text, re.IGNORECASE)
        if match:
            category_string = match.group(1).strip()
            break

    if not category_string:
        parts = description_text.split('.')
        if parts:
            last_part = parts[-1].strip()
            if last_part:
                potential_categories = re.findall(r'[A-Z][a-z]+(?:\s+[A-Z][a-z]+)*', last_part)
                category_string = ', '.join(potential_categories)

    if not category_string:
        return []

    categories = [cat.strip() for cat in re.split(r'[,&/]', category_string) if cat.strip()]
    
    non_category_keywords = [
        'located at', 'unit', 'rd', 'dr', 'pike', 'st', 'mo', 'ca', 'id', 'pa', 'in', 'us', 'hwy',
        'w', 'e', 's', 'n', 'facility', 'establishment', 'destination', 'business', 'environment',
        'range', 'wide', 'diverse', 'services', 'products', 'fields', 'including', 'etc'
    ]
    categories = [cat for cat in categories if not any(keyword in cat.lower() for keyword in non_category_keywords)]
    
    return [cat.strip() for cat in categories if cat.strip()]

# The raw output from query_db is a dictionary containing a 'query_db_response' key, 
# which then contains a 'results' key that holds a list of strings.
# The actual JSON data we need is embedded within the first string of this 'results' list.
raw_output_dict = locals()['var_function-call-15140377174569186594']
raw_output_string = raw_output_dict['query_db_response']['results'][0]

# Extract the JSON array string from the raw output string
# It is typically enclosed in square brackets and contains JSON objects.
json_match = re.search(r'\[.*\]', raw_output_string, re.DOTALL)

business_data = []
if json_match:
    json_string = json_match.group(0)
    business_data = json.loads(json_string)

business_categories = {}
business_id_to_categories = {}

for record in business_data:
    business_id = record['business_id']
    description = record['description']
    
    categories = parse_description_for_categories(description)
    business_id_to_categories[business_id] = categories

    for category in categories:
        if category not in business_categories:
            business_categories[category] = 0
        business_categories[category] += 1

most_common_category = None
max_businesses = 0

for category, count in business_categories.items():
    if count > max_businesses:
        max_businesses = count
        most_common_category = category

# Get all business_ids for the most common category
business_ids_for_most_common_category = []
if most_common_category:
    for business_id, categories_list in business_id_to_categories.items():
        if most_common_category in categories_list:
            business_ids_for_most_common_category.append(business_id)

# Convert business_id to business_ref format for the next query to user_database
business_refs_for_most_common_category = []
for bid in business_ids_for_most_common_category:
    business_refs_for_most_common_category.append(bid.replace('businessid_', 'businessref_'))

output = {
    "most_common_category": most_common_category,
    "max_businesses_in_category": max_businesses,
    "business_refs_for_most_common_category": business_refs_for_most_common_category
}

print("__RESULT__:")
print(json.dumps(output))"""

env_args = {'var_function-call-12894765245162637948': [{'_id': '6859a000fe8b31cd7362e2ab', 'attributes': {'BusinessAcceptsCreditCards': 'True', 'WiFi': "u'no'", 'BusinessAcceptsBitcoin': 'False'}, 'description': 'Located at 6901 Phelps Rd in Goleta, CA, this facility offers a nurturing environment for young learners, providing a range of services in Education, Elementary Schools, Child Care & Day Care, Local Services, Preschools, and Montessori Schools.'}], 'var_function-call-11309226368549867683': [{'_id': '6859a000fe8b31cd7362e2ab', 'business_id': 'businessid_49', 'description': 'Located at 6901 Phelps Rd in Goleta, CA, this facility offers a nurturing environment for young learners, providing a range of services in Education, Elementary Schools, Child Care & Day Care, Local Services, Preschools, and Montessori Schools.'}, {'_id': '6859a000fe8b31cd7362e2ac', 'business_id': 'businessid_47', 'description': 'Located at 9916 Clayton Rd in St. Louis, MO, this establishment offers a wide range of services, including Hair Salons, Beauty & Spas, Hair Stylists, Skin Care, Blow Dry/Out Services, and Makeup Artists.'}, {'_id': '6859a000fe8b31cd7362e2ad', 'business_id': 'businessid_88', 'description': 'Located at 11655 W Executive Dr in Boise, ID, this facility offers enthusiasts a premier destination for Gun/Rifle Ranges, Active Life.'}, {'_id': '6859a000fe8b31cd7362e2af', 'business_id': 'businessid_33', 'description': 'Located at 9655 E US Hwy 36, Unit H in Avon, IN, this establishment offers a range of services including Nail Salons, Hair Removal, Beauty & Spas, and Waxing.'}, {'_id': '6859a000fe8b31cd7362e2b1', 'business_id': 'businessid_92', 'description': 'Located at 690 W Dekalb Pike in King of Prussia, PA, this business offers a diverse range of services and products in the fields of Cosmetics & Beauty Supply, Cosmetic Dentists, Tanning, Teeth Whitening, Beauty & Spas, Dentists, Shopping, Blow Dry/Out Services, Health & Medical, Spray Tanning, and Hair Salons.'}], 'var_function-call-15140377174569186594': [{'_id': '6859a000fe8b31cd7362e2ab', 'business_id': 'businessid_49', 'description': 'Located at 6901 Phelps Rd in Goleta, CA, this facility offers a nurturing environment for young learners, providing a range of services in Education, Elementary Schools, Child Care & Day Care, Local Services, Preschools, and Montessori Schools.'}, {'_id': '6859a000fe8b31cd7362e2ac', 'business_id': 'businessid_47', 'description': 'Located at 9916 Clayton Rd in St. Louis, MO, this establishment offers a wide range of services, including Hair Salons, Beauty & Spas, Hair Stylists, Skin Care, Blow Dry/Out Services, and Makeup Artists.'}, {'_id': '6859a000fe8b31cd7362e2ad', 'business_id': 'businessid_88', 'description': 'Located at 11655 W Executive Dr in Boise, ID, this facility offers enthusiasts a premier destination for Gun/Rifle Ranges, Active Life.'}, {'_id': '6859a000fe8b31cd7362e2af', 'business_id': 'businessid_33', 'description': 'Located at 9655 E US Hwy 36, Unit H in Avon, IN, this establishment offers a range of services including Nail Salons, Hair Removal, Beauty & Spas, and Waxing.'}, {'_id': '6859a000fe8b31cd7362e2b1', 'business_id': 'businessid_92', 'description': 'Located at 690 W Dekalb Pike in King of Prussia, PA, this business offers a diverse range of services and products in the fields of Cosmetics & Beauty Supply, Cosmetic Dentists, Tanning, Teeth Whitening, Beauty & Spas, Dentists, Shopping, Blow Dry/Out Services, Health & Medical, Spray Tanning, and Hair Salons.'}]}

exec(code, env_args)
