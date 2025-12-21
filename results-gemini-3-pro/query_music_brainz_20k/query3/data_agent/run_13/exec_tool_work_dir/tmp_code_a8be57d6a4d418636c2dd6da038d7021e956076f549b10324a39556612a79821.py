code = """import json
import pandas as pd

# Load data
with open(locals()['var_function-call-7603886357055213310'], 'r') as f:
    sales_data = json.load(f)
with open(locals()['var_function-call-3062453601885258613'], 'r') as f:
    tracks_data = json.load(f)

df_sales = pd.DataFrame(sales_data)
df_tracks = pd.DataFrame(tracks_data)

df_sales['track_id'] = df_sales['track_id'].astype(str)
df_sales['total_revenue'] = df_sales['total_revenue'].astype(float)
df_tracks['track_id'] = df_tracks['track_id'].astype(str)

# Join
df_merged = pd.merge(df_sales, df_tracks, on='track_id', how='left')

# Get top 20 raw revenue tracks
top_raw = df_merged.sort_values('total_revenue', ascending=False).head(20)[['track_id', 'title', 'artist', 'total_revenue']].to_dict(orient='records')

print("__RESULT__:")
print(json.dumps(top_raw))"""

env_args = {'var_function-call-7603886357055213310': 'file_storage/function-call-7603886357055213310.json', 'var_function-call-3062453601885258613': 'file_storage/function-call-3062453601885258613.json', 'var_function-call-9915776680240783115': [{'title': 'None', 'artist': 'None', 'total_revenue': 14647.52}, {'title': '010-', 'artist': 'None', 'total_revenue': 4163.48}, {'title': 'Groovey', 'artist': 'Rich Matteson', 'total_revenue': 4128.59}, {'title': 'The Fire Still Burns', 'artist': 'Russ Ballard', 'total_revenue': 3807.4}, {'title': 'Vostok', 'artist': 'Craig Padilla', 'total_revenue': 3767.95}], 'var_function-call-11307769233160746123': [{'title': '010-', 'artist': 'None', 'total_revenue': 4163.48}, {'title': 'Groovey', 'artist': 'Rich Matteson', 'total_revenue': 4128.59}, {'title': 'The Fire Still Burns', 'artist': 'Russ Ballard', 'total_revenue': 3807.4}, {'title': 'Vostok', 'artist': 'Craig Padilla', 'total_revenue': 3767.95}, {'title': '001-', 'artist': 'None', 'total_revenue': 3742.4399999999996}]}

exec(code, env_args)
