code = """import json
# Access previous query result
data = var_call_VTbNontnOulQtskKOTpw4h8N
# Process
processed = []
for r in data:
    try:
        rev = float(r.get('revenue_usd'))
    except Exception:
        rev = None
    processed.append({'store': r.get('store'), 'revenue_usd': rev})
processed = [r for r in processed if r['revenue_usd'] is not None]
processed.sort(key=lambda x: x['revenue_usd'], reverse=True)
result = processed[0] if processed else {'store': None, 'revenue_usd': None}
# Build the exact required print block
block = '----BEGIN PRINT FORMAT----\nprint("__RESULT__:")\nprint(' + json.dumps(result) + ')\n----END PRINT FORMAT----'
print(block)"""

env_args = {'var_call_olRootycY9yeJvLvW6Ne7kdb': ['tracks'], 'var_call_wmx7d3LGK7gtlrkjd5F7f21O': ['sales'], 'var_call_ixFD7xWltLq446cSYbrn0A23': [{'track_id': '4122', 'title': 'Street Hype', 'artist': 'Brucqe Maginnis', 'album': 'Groove City', 'year': '2005'}, {'track_id': '4628', 'title': 'Street Hype - Groove City', 'artist': 'Bruce Maginnis', 'album': 'None', 'year': "'05"}, {'track_id': '14080', 'title': '011-Street Hype', 'artist': 'Bruce Maginnis', 'album': 'Groove City (2005)', 'year': 'None'}], 'var_call_VTbNontnOulQtskKOTpw4h8N': [{'store': 'iTunes', 'revenue_usd': '505.61'}, {'store': 'Amazon Music', 'revenue_usd': '304.13'}, {'store': 'Apple Music', 'revenue_usd': '116.20000000000002'}]}

exec(code, env_args)
