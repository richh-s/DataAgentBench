code = """import json
# var_call_VTbNontnOulQtskKOTpw4h8N is available from previous query
data = var_call_VTbNontnOulQtskKOTpw4h8N
# Convert revenue to float and find top store
processed = []
for r in data:
    rev = r.get('revenue_usd')
    try:
        rev_f = float(rev)
    except Exception:
        rev_f = None
    processed.append({'store': r.get('store'), 'revenue_usd': rev_f})
processed = [r for r in processed if r['revenue_usd'] is not None]
processed.sort(key=lambda x: x['revenue_usd'], reverse=True)
if processed:
    top = processed[0]
    result = top
else:
    result = {'store': None, 'revenue_usd': None}
print("----BEGIN PRINT FORMAT----")
print("print(\"__RESULT__:\")")
print("print('" + json.dumps(result) + "')")
print("----END PRINT FORMAT----")"""

env_args = {'var_call_olRootycY9yeJvLvW6Ne7kdb': ['tracks'], 'var_call_wmx7d3LGK7gtlrkjd5F7f21O': ['sales'], 'var_call_ixFD7xWltLq446cSYbrn0A23': [{'track_id': '4122', 'title': 'Street Hype', 'artist': 'Brucqe Maginnis', 'album': 'Groove City', 'year': '2005'}, {'track_id': '4628', 'title': 'Street Hype - Groove City', 'artist': 'Bruce Maginnis', 'album': 'None', 'year': "'05"}, {'track_id': '14080', 'title': '011-Street Hype', 'artist': 'Bruce Maginnis', 'album': 'Groove City (2005)', 'year': 'None'}], 'var_call_VTbNontnOulQtskKOTpw4h8N': [{'store': 'iTunes', 'revenue_usd': '505.61'}, {'store': 'Amazon Music', 'revenue_usd': '304.13'}, {'store': 'Apple Music', 'revenue_usd': '116.20000000000002'}]}

exec(code, env_args)
