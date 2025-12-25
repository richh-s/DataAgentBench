code = """import json, pandas as pd

# Load reviews from file path
with open(var_call_Hr6VrH5J2BcDP71SbIr3IMrR, 'r') as f:
    reviews = json.load(f)

biz_cc = pd.DataFrame(var_call_9Rbjsyjh2lqluhUGEhwwqNE6)
reviews_df = pd.DataFrame(reviews)

# Map business_id -> business_ref
biz_cc['business_ref'] = biz_cc['business_id'].str.replace('businessid_', 'businessref_', regex=False)

# Merge reviews with cc businesses
merged = pd.merge(reviews_df, biz_cc, on='business_ref', how='inner')

# Extract categories; assume field may be missing
if 'categories' in merged.columns:
    merged['categories'] = merged['categories'].fillna('')
else:
    merged['categories'] = ''

# Convert rating to float
merged['rating'] = merged['rating'].astype(float)

# For simplicity, treat full categories string as the category key
agg = merged.groupby('categories').agg(business_count=('business_id', 'nunique'), avg_rating=('rating', 'mean')).reset_index()

# Find category with max business_count
if len(agg) == 0:
    result = {"category": None, "business_count": 0, "average_rating": None}
else:
    top = agg.sort_values(['business_count', 'avg_rating'], ascending=[False, False]).iloc[0]
    result = {
        "category": top['categories'],
        "business_count": int(top['business_count']),
        "average_rating": round(float(top['avg_rating']), 3)
    }

out = json.dumps(result)
print("__RESULT__:")
print(out)"""

env_args = {'var_call_9Rbjsyjh2lqluhUGEhwwqNE6': [{'business_id': 'businessid_49'}, {'business_id': 'businessid_47'}, {'business_id': 'businessid_88'}, {'business_id': 'businessid_33'}, {'business_id': 'businessid_92'}], 'var_call_Hr6VrH5J2BcDP71SbIr3IMrR': 'file_storage/call_Hr6VrH5J2BcDP71SbIr3IMrR.json'}

exec(code, env_args)
