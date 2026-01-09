code = """import json
proj=var_call_yBrGsCdEpIIOYccov4FSNtIA['projects']
keep=[p for p in proj if p in ['Bluffs Park Shade Structure','Malibu Park Drainage Improvements','Permanent Skate Park']]
print('__RESULT__:')
print(json.dumps({'projects':keep}))"""

env_args = {'var_call_You8HiLjwrNqLWkqtjg5UWXj': ['civic_docs'], 'var_call_W0WylhYl6POMeBfHyo3yNJzR': ['Funding'], 'var_call_S2omvDbArhESgAUSzOBp3R6S': 'file_storage/call_S2omvDbArhESgAUSzOBp3R6S.json', 'var_call_yBrGsCdEpIIOYccov4FSNtIA': {'projects': ['Bluffs Park Shade Structure', 'Malibu Park Drainage Improvements', 'Permanent Skate Park', 'need of replacing at Malibu Bluffs Park', 'permanent skate park located on the Crummer/Case Court parcel adjacent', 'the Malibu Park Drainage', 'to Malibu Bluffs Park. The project would include parking and additional site']}}

exec(code, env_args)
