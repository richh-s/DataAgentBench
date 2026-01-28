code = """import json
records = var_call_lr0DaPtNj736rgro5pYNOwgm
for r in records:
    # ensure revenue is numeric
    r['total_revenue_usd'] = float(r['total_revenue_usd'])
best = max(records, key=lambda r: r['total_revenue_usd'])
result = json.dumps({
    "store": best['store'],
    "total_revenue_usd": round(best['total_revenue_usd'], 2),
    "message": f"{best['store']} earned the most revenue for 'Street Hype' across all countries."
})
print("__RESULT__:")
print(result)"""

env_args = {'var_call_g2MKR8f3fShSIo4GL5wshwql': [{'track_id': '4122', 'source_id': '5', 'source_track_id': '10609996', 'title': 'Street Hype', 'artist': 'Brucqe Maginnis', 'album': 'Groove City', 'year': '2005', 'length': '177000', 'language': 'English'}, {'track_id': '4628', 'source_id': '3', 'source_track_id': '46130411MB-01', 'title': 'Street Hype - Groove City', 'artist': 'Bruce Maginnis', 'album': 'None', 'year': "'05", 'length': '2.95', 'language': 'English'}, {'track_id': '14080', 'source_id': '4', 'source_track_id': '149437-A02', 'title': '011-Street Hype', 'artist': 'Bruce Maginnis', 'album': 'Groove City (2005)', 'year': 'None', 'length': '2m 57sec', 'language': 'Eng.'}], 'var_call_lr0DaPtNj736rgro5pYNOwgm': [{'store': 'iTunes', 'total_revenue_usd': '505.61'}, {'store': 'Amazon Music', 'total_revenue_usd': '304.13'}, {'store': 'Apple Music', 'total_revenue_usd': '116.20000000000002'}]}

exec(code, env_args)
