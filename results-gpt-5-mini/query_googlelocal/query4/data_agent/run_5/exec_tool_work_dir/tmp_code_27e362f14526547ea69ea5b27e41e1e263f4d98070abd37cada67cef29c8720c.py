code = """import json
import pandas as pd

# Load results from previous tool calls (available in storage variables)
reviews = pd.DataFrame(var_call_6iqeK4kMiiEzJc2iCmHzozqM)
biz = pd.DataFrame(var_call_TdJZBieAyCArX5kYFld3EzE2)

# Ensure counts are integers
reviews['high_reviews'] = reviews['high_reviews'].astype(int)

# Merge to get business names
merged = pd.merge(reviews, biz, on='gmap_id', how='left')

# Get top 3
top3 = merged.sort_values('high_reviews', ascending=False).head(3)

# Prepare output list
output = []
for _, row in top3.iterrows():
    output.append({'name': row['name'], 'high_rating_review_count': int(row['high_reviews'])})

result = json.dumps(output)
print("__RESULT__:")
print(result)"""

env_args = {'var_call_6iqeK4kMiiEzJc2iCmHzozqM': [{'gmap_id': 'gmap_20', 'high_reviews': '8'}, {'gmap_id': 'gmap_53', 'high_reviews': '7'}, {'gmap_id': 'gmap_40', 'high_reviews': '6'}, {'gmap_id': 'gmap_35', 'high_reviews': '6'}, {'gmap_id': 'gmap_72', 'high_reviews': '5'}, {'gmap_id': 'gmap_62', 'high_reviews': '5'}, {'gmap_id': 'gmap_46', 'high_reviews': '5'}, {'gmap_id': 'gmap_17', 'high_reviews': '4'}, {'gmap_id': 'gmap_69', 'high_reviews': '3'}, {'gmap_id': 'gmap_56', 'high_reviews': '3'}], 'var_call_TdJZBieAyCArX5kYFld3EzE2': [{'name': 'Aurora Massage', 'gmap_id': 'gmap_20'}, {'name': 'The Boochyard @ Local Roots', 'gmap_id': 'gmap_53'}, {'name': 'Widows Peak Salon', 'gmap_id': 'gmap_40'}]}

exec(code, env_args)
