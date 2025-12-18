code = """import pandas as pd
import re
import json

# The raw output from query_db is a dictionary.
# The actual data is within 'query_db_response' -> 'results'.
# 'results' is a list, and its first (and likely only) element is a string that contains the JSON array.
full_output_string = locals()['var_function-call-1556772238026997466']['query_db_response']['results'][0]

# Use a regular expression to find the JSON array part robustly within the string
# This pattern looks for an opening square bracket, then any characters (non-greedy), then a closing square bracket.
# re.DOTALL is crucial here to match across newlines.
json_match = re.search(r'\[.*?\]', full_output_string, re.DOTALL)

businesses_credit_card_data = []
if json_match:
    json_array_string = json_match.group(0)
    businesses_credit_card_data = json.loads(json_array_string)
else:
    # If no JSON array is found, return an error message.
    print('__RESULT__:')
    print(json.dumps({'error': 'Failed to extract JSON array from query_db result string.'}))
    exit()

df_businesses = pd.DataFrame(businesses_credit_card_data)

# Function to extract categories from the description field
def extract_categories(description):
    # This regex looks for 'services in ' followed by one or more characters (non-greedy) up to a period.
    match = re.search(r'services in (.+?)[.]', description)
    if match:
        categories_str = match.group(1)
        # Split the extracted string by comma and strip whitespace from each category
        return [cat.strip() for cat in categories_str.split(',')]
    return []

# Apply the category extraction function to the 'description' column
df_businesses['categories'] = df_businesses['description'].apply(extract_categories)

# Explode the DataFrame so that each category for a business gets its own row
df_exploded = df_businesses.explode('categories')

# Count the number of businesses in each category
category_counts = df_exploded['categories'].value_counts().reset_index()
category_counts.columns = ['category', 'business_count']

# Find the category with the highest business count
most_common_category_info = category_counts.loc[category_counts['business_count'].idxmax()]
most_common_category = most_common_category_info['category']

# Filter the exploded DataFrame to get businesses only in the most common category
filtered_businesses = df_exploded[df_exploded['categories'] == most_common_category]
business_ids_in_category = filtered_businesses['business_id'].tolist()

# Convert the MongoDB 'business_id' format to the DuckDB 'business_ref' format
formatted_business_refs = []
for bid in business_ids_in_category:
    # Ensure the business ID starts with 'businessid_' before attempting to split
    if bid.startswith('businessid_'):
        # Split once to get the numerical part after 'businessid_'
        numeric_id = bid.split('businessid_', 1)[1]
        formatted_business_refs.append(f"businessref_{numeric_id}")
    else:
        # If for some reason the prefix is missing or different, keep it as is
        formatted_business_refs.append(bid)

# Output the most common category and the list of formatted business references
print('__RESULT__:')
print(json.dumps({
    'most_common_category': most_common_category,
    'business_refs_for_category': formatted_business_refs
}))"""

