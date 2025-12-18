code = """import json
import re

def parse_description_for_categories(description_text):
    if not description_text:
        return []
    # The categories are usually after 'in the fields of' or similar phrases, or at the end of the string
    # I'll look for capitalized words that appear to be categories.
    # A more robust solution might involve a list of known categories or more complex NLP.
    
    # Extract text after 'services in' or 'fields of' or similar patterns
    match = re.search(r'(?:services in|fields of|including|offers a range of services|premier destination for|diverse range of services and products in the fields of)\s+([\w\s,&/\-]+(?:\band\b\s+[\w\s,&/\-]+)*)', description_text, re.IGNORECASE)
    if match:
        category_string = match.group(1)
    else:
        # If no specific pattern is found, try to extract capitalized words/phrases at the end
        category_string = description_text.split('.')[-1].strip()

    # Split by common delimiters and clean up
    categories = [cat.strip() for cat in re.split(r'[,&/]', category_string) if cat.strip()]
    
    # Further refinement: filter out location/non-category words if any simple ones are present
    # This is a very basic attempt and might need more sophistication depending on data variety
    categories = [cat for cat in categories if not any(word in cat.lower() for word in ['located at', 'unit', 'e us hwy', 'rd', 'dr', 'pike', 'st', 'mo', 'ca', 'id', 'pa', 'in', 'us', 'hwy', 'w', 'e', 's', 'n'])]
    
    # Final cleaning: remove leading/trailing spaces and empty strings
    return [cat.strip() for cat in categories if cat.strip()]

business_data = locals()['var_function-call-11309226368549867683']['results']

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

# Find the category with the largest number of businesses
most_common_category = None
max_businesses = 0

for category, count in business_categories.items():
    if count > max_businesses:
        max_businesses = count
        most_common_category = category

# Prepare the output
output = {
    "most_common_category": most_common_category,
    "max_businesses_in_category": max_businesses,
    "business_id_to_categories": business_id_to_categories
}

print("__RESULT__:")
print(json.dumps(output))"""

env_args = {'var_function-call-12894765245162637948': [{'_id': '6859a000fe8b31cd7362e2ab', 'attributes': {'BusinessAcceptsCreditCards': 'True', 'WiFi': "u'no'", 'BusinessAcceptsBitcoin': 'False'}, 'description': 'Located at 6901 Phelps Rd in Goleta, CA, this facility offers a nurturing environment for young learners, providing a range of services in Education, Elementary Schools, Child Care & Day Care, Local Services, Preschools, and Montessori Schools.'}], 'var_function-call-11309226368549867683': [{'_id': '6859a000fe8b31cd7362e2ab', 'business_id': 'businessid_49', 'description': 'Located at 6901 Phelps Rd in Goleta, CA, this facility offers a nurturing environment for young learners, providing a range of services in Education, Elementary Schools, Child Care & Day Care, Local Services, Preschools, and Montessori Schools.'}, {'_id': '6859a000fe8b31cd7362e2ac', 'business_id': 'businessid_47', 'description': 'Located at 9916 Clayton Rd in St. Louis, MO, this establishment offers a wide range of services, including Hair Salons, Beauty & Spas, Hair Stylists, Skin Care, Blow Dry/Out Services, and Makeup Artists.'}, {'_id': '6859a000fe8b31cd7362e2ad', 'business_id': 'businessid_88', 'description': 'Located at 11655 W Executive Dr in Boise, ID, this facility offers enthusiasts a premier destination for Gun/Rifle Ranges, Active Life.'}, {'_id': '6859a000fe8b31cd7362e2af', 'business_id': 'businessid_33', 'description': 'Located at 9655 E US Hwy 36, Unit H in Avon, IN, this establishment offers a range of services including Nail Salons, Hair Removal, Beauty & Spas, and Waxing.'}, {'_id': '6859a000fe8b31cd7362e2b1', 'business_id': 'businessid_92', 'description': 'Located at 690 W Dekalb Pike in King of Prussia, PA, this business offers a diverse range of services and products in the fields of Cosmetics & Beauty Supply, Cosmetic Dentists, Tanning, Teeth Whitening, Beauty & Spas, Dentists, Shopping, Blow Dry/Out Services, Health & Medical, Spray Tanning, and Hair Salons.'}]}

exec(code, env_args)
