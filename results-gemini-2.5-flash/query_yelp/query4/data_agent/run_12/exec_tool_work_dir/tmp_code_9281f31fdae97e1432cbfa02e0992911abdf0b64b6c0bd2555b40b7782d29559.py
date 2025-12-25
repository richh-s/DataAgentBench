code = """import pandas as pd
import json

# The result from query_db is a dictionary with a 'query_db_response' key, which contains a 'results' key.
# The 'results' key holds a list of strings, where the first string contains the actual JSON array.
raw_string_from_db = locals()['var_function-call-14973647755309781398']['query_db_response']['results'][0]

# Extract the JSON array string from the raw string. It typically starts with '[' and ends with ']'.
json_start_index = raw_string_from_db.find('[')
json_end_index = raw_string_from_db.rfind(']')

if json_start_index != -1 and json_end_index != -1:
    json_data_str = raw_string_from_db[json_start_index : json_end_index + 1]
    business_data = json.loads(json_data_str)
    df_business = pd.DataFrame(business_data)
else:
    print('__RESULT__:')
    print(json.dumps({'error': 'Could not extract JSON array from the business data string.'}))
    exit()

def extract_categories(description):
    if not isinstance(description, str):
        return []
    # Keywords to look for indicating the start of category listings
    start_phrases = ['services in ', 'including ']
    for phrase in start_phrases:
        if phrase in description:
            start_index = description.find(phrase) + len(phrase)
            # Extract the segment that likely contains categories, usually ending before a period.
            category_segment = description[start_index:].split('.')[0].strip()
            
            # Split by comma and clean each category item.
            categories = [cat.strip() for cat in category_segment.split(',') if cat.strip()]
            
            # Filter out common non-category words that might be parsed as categories
            cleaned_categories = [cat for cat in categories if cat.lower() not in [
                'and', 'or', 'etc', 'services', 'a range of', 'a wide range of', 'the',
                'facilities', 'products', 'facility offers', 'establishment offers',
                'premier destination for', 'young learners', 'nurturing environment for',
                'diverse range of services and', 'diverse range of services and products in the fields of'
            ]]
            return cleaned_categories
    return []

df_business['categories'] = df_business['description'].apply(extract_categories)

# Explode the DataFrame so that each category for a business gets its own row
df_exploded = df_business.explode('categories')
# Remove any rows where the category might be empty after cleaning or explosion
df_exploded = df_exploded[df_exploded['categories'] != '']

# Count the number of businesses for each unique category
category_counts = df_exploded['categories'].value_counts().reset_index()
category_counts.columns = ['category', 'business_count']

# Find the category with the highest number of businesses
most_common_category_info = category_counts.loc[category_counts['business_count'].idxmax()]
most_common_category_name = most_common_category_info['category']

# Get all business_ids associated with this most common category
business_ids_for_category = df_exploded[df_exploded['categories'] == most_common_category_name]['business_id'].tolist()

# Convert business_id format (e.g., "businessid_123") to business_ref format (e.g., "businessref_123")
# This is necessary for querying the 'review' table in the user_database.
business_refs_for_category = [bid.replace("businessid_", "businessref_") for bid in business_ids_for_category]

# Output the results for the next step
print('__RESULT__:')
print(json.dumps({
    'most_common_category_name': most_common_category_name,
    'business_refs_for_category': business_refs_for_category
}))"""

