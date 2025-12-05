code = """import json
import pandas as pd

reviews = var_call_0GY8Z5tQc0QkOS1YSEgmJFRm
businesses = var_call_ScRT5SoXPcdFSMkQ5ju4FIo5

rev_df = pd.DataFrame(reviews)
biz_df = pd.DataFrame(businesses)

merged = rev_df.merge(biz_df, on='gmap_id')
merged = merged[['name', 'high_review_count']]
merged['high_review_count'] = merged['high_review_count'].astype(int)
merged = merged.sort_values('high_review_count', ascending=False)

result = merged.to_dict(orient='records')

print("__RESULT__:")
print(json.dumps(result))"""

env_args = {'var_call_0GY8Z5tQc0QkOS1YSEgmJFRm': [{'gmap_id': 'gmap_20', 'high_review_count': '8'}, {'gmap_id': 'gmap_53', 'high_review_count': '7'}, {'gmap_id': 'gmap_40', 'high_review_count': '6'}], 'var_call_C4DWrdXJuKqUMUOJiFFsr1Mu': ['business_description'], 'var_call_ScRT5SoXPcdFSMkQ5ju4FIo5': [{'gmap_id': 'gmap_20', 'name': 'Aurora Massage'}, {'gmap_id': 'gmap_53', 'name': 'The Boochyard @ Local Roots'}, {'gmap_id': 'gmap_40', 'name': 'Widows Peak Salon'}]}

exec(code, env_args)
