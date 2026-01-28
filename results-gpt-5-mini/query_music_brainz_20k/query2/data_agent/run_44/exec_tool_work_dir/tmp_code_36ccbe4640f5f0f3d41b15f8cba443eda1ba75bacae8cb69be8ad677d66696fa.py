code = """import pandas as pd
import json
# var_call_SBQDsTqQIovrt2rOgvzqq7D9 is available from previous query_db call
records = var_call_SBQDsTqQIovrt2rOgvzqq7D9
df = pd.DataFrame(records)
# convert revenue to float
df['revenue_usd'] = df['revenue_usd'].astype(float)
# aggregate revenue by store
store_totals = df.groupby('store', dropna=False)['revenue_usd'].sum().reset_index()
# find top store
top_row = store_totals.loc[store_totals['revenue_usd'].idxmax()]
result = {
    'store_totals': dict(zip(store_totals['store'], store_totals['revenue_usd'].round(2).astype(float))),
    'top_store': top_row['store'],
    'top_revenue_usd': round(float(top_row['revenue_usd']), 2)
}
print("__RESULT__:")
print(json.dumps(result))"""

env_args = {'var_call_vgCwN5KYL0xkDYColN5cPIIQ': [{'track_id': '4122', 'source_id': '5', 'source_track_id': '10609996', 'title': 'Street Hype', 'artist': 'Brucqe Maginnis', 'album': 'Groove City', 'year': '2005'}], 'var_call_HpfquAoBUclWULb3tAX18pSI': [{'track_id': '4122', 'country': 'France', 'store': 'Amazon Music', 'revenue_usd': '304.13'}, {'track_id': '4122', 'country': 'Germany', 'store': 'Apple Music', 'revenue_usd': '47.52'}], 'var_call_v2tlhJtadMvv0idZ5RHA1ohp': [{'track_id': '4122', 'title': 'Street Hype', 'artist': 'Brucqe Maginnis', 'album': 'Groove City', 'year': '2005'}, {'track_id': '4628', 'title': 'Street Hype - Groove City', 'artist': 'Bruce Maginnis', 'album': 'None', 'year': "'05"}, {'track_id': '13758', 'title': 'StreetH ype (Groove City)', 'artist': 'Bruce Maginnis', 'album': 'Groove City', 'year': '2005'}, {'track_id': '14080', 'title': '011-Street Hype', 'artist': 'Bruce Maginnis', 'album': 'Groove City (2005)', 'year': 'None'}], 'var_call_SBQDsTqQIovrt2rOgvzqq7D9': [{'track_id': '13758', 'store': 'iTunes', 'country': 'USA', 'revenue_usd': '148.95'}, {'track_id': '13758', 'store': 'Google Play', 'country': 'UK', 'revenue_usd': '51.4'}, {'track_id': '4122', 'store': 'Apple Music', 'country': 'Germany', 'revenue_usd': '47.52'}, {'track_id': '4122', 'store': 'Amazon Music', 'country': 'France', 'revenue_usd': '304.13'}, {'track_id': '14080', 'store': 'Apple Music', 'country': 'UK', 'revenue_usd': '68.68'}, {'track_id': '4628', 'store': 'iTunes', 'country': 'France', 'revenue_usd': '505.61'}, {'track_id': '13758', 'store': 'Apple Music', 'country': 'UK', 'revenue_usd': '477.06'}, {'track_id': '13758', 'store': 'Amazon Music', 'country': 'France', 'revenue_usd': '378.1'}]}

exec(code, env_args)
