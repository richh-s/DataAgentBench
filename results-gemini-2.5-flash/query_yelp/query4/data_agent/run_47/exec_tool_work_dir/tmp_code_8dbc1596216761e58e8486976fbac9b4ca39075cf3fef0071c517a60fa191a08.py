code = """import pandas as pd
import json

# Access the raw string output from the previous tool call
raw_output = locals()['var_function-call-267018790299620375']['query_db_response']['results'][0]

# Find the starting point of the actual JSON array string
json_start_index = raw_output.find('[{')

# Extract the JSON array string
business_data_json_str = raw_output[json_start_index:].strip()

# Load the JSON string into a Python list of dictionaries
business_data = json.loads(business_data_json_str)
df_business = pd.DataFrame(business_data)

# Function to extract categories from description field
def extract_categories(description):
    if isinstance(description, str):
        patterns = [
            'in the fields of',
            'services in',
            'offers a range of services, including',
            'offers a diverse range of services and products in the fields of',
            'offers a range of services including'
        ]
        for pattern in patterns:
            if pattern in description:
                parts = description.split(pattern)
                if len(parts) > 1:
                    categories_str = parts[1].strip().replace('.', '')
                    return [cat.strip() for cat in categories_str.split(',')]
    return []

df_business['categories'] = df_business['description'].apply(extract_categories)

# Explode the categories list to have one row per category
df_exploded_categories = df_business.explode('categories')

# Remove any empty or whitespace-only categories
df_exploded_categories = df_exploded_categories[df_exploded_categories['categories'].str.strip() != '']

# Count businesses per category
category_counts = df_exploded_categories['categories'].value_counts().reset_index()
category_counts.columns = ['category', 'business_count']

# Get the category with the largest number of businesses
top_category = category_counts.iloc[0]['category']

# Get business_ids for the top category
top_category_business_ids_raw = df_exploded_categories[df_exploded_categories['categories'] == top_category]['business_id'].tolist()

# Reformat business_ids for the SQL query (replace 'businessid_' with 'businessref_')
top_category_business_ids = [bid.replace('businessid_', 'businessref_') for bid in top_category_business_ids_raw]

print('__RESULT__:')
print(json.dumps({'top_category': top_category, 'top_category_business_ids': top_category_business_ids}))"""

env_args = {'var_function-call-90151162188380415': ['checkin', 'business'], 'var_function-call-267018790299620375': [{'_id': '6859a000fe8b31cd7362e2ab', 'business_id': 'businessid_49', 'description': 'Located at 6901 Phelps Rd in Goleta, CA, this facility offers a nurturing environment for young learners, providing a range of services in Education, Elementary Schools, Child Care & Day Care, Local Services, Preschools, and Montessori Schools.'}, {'_id': '6859a000fe8b31cd7362e2ac', 'business_id': 'businessid_47', 'description': 'Located at 9916 Clayton Rd in St. Louis, MO, this establishment offers a wide range of services, including Hair Salons, Beauty & Spas, Hair Stylists, Skin Care, Blow Dry/Out Services, and Makeup Artists.'}, {'_id': '6859a000fe8b31cd7362e2ad', 'business_id': 'businessid_88', 'description': 'Located at 11655 W Executive Dr in Boise, ID, this facility offers enthusiasts a premier destination for Gun/Rifle Ranges, Active Life.'}, {'_id': '6859a000fe8b31cd7362e2af', 'business_id': 'businessid_33', 'description': 'Located at 9655 E US Hwy 36, Unit H in Avon, IN, this establishment offers a range of services including Nail Salons, Hair Removal, Beauty & Spas, and Waxing.'}, {'_id': '6859a000fe8b31cd7362e2b1', 'business_id': 'businessid_92', 'description': 'Located at 690 W Dekalb Pike in King of Prussia, PA, this business offers a diverse range of services and products in the fields of Cosmetics & Beauty Supply, Cosmetic Dentists, Tanning, Teeth Whitening, Beauty & Spas, Dentists, Shopping, Blow Dry/Out Services, Health & Medical, Spray Tanning, and Hair Salons.'}]}

exec(code, env_args)
