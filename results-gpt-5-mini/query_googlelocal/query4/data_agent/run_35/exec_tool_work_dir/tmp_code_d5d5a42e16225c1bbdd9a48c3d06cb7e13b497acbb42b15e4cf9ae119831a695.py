code = """import json
import pandas as pd
# var_call_K1LDCGZjxxRI337s0rgEhLNk and var_call_EVBZhAiVThBC6UgYdZqDoxzl are available from storage
reviews = pd.DataFrame(var_call_K1LDCGZjxxRI337s0rgEhLNk)
biz = pd.DataFrame(var_call_EVBZhAiVThBC6UgYdZqDoxzl)
# Convert high_reviews to int
reviews['high_reviews'] = reviews['high_reviews'].astype(int)
# Merge to get names for top 3
merged = pd.merge(reviews, biz, on='gmap_id', how='left')
# Take top 3 by high_reviews
top3 = merged.sort_values('high_reviews', ascending=False).head(3)
# Build output list
output = []
for _, row in top3.iterrows():
    output.append({
        'name': row['name'],
        'high_rating_review_count': int(row['high_reviews'])
    })

print("__RESULT__:")
print(json.dumps(output))"""

env_args = {'var_call_K1LDCGZjxxRI337s0rgEhLNk': [{'gmap_id': 'gmap_20', 'high_reviews': '8'}, {'gmap_id': 'gmap_53', 'high_reviews': '7'}, {'gmap_id': 'gmap_40', 'high_reviews': '6'}, {'gmap_id': 'gmap_35', 'high_reviews': '6'}, {'gmap_id': 'gmap_72', 'high_reviews': '5'}, {'gmap_id': 'gmap_62', 'high_reviews': '5'}, {'gmap_id': 'gmap_46', 'high_reviews': '5'}, {'gmap_id': 'gmap_17', 'high_reviews': '4'}, {'gmap_id': 'gmap_69', 'high_reviews': '3'}, {'gmap_id': 'gmap_56', 'high_reviews': '3'}], 'var_call_EVBZhAiVThBC6UgYdZqDoxzl': [{'gmap_id': 'gmap_20', 'name': 'Aurora Massage'}, {'gmap_id': 'gmap_53', 'name': 'The Boochyard @ Local Roots'}, {'gmap_id': 'gmap_40', 'name': 'Widows Peak Salon'}]}

exec(code, env_args)
