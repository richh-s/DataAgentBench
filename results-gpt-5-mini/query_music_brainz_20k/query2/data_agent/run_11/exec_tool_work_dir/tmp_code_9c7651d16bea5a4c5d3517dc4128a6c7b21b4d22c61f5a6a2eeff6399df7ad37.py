code = """import json
records = var_call_EGnnGCwwS8985MsnnAXitxlQ
# Convert revenue to float
for r in records:
    try:
        r['total_revenue_usd'] = float(r['total_revenue_usd'])
    except:
        r['total_revenue_usd'] = None
# Find top store
records_valid = [r for r in records if r['total_revenue_usd'] is not None]
if records_valid:
    top = max(records_valid, key=lambda x: x['total_revenue_usd'])
    result = {"top_store": top['store'], "total_revenue_usd": top['total_revenue_usd']}
else:
    result = {"top_store": None, "total_revenue_usd": None}
print("__RESULT__:")
print(json.dumps(result))"""

env_args = {'var_call_DQnBQebUlktbWN86LyhWZAYy': [{'track_id': '4122', 'title': 'Street Hype', 'artist': 'Brucqe Maginnis', 'album': 'Groove City', 'year': '2005', 'length': '177000', 'language': 'English'}, {'track_id': '4628', 'title': 'Street Hype - Groove City', 'artist': 'Bruce Maginnis', 'album': 'None', 'year': "'05", 'length': '2.95', 'language': 'English'}, {'track_id': '13758', 'title': 'StreetH ype (Groove City)', 'artist': 'Bruce Maginnis', 'album': 'Groove City', 'year': '2005', 'length': 'None', 'language': '02:57'}, {'track_id': '14080', 'title': '011-Street Hype', 'artist': 'Bruce Maginnis', 'album': 'Groove City (2005)', 'year': 'None', 'length': '2m 57sec', 'language': 'Eng.'}], 'var_call_EGnnGCwwS8985MsnnAXitxlQ': [{'store': 'Amazon Music', 'total_revenue_usd': '682.23'}, {'store': 'iTunes', 'total_revenue_usd': '654.56'}, {'store': 'Apple Music', 'total_revenue_usd': '593.26'}, {'store': 'Google Play', 'total_revenue_usd': '51.4'}]}

exec(code, env_args)
