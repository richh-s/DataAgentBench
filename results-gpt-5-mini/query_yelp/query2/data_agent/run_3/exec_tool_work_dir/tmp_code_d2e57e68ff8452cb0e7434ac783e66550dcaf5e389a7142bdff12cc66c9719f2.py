code = """import json
import re
import pandas as pd

reviews_path = var_call_YiEYGld1ya0k8BarnLXoU7o1
business_path = var_call_Bm2uvDw7QJnUsy7daA2cu3oH

with open(reviews_path, 'r') as f:
    reviews = json.load(f)
with open(business_path, 'r') as f:
    businesses = json.load(f)

rdf = pd.DataFrame(reviews)
bdf = pd.DataFrame(businesses)

# Ensure rating numeric
rdf['rating'] = rdf['rating'].astype(int)
# Map business_ref to business_id
rdf['business_id'] = rdf['business_ref'].str.replace('businessref_', 'businessid_', regex=False)

# Build mapping from business_id to description
biz_desc = {b['business_id']: b.get('description') for b in businesses}

# US states set
states = set(['AL','AK','AZ','AR','CA','CO','CT','DE','FL','GA','HI','ID','IL','IN','IA','KS','KY','LA','ME','MD','MA','MI','MN','MS','MO','MT','NE','NV','NH','NJ','NM','NY','NC','ND','OH','OK','OR','PA','RI','SC','SD','TN','TX','UT','VT','VA','WA','WV','WI','WY'])

# Patterns to try
patterns = [re.compile(r',\s*([A-Za-z]{2}),'),
            re.compile(r'in\s+[^,]+,\s*([A-Za-z]{2})[,\s]'),
            re.compile(r'\b([A-Za-z]{2})\b')]

biz_state = {}
for bid, desc in biz_desc.items():
    state_found = None
    if isinstance(desc, str):
        for pat in patterns:
            m = pat.search(desc)
            if m:
                cand = m.group(1).upper()
                if cand in states:
                    state_found = cand
                    break
    biz_state[bid] = state_found

# Map to reviews
rdf['state'] = rdf['business_id'].map(biz_state)

# Filter reviews with state
rf = rdf[rdf['state'].notna()].copy()

if rf.empty:
    result = {"state": None, "review_count": 0, "average_rating": None}
else:
    grp = rf.groupby('state').agg(review_count=('rating','count'), average_rating=('rating','mean')).reset_index()
    top = grp.sort_values(by='review_count', ascending=False).iloc[0]
    result = {"state": top['state'], "review_count": int(top['review_count']), "average_rating": round(float(top['average_rating']), 2)}

print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_call_A9JqEFm4qqMrKC8bcXwY0iyq': ['business', 'checkin'], 'var_call_ALf0KC0Q08mDuxtPzHdGIDzz': ['review', 'tip', 'user'], 'var_call_evcPb0YLqREngMtRfpjdOKeV': [{'business_id': 'businessid_49', 'description': 'Located at 6901 Phelps Rd in Goleta, CA, this facility offers a nurturing environment for young learners, providing a range of services in Education, Elementary Schools, Child Care & Day Care, Local Services, Preschools, and Montessori Schools.'}, {'business_id': 'businessid_47', 'description': 'Located at 9916 Clayton Rd in St. Louis, MO, this establishment offers a wide range of services, including Hair Salons, Beauty & Spas, Hair Stylists, Skin Care, Blow Dry/Out Services, and Makeup Artists.'}, {'business_id': 'businessid_88', 'description': 'Located at 11655 W Executive Dr in Boise, ID, this facility offers enthusiasts a premier destination for Gun/Rifle Ranges, Active Life.'}, {'business_id': 'businessid_41', 'description': 'Located at 1615 Pasadena Ave S, Ste 430 in Saint Petersburg, FL, this facility offers a range of services in Internal Medicine, Doctors, Health & Medical.'}, {'business_id': 'businessid_33', 'description': 'Located at 9655 E US Hwy 36, Unit H in Avon, IN, this establishment offers a range of services including Nail Salons, Hair Removal, Beauty & Spas, and Waxing.'}], 'var_call_YiEYGld1ya0k8BarnLXoU7o1': 'file_storage/call_YiEYGld1ya0k8BarnLXoU7o1.json', 'var_call_8Qx06XwLVfY1r5sXAfw0BhE5': {'state': None, 'review_count': 0, 'average_rating': None}, 'var_call_2TFq7sT8U3MgsL8JPMv6x3kV': 'file_storage/call_2TFq7sT8U3MgsL8JPMv6x3kV.json', 'var_call_Bm2uvDw7QJnUsy7daA2cu3oH': 'file_storage/call_Bm2uvDw7QJnUsy7daA2cu3oH.json', 'var_call_QXgoWXf2gygZ8g4z0XccNs7V': {'state': None, 'review_count': 0, 'average_rating': None}, 'var_call_d6xnECHKWAVBWWpCMf1KRdbI': 'file_storage/call_d6xnECHKWAVBWWpCMf1KRdbI.json', 'var_call_q4vXMPbu83WUVu4jwdu2AkJe': {'state': None, 'review_count': 0, 'average_rating': None}, 'var_call_6lpLtelCMMSgF11D3ffpapft': {'businessid_49': 'Located at 6901 Phelps Rd in Goleta, CA, this facility offers a nurturing environment for young learners, providing a range of services in Education, Elementary Schools, Child Care & Day Care, Local Services, Preschools, and Montessori Schools.', 'businessid_47': 'Located at 9916 Clayton Rd in St. Louis, MO, this establishment offers a wide range of services, including Hair Salons, Beauty & Spas, Hair Stylists, Skin Care, Blow Dry/Out Services, and Makeup Artists.', 'businessid_88': 'Located at 11655 W Executive Dr in Boise, ID, this facility offers enthusiasts a premier destination for Gun/Rifle Ranges, Active Life.', 'businessid_41': 'Located at 1615 Pasadena Ave S, Ste 430 in Saint Petersburg, FL, this facility offers a range of services in Internal Medicine, Doctors, Health & Medical.', 'businessid_33': 'Located at 9655 E US Hwy 36, Unit H in Avon, IN, this establishment offers a range of services including Nail Salons, Hair Removal, Beauty & Spas, and Waxing.'}, 'var_call_Ju5CmebTl1vPaIcqceTCjkHz': [{'desc': 'Located at 6901 Phelps Rd in Goleta, CA, this facility offers a nurturing environment for young learners, providing a range of services in Education, Elementary Schools, Child Care & Day Care, Local Services, Preschools, and Montessori Schools.', 'p1': False, 'p1_match': None, 'p2': False, 'p2_match': None}, {'desc': 'Located at 9916 Clayton Rd in St. Louis, MO, this establishment offers a wide range of services, including Hair Salons, Beauty & Spas, Hair Stylists, Skin Care, Blow Dry/Out Services, and Makeup Artists.', 'p1': False, 'p1_match': None, 'p2': False, 'p2_match': None}, {'desc': 'Located at 11655 W Executive Dr in Boise, ID, this facility offers enthusiasts a premier destination for Gun/Rifle Ranges, Active Life.', 'p1': False, 'p1_match': None, 'p2': False, 'p2_match': None}, {'desc': 'Located at 1615 Pasadena Ave S, Ste 430 in Saint Petersburg, FL, this facility offers a range of services in Internal Medicine, Doctors, Health & Medical.', 'p1': False, 'p1_match': None, 'p2': False, 'p2_match': None}, {'desc': 'Located at 9655 E US Hwy 36, Unit H in Avon, IN, this establishment offers a range of services including Nail Salons, Hair Removal, Beauty & Spas, and Waxing.', 'p1': False, 'p1_match': None, 'p2': False, 'p2_match': None}, {'desc': 'Located at 735 Dodecanese Blvd in Tarpon Springs, FL, this charming establishment offers a delightful selection of treats, making it a must-visit for anyone seeking Candy Stores, Specialty Food, Food.', 'p1': False, 'p1_match': None, 'p2': False, 'p2_match': None}, {'desc': 'Located at 690 W Dekalb Pike in King of Prussia, PA, this business offers a diverse range of services and products in the fields of Cosmetics & Beauty Supply, Cosmetic Dentists, Tanning, Teeth Whitening, Beauty & Spas, Dentists, Shopping, Blow Dry/Out Services, Health & Medical, Spray Tanning, and Hair Salons.', 'p1': False, 'p1_match': None, 'p2': False, 'p2_match': None}, {'desc': 'Located at 12337 Olive Blvd in Creve Coeur, MO, this establishment offers a range of services in Nail Salons, Beauty & Spas.', 'p1': False, 'p1_match': None, 'p2': False, 'p2_match': None}, {'desc': 'Located at 5000 W 96th St in Indianapolis, IN, this establishment offers a diverse selection of Antiques, Shopping, Home Services, and Lighting Fixtures & Equipment for all your home and decorative needs.', 'p1': False, 'p1_match': None, 'p2': False, 'p2_match': None}, {'desc': 'Located at 41 Haddon Ave in Collingswood, NJ, this versatile establishment offers a range of services including Wedding Planning, Flowers & Gifts, Event Planning & Services, Financial Services, Shopping, and Florists.', 'p1': False, 'p1_match': None, 'p2': False, 'p2_match': None}]}

exec(code, env_args)
