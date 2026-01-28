code = """import json
rows = var_call_nkBuJvtjtcHkFzfW8CCQiADU
s = sum(float(r['Total_Amount']) for r in rows)
print('__RESULT__:')
print(json.dumps({'total_funding': s}))"""

env_args = {'var_call_1mgfrIM9pU0UjpbLFEUhUinP': ['Funding'], 'var_call_4IxugqawmZ4fkQ7HkP3qZkcJ': ['civic_docs'], 'var_call_MIofTe0n8KOLSWwt31iMnvsM': 'file_storage/call_MIofTe0n8KOLSWwt31iMnvsM.json', 'var_call_twsVhJ8oKfdSjTs7R31GXFoB': [{'Project_Name': 'Bluffs Park Shade Structure'}], 'var_call_nkBuJvtjtcHkFzfW8CCQiADU': [{'Project_Name': 'Bluffs Park Shade Structure', 'Total_Amount': '21000'}]}

exec(code, env_args)
