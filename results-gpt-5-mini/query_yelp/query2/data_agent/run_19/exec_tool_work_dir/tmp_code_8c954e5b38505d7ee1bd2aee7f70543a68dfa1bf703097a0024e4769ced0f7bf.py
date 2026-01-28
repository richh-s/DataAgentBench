code = """import json
import pandas as pd
import re

with open(var_call_hmTBT2DHTxceJVlLDlvqmGy5, 'r') as f:
    businesses = json.load(f)
with open(var_call_C26XA720lemvNYIWrVw6IXtD, 'r') as f:
    reviews = json.load(f)

df_b = pd.DataFrame(businesses)
df_r = pd.DataFrame(reviews)

# Robust state extraction
def extract_state(desc):
    if not isinstance(desc, str):
        return None
    # 1. pattern: comma + space + 2 uppercase letters
    m = re.search(r",\s*([A-Z]{2})(?:\b|,|\.)", desc)
    if m:
        return m.group(1)
    # 2. pattern: 'in City, ST' or 'Located at ... in City, ST,'
    m = re.search(r"in\s+[^,]+,\s*([A-Z]{2})", desc)
    if m:
        return m.group(1)
    # 3. split by commas and look for token that's 2 letters
    parts = [p.strip() for p in desc.split(',')]
    for p in parts:
        if re.fullmatch(r"[A-Z]{2}", p):
            return p
    # 4. fallback: find any 2-letter uppercase sequence
    m = re.findall(r"([A-Z]{2})", desc)
    if m:
        return m[-1]
    return None

# Apply
if 'description' not in df_b.columns:
    df_b['description'] = None

df_b['state'] = df_b['description'].apply(extract_state)

# create id_suffix
df_b['id_suffix'] = df_b['business_id'].astype(str).apply(lambda s: s.split('_')[-1] if isinstance(s, str) and '_' in s else None)
if 'business_ref' in df_r.columns:
    df_r['id_suffix'] = df_r['business_ref'].astype(str).apply(lambda s: s.split('_')[-1] if isinstance(s, str) and '_' in s else None)
else:
    df_r['id_suffix'] = None

# ratings to numeric
df_r['rating'] = pd.to_numeric(df_r['rating'], errors='coerce')

# merge
df = df_r.merge(df_b[['id_suffix','state']], on='id_suffix', how='left')

# filter
df = df[df['state'].notna() & df['rating'].notna()]

if df.empty:
    result = {"state": None, "review_count": 0, "average_rating": None}
else:
    grp = df.groupby('state').agg(review_count=('rating','size'), average_rating=('rating','mean')).reset_index()
    max_row = grp.loc[grp['review_count'].idxmax()]
    result = {"state": str(max_row['state']), "review_count": int(max_row['review_count']), "average_rating": float(round(float(max_row['average_rating']),3))}

print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_call_35fgkqrbnU6wwvPZlWOULiZy': ['business', 'checkin'], 'var_call_4aMIiTGqEUjIrhUXk4fjUb2X': ['review', 'tip', 'user'], 'var_call_hmTBT2DHTxceJVlLDlvqmGy5': 'file_storage/call_hmTBT2DHTxceJVlLDlvqmGy5.json', 'var_call_C26XA720lemvNYIWrVw6IXtD': 'file_storage/call_C26XA720lemvNYIWrVw6IXtD.json', 'var_call_peDaDbKsBikc6B6arqepJNai': {'state': None, 'review_count': 0, 'average_rating': None}, 'var_call_rhUHUAoix8Kx20sGxktmNhu8': {'df_b_sample': [{'business_id': 'businessid_49', 'description': 'Located at 6901 Phelps Rd in Goleta, CA, this facility offers a nurturing environment for young learners, providing a range of services in Education, Elementary Schools, Child Care & Day Care, Local Services, Preschools, and Montessori Schools.', 'state': None}, {'business_id': 'businessid_47', 'description': 'Located at 9916 Clayton Rd in St. Louis, MO, this establishment offers a wide range of services, including Hair Salons, Beauty & Spas, Hair Stylists, Skin Care, Blow Dry/Out Services, and Makeup Artists.', 'state': None}, {'business_id': 'businessid_88', 'description': 'Located at 11655 W Executive Dr in Boise, ID, this facility offers enthusiasts a premier destination for Gun/Rifle Ranges, Active Life.', 'state': None}, {'business_id': 'businessid_41', 'description': 'Located at 1615 Pasadena Ave S, Ste 430 in Saint Petersburg, FL, this facility offers a range of services in Internal Medicine, Doctors, Health & Medical.', 'state': None}, {'business_id': 'businessid_33', 'description': 'Located at 9655 E US Hwy 36, Unit H in Avon, IN, this establishment offers a range of services including Nail Salons, Hair Removal, Beauty & Spas, and Waxing.', 'state': None}, {'business_id': 'businessid_74', 'description': 'Located at 735 Dodecanese Blvd in Tarpon Springs, FL, this charming establishment offers a delightful selection of treats, making it a must-visit for anyone seeking Candy Stores, Specialty Food, Food.', 'state': None}, {'business_id': 'businessid_92', 'description': 'Located at 690 W Dekalb Pike in King of Prussia, PA, this business offers a diverse range of services and products in the fields of Cosmetics & Beauty Supply, Cosmetic Dentists, Tanning, Teeth Whitening, Beauty & Spas, Dentists, Shopping, Blow Dry/Out Services, Health & Medical, Spray Tanning, and Hair Salons.', 'state': None}, {'business_id': 'businessid_64', 'description': 'Located at 12337 Olive Blvd in Creve Coeur, MO, this establishment offers a range of services in Nail Salons, Beauty & Spas.', 'state': None}, {'business_id': 'businessid_52', 'description': 'Located at 5000 W 96th St in Indianapolis, IN, this establishment offers a diverse selection of Antiques, Shopping, Home Services, and Lighting Fixtures & Equipment for all your home and decorative needs.', 'state': None}, {'business_id': 'businessid_29', 'description': 'Located at 41 Haddon Ave in Collingswood, NJ, this versatile establishment offers a range of services including Wedding Planning, Flowers & Gifts, Event Planning & Services, Financial Services, Shopping, and Florists.', 'state': None}, {'business_id': 'businessid_10', 'description': "Located at 4319 Telegraph Rd in Saint Louis, MO, this establishment offers a delightful array of dishes in the category of 'Restaurants, Chinese'.", 'state': None}, {'business_id': 'businessid_61', 'description': 'Located at 1218 Millennium Pkwy in Brandon, FL, this facility provides essential services in the categories of Medical Centers, Health & Medical.', 'state': None}, {'business_id': 'businessid_54', 'description': 'Located at 13151 Race Track Rd in Tampa, FL, this establishment offers a variety of services including Service Stations, Coffee & Tea, Gas Stations, Automotive, Gas Stations, Food, and Convenience Stores.', 'state': None}, {'business_id': 'businessid_8', 'description': 'This Philadelphia, PA location offers a range of services including Hotels & Travel, Taxis, Transportation, Local Services, and Automotive to meet all your travel and transportation needs.', 'state': None}, {'business_id': 'businessid_59', 'description': 'Located at 4403 Chestnut St in Philadelphia, PA, this vibrant spot offers a delightful mix of Food, Bubble Tea, Restaurants, Sandwiches, Vietnamese, Cafes, perfect for a casual meal or a refreshing drink.', 'state': None}, {'business_id': 'businessid_91', 'description': 'Located at 1625 Baronne St in New Orleans, LA, this vibrant establishment offers a delightful array of options ranging from Food, Shaved Ice, Cajun/Creole, Breakfast & Brunch, Party & Event Planning, Comfort Food, Cafes, Restaurants, to Event Planning & Services, making it a perfect spot for any occasion.', 'state': None}, {'business_id': 'businessid_83', 'description': 'Located at 13002 Seminole Blvd, Ste 10-11 in Largo, FL, this business specializes in Optometrists, Health & Medical, Eyewear & Opticians, Ophthalmologists, Doctors, Shopping, offering a range of eye care services and products.', 'state': None}, {'business_id': 'businessid_93', 'description': 'Located at 914 Edwardsville Rd in Troy, IL, this vibrant spot offers a diverse menu featuring American (New) cuisine, along with a lively atmosphere perfect for nightlife, bars, restaurants, and sports bars.', 'state': None}, {'business_id': 'businessid_1', 'description': 'Located in Pennsauken, NJ, this business specializes in Home Services, Pool & Hot Tub Service, providing expert care for all your residential maintenance needs.', 'state': None}, {'business_id': 'businessid_24', 'description': 'Located at 4663 Maryland Ave in Saint Louis, MO, this delightful spot offers a tempting selection of treats in the categories of Food, Ice Cream & Frozen Yogurt.', 'state': None}], 'df_r_sample': [{'business_ref': 'businessref_34', 'rating': '2'}, {'business_ref': 'businessref_89', 'rating': '5'}, {'business_ref': 'businessref_82', 'rating': '4'}, {'business_ref': 'businessref_66', 'rating': '2'}, {'business_ref': 'businessref_95', 'rating': '1'}, {'business_ref': 'businessref_24', 'rating': '4'}, {'business_ref': 'businessref_40', 'rating': '4'}, {'business_ref': 'businessref_47', 'rating': '5'}, {'business_ref': 'businessref_16', 'rating': '3'}, {'business_ref': 'businessref_96', 'rating': '5'}, {'business_ref': 'businessref_46', 'rating': '5'}, {'business_ref': 'businessref_21', 'rating': '1'}, {'business_ref': 'businessref_9', 'rating': '5'}, {'business_ref': 'businessref_26', 'rating': '1'}, {'business_ref': 'businessref_96', 'rating': '4'}, {'business_ref': 'businessref_43', 'rating': '1'}, {'business_ref': 'businessref_68', 'rating': '2'}, {'business_ref': 'businessref_24', 'rating': '4'}, {'business_ref': 'businessref_22', 'rating': '1'}, {'business_ref': 'businessref_57', 'rating': '5'}], 'merged_sample': [{'business_ref': 'businessref_34', 'rating': '2', 'id_suffix': '34', 'state': None}, {'business_ref': 'businessref_89', 'rating': '5', 'id_suffix': '89', 'state': None}, {'business_ref': 'businessref_82', 'rating': '4', 'id_suffix': '82', 'state': None}, {'business_ref': 'businessref_66', 'rating': '2', 'id_suffix': '66', 'state': None}, {'business_ref': 'businessref_95', 'rating': '1', 'id_suffix': '95', 'state': None}, {'business_ref': 'businessref_24', 'rating': '4', 'id_suffix': '24', 'state': None}, {'business_ref': 'businessref_40', 'rating': '4', 'id_suffix': '40', 'state': None}, {'business_ref': 'businessref_47', 'rating': '5', 'id_suffix': '47', 'state': None}, {'business_ref': 'businessref_16', 'rating': '3', 'id_suffix': '16', 'state': None}, {'business_ref': 'businessref_96', 'rating': '5', 'id_suffix': '96', 'state': None}, {'business_ref': 'businessref_46', 'rating': '5', 'id_suffix': '46', 'state': None}, {'business_ref': 'businessref_21', 'rating': '1', 'id_suffix': '21', 'state': None}, {'business_ref': 'businessref_9', 'rating': '5', 'id_suffix': '9', 'state': None}, {'business_ref': 'businessref_26', 'rating': '1', 'id_suffix': '26', 'state': None}, {'business_ref': 'businessref_96', 'rating': '4', 'id_suffix': '96', 'state': None}, {'business_ref': 'businessref_43', 'rating': '1', 'id_suffix': '43', 'state': None}, {'business_ref': 'businessref_68', 'rating': '2', 'id_suffix': '68', 'state': None}, {'business_ref': 'businessref_24', 'rating': '4', 'id_suffix': '24', 'state': None}, {'business_ref': 'businessref_22', 'rating': '1', 'id_suffix': '22', 'state': None}, {'business_ref': 'businessref_57', 'rating': '5', 'id_suffix': '57', 'state': None}], 'businesses_with_state_count': 0}, 'var_call_lDevAVFwdCvEq4Pnr5APaI4v': {'desc_repr': "'Located at 6901 Phelps Rd in Goleta, CA, this facility offers a nurturing environment for young learners, providing a range of services in Education, Elementary Schools, Child Care & Day Care, Local Services, Preschools, and Montessori Schools.'", 'matches': []}}

exec(code, env_args)
