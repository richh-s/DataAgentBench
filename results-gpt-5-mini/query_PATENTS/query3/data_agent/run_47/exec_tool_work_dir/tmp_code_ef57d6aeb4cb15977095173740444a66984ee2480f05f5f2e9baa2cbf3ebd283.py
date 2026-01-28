code = """import json
# load assignee to cpcs result
res = var_call_Eti6l8wuH8QAkIDmroemnvOP
# load cpc definitions
cpc_defs = var_call_gtlVniwUCGRoqqHlgPWJjwAB
# build mapping
assignee_map = res['assignee_to_cpcs']
symbol_to_title = {r['symbol']: r['titleFull'] for r in cpc_defs}
output = []
for assignee, codes in assignee_map.items():
    for code in codes:
        title = symbol_to_title.get(code, None)
        if title:
            output.append({'assignee': assignee, 'cpc': code, 'titleFull': title})

print('__RESULT__:')
print(json.dumps(output))"""

env_args = {'var_call_gDrSP1Sva9xFHcnb3CZWe5Hy': 'file_storage/call_gDrSP1Sva9xFHcnb3CZWe5Hy.json', 'var_call_eWOblcZdr0yKyeHcZjYuDGdv': 'file_storage/call_eWOblcZdr0yKyeHcZjYuDGdv.json', 'var_call_oKnfuZPM2rRjOch4s2WsCqEb': 'file_storage/call_oKnfuZPM2rRjOch4s2WsCqEb.json', 'var_call_Eti6l8wuH8QAkIDmroemnvOP': {'assignee_to_cpcs': {'CALIFORNIA INST OF TECHN': ['G01V1/01'], 'CRYSTAL IS INC': ['C30B11/003'], 'SCHOWALTER LEO J': ['H01L21/0262']}, 'unique_cpcs': ['C30B11/003', 'G01V1/01', 'H01L21/0262'], 'matched_count': 3}, 'var_call_gtlVniwUCGRoqqHlgPWJjwAB': [{'symbol': 'H01L21/0262', 'titleFull': 'Reduction or decomposition of gaseous compounds, e.g. CVD'}, {'symbol': 'G01V1/01', 'titleFull': 'Measuring or predicting earthquakes'}, {'symbol': 'C30B11/003', 'titleFull': 'Heating or cooling of the melt or the crystallised material'}]}

exec(code, env_args)
