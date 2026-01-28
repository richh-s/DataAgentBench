code = """import json
import pandas as pd
# load results from previous query calls
rev_counts = pd.DataFrame(var_call_xn8xLICy5aHnmoKWJJPY6bdZ)
biz = pd.DataFrame(var_call_iGV8ADsxkkvG3QB6dPU4kcCZ)

# merge to get names with counts
merged = pd.merge(biz, rev_counts, on='gmap_id')
# ensure counts are integers
merged['high_reviews'] = merged['high_reviews'].astype(int)
# sort
merged = merged.sort_values('high_reviews', ascending=False)
# prepare final list of dicts
result = merged[['name','high_reviews']].to_dict(orient='records')

print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_call_xn8xLICy5aHnmoKWJJPY6bdZ': [{'gmap_id': 'gmap_20', 'high_reviews': '8'}, {'gmap_id': 'gmap_53', 'high_reviews': '7'}, {'gmap_id': 'gmap_40', 'high_reviews': '6'}], 'var_call_iGV8ADsxkkvG3QB6dPU4kcCZ': [{'name': 'Aurora Massage', 'gmap_id': 'gmap_20'}, {'name': 'The Boochyard @ Local Roots', 'gmap_id': 'gmap_53'}, {'name': 'Widows Peak Salon', 'gmap_id': 'gmap_40'}]}

exec(code, env_args)
