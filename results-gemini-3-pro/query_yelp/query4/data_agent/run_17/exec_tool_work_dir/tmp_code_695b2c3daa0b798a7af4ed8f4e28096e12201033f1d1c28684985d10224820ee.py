code = """import pandas as pd
import json
import re

# Load data
businesses = locals()['var_function-call-16465432854484452110']
review_file = locals()['var_function-call-16465432854484454531']

with open(review_file, 'r') as f:
    reviews = json.load(f)

# Convert to DataFrames
df_b = pd.DataFrame(businesses)
df_r = pd.DataFrame(reviews)

# Fix ratings (ensure numeric)
df_r['rating'] = pd.to_numeric(df_r['rating'])

# Parse Categories
def extract_categories(desc):
    if not desc:
        return []
    
    # known patterns triggering the category list
    patterns = [
        "providing a range of services in ",
        "offers a wide range of services, including ",
        "offers a range of services including ",
        "offers a diverse range of services and products in the fields of ",
        "offers enthusiasts a premier destination for "
    ]
    
    category_text = ""
    for p in patterns:
        if p in desc:
            category_text = desc.split(p)[-1]
            break
            
    if not category_text:
        # Fallback: maybe just look for the list after the last "offers" or similar?
        # Or look for text after the address?
        # Let's assume the provided patterns cover most. 
        # If not, we might miss some, but let's hope it's consistent.
        # Check for simple "offers ... including"
        if " including " in desc:
             category_text = desc.split(" including ")[-1]
        elif " in the fields of " in desc:
             category_text = desc.split(" in the fields of ")[-1]
        else:
            return []

    # Clean text
    # Remove trailing period
    category_text = category_text.strip().rstrip('.')
    
    # Split by comma
    raw_cats = category_text.split(', ')
    
    cats = []
    for c in raw_cats:
        c = c.strip()
        if c.startswith('and '):
            c = c[4:]
        cats.append(c)
    return cats

# Process businesses
category_map = [] # (category, business_ref)

for _, row in df_b.iterrows():
    b_id_mongo = row['business_id']
    # Transform ID: businessid_XX -> businessref_XX
    b_ref = b_id_mongo.replace('businessid_', 'businessref_')
    
    desc = row.get('description', '')
    cats = extract_categories(desc)
    
    for c in cats:
        category_map.append({'category': c, 'business_ref': b_ref})

df_cat = pd.DataFrame(category_map)

# Join with reviews to get ratings
# We need to answer: 
# 1. Category with largest number of businesses (accepting credit cards - already filtered in query)
# 2. Average rating of that category

if df_cat.empty:
    print("__RESULT__:")
    print(json.dumps({"error": "No categories found"}))
else:
    # 1. Count businesses per category
    # Ensure unique businesses per category count
    cat_counts = df_cat.groupby('category')['business_ref'].nunique().reset_index()
    cat_counts = cat_counts.rename(columns={'business_ref': 'business_count'})
    
    # Find top category
    # Sort by count desc
    top_cat_row = cat_counts.sort_values(by='business_count', ascending=False).iloc[0]
    top_category = top_cat_row['category']
    num_businesses = int(top_cat_row['business_count'])
    
    # 2. Calculate average rating for this category
    # Get all businesses in this category
    businesses_in_top_cat = df_cat[df_cat['category'] == top_category]['business_ref'].unique()
    
    # Filter reviews for these businesses
    relevant_reviews = df_r[df_r['business_ref'].isin(businesses_in_top_cat)]
    
    if relevant_reviews.empty:
        avg_rating = 0.0
    else:
        avg_rating = relevant_reviews['rating'].mean()
        
    result = {
        "top_category": top_category,
        "business_count": num_businesses,
        "average_rating": round(avg_rating, 4)
    }

    print("__RESULT__:")
    print(json.dumps(result))"""

env_args = {'var_function-call-1265267779807000548': [{'_id': '6859a000fe8b31cd7362e2ab', 'business_id': 'businessid_49', 'name': 'Steps to Learning Montessori Preschool', 'review_count': '8', 'is_open': '1', 'attributes': {'BusinessAcceptsCreditCards': 'True', 'WiFi': "u'no'", 'BusinessAcceptsBitcoin': 'False'}, 'hours': {'Monday': '0:0-0:0', 'Tuesday': '8:0-17:0', 'Wednesday': '8:0-17:0', 'Thursday': '8:0-17:0', 'Friday': '8:0-17:0'}, 'description': 'Located at 6901 Phelps Rd in Goleta, CA, this facility offers a nurturing environment for young learners, providing a range of services in Education, Elementary Schools, Child Care & Day Care, Local Services, Preschools, and Montessori Schools.'}], 'var_function-call-16465432854484452110': [{'_id': '6859a000fe8b31cd7362e2ab', 'business_id': 'businessid_49', 'description': 'Located at 6901 Phelps Rd in Goleta, CA, this facility offers a nurturing environment for young learners, providing a range of services in Education, Elementary Schools, Child Care & Day Care, Local Services, Preschools, and Montessori Schools.'}, {'_id': '6859a000fe8b31cd7362e2ac', 'business_id': 'businessid_47', 'description': 'Located at 9916 Clayton Rd in St. Louis, MO, this establishment offers a wide range of services, including Hair Salons, Beauty & Spas, Hair Stylists, Skin Care, Blow Dry/Out Services, and Makeup Artists.'}, {'_id': '6859a000fe8b31cd7362e2ad', 'business_id': 'businessid_88', 'description': 'Located at 11655 W Executive Dr in Boise, ID, this facility offers enthusiasts a premier destination for Gun/Rifle Ranges, Active Life.'}, {'_id': '6859a000fe8b31cd7362e2af', 'business_id': 'businessid_33', 'description': 'Located at 9655 E US Hwy 36, Unit H in Avon, IN, this establishment offers a range of services including Nail Salons, Hair Removal, Beauty & Spas, and Waxing.'}, {'_id': '6859a000fe8b31cd7362e2b1', 'business_id': 'businessid_92', 'description': 'Located at 690 W Dekalb Pike in King of Prussia, PA, this business offers a diverse range of services and products in the fields of Cosmetics & Beauty Supply, Cosmetic Dentists, Tanning, Teeth Whitening, Beauty & Spas, Dentists, Shopping, Blow Dry/Out Services, Health & Medical, Spray Tanning, and Hair Salons.'}], 'var_function-call-16465432854484454531': 'file_storage/function-call-16465432854484454531.json'}

exec(code, env_args)
