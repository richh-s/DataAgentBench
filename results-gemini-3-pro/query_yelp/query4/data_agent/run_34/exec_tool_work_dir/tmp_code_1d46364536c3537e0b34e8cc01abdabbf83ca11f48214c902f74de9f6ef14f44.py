code = """import json
import pandas as pd
import re

# Load businesses
with open(locals()['var_function-call-9445382624692412632'], 'r') as f:
    businesses = json.load(f)

def extract_categories(desc):
    if not desc:
        return []
    match = re.search(r"(?:services in|services, including|services including|destination for|fields of|category of|categories of) (.+?)\.$", desc)
    if match:
        cat_str = match.group(1)
        cat_str = cat_str.replace("'", "")
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

df_biz = pd.DataFrame(biz_data)

# Load reviews
with open(locals()['var_function-call-4420950461246935437'], 'r') as f:
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

env_args = {'var_function-call-2084756888653713256': [{'_id': '6859a000fe8b31cd7362e2ab', 'business_id': 'businessid_49', 'name': 'Steps to Learning Montessori Preschool', 'review_count': '8', 'is_open': '1', 'attributes': {'BusinessAcceptsCreditCards': 'True', 'WiFi': "u'no'", 'BusinessAcceptsBitcoin': 'False'}, 'hours': {'Monday': '0:0-0:0', 'Tuesday': '8:0-17:0', 'Wednesday': '8:0-17:0', 'Thursday': '8:0-17:0', 'Friday': '8:0-17:0'}, 'description': 'Located at 6901 Phelps Rd in Goleta, CA, this facility offers a nurturing environment for young learners, providing a range of services in Education, Elementary Schools, Child Care & Day Care, Local Services, Preschools, and Montessori Schools.'}], 'var_function-call-1537264372374228069': [{'business_id': 'businessid_49', 'description': 'Located at 6901 Phelps Rd in Goleta, CA, this facility offers a nurturing environment for young learners, providing a range of services in Education, Elementary Schools, Child Care & Day Care, Local Services, Preschools, and Montessori Schools.'}, {'business_id': 'businessid_47', 'description': 'Located at 9916 Clayton Rd in St. Louis, MO, this establishment offers a wide range of services, including Hair Salons, Beauty & Spas, Hair Stylists, Skin Care, Blow Dry/Out Services, and Makeup Artists.'}, {'business_id': 'businessid_88', 'description': 'Located at 11655 W Executive Dr in Boise, ID, this facility offers enthusiasts a premier destination for Gun/Rifle Ranges, Active Life.'}, {'business_id': 'businessid_33', 'description': 'Located at 9655 E US Hwy 36, Unit H in Avon, IN, this establishment offers a range of services including Nail Salons, Hair Removal, Beauty & Spas, and Waxing.'}, {'business_id': 'businessid_92', 'description': 'Located at 690 W Dekalb Pike in King of Prussia, PA, this business offers a diverse range of services and products in the fields of Cosmetics & Beauty Supply, Cosmetic Dentists, Tanning, Teeth Whitening, Beauty & Spas, Dentists, Shopping, Blow Dry/Out Services, Health & Medical, Spray Tanning, and Hair Salons.'}], 'var_function-call-4420950461246935437': 'file_storage/function-call-4420950461246935437.json', 'var_function-call-2756658905368286981': {'category': '', 'business_count': 4, 'average_rating': 4.042231319405232}, 'var_function-call-13307484395240900577': [{'desc': 'Located at 6901 Phelps Rd in Goleta, CA, this facility offers a nurturing environment for young learners, providing a range of services in Education, Elementary Schools, Child Care & Day Care, Local Services, Preschools, and Montessori Schools.', 'cats': ['Education', 'Elementary Schools', 'Child Care & Day Care', 'Local Services', 'Preschools', 'Montessori Schools']}, {'desc': 'Located at 9916 Clayton Rd in St. Louis, MO, this establishment offers a wide range of services, including Hair Salons, Beauty & Spas, Hair Stylists, Skin Care, Blow Dry/Out Services, and Makeup Artists.', 'cats': ['Hair Salons', 'Beauty & Spas', 'Hair Stylists', 'Skin Care', 'Blow Dry/Out Services', 'Makeup Artists']}, {'desc': 'Located at 11655 W Executive Dr in Boise, ID, this facility offers enthusiasts a premier destination for Gun/Rifle Ranges, Active Life.', 'cats': ['Gun/Rifle Ranges', 'Active Life']}, {'desc': 'Located at 9655 E US Hwy 36, Unit H in Avon, IN, this establishment offers a range of services including Nail Salons, Hair Removal, Beauty & Spas, and Waxing.', 'cats': ['Nail Salons', 'Hair Removal', 'Beauty & Spas', 'Waxing']}, {'desc': 'Located at 690 W Dekalb Pike in King of Prussia, PA, this business offers a diverse range of services and products in the fields of Cosmetics & Beauty Supply, Cosmetic Dentists, Tanning, Teeth Whitening, Beauty & Spas, Dentists, Shopping, Blow Dry/Out Services, Health & Medical, Spray Tanning, and Hair Salons.', 'cats': ['Cosmetics & Beauty Supply', 'Cosmetic Dentists', 'Tanning', 'Teeth Whitening', 'Beauty & Spas', 'Dentists', 'Shopping', 'Blow Dry/Out Services', 'Health & Medical', 'Spray Tanning', 'Hair Salons']}], 'var_function-call-2439769957645801020': [{'categories': 'Beauty & Spas', 'business_count': 3, 'avg_cat_rating': 4.0007528703}, {'categories': 'Blow Dry/Out Services', 'business_count': 2, 'avg_cat_rating': 4.2402597403}, {'categories': 'Hair Salons', 'business_count': 2, 'avg_cat_rating': 4.2402597403}, {'categories': 'Child Care & Day Care', 'business_count': 1, 'avg_cat_rating': 4.1666666667}, {'categories': 'Active Life', 'business_count': 1, 'avg_cat_rating': 3.2121212121}], 'var_function-call-7034192728644468956': [{'_id': '6859a000fe8b31cd7362e2ab', 'business_id': 'businessid_49', 'name': 'Steps to Learning Montessori Preschool', 'review_count': '8', 'is_open': '1', 'attributes': {'BusinessAcceptsCreditCards': 'True', 'WiFi': "u'no'", 'BusinessAcceptsBitcoin': 'False'}, 'hours': {'Monday': '0:0-0:0', 'Tuesday': '8:0-17:0', 'Wednesday': '8:0-17:0', 'Thursday': '8:0-17:0', 'Friday': '8:0-17:0'}, 'description': 'Located at 6901 Phelps Rd in Goleta, CA, this facility offers a nurturing environment for young learners, providing a range of services in Education, Elementary Schools, Child Care & Day Care, Local Services, Preschools, and Montessori Schools.'}, {'_id': '6859a000fe8b31cd7362e2ac', 'business_id': 'businessid_47', 'name': 'Breeze Blow Dry Bar', 'review_count': '81', 'is_open': '0', 'attributes': {'ByAppointmentOnly': 'False', 'BusinessAcceptsCreditCards': 'True', 'GoodForKids': 'True', 'RestaurantsPriceRange2': '2', 'BikeParking': 'False', 'BusinessParking': "{'garage': False, 'street': False, 'validated': False, 'lot': True, 'valet': False}"}, 'hours': {'Monday': '7:0-18:0', 'Tuesday': '7:0-18:0', 'Wednesday': '7:0-18:0', 'Thursday': '7:0-18:0', 'Friday': '7:0-19:0', 'Saturday': '8:0-19:0', 'Sunday': '10:0-17:0'}, 'description': 'Located at 9916 Clayton Rd in St. Louis, MO, this establishment offers a wide range of services, including Hair Salons, Beauty & Spas, Hair Stylists, Skin Care, Blow Dry/Out Services, and Makeup Artists.'}, {'_id': '6859a000fe8b31cd7362e2ad', 'business_id': 'businessid_88', 'name': 'Impact Guns', 'review_count': '39', 'is_open': '1', 'attributes': {'BusinessParking': "{'garage': False, 'street': False, 'validated': False, 'lot': False, 'valet': False}", 'GoodForKids': 'True', 'BusinessAcceptsCreditCards': 'True', 'ByAppointmentOnly': 'False', 'BikeParking': 'True'}, 'hours': {'Monday': '10:0-19:0', 'Tuesday': '10:0-19:0', 'Wednesday': '10:0-19:0', 'Thursday': '10:0-19:0', 'Friday': '10:0-19:0', 'Saturday': '10:0-19:0'}, 'description': 'Located at 11655 W Executive Dr in Boise, ID, this facility offers enthusiasts a premier destination for Gun/Rifle Ranges, Active Life.'}, {'_id': '6859a000fe8b31cd7362e2ae', 'business_id': 'businessid_41', 'name': 'Palms Primary Care', 'review_count': '5', 'is_open': '1', 'attributes': 'None', 'hours': {'Monday': '8:30-17:0', 'Tuesday': '8:30-17:0', 'Wednesday': '8:30-17:0', 'Thursday': '8:30-17:0', 'Friday': '8:30-17:0'}, 'description': 'Located at 1615 Pasadena Ave S, Ste 430 in Saint Petersburg, FL, this facility offers a range of services in Internal Medicine, Doctors, Health & Medical.'}, {'_id': '6859a000fe8b31cd7362e2af', 'business_id': 'businessid_33', 'name': 'J&Q Nails', 'review_count': '28', 'is_open': '1', 'attributes': {'BusinessParking': "{'garage': False, 'street': False, 'validated': False, 'lot': False, 'valet': False}", 'BusinessAcceptsCreditCards': 'True', 'AcceptsInsurance': 'False', 'ByAppointmentOnly': 'False', 'RestaurantsPriceRange2': '2', 'WheelchairAccessible': 'True', 'BikeParking': 'False'}, 'hours': {'Monday': '9:30-19:0', 'Tuesday': '9:30-19:0', 'Wednesday': '9:30-19:0', 'Thursday': '9:30-19:0', 'Friday': '9:30-19:0', 'Saturday': '9:30-17:30'}, 'description': 'Located at 9655 E US Hwy 36, Unit H in Avon, IN, this establishment offers a range of services including Nail Salons, Hair Removal, Beauty & Spas, and Waxing.'}], 'var_function-call-9445382624692412632': 'file_storage/function-call-9445382624692412632.json', 'var_function-call-14441834076463932931': {'category': 'Shopping', 'business_count': 6, 'average_rating': 3.7944805194805196}}

exec(code, env_args)
