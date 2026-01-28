code = """import json, re
import pandas as pd

businesses = var_call_8OFKxgaVzHgJgMY9djEanppl
with open(var_call_lZmRttBv8Pzc064QJaUFRaa8, 'r') as f:
    reviews = json.load(f)

df_b = pd.DataFrame(businesses)
df_r = pd.DataFrame(reviews)

# robust state extraction
patterns = [r',\s*([A-Z]{2})(?:\b|,)', r'\b([A-Z]{2})\s+\d{5}\b']

def extract_state(desc):
    if not isinstance(desc, str):
        return None
    # Try to find two-letter state code (all caps)
    m = re.search(r',\s*([A-Z]{2})(?:\b|,)', desc)
    if m:
        return m.group(1)
    # try words like 'City, State '
    m2 = re.search(r' in [A-Za-z .]+,\s*([A-Za-z]{2})', desc)
    if m2:
        return m2.group(1).upper()
    return None

df_b['state'] = df_b['description'].apply(extract_state)

# Map review business_ref to business_id
if 'rating' in df_r.columns:
    df_r['rating'] = pd.to_numeric(df_r['rating'], errors='coerce')

df_r['business_id'] = df_r['business_ref'].str.replace('businessref_', 'businessid_', regex=False)

# counts per business_id in reviews
counts = df_r.groupby('business_id').size().reset_index(name='review_count')

# Merge business data
merged = counts.merge(df_b[['business_id','state']], on='business_id', how='left')

# For debugging
matched = merged[merged['state'].notna()]

# Compute per-state review counts and avg rating using review-level merge
df_reviews_merged = df_r.merge(df_b[['business_id','state']], on='business_id', how='left')
state_group = df_reviews_merged[df_reviews_merged['state'].notna()].groupby('state').agg(review_count=('rating','count'), average_rating=('rating','mean')).reset_index()

if not state_group.empty:
    best = state_group.loc[state_group['review_count'].idxmax()]
    result = {
        'state': best['state'],
        'review_count': int(best['review_count']),
        'average_rating': round(float(best['average_rating']),2)
    }
else:
    result = {
        'state': None,
        'review_count': 0,
        'average_rating': None,
        'note': 'No reviews could be linked to businesses with extracted state from business descriptions.'
    }

print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_call_dVDQKJmfHPp9d7FPGQP6jiAE': ['business', 'checkin'], 'var_call_plK4ltDd1O3Ctx1mY9p0kb6b': ['review', 'tip', 'user'], 'var_call_8OFKxgaVzHgJgMY9djEanppl': [{'business_id': 'businessid_49', 'review_count': '8', 'description': 'Located at 6901 Phelps Rd in Goleta, CA, this facility offers a nurturing environment for young learners, providing a range of services in Education, Elementary Schools, Child Care & Day Care, Local Services, Preschools, and Montessori Schools.'}, {'business_id': 'businessid_47', 'review_count': '81', 'description': 'Located at 9916 Clayton Rd in St. Louis, MO, this establishment offers a wide range of services, including Hair Salons, Beauty & Spas, Hair Stylists, Skin Care, Blow Dry/Out Services, and Makeup Artists.'}, {'business_id': 'businessid_88', 'review_count': '39', 'description': 'Located at 11655 W Executive Dr in Boise, ID, this facility offers enthusiasts a premier destination for Gun/Rifle Ranges, Active Life.'}, {'business_id': 'businessid_41', 'review_count': '5', 'description': 'Located at 1615 Pasadena Ave S, Ste 430 in Saint Petersburg, FL, this facility offers a range of services in Internal Medicine, Doctors, Health & Medical.'}, {'business_id': 'businessid_33', 'review_count': '28', 'description': 'Located at 9655 E US Hwy 36, Unit H in Avon, IN, this establishment offers a range of services including Nail Salons, Hair Removal, Beauty & Spas, and Waxing.'}], 'var_call_lZmRttBv8Pzc064QJaUFRaa8': 'file_storage/call_lZmRttBv8Pzc064QJaUFRaa8.json', 'var_call_Va7cfeMtMLKTHSxEUozk3iLU': {'state': None, 'review_count': 0, 'average_rating': None}, 'var_call_DTl0KAovyPLnc14knQUnmSmt': {'total_reviews': 2000, 'unique_review_business_ids_count': 100, 'unique_business_ids_in_business_collection_count': 5, 'matching_business_ids_example': ['businessid_33', 'businessid_41', 'businessid_47', 'businessid_49', 'businessid_88'], 'nonmatching_business_ids_sample': ['businessid_1', 'businessid_10', 'businessid_100', 'businessid_11', 'businessid_12', 'businessid_13', 'businessid_14', 'businessid_15', 'businessid_16', 'businessid_17', 'businessid_18', 'businessid_19', 'businessid_2', 'businessid_20', 'businessid_21', 'businessid_22', 'businessid_23', 'businessid_24', 'businessid_25', 'businessid_26'], 'matched_reviews_count': 0, 'state_group': []}, 'var_call_pgEtlVwCLkTK87zozkI0rV6b': [{'business_id': 'businessid_49', 'description': 'Located at 6901 Phelps Rd in Goleta, CA, this facility offers a nurturing environment for young learners, providing a range of services in Education, Elementary Schools, Child Care & Day Care, Local Services, Preschools, and Montessori Schools.', 'extracted_state': None}, {'business_id': 'businessid_47', 'description': 'Located at 9916 Clayton Rd in St. Louis, MO, this establishment offers a wide range of services, including Hair Salons, Beauty & Spas, Hair Stylists, Skin Care, Blow Dry/Out Services, and Makeup Artists.', 'extracted_state': None}, {'business_id': 'businessid_88', 'description': 'Located at 11655 W Executive Dr in Boise, ID, this facility offers enthusiasts a premier destination for Gun/Rifle Ranges, Active Life.', 'extracted_state': None}, {'business_id': 'businessid_41', 'description': 'Located at 1615 Pasadena Ave S, Ste 430 in Saint Petersburg, FL, this facility offers a range of services in Internal Medicine, Doctors, Health & Medical.', 'extracted_state': None}, {'business_id': 'businessid_33', 'description': 'Located at 9655 E US Hwy 36, Unit H in Avon, IN, this establishment offers a range of services including Nail Salons, Hair Removal, Beauty & Spas, and Waxing.', 'extracted_state': None}]}

exec(code, env_args)
