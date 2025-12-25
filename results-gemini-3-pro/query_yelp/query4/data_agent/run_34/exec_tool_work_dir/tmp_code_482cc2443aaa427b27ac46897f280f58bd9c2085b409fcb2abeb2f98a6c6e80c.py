code = """import json
import pandas as pd
import re

businesses = locals()['var_function-call-1537264372374228069']
reviews_file = locals()['var_function-call-4420950461246935437']

print(f"Total businesses loaded: {len(businesses)}")

def extract_categories(desc):
    if not desc:
        return []
    match = re.search(r"(?:services in|services, including|services including|destination for|fields of) (.+?)\.$", desc)
    if match:
        cat_str = match.group(1)
        cat_str = re.sub(r",? and ", ", ", cat_str)
        cats = [c.strip() for c in cat_str.split(',')]
        cats = [c for c in cats if c]
        return cats
    return []

biz_data = []
for b in businesses:
    cats = extract_categories(b['description'])
    if cats:
        biz_data.append({'business_id': b['business_id'], 'categories': cats})
    else:
        # Debug failed extraction
        print(f"Extraction failed for: {b.get('description', 'NO DESC')[:50]}...")

df_biz = pd.DataFrame(biz_data)
print(f"df_biz shape: {df_biz.shape}")

if df_biz.empty:
    print("__RESULT__:")
    print(json.dumps("No categories extracted"))
else:
    with open(reviews_file, 'r') as f:
        reviews = json.load(f)
    
    df_reviews = pd.DataFrame(reviews)
    df_reviews['business_id'] = df_reviews['business_ref'].str.replace('businessref_', 'businessid_')
    df_reviews['rating'] = pd.to_numeric(df_reviews['rating'])
    
    biz_ratings = df_reviews.groupby('business_id')['rating'].mean().reset_index()
    biz_ratings.rename(columns={'rating': 'avg_rating'}, inplace=True)
    
    df_merged = pd.merge(df_biz, biz_ratings, on='business_id', how='inner')
    
    df_exploded = df_merged.explode('categories')
    
    cat_stats = df_exploded.groupby('categories').agg(
        business_count=('business_id', 'nunique'),
        avg_cat_rating=('avg_rating', 'mean')
    ).reset_index()
    
    top_cats = cat_stats.sort_values(by='business_count', ascending=False).head(5)
    
    print("__RESULT__:")
    print(top_cats.to_json(orient='records'))"""

env_args = {'var_function-call-2084756888653713256': [{'_id': '6859a000fe8b31cd7362e2ab', 'business_id': 'businessid_49', 'name': 'Steps to Learning Montessori Preschool', 'review_count': '8', 'is_open': '1', 'attributes': {'BusinessAcceptsCreditCards': 'True', 'WiFi': "u'no'", 'BusinessAcceptsBitcoin': 'False'}, 'hours': {'Monday': '0:0-0:0', 'Tuesday': '8:0-17:0', 'Wednesday': '8:0-17:0', 'Thursday': '8:0-17:0', 'Friday': '8:0-17:0'}, 'description': 'Located at 6901 Phelps Rd in Goleta, CA, this facility offers a nurturing environment for young learners, providing a range of services in Education, Elementary Schools, Child Care & Day Care, Local Services, Preschools, and Montessori Schools.'}], 'var_function-call-1537264372374228069': [{'business_id': 'businessid_49', 'description': 'Located at 6901 Phelps Rd in Goleta, CA, this facility offers a nurturing environment for young learners, providing a range of services in Education, Elementary Schools, Child Care & Day Care, Local Services, Preschools, and Montessori Schools.'}, {'business_id': 'businessid_47', 'description': 'Located at 9916 Clayton Rd in St. Louis, MO, this establishment offers a wide range of services, including Hair Salons, Beauty & Spas, Hair Stylists, Skin Care, Blow Dry/Out Services, and Makeup Artists.'}, {'business_id': 'businessid_88', 'description': 'Located at 11655 W Executive Dr in Boise, ID, this facility offers enthusiasts a premier destination for Gun/Rifle Ranges, Active Life.'}, {'business_id': 'businessid_33', 'description': 'Located at 9655 E US Hwy 36, Unit H in Avon, IN, this establishment offers a range of services including Nail Salons, Hair Removal, Beauty & Spas, and Waxing.'}, {'business_id': 'businessid_92', 'description': 'Located at 690 W Dekalb Pike in King of Prussia, PA, this business offers a diverse range of services and products in the fields of Cosmetics & Beauty Supply, Cosmetic Dentists, Tanning, Teeth Whitening, Beauty & Spas, Dentists, Shopping, Blow Dry/Out Services, Health & Medical, Spray Tanning, and Hair Salons.'}], 'var_function-call-4420950461246935437': 'file_storage/function-call-4420950461246935437.json', 'var_function-call-2756658905368286981': {'category': '', 'business_count': 4, 'average_rating': 4.042231319405232}, 'var_function-call-13307484395240900577': [{'desc': 'Located at 6901 Phelps Rd in Goleta, CA, this facility offers a nurturing environment for young learners, providing a range of services in Education, Elementary Schools, Child Care & Day Care, Local Services, Preschools, and Montessori Schools.', 'cats': ['Education', 'Elementary Schools', 'Child Care & Day Care', 'Local Services', 'Preschools', 'Montessori Schools']}, {'desc': 'Located at 9916 Clayton Rd in St. Louis, MO, this establishment offers a wide range of services, including Hair Salons, Beauty & Spas, Hair Stylists, Skin Care, Blow Dry/Out Services, and Makeup Artists.', 'cats': ['Hair Salons', 'Beauty & Spas', 'Hair Stylists', 'Skin Care', 'Blow Dry/Out Services', 'Makeup Artists']}, {'desc': 'Located at 11655 W Executive Dr in Boise, ID, this facility offers enthusiasts a premier destination for Gun/Rifle Ranges, Active Life.', 'cats': ['Gun/Rifle Ranges', 'Active Life']}, {'desc': 'Located at 9655 E US Hwy 36, Unit H in Avon, IN, this establishment offers a range of services including Nail Salons, Hair Removal, Beauty & Spas, and Waxing.', 'cats': ['Nail Salons', 'Hair Removal', 'Beauty & Spas', 'Waxing']}, {'desc': 'Located at 690 W Dekalb Pike in King of Prussia, PA, this business offers a diverse range of services and products in the fields of Cosmetics & Beauty Supply, Cosmetic Dentists, Tanning, Teeth Whitening, Beauty & Spas, Dentists, Shopping, Blow Dry/Out Services, Health & Medical, Spray Tanning, and Hair Salons.', 'cats': ['Cosmetics & Beauty Supply', 'Cosmetic Dentists', 'Tanning', 'Teeth Whitening', 'Beauty & Spas', 'Dentists', 'Shopping', 'Blow Dry/Out Services', 'Health & Medical', 'Spray Tanning', 'Hair Salons']}]}

exec(code, env_args)
