code = """import json
rows=var_call_ctwSeqdsAfaiJUA2buyvYxcQ
Total=sum(int(r['Total_Amount']) for r in rows)
print('__RESULT__:')
print(json.dumps({'total_funding':Total}))"""

env_args = {'var_call_You8HiLjwrNqLWkqtjg5UWXj': ['civic_docs'], 'var_call_W0WylhYl6POMeBfHyo3yNJzR': ['Funding'], 'var_call_S2omvDbArhESgAUSzOBp3R6S': 'file_storage/call_S2omvDbArhESgAUSzOBp3R6S.json', 'var_call_yBrGsCdEpIIOYccov4FSNtIA': {'projects': ['Bluffs Park Shade Structure', 'Malibu Park Drainage Improvements', 'Permanent Skate Park', 'need of replacing at Malibu Bluffs Park', 'permanent skate park located on the Crummer/Case Court parcel adjacent', 'the Malibu Park Drainage', 'to Malibu Bluffs Park. The project would include parking and additional site']}, 'var_call_Y9q5axOFSHEPPSa4jnjDooEB': {'projects': ['Bluffs Park Shade Structure', 'Malibu Park Drainage Improvements', 'Permanent Skate Park']}, 'var_call_ctwSeqdsAfaiJUA2buyvYxcQ': [{'Project_Name': 'Bluffs Park Shade Structure', 'Total_Amount': '21000'}, {'Project_Name': 'Malibu Park Drainage Improvements', 'Total_Amount': '17000'}, {'Project_Name': 'Permanent Skate Park', 'Total_Amount': '97000'}]}

exec(code, env_args)
