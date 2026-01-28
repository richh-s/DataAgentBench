code = """import json
import pandas as pd
import string
with open(var_call_bmGsDrqzEb8WIXr84xa3oUqv, 'r') as f:
    businesses = json.load(f)
with open(var_call_Frbu60r0fEgy6ljG6I74NfbJ, 'r') as f:
    reviews = json.load(f)

df_b = pd.DataFrame(businesses)
df_r = pd.DataFrame(reviews)

# prepare business_ref
df_b['business_ref'] = df_b['business_id'].astype(str).str.replace('businessid_', 'businessref_', regex=False)

states = {"AL","AK","AZ","AR","CA","CO","CT","DE","FL","GA","HI","ID","IL","IN","IA","KS","KY","LA","ME","MD","MA","MI","MN","MS","MO","MT","NE","NV","NH","NJ","NM","NY","NC","ND","OH","OK","OR","PA","RI","SC","SD","TN","TX","UT","VT","VA","WA","WV","WI","WY","DC"}

import re

def extract_state(desc):
    if not isinstance(desc, str):
        return None
    # split by commas, examine each segment for a two-letter state
    parts = [p.strip() for p in desc.split(',') if p.strip()]
    for p in parts:
        # split into words
        words = re.split(r"\s+", p)
        for w in words:
            # strip punctuation
            ww = w.strip(string.punctuation)
            if ww in states:
                return ww
            # also check if ends with state (like 'PA' followed by other chars)
            # check leading two uppercase
            if len(ww) >= 2 and ww[:2] in states and ww[:2].isupper():
                return ww[:2]
    return None

# apply
if 'description' in df_b.columns:
    df_b['state'] = df_b['description'].apply(extract_state)
else:
    df_b['state'] = None

# Convert ratings
if 'rating' in df_r.columns:
    df_r['rating'] = pd.to_numeric(df_r['rating'], errors='coerce')
else:
    df_r['rating'] = None

# Merge
merged = df_r.merge(df_b[['business_ref','state']], on='business_ref', how='left')

# aggregate by state based on reviews: count reviews per state and average rating
merged2 = merged[merged['state'].notna()].copy()
agg = merged2.groupby('state').agg(review_count=('rating','count'), average_rating=('rating','mean')).reset_index()

if agg.empty:
    result = {'state': None, 'review_count': 0, 'average_rating': None}
else:
    top = agg.sort_values('review_count', ascending=False).iloc[0]
    result = {'state': top['state'], 'review_count': int(top['review_count']), 'average_rating': round(float(top['average_rating']), 4) if pd.notna(top['average_rating']) else None}

print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_call_fpPF93D0p5wuk9Tn3xlYkuTv': ['business', 'checkin'], 'var_call_gpCk0rwl1WBa0LKN6UThykCT': ['review', 'tip', 'user'], 'var_call_bmGsDrqzEb8WIXr84xa3oUqv': 'file_storage/call_bmGsDrqzEb8WIXr84xa3oUqv.json', 'var_call_Frbu60r0fEgy6ljG6I74NfbJ': 'file_storage/call_Frbu60r0fEgy6ljG6I74NfbJ.json', 'var_call_7RzGb3nMu6E1KfVunxradW7s': {'state': None, 'review_count': 0, 'average_rating': None}, 'var_call_pbw10swcYHjPNyVydkUvudvo': 'file_storage/call_pbw10swcYHjPNyVydkUvudvo.json', 'var_call_N6h0ZsV14EmVlP9u66m6n2ec': [{'business_id': 'businessid_49', 'description': 'Located at 6901 Phelps Rd in Goleta, CA, this facility offers a nurturing environment for young learners, providing a range of services in Education, Elementary Schools, Child Care & Day Care, Local Services, Preschools, and Montessori Schools.', 'repr': "'Located at 6901 Phelps Rd in Goleta, CA, this facility offers a nurturing environment for young learners, providing a range of services in Education, Elementary Schools, Child Care & Day Care, Local Services, Preschools, and Montessori Schools.'"}, {'business_id': 'businessid_47', 'description': 'Located at 9916 Clayton Rd in St. Louis, MO, this establishment offers a wide range of services, including Hair Salons, Beauty & Spas, Hair Stylists, Skin Care, Blow Dry/Out Services, and Makeup Artists.', 'repr': "'Located at 9916 Clayton Rd in St. Louis, MO, this establishment offers a wide range of services, including Hair Salons, Beauty & Spas, Hair Stylists, Skin Care, Blow Dry/Out Services, and Makeup Artists.'"}, {'business_id': 'businessid_88', 'description': 'Located at 11655 W Executive Dr in Boise, ID, this facility offers enthusiasts a premier destination for Gun/Rifle Ranges, Active Life.', 'repr': "'Located at 11655 W Executive Dr in Boise, ID, this facility offers enthusiasts a premier destination for Gun/Rifle Ranges, Active Life.'"}, {'business_id': 'businessid_41', 'description': 'Located at 1615 Pasadena Ave S, Ste 430 in Saint Petersburg, FL, this facility offers a range of services in Internal Medicine, Doctors, Health & Medical.', 'repr': "'Located at 1615 Pasadena Ave S, Ste 430 in Saint Petersburg, FL, this facility offers a range of services in Internal Medicine, Doctors, Health & Medical.'"}, {'business_id': 'businessid_33', 'description': 'Located at 9655 E US Hwy 36, Unit H in Avon, IN, this establishment offers a range of services including Nail Salons, Hair Removal, Beauty & Spas, and Waxing.', 'repr': "'Located at 9655 E US Hwy 36, Unit H in Avon, IN, this establishment offers a range of services including Nail Salons, Hair Removal, Beauty & Spas, and Waxing.'"}, {'business_id': 'businessid_74', 'description': 'Located at 735 Dodecanese Blvd in Tarpon Springs, FL, this charming establishment offers a delightful selection of treats, making it a must-visit for anyone seeking Candy Stores, Specialty Food, Food.', 'repr': "'Located at 735 Dodecanese Blvd in Tarpon Springs, FL, this charming establishment offers a delightful selection of treats, making it a must-visit for anyone seeking Candy Stores, Specialty Food, Food.'"}, {'business_id': 'businessid_92', 'description': 'Located at 690 W Dekalb Pike in King of Prussia, PA, this business offers a diverse range of services and products in the fields of Cosmetics & Beauty Supply, Cosmetic Dentists, Tanning, Teeth Whitening, Beauty & Spas, Dentists, Shopping, Blow Dry/Out Services, Health & Medical, Spray Tanning, and Hair Salons.', 'repr': "'Located at 690 W Dekalb Pike in King of Prussia, PA, this business offers a diverse range of services and products in the fields of Cosmetics & Beauty Supply, Cosmetic Dentists, Tanning, Teeth Whitening, Beauty & Spas, Dentists, Shopping, Blow Dry/Out Services, Health & Medical, Spray Tanning, and Hair Salons.'"}, {'business_id': 'businessid_64', 'description': 'Located at 12337 Olive Blvd in Creve Coeur, MO, this establishment offers a range of services in Nail Salons, Beauty & Spas.', 'repr': "'Located at 12337 Olive Blvd in Creve Coeur, MO, this establishment offers a range of services in Nail Salons, Beauty & Spas.'"}, {'business_id': 'businessid_52', 'description': 'Located at 5000 W 96th St in Indianapolis, IN, this establishment offers a diverse selection of Antiques, Shopping, Home Services, and Lighting Fixtures & Equipment for all your home and decorative needs.', 'repr': "'Located at 5000 W 96th St in Indianapolis, IN, this establishment offers a diverse selection of Antiques, Shopping, Home Services, and Lighting Fixtures & Equipment for all your home and decorative needs.'"}, {'business_id': 'businessid_29', 'description': 'Located at 41 Haddon Ave in Collingswood, NJ, this versatile establishment offers a range of services including Wedding Planning, Flowers & Gifts, Event Planning & Services, Financial Services, Shopping, and Florists.', 'repr': "'Located at 41 Haddon Ave in Collingswood, NJ, this versatile establishment offers a range of services including Wedding Planning, Flowers & Gifts, Event Planning & Services, Financial Services, Shopping, and Florists.'"}, {'business_id': 'businessid_10', 'description': "Located at 4319 Telegraph Rd in Saint Louis, MO, this establishment offers a delightful array of dishes in the category of 'Restaurants, Chinese'.", 'repr': '"Located at 4319 Telegraph Rd in Saint Louis, MO, this establishment offers a delightful array of dishes in the category of \'Restaurants, Chinese\'."'}, {'business_id': 'businessid_61', 'description': 'Located at 1218 Millennium Pkwy in Brandon, FL, this facility provides essential services in the categories of Medical Centers, Health & Medical.', 'repr': "'Located at 1218 Millennium Pkwy in Brandon, FL, this facility provides essential services in the categories of Medical Centers, Health & Medical.'"}, {'business_id': 'businessid_54', 'description': 'Located at 13151 Race Track Rd in Tampa, FL, this establishment offers a variety of services including Service Stations, Coffee & Tea, Gas Stations, Automotive, Gas Stations, Food, and Convenience Stores.', 'repr': "'Located at 13151 Race Track Rd in Tampa, FL, this establishment offers a variety of services including Service Stations, Coffee & Tea, Gas Stations, Automotive, Gas Stations, Food, and Convenience Stores.'"}, {'business_id': 'businessid_8', 'description': 'This Philadelphia, PA location offers a range of services including Hotels & Travel, Taxis, Transportation, Local Services, and Automotive to meet all your travel and transportation needs.', 'repr': "'This Philadelphia, PA location offers a range of services including Hotels & Travel, Taxis, Transportation, Local Services, and Automotive to meet all your travel and transportation needs.'"}, {'business_id': 'businessid_59', 'description': 'Located at 4403 Chestnut St in Philadelphia, PA, this vibrant spot offers a delightful mix of Food, Bubble Tea, Restaurants, Sandwiches, Vietnamese, Cafes, perfect for a casual meal or a refreshing drink.', 'repr': "'Located at 4403 Chestnut St in Philadelphia, PA, this vibrant spot offers a delightful mix of Food, Bubble Tea, Restaurants, Sandwiches, Vietnamese, Cafes, perfect for a casual meal or a refreshing drink.'"}, {'business_id': 'businessid_91', 'description': 'Located at 1625 Baronne St in New Orleans, LA, this vibrant establishment offers a delightful array of options ranging from Food, Shaved Ice, Cajun/Creole, Breakfast & Brunch, Party & Event Planning, Comfort Food, Cafes, Restaurants, to Event Planning & Services, making it a perfect spot for any occasion.', 'repr': "'Located at 1625 Baronne St in New Orleans, LA, this vibrant establishment offers a delightful array of options ranging from Food, Shaved Ice, Cajun/Creole, Breakfast & Brunch, Party & Event Planning, Comfort Food, Cafes, Restaurants, to Event Planning & Services, making it a perfect spot for any occasion.'"}, {'business_id': 'businessid_83', 'description': 'Located at 13002 Seminole Blvd, Ste 10-11 in Largo, FL, this business specializes in Optometrists, Health & Medical, Eyewear & Opticians, Ophthalmologists, Doctors, Shopping, offering a range of eye care services and products.', 'repr': "'Located at 13002 Seminole Blvd, Ste 10-11 in Largo, FL, this business specializes in Optometrists, Health & Medical, Eyewear & Opticians, Ophthalmologists, Doctors, Shopping, offering a range of eye care services and products.'"}, {'business_id': 'businessid_93', 'description': 'Located at 914 Edwardsville Rd in Troy, IL, this vibrant spot offers a diverse menu featuring American (New) cuisine, along with a lively atmosphere perfect for nightlife, bars, restaurants, and sports bars.', 'repr': "'Located at 914 Edwardsville Rd in Troy, IL, this vibrant spot offers a diverse menu featuring American (New) cuisine, along with a lively atmosphere perfect for nightlife, bars, restaurants, and sports bars.'"}, {'business_id': 'businessid_1', 'description': 'Located in Pennsauken, NJ, this business specializes in Home Services, Pool & Hot Tub Service, providing expert care for all your residential maintenance needs.', 'repr': "'Located in Pennsauken, NJ, this business specializes in Home Services, Pool & Hot Tub Service, providing expert care for all your residential maintenance needs.'"}, {'business_id': 'businessid_24', 'description': 'Located at 4663 Maryland Ave in Saint Louis, MO, this delightful spot offers a tempting selection of treats in the categories of Food, Ice Cream & Frozen Yogurt.', 'repr': "'Located at 4663 Maryland Ave in Saint Louis, MO, this delightful spot offers a tempting selection of treats in the categories of Food, Ice Cream & Frozen Yogurt.'"}], 'var_call_mxQltPxh6wTsVgi4b9z9RcXb': {'state': None, 'review_count': 0, 'average_rating': None}, 'var_call_CE3zAGRInCUU22N0JHp6t5gU': {'business_rows': 100, 'review_rows': 2000, 'business_columns': ['business_id', 'review_count', 'description'], 'review_columns': ['business_ref', 'rating'], 'num_business_refs': 100, 'num_review_refs': 100, 'num_common': 100, 'common_sample': ['businessref_99', 'businessref_82', 'businessref_80', 'businessref_1', 'businessref_43', 'businessref_90', 'businessref_81', 'businessref_54', 'businessref_31', 'businessref_32', 'businessref_78', 'businessref_63', 'businessref_21', 'businessref_86', 'businessref_64', 'businessref_34', 'businessref_84', 'businessref_74', 'businessref_13', 'businessref_57']}}

exec(code, env_args)
