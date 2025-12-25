code = """import json, re, pandas as pd

# Load full results from files
with open(var_call_1v3msmDy5Tql2X3IIYAkpGsD, 'r') as f:
    business_records = json.load(f)
with open(var_call_m9GVRhLdC4511ssOavwQOvij, 'r') as f:
    review_records = json.load(f)

# Create DataFrames
df_bus = pd.DataFrame(business_records)
df_rev = pd.DataFrame(review_records)

# Extract state from description assuming pattern "<city>, <ST>" or "in <City>, <ST>"
state_pattern = re.compile(r',\s*([A-Z]{2})\b')

def extract_state(desc):
    if not isinstance(desc, str):
        return None
    m = state_pattern.search(desc)
    if m:
        return m.group(1)
    return None

df_bus['state'] = df_bus['description'].apply(extract_state)

# Normalize IDs: business_id_# -> businessref_#

def to_business_ref(bid):
    if not isinstance(bid, str):
        return None
    return bid.replace('businessid_', 'businessref_')

df_bus['business_ref'] = df_bus['business_id'].apply(to_business_ref)

# Merge reviews with business to get state
# Ensure rating numeric
df_rev['rating'] = pd.to_numeric(df_rev['rating'])
df = pd.merge(df_rev, df_bus[['business_ref', 'state']], on='business_ref', how='left')

# Drop rows without a US state
states = set(['AL','AK','AZ','AR','CA','CO','CT','DE','FL','GA','HI','ID','IL','IN','IA','KS','KY','LA','ME','MD','MA','MI','MN','MS','MO','MT','NE','NV','NH','NJ','NM','NY','NC','ND','OH','OK','OR','PA','RI','SC','SD','TN','TX','UT','VT','VA','WA','WV','WI','WY'])

df = df[df['state'].isin(states)]

# Aggregate by state
agg = df.groupby('state').agg(review_count=('rating','size'), avg_rating=('rating','mean')).reset_index()

# Get state with max reviews
idx = agg['review_count'].idxmax()
row = agg.loc[idx]

result = {
    'state_with_most_reviews': row['state'],
    'number_of_reviews': int(row['review_count']),
    'average_rating_in_state': round(float(row['avg_rating']), 3)
}

out = json.dumps(result)
print("__RESULT__:")
print(out)"""

env_args = {'var_call_1v3msmDy5Tql2X3IIYAkpGsD': 'file_storage/call_1v3msmDy5Tql2X3IIYAkpGsD.json', 'var_call_m9GVRhLdC4511ssOavwQOvij': 'file_storage/call_m9GVRhLdC4511ssOavwQOvij.json'}

exec(code, env_args)
