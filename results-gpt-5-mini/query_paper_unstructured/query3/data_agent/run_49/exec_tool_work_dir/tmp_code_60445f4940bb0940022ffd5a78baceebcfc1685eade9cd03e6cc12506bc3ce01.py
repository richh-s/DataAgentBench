code = """import json
# load the small citations result
data = var_call_76oDuQfpBtAkenHr0NHbrdbi
# normalize
out = []
for r in data:
    t = r['title']
    tc = int(r['total_citations']) if r['total_citations'] is not None else None
    out.append({'title': t, 'total_citations': tc})
print('__RESULT__:')
print(json.dumps(out))"""

env_args = {'var_call_O6T9ov9jzG5YdiuSjrbbVoPU': ['paper_docs'], 'var_call_CGhz2TCzvXvH0HGqonLb9qg7': 'file_storage/call_CGhz2TCzvXvH0HGqonLb9qg7.json', 'var_call_YMGpqlZGu0Ru3MTyBeiGGaXL': [], 'var_call_lNdRBtmAjueUf49lJMDLkygD': 'file_storage/call_lNdRBtmAjueUf49lJMDLkygD.json', 'var_call_paHLpoipdY0FxATN0W1kuYUM': ['Citations', 'sqlite_sequence'], 'var_call_LOZUWIdfPemCtSAQhAHcUAdw': 'file_storage/call_LOZUWIdfPemCtSAQhAHcUAdw.json', 'var_call_6pF9CiLk8kixPf8GWCy6dT6W': 'file_storage/call_6pF9CiLk8kixPf8GWCy6dT6W.json', 'var_call_yPIk0rqiWwJQULCnISsF4jwb': [], 'var_call_a91mQ9F4i7UWmuPKcZJ2iUho': [], 'var_call_76oDuQfpBtAkenHr0NHbrdbi': [{'title': 'An Empirical Exploration of Mindfulness Design Using Solo Travel Domain', 'total_citations': '352'}, {'title': 'Understanding the Adoption of Quantified Self-tracking Wearable Devices in the Organization Environment: An Empirical Case Study', 'total_citations': '231'}]}

exec(code, env_args)
