code = """import json
import pandas as pd
import re

# Load business data from the JSON file path stored in var_call_99E5q3dmMndEDUfxbuQsdkl1
business = pd.read_json(var_call_99E5q3dmMndEDUfxbuQsdkl1)
# Load aggregated reviews per business from var_call_enhSIvPnTMa9Y9p6kYApNvsh (already a list of dicts)
reviews = pd.DataFrame(var_call_enhSIvPnTMa9Y9p6kYApNvsh)
# Normalize types
reviews['review_count'] = reviews['review_count'].astype(int)
# Map review business_ref to business collection business_id
reviews['business_id'] = reviews['business_ref'].str.replace('businessref_', 'businessid_')

# Merge to get business descriptions
merged = reviews.merge(business[['business_id', 'description']], on='business_id', how='left')

# Function to extract category tokens from description
def extract_categories(desc):
    if not isinstance(desc, str):
        return []
    # Take the last occurrence after ' in ' which tends to list categories
    if ' in ' in desc:
        part = desc.rsplit(' in ', 1)[-1]
    else:
        part = desc
    # Remove trailing punctuation
    part = part.strip().strip('.')
    # Normalize separators: replace '&' with ' and '
    part = part.replace('&', ' and ')
    # Split on commas, slashes, semicolons, and the word ' and '
    tokens = [t.strip() for t in re.split(',|/|;|\band\b', part) if t.strip()]
    # Further split tokens that contain other separators like ' and ' already handled
    # Clean tokens: remove stray words like 'services' or 'offers a range of services' not expected here
    cleaned = []
    for t in tokens:
        # remove leading phrases like 'this establishment offers a range of services in'
        t = re.sub(r"this establishment offers a range of services in\s*", '', t, flags=re.I)
        t = re.sub(r"this facility offers a range of services in\s*", '', t, flags=re.I)
        t = re.sub(r"offers a range of services in\s*", '', t, flags=re.I)
        t = re.sub(r"offers .* in\s*", '', t, flags=re.I)
        t = t.strip().strip('.')
        if t:
            cleaned.append(t)
    return cleaned

# Extract categories and explode
merged['categories'] = merged['description'].apply(extract_categories)
exploded = merged.explode('categories')
# Drop rows without categories
exploded = exploded[exploded['categories'].notna() & (exploded['categories'] != '')]

# Group by category and sum review_count
grouped = exploded.groupby('categories', dropna=True)['review_count'].sum().reset_index()
# Sort descending and take top 5
grouped = grouped.sort_values('review_count', ascending=False).head(5)

# Prepare output list of dicts
result_list = []
for _, row in grouped.iterrows():
    result_list.append({
        'category': row['categories'],
        'total_reviews': int(row['review_count'])
    })

# Print in required format
print("__RESULT__:")
print(json.dumps(result_list))"""

env_args = {'var_call_rb1hhwBE8GUJk0nF0CCsLw2d': ['business', 'checkin'], 'var_call_c72JYk1I8DPeTJAdZBj5XKKE': ['review', 'tip', 'user'], 'var_call_99E5q3dmMndEDUfxbuQsdkl1': 'file_storage/call_99E5q3dmMndEDUfxbuQsdkl1.json', 'var_call_enhSIvPnTMa9Y9p6kYApNvsh': [{'business_ref': 'businessref_13', 'review_count': '1'}, {'business_ref': 'businessref_79', 'review_count': '1'}, {'business_ref': 'businessref_6', 'review_count': '1'}, {'business_ref': 'businessref_74', 'review_count': '2'}, {'business_ref': 'businessref_66', 'review_count': '2'}, {'business_ref': 'businessref_15', 'review_count': '1'}, {'business_ref': 'businessref_33', 'review_count': '2'}, {'business_ref': 'businessref_36', 'review_count': '2'}, {'business_ref': 'businessref_60', 'review_count': '2'}, {'business_ref': 'businessref_12', 'review_count': '1'}, {'business_ref': 'businessref_53', 'review_count': '1'}, {'business_ref': 'businessref_57', 'review_count': '2'}, {'business_ref': 'businessref_86', 'review_count': '1'}, {'business_ref': 'businessref_62', 'review_count': '1'}, {'business_ref': 'businessref_37', 'review_count': '1'}, {'business_ref': 'businessref_92', 'review_count': '2'}, {'business_ref': 'businessref_31', 'review_count': '1'}, {'business_ref': 'businessref_26', 'review_count': '1'}, {'business_ref': 'businessref_68', 'review_count': '1'}, {'business_ref': 'businessref_45', 'review_count': '3'}, {'business_ref': 'businessref_96', 'review_count': '2'}, {'business_ref': 'businessref_98', 'review_count': '1'}, {'business_ref': 'businessref_14', 'review_count': '1'}, {'business_ref': 'businessref_20', 'review_count': '1'}, {'business_ref': 'businessref_41', 'review_count': '1'}, {'business_ref': 'businessref_10', 'review_count': '1'}]}

exec(code, env_args)