env_args = {'var_function-call-10183439632655763157': [{'_id': '6859a000fe8b31cd7362e2ab', 'business_id': 'businessid_49', 'name': 'Steps to Learning Montessori Preschool', 'review_count': '8', 'is_open': '1', 'attributes': {'BusinessAcceptsCreditCards': 'True', 'WiFi': "u'no'", 'BusinessAcceptsBitcoin': 'False'}, 'hours': {'Monday': '0:0-0:0', 'Tuesday': '8:0-17:0', 'Wednesday': '8:0-17:0', 'Thursday': '8:0-17:0', 'Friday': '8:0-17:0'}, 'description': 'Located at 6901 Phelps Rd in Goleta, CA, this facility offers a nurturing environment for young learners, providing a range of services in Education, Elementary Schools, Child Care & Day Care, Local Services, Preschools, and Montessori Schools.'}, {'_id': '6859a000fe8b31cd7362e2ac', 'business_id': 'businessid_47', 'name': 'Breeze Blow Dry Bar', 'review_count': '81', 'is_open': '0', 'attributes': {'ByAppointmentOnly': 'False', 'BusinessAcceptsCreditCards': 'True', 'GoodForKids': 'True', 'RestaurantsPriceRange2': '2', 'BikeParking': 'False', 'BusinessParking': "{'garage': False, 'street': False, 'validated': False, 'lot': True, 'valet': False}"}, 'hours': {'Monday': '7:0-18:0', 'Tuesday': '7:0-18:0', 'Wednesday': '7:0-18:0', 'Thursday': '7:0-18:0', 'Friday': '7:0-19:0', 'Saturday': '8:0-19:0', 'Sunday': '10:0-17:0'}, 'description': 'Located at 9916 Clayton Rd in St. Louis, MO, this establishment offers a wide range of services, including Hair Salons, Beauty & Spas, Hair Stylists, Skin Care, Blow Dry/Out Services, and Makeup Artists.'}, {'_id': '6859a000fe8b31cd7362e2ad', 'business_id': 'businessid_88', 'name': 'Impact Guns', 'review_count': '39', 'is_open': '1', 'attributes': {'BusinessParking': "{'garage': False, 'street': False, 'validated': False, 'lot': False, 'valet': False}", 'GoodForKids': 'True', 'BusinessAcceptsCreditCards': 'True', 'ByAppointmentOnly': 'False', 'BikeParking': 'True'}, 'hours': {'Monday': '10:0-19:0', 'Tuesday': '10:0-19:0', 'Wednesday': '10:0-19:0', 'Thursday': '10:0-19:0', 'Friday': '10:0-19:0', 'Saturday': '10:0-19:0'}, 'description': 'Located at 11655 W Executive Dr in Boise, ID, this facility offers enthusiasts a premier destination for Gun/Rifle Ranges, Active Life.'}, {'_id': '6859a000fe8b31cd7362e2ae', 'business_id': 'businessid_41', 'name': 'Palms Primary Care', 'review_count': '5', 'is_open': '1', 'attributes': 'None', 'hours': {'Monday': '8:30-17:0', 'Tuesday': '8:30-17:0', 'Wednesday': '8:30-17:0', 'Thursday': '8:30-17:0', 'Friday': '8:30-17:0'}, 'description': 'Located at 1615 Pasadena Ave S, Ste 430 in Saint Petersburg, FL, this facility offers a range of services in Internal Medicine, Doctors, Health & Medical.'}, {'_id': '6859a000fe8b31cd7362e2af', 'business_id': 'businessid_33', 'name': 'J&Q Nails', 'review_count': '28', 'is_open': '1', 'attributes': {'BusinessParking': "{'garage': False, 'street': False, 'validated': False, 'lot': False, 'valet': False}", 'BusinessAcceptsCreditCards': 'True', 'AcceptsInsurance': 'False', 'ByAppointmentOnly': 'False', 'RestaurantsPriceRange2': '2', 'WheelchairAccessible': 'True', 'BikeParking': 'False'}, 'hours': {'Monday': '9:30-19:0', 'Tuesday': '9:30-19:0', 'Wednesday': '9:30-19:0', 'Thursday': '9:30-19:0', 'Friday': '9:30-19:0', 'Saturday': '9:30-17:30'}, 'description': 'Located at 9655 E US Hwy 36, Unit H in Avon, IN, this establishment offers a range of services including Nail Salons, Hair Removal, Beauty & Spas, and Waxing.'}], 'var_function-call-14973647755309781398': [{'business_id': 'businessid_49', 'description': 'Located at 6901 Phelps Rd in Goleta, CA, this facility offers a nurturing environment for young learners, providing a range of services in Education, Elementary Schools, Child Care & Day Care, Local Services, Preschools, and Montessori Schools.'}, {'business_id': 'businessid_47', 'description': 'Located at 9916 Clayton Rd in St. Louis, MO, this establishment offers a wide range of services, including Hair Salons, Beauty & Spas, Hair Stylists, Skin Care, Blow Dry/Out Services, and Makeup Artists.'}, {'business_id': 'businessid_88', 'description': 'Located at 11655 W Executive Dr in Boise, ID, this facility offers enthusiasts a premier destination for Gun/Rifle Ranges, Active Life.'}, {'business_id': 'businessid_33', 'description': 'Located at 9655 E US Hwy 36, Unit H in Avon, IN, this establishment offers a range of services including Nail Salons, Hair Removal, Beauty & Spas, and Waxing.'}, {'business_id': 'businessid_92', 'description': 'Located at 690 W Dekalb Pike in King of Prussia, PA, this business offers a diverse range of services and products in the fields of Cosmetics & Beauty Supply, Cosmetic Dentists, Tanning, Teeth Whitening, Beauty & Spas, Dentists, Shopping, Blow Dry/Out Services, Health & Medical, Spray Tanning, and Hair Salons.'}]}

exec(code, env_args)
