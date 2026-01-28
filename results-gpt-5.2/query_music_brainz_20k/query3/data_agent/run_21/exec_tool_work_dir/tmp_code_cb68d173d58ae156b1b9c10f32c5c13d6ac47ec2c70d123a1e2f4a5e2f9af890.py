code = """import json, pandas as pd

sales_top = pd.DataFrame(var_call_V2KNycp7Tv6DeDnK4tflUpdD)
sales_top['track_id'] = sales_top['track_id'].astype(int)
sales_top['total_revenue_usd'] = sales_top['total_revenue_usd'].astype(float)

# Load full tracks table from json file
path = var_call_MSmS9CnMSoQ06wNOflaumeiM
with open(path, 'r', encoding='utf-8') as f:
    tracks_records = json.load(f)
tracks = pd.DataFrame(tracks_records)
tracks['track_id'] = tracks['track_id'].astype(int)

# Merge for the top track_id only
best = sales_top.sort_values('total_revenue_usd', ascending=False).iloc[0]
best_track = tracks.loc[tracks['track_id'] == int(best['track_id'])].iloc[0].to_dict()

result = {
    'track_id': int(best['track_id']),
    'title': best_track.get('title'),
    'artist': best_track.get('artist'),
    'album': best_track.get('album'),
    'year': best_track.get('year'),
    'total_revenue_usd': float(best['total_revenue_usd'])
}

print('__RESULT__:')
print(json.dumps(result, ensure_ascii=False))"""

env_args = {'var_call_V2KNycp7Tv6DeDnK4tflUpdD': [{'track_id': '14719', 'total_revenue_usd': '2522.82'}, {'track_id': '5124', 'total_revenue_usd': '2503.1899999999996'}, {'track_id': '1344', 'total_revenue_usd': '2500.72'}, {'track_id': '6725', 'total_revenue_usd': '2489.81'}, {'track_id': '10377', 'total_revenue_usd': '2466.71'}, {'track_id': '5050', 'total_revenue_usd': '2466.3100000000004'}, {'track_id': '6667', 'total_revenue_usd': '2452.7000000000003'}, {'track_id': '7245', 'total_revenue_usd': '2436.9700000000003'}, {'track_id': '11641', 'total_revenue_usd': '2428.2200000000003'}, {'track_id': '964', 'total_revenue_usd': '2425.61'}, {'track_id': '12984', 'total_revenue_usd': '2401.71'}, {'track_id': '6208', 'total_revenue_usd': '2385.0299999999997'}, {'track_id': '666', 'total_revenue_usd': '2382.74'}, {'track_id': '12620', 'total_revenue_usd': '2377.59'}, {'track_id': '19232', 'total_revenue_usd': '2368.7499999999995'}, {'track_id': '17757', 'total_revenue_usd': '2365.59'}, {'track_id': '3462', 'total_revenue_usd': '2359.23'}, {'track_id': '9639', 'total_revenue_usd': '2351.68'}, {'track_id': '18760', 'total_revenue_usd': '2349.33'}, {'track_id': '2516', 'total_revenue_usd': '2346.18'}, {'track_id': '6326', 'total_revenue_usd': '2331.91'}, {'track_id': '5836', 'total_revenue_usd': '2321.31'}, {'track_id': '9988', 'total_revenue_usd': '2317.41'}, {'track_id': '18508', 'total_revenue_usd': '2308.44'}, {'track_id': '10760', 'total_revenue_usd': '2293.1099999999997'}, {'track_id': '9002', 'total_revenue_usd': '2288.23'}, {'track_id': '14169', 'total_revenue_usd': '2281.23'}, {'track_id': '9649', 'total_revenue_usd': '2276.7200000000003'}, {'track_id': '10856', 'total_revenue_usd': '2275.85'}, {'track_id': '7422', 'total_revenue_usd': '2275.04'}, {'track_id': '8705', 'total_revenue_usd': '2273.46'}, {'track_id': '5933', 'total_revenue_usd': '2271.62'}, {'track_id': '5809', 'total_revenue_usd': '2269.24'}, {'track_id': '16084', 'total_revenue_usd': '2259.8599999999997'}, {'track_id': '9652', 'total_revenue_usd': '2251.2200000000003'}, {'track_id': '3412', 'total_revenue_usd': '2250.04'}, {'track_id': '15664', 'total_revenue_usd': '2249.3900000000003'}, {'track_id': '12207', 'total_revenue_usd': '2248.7200000000003'}, {'track_id': '5467', 'total_revenue_usd': '2246.94'}, {'track_id': '13102', 'total_revenue_usd': '2244.51'}, {'track_id': '4145', 'total_revenue_usd': '2243.27'}, {'track_id': '13132', 'total_revenue_usd': '2238.21'}, {'track_id': '13211', 'total_revenue_usd': '2233.62'}, {'track_id': '2244', 'total_revenue_usd': '2230.04'}, {'track_id': '18846', 'total_revenue_usd': '2227.95'}, {'track_id': '2029', 'total_revenue_usd': '2226.42'}, {'track_id': '3488', 'total_revenue_usd': '2222.25'}, {'track_id': '17669', 'total_revenue_usd': '2212.4700000000003'}, {'track_id': '12969', 'total_revenue_usd': '2211.97'}, {'track_id': '12551', 'total_revenue_usd': '2210.78'}], 'var_call_MSmS9CnMSoQ06wNOflaumeiM': 'file_storage/call_MSmS9CnMSoQ06wNOflaumeiM.json'}

exec(code, env_args)
