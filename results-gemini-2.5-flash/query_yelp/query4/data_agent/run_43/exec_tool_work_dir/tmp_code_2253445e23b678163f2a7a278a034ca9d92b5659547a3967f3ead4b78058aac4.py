code = """import pandas as pd
import json
import re

businesses_data = locals()['var_function-call-9141377590365096836']

credit_card_businesses_with_categories = []

for business in businesses_data:
    business_id = business['business_id']
    description = business.get('description', '')
    
    categories_list = []
    
    # Pattern 1: 'in <Category1>, <Category2>, and <Category3>.'
    match1 = re.search(r"in (?:Education|services|the fields of|including)\s+([a-zA-Z0-9&,\s]+?)(?:\.|for all your|to meet all your|perfect for|for any|to meet)", description)
    if match1:
        categories_str = match1.group(1).replace("\'", "").strip()
        categories_list.extend([c.strip() for c in re.split(r',\s*|\s*and\s+', categories_str) if c.strip()])

    # Fallback to a broader pattern if no categories are found with previous patterns
    if not categories_list:
        # Try to find common phrases indicating categories, typically at the end of the description
        match_gen = re.search(r'(?:in|including|of)\s+([A-Za-z0-9&,\s\-]+?)\.', description)
        if match_gen:
            categories_str = match_gen.group(1).replace("\'", "").strip()
            categories_list.extend([c.strip() for c in re.split(r',\s*|\s*and\s+', categories_str) if c.strip()])

    for category in categories_list:
        if category:
            credit_card_businesses_with_categories.append({'business_id': business_id, 'category': category})

df_credit_card_businesses = pd.DataFrame(credit_card_businesses_with_categories)

# Count businesses per category
category_counts = df_credit_card_businesses.groupby('category').agg(num_businesses=('business_id', 'nunique')).reset_index()

# Find the category with the largest number of businesses
top_category = category_counts.loc[category_counts['num_businesses'].idxmax()]

# Get business_ids for the top category
top_category_name = top_category['category']
business_ids_in_top_category_df = df_credit_card_businesses[df_credit_card_businesses['category'] == top_category_name]['business_id']

# Prepare business_ids for SQL query (add prefix and convert to tuple/list)
business_ids_for_sql = tuple([bid.replace("businessid_", "businessref_") for bid in business_ids_in_top_category_df])

result = {
    "top_category_name": top_category_name,
    "num_businesses": int(top_category['num_businesses']),
    "business_ids_for_sql": business_ids_for_sql
}

print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_function-call-10589892332600436595': ['checkin', 'business'], 'var_function-call-654616051907714223': [], 'var_function-call-1707409851110908864': [], 'var_function-call-7753006022657153088': 'file_storage/function-call-7753006022657153088.json', 'var_function-call-18179607718987131206': [{'_id': '6859a000fe8b31cd7362e2ab', 'business_id': 'businessid_49', 'description': 'Located at 6901 Phelps Rd in Goleta, CA, this facility offers a nurturing environment for young learners, providing a range of services in Education, Elementary Schools, Child Care & Day Care, Local Services, Preschools, and Montessori Schools.'}, {'_id': '6859a000fe8b31cd7362e2ac', 'business_id': 'businessid_47', 'description': 'Located at 9916 Clayton Rd in St. Louis, MO, this establishment offers a wide range of services, including Hair Salons, Beauty & Spas, Hair Stylists, Skin Care, Blow Dry/Out Services, and Makeup Artists.'}, {'_id': '6859a000fe8b31cd7362e2ad', 'business_id': 'businessid_88', 'description': 'Located at 11655 W Executive Dr in Boise, ID, this facility offers enthusiasts a premier destination for Gun/Rifle Ranges, Active Life.'}, {'_id': '6859a000fe8b31cd7362e2af', 'business_id': 'businessid_33', 'description': 'Located at 9655 E US Hwy 36, Unit H in Avon, IN, this establishment offers a range of services including Nail Salons, Hair Removal, Beauty & Spas, and Waxing.'}, {'_id': '6859a000fe8b31cd7362e2b1', 'business_id': 'businessid_92', 'description': 'Located at 690 W Dekalb Pike in King of Prussia, PA, this business offers a diverse range of services and products in the fields of Cosmetics & Beauty Supply, Cosmetic Dentists, Tanning, Teeth Whitening, Beauty & Spas, Dentists, Shopping, Blow Dry/Out Services, Health & Medical, Spray Tanning, and Hair Salons.'}], 'var_function-call-9141377590365096836': [{'_id': '6859a000fe8b31cd7362e2ab', 'business_id': 'businessid_49', 'description': 'Located at 6901 Phelps Rd in Goleta, CA, this facility offers a nurturing environment for young learners, providing a range of services in Education, Elementary Schools, Child Care & Day Care, Local Services, Preschools, and Montessori Schools.'}, {'_id': '6859a000fe8b31cd7362e2ac', 'business_id': 'businessid_47', 'description': 'Located at 9916 Clayton Rd in St. Louis, MO, this establishment offers a wide range of services, including Hair Salons, Beauty & Spas, Hair Stylists, Skin Care, Blow Dry/Out Services, and Makeup Artists.'}, {'_id': '6859a000fe8b31cd7362e2ad', 'business_id': 'businessid_88', 'description': 'Located at 11655 W Executive Dr in Boise, ID, this facility offers enthusiasts a premier destination for Gun/Rifle Ranges, Active Life.'}, {'_id': '6859a000fe8b31cd7362e2af', 'business_id': 'businessid_33', 'description': 'Located at 9655 E US Hwy 36, Unit H in Avon, IN, this establishment offers a range of services including Nail Salons, Hair Removal, Beauty & Spas, and Waxing.'}, {'_id': '6859a000fe8b31cd7362e2b1', 'business_id': 'businessid_92', 'description': 'Located at 690 W Dekalb Pike in King of Prussia, PA, this business offers a diverse range of services and products in the fields of Cosmetics & Beauty Supply, Cosmetic Dentists, Tanning, Teeth Whitening, Beauty & Spas, Dentists, Shopping, Blow Dry/Out Services, Health & Medical, Spray Tanning, and Hair Salons.'}]}

exec(code, env_args)
