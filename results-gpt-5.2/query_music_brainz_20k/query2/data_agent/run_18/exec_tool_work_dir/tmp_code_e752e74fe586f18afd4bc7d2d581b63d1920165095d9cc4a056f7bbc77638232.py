code = """import json, pandas as pd

df = pd.DataFrame(var_call_HYOGS51ZZBx4oYTqOws0oV2D)
# Ensure numeric
if not df.empty:
    df['total_revenue_usd'] = pd.to_numeric(df['total_revenue_usd'])
    top = df.sort_values('total_revenue_usd', ascending=False).iloc[0]
    result = {
        'store': str(top['store']),
        'total_revenue_usd': float(top['total_revenue_usd'])
    }
else:
    result = None

print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_call_V0SxvPESQoDfIiHY4NtvvDM5': [{'track_id': '4122', 'title': 'Street Hype', 'artist': 'Brucqe Maginnis', 'album': 'Groove City', 'year': '2005', 'length': '177000', 'language': 'English'}], 'var_call_UfDVpvOC2H2WObX3n9agIUW7': [{'track_id': '4628', 'title': 'Street Hype - Groove City', 'artist': 'Bruce Maginnis', 'album': 'None', 'year': "'05", 'length': '2.95', 'language': 'English'}, {'track_id': '14080', 'title': '011-Street Hype', 'artist': 'Bruce Maginnis', 'album': 'Groove City (2005)', 'year': 'None', 'length': '2m 57sec', 'language': 'Eng.'}, {'track_id': '4122', 'title': 'Street Hype', 'artist': 'Brucqe Maginnis', 'album': 'Groove City', 'year': '2005', 'length': '177000', 'language': 'English'}], 'var_call_9QJO2uOXsXHOQD392Essh1BZ': ['sales'], 'var_call_HYOGS51ZZBx4oYTqOws0oV2D': [{'store': 'iTunes', 'total_revenue_usd': '505.61'}, {'store': 'Amazon Music', 'total_revenue_usd': '304.13'}, {'store': 'Apple Music', 'total_revenue_usd': '116.20000000000002'}]}

exec(code, env_args)
