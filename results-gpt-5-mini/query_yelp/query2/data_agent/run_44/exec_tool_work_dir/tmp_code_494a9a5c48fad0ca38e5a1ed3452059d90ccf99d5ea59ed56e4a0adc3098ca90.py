code = """import json
import re
import pandas as pd

biz = var_call_sjU0gxiN4j5ujlsu5JKnWCGD
reviews_path = var_call_OtIIQA6kEpd4jg9w3UlnX9u7
with open(reviews_path, 'r') as f:
    reviews = json.load(f)

# Build business df
df_b = pd.DataFrame(biz)
# id and business_ref
df_b['id_num'] = df_b['business_id'].str.replace(r'^[^0-9]*', '', regex=True)
df_b['business_ref'] = 'businessref_' + df_b['id_num']

# Try multiple patterns to extract state
patterns = [r',\s*([A-Z]{2}),', r',\s*([A-Z]{2})\b', r'in [^,]+,\s*([A-Z]{2})', r'\b([A-Z]{2})\b']

def extract_state(desc):
    if not desc or not isinstance(desc, str):
        return None
    for p in patterns:
        m = re.search(p, desc)
        if m:
            s = m.group(1)
            # validate s is a US state code length 2
            if len(s) == 2 and s.isalpha():
                return s
    return None

df_b['state'] = df_b['description'].apply(extract_state)

# Build reviews df
with open(reviews_path, 'r') as f:
    reviews = json.load(f)
df_r = pd.DataFrame(reviews)
df_r['rating'] = pd.to_numeric(df_r['rating'], errors='coerce')

# Merge
df = df_r.merge(df_b[['business_ref','state']], on='business_ref', how='left')

# Group
grp = df.dropna(subset=['state']).groupby('state').agg(review_count=('review_id','count'), average_rating=('rating','mean')).reset_index()

# Prepare result
if grp.empty:
    result = {"state": None, "review_count": 0, "average_rating": None, "state_groups": []}
else:
    grp['average_rating'] = grp['average_rating'].round(2)
    top = grp.loc[grp['review_count'].idxmax()]
    result = {"state": top['state'], "review_count": int(top['review_count']), "average_rating": float(top['average_rating']), "state_groups": grp.to_dict(orient='records')}

print("__RESULT__:")
print(json.dumps(result))"""

env_args = {'var_call_M53Zd50Tdxo3C8spMUnoWPOA': ['business', 'checkin'], 'var_call_QIGLXDR8UK49ck6WHsYD4aTj': ['review', 'tip', 'user'], 'var_call_sjU0gxiN4j5ujlsu5JKnWCGD': [{'business_id': 'businessid_49', 'review_count': '8', 'description': 'Located at 6901 Phelps Rd in Goleta, CA, this facility offers a nurturing environment for young learners, providing a range of services in Education, Elementary Schools, Child Care & Day Care, Local Services, Preschools, and Montessori Schools.'}, {'business_id': 'businessid_47', 'review_count': '81', 'description': 'Located at 9916 Clayton Rd in St. Louis, MO, this establishment offers a wide range of services, including Hair Salons, Beauty & Spas, Hair Stylists, Skin Care, Blow Dry/Out Services, and Makeup Artists.'}, {'business_id': 'businessid_88', 'review_count': '39', 'description': 'Located at 11655 W Executive Dr in Boise, ID, this facility offers enthusiasts a premier destination for Gun/Rifle Ranges, Active Life.'}, {'business_id': 'businessid_41', 'review_count': '5', 'description': 'Located at 1615 Pasadena Ave S, Ste 430 in Saint Petersburg, FL, this facility offers a range of services in Internal Medicine, Doctors, Health & Medical.'}, {'business_id': 'businessid_33', 'review_count': '28', 'description': 'Located at 9655 E US Hwy 36, Unit H in Avon, IN, this establishment offers a range of services including Nail Salons, Hair Removal, Beauty & Spas, and Waxing.'}], 'var_call_OtIIQA6kEpd4jg9w3UlnX9u7': 'file_storage/call_OtIIQA6kEpd4jg9w3UlnX9u7.json', 'var_call_uDFvRZebNdcirwemcZg9t5iA': {'state': None, 'review_count': 0, 'average_rating': None}, 'var_call_0GFycG4Z9snBrZyDJuKbuR33': {'businesses': [{'business_id': 'businessid_49', 'review_count': '8', 'description': 'Located at 6901 Phelps Rd in Goleta, CA, this facility offers a nurturing environment for young learners, providing a range of services in Education, Elementary Schools, Child Care & Day Care, Local Services, Preschools, and Montessori Schools.', 'id_num': '49', 'business_ref': 'businessref_49', 'state': None}, {'business_id': 'businessid_47', 'review_count': '81', 'description': 'Located at 9916 Clayton Rd in St. Louis, MO, this establishment offers a wide range of services, including Hair Salons, Beauty & Spas, Hair Stylists, Skin Care, Blow Dry/Out Services, and Makeup Artists.', 'id_num': '47', 'business_ref': 'businessref_47', 'state': None}, {'business_id': 'businessid_88', 'review_count': '39', 'description': 'Located at 11655 W Executive Dr in Boise, ID, this facility offers enthusiasts a premier destination for Gun/Rifle Ranges, Active Life.', 'id_num': '88', 'business_ref': 'businessref_88', 'state': None}, {'business_id': 'businessid_41', 'review_count': '5', 'description': 'Located at 1615 Pasadena Ave S, Ste 430 in Saint Petersburg, FL, this facility offers a range of services in Internal Medicine, Doctors, Health & Medical.', 'id_num': '41', 'business_ref': 'businessref_41', 'state': None}, {'business_id': 'businessid_33', 'review_count': '28', 'description': 'Located at 9655 E US Hwy 36, Unit H in Avon, IN, this establishment offers a range of services including Nail Salons, Hair Removal, Beauty & Spas, and Waxing.', 'id_num': '33', 'business_ref': 'businessref_33', 'state': None}], 'matches': [{'business_ref': 'businessref_49', 'state': None, 'review_matches': 6}, {'business_ref': 'businessref_47', 'state': None, 'review_matches': 42}, {'business_ref': 'businessref_88', 'state': None, 'review_matches': 33}, {'business_ref': 'businessref_41', 'state': None, 'review_matches': 4}, {'business_ref': 'businessref_33', 'state': None, 'review_matches': 23}], 'state_groups': []}}

exec(code, env_args)
