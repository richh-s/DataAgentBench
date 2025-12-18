code = """import pandas as pd
import json
import re

# Access the single string element from the tool output
# The variable name is var_function-call-14776729787347464534
# The content is a dictionary, and we need to access its 'query_db_response' key, then 'results' key, then the first element of that list.
raw_string_output = locals()['var_function-call-14776729787347464534']['query_db_response']['results'][0]

businesses_credit_card_data = []

# Use regex to find the JSON array part, which starts with '[' and ends with ']'
# re.DOTALL is crucial for matching across multiple lines (e.g., if JSON is formatted with newlines)
match = re.search(r'\[.*\]', raw_string_output, re.DOTALL)

if match:
    json_array_string = match.group(0)
    try:
        parsed_list = json.loads(json_array_string)
        if isinstance(parsed_list, list):
            businesses_credit_card_data.extend(parsed_list)
        else:
            # If the parsed JSON is not a list, it\'s an unexpected format.
            print(f'Parsed JSON is not a list: {type(parsed_list)}')
    except json.JSONDecodeError as e:
        print(f'JSON Decode Error for extracted array part: {e} in string: {json_array_string[:500]}...')
else:
    print(f'Could not find JSON array pattern in raw string: {raw_string_output[:500]}...')

df_businesses = pd.DataFrame(businesses_credit_card_data)

# --- Category Extraction and Most Common Category Logic ---
def extract_categories_from_description(description):
    categories_start_phrases = [
        'services in ',
        'services, including ',
        'services and products in the fields of ',
        'premier destination for ',
        'services including ',
        'range of services including ',
        'wide range of services, including ',
        'diverse range of services and products in the fields of '
    ]
    
    extracted_text = ''
    description_lower = description.lower()
    for phrase in categories_start_phrases:
        if phrase in description_lower:
            extracted_text = description_lower.split(phrase, 1)[1]
            break
            
    if not extracted_text:
        return []

    # Clean up and split
    extracted_text = extracted_text.replace('.', '').strip()
    extracted_text = extracted_text.replace(' and ', ', ')
    categories = [cat.strip().title() for cat in extracted_text.split(',') if cat.strip()]
    return categories

df_businesses['categories'] = df_businesses['description'].apply(extract_categories_from_description)

all_categories = []
for index, row in df_businesses.iterrows():
    for category in row['categories']:
        all_categories.append({'business_id': row['business_id'], 'category': category})

if not all_categories:
    print('__RESULT__:')
    print(json.dumps({'most_common_category': None, 'business_refs': []}))
else:
    categories_df = pd.DataFrame(all_categories)
    category_counts = categories_df['category'].value_counts().reset_index()
    category_counts.columns = ['category', 'count']
    
    most_common_category_info = category_counts.loc[category_counts['count'].idxmax()]
    
    business_ids_for_most_common_category = categories_df[
        categories_df['category'] == most_common_category_info['category']
    ]['business_id'].tolist()

    # Transform business_id to business_ref for the user_database
    business_refs_for_most_common_category = [bid.replace('businessid_', 'businessref_') for bid in business_ids_for_most_common_category]

    print('__RESULT__:')
    print(json.dumps({
        'most_common_category': most_common_category_info['category'],
        'business_refs': business_refs_for_most_common_category
    }))"""

env_args = {'var_function-call-11159201518443473329': [{'_id': '6859a000fe8b31cd7362e2ab', 'business_id': 'businessid_49', 'name': 'Steps to Learning Montessori Preschool', 'review_count': '8', 'is_open': '1', 'attributes': {'BusinessAcceptsCreditCards': 'True', 'WiFi': "u'no'", 'BusinessAcceptsBitcoin': 'False'}, 'hours': {'Monday': '0:0-0:0', 'Tuesday': '8:0-17:0', 'Wednesday': '8:0-17:0', 'Thursday': '8:0-17:0', 'Friday': '8:0-17:0'}, 'description': 'Located at 6901 Phelps Rd in Goleta, CA, this facility offers a nurturing environment for young learners, providing a range of services in Education, Elementary Schools, Child Care & Day Care, Local Services, Preschools, and Montessori Schools.'}], 'var_function-call-7114287859614031209': [{'_id': '6859a000fe8b31cd7362e2ab', 'business_id': 'businessid_49', 'description': 'Located at 6901 Phelps Rd in Goleta, CA, this facility offers a nurturing environment for young learners, providing a range of services in Education, Elementary Schools, Child Care & Day Care, Local Services, Preschools, and Montessori Schools.'}, {'_id': '6859a000fe8b31cd7362e2ac', 'business_id': 'businessid_47', 'description': 'Located at 9916 Clayton Rd in St. Louis, MO, this establishment offers a wide range of services, including Hair Salons, Beauty & Spas, Hair Stylists, Skin Care, Blow Dry/Out Services, and Makeup Artists.'}, {'_id': '6859a000fe8b31cd7362e2ad', 'business_id': 'businessid_88', 'description': 'Located at 11655 W Executive Dr in Boise, ID, this facility offers enthusiasts a premier destination for Gun/Rifle Ranges, Active Life.'}, {'_id': '6859a000fe8b31cd7362e2af', 'business_id': 'businessid_33', 'description': 'Located at 9655 E US Hwy 36, Unit H in Avon, IN, this establishment offers a range of services including Nail Salons, Hair Removal, Beauty & Spas, and Waxing.'}, {'_id': '6859a000fe8b31cd7362e2b1', 'business_id': 'businessid_92', 'description': 'Located at 690 W Dekalb Pike in King of Prussia, PA, this business offers a diverse range of services and products in the fields of Cosmetics & Beauty Supply, Cosmetic Dentists, Tanning, Teeth Whitening, Beauty & Spas, Dentists, Shopping, Blow Dry/Out Services, Health & Medical, Spray Tanning, and Hair Salons.'}], 'var_function-call-14776729787347464534': [{'_id': '6859a000fe8b31cd7362e2ab', 'business_id': 'businessid_49', 'description': 'Located at 6901 Phelps Rd in Goleta, CA, this facility offers a nurturing environment for young learners, providing a range of services in Education, Elementary Schools, Child Care & Day Care, Local Services, Preschools, and Montessori Schools.'}, {'_id': '6859a000fe8b31cd7362e2ac', 'business_id': 'businessid_47', 'description': 'Located at 9916 Clayton Rd in St. Louis, MO, this establishment offers a wide range of services, including Hair Salons, Beauty & Spas, Hair Stylists, Skin Care, Blow Dry/Out Services, and Makeup Artists.'}, {'_id': '6859a000fe8b31cd7362e2ad', 'business_id': 'businessid_88', 'description': 'Located at 11655 W Executive Dr in Boise, ID, this facility offers enthusiasts a premier destination for Gun/Rifle Ranges, Active Life.'}, {'_id': '6859a000fe8b31cd7362e2af', 'business_id': 'businessid_33', 'description': 'Located at 9655 E US Hwy 36, Unit H in Avon, IN, this establishment offers a range of services including Nail Salons, Hair Removal, Beauty & Spas, and Waxing.'}, {'_id': '6859a000fe8b31cd7362e2b1', 'business_id': 'businessid_92', 'description': 'Located at 690 W Dekalb Pike in King of Prussia, PA, this business offers a diverse range of services and products in the fields of Cosmetics & Beauty Supply, Cosmetic Dentists, Tanning, Teeth Whitening, Beauty & Spas, Dentists, Shopping, Blow Dry/Out Services, Health & Medical, Spray Tanning, and Hair Salons.'}]}

exec(code, env_args)