env_args = {'var_function-call-5222115913669914479': [{'_id': '6859a000fe8b31cd7362e2ab', 'business_id': 'businessid_49', 'name': 'Steps to Learning Montessori Preschool', 'review_count': '8', 'is_open': '1', 'attributes': {'BusinessAcceptsCreditCards': 'True', 'WiFi': "u'no'", 'BusinessAcceptsBitcoin': 'False'}, 'hours': {'Monday': '0:0-0:0', 'Tuesday': '8:0-17:0', 'Wednesday': '8:0-17:0', 'Thursday': '8:0-17:0', 'Friday': '8:0-17:0'}, 'description': 'Located at 6901 Phelps Rd in Goleta, CA, this facility offers a nurturing environment for young learners, providing a range of services in Education, Elementary Schools, Child Care & Day Care, Local Services, Preschools, and Montessori Schools.'}, {'_id': '6859a000fe8b31cd7362e2ac', 'business_id': 'businessid_47', 'name': 'Breeze Blow Dry Bar', 'review_count': '81', 'is_open': '0', 'attributes': {'ByAppointmentOnly': 'False', 'BusinessAcceptsCreditCards': 'True', 'GoodForKids': 'True', 'RestaurantsPriceRange2': '2', 'BikeParking': 'False', 'BusinessParking': "{'garage': False, 'street': False, 'validated': False, 'lot': True, 'valet': False}"}, 'hours': {'Monday': '7:0-18:0', 'Tuesday': '7:0-18:0', 'Wednesday': '7:0-18:0', 'Thursday': '7:0-18:0', 'Friday': '7:0-19:0', 'Saturday': '8:0-19:0', 'Sunday': '10:0-17:0'}, 'description': 'Located at 9916 Clayton Rd in St. Louis, MO, this establishment offers a wide range of services, including Hair Salons, Beauty & Spas, Hair Stylists, Skin Care, Blow Dry/Out Services, and Makeup Artists.'}, {'_id': '6859a000fe8b31cd7362e2ad', 'business_id': 'businessid_88', 'name': 'Impact Guns', 'review_count': '39', 'is_open': '1', 'attributes': {'BusinessParking': "{'garage': False, 'street': False, 'validated': False, 'lot': False, 'valet': False}", 'GoodForKids': 'True', 'BusinessAcceptsCreditCards': 'True', 'ByAppointmentOnly': 'False', 'BikeParking': 'True'}, 'hours': {'Monday': '10:0-19:0', 'Tuesday': '10:0-19:0', 'Wednesday': '10:0-19:0', 'Thursday': '10:0-19:0', 'Friday': '10:0-19:0', 'Saturday': '10:0-19:0'}, 'description': 'Located at 11655 W Executive Dr in Boise, ID, this facility offers enthusiasts a premier destination for Gun/Rifle Ranges, Active Life.'}, {'_id': '6859a000fe8b31cd7362e2ae', 'business_id': 'businessid_41', 'name': 'Palms Primary Care', 'review_count': '5', 'is_open': '1', 'attributes': 'None', 'hours': {'Monday': '8:30-17:0', 'Tuesday': '8:30-17:0', 'Wednesday': '8:30-17:0', 'Thursday': '8:30-17:0', 'Friday': '8:30-17:0'}, 'description': 'Located at 1615 Pasadena Ave S, Ste 430 in Saint Petersburg, FL, this facility offers a range of services in Internal Medicine, Doctors, Health & Medical.'}, {'_id': '6859a000fe8b31cd7362e2af', 'business_id': 'businessid_33', 'name': 'J&Q Nails', 'review_count': '28', 'is_open': '1', 'attributes': {'BusinessParking': "{'garage': False, 'street': False, 'validated': False, 'lot': False, 'valet': False}", 'BusinessAcceptsCreditCards': 'True', 'AcceptsInsurance': 'False', 'ByAppointmentOnly': 'False', 'RestaurantsPriceRange2': '2', 'WheelchairAccessible': 'True', 'BikeParking': 'False'}, 'hours': {'Monday': '9:30-19:0', 'Tuesday': '9:30-19:0', 'Wednesday': '9:30-19:0', 'Thursday': '9:30-19:0', 'Friday': '9:30-19:0', 'Saturday': '9:30-17:30'}, 'description': 'Located at 9655 E US Hwy 36, Unit H in Avon, IN, this establishment offers a range of services including Nail Salons, Hair Removal, Beauty & Spas, and Waxing.'}], 'var_function-call-1556772238026997466': [{'business_id': 'businessid_49', 'description': 'Located at 6901 Phelps Rd in Goleta, CA, this facility offers a nurturing environment for young learners, providing a range of services in Education, Elementary Schools, Child Care & Day Care, Local Services, Preschools, and Montessori Schools.'}, {'business_id': 'businessid_47', 'description': 'Located at 9916 Clayton Rd in St. Louis, MO, this establishment offers a wide range of services, including Hair Salons, Beauty & Spas, Hair Stylists, Skin Care, Blow Dry/Out Services, and Makeup Artists.'}, {'business_id': 'businessid_88', 'description': 'Located at 11655 W Executive Dr in Boise, ID, this facility offers enthusiasts a premier destination for Gun/Rifle Ranges, Active Life.'}, {'business_id': 'businessid_33', 'description': 'Located at 9655 E US Hwy 36, Unit H in Avon, IN, this establishment offers a range of services including Nail Salons, Hair Removal, Beauty & Spas, and Waxing.'}, {'business_id': 'businessid_92', 'description': 'Located at 690 W Dekalb Pike in King of Prussia, PA, this business offers a diverse range of services and products in the fields of Cosmetics & Beauty Supply, Cosmetic Dentists, Tanning, Teeth Whitening, Beauty & Spas, Dentists, Shopping, Blow Dry/Out Services, Health & Medical, Spray Tanning, and Hair Salons.'}]}

exec(code, env_args)
