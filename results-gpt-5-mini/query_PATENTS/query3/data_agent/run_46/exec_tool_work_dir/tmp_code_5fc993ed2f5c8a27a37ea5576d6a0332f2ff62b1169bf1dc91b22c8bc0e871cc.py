code = """import json

# Access stored variables from previous tool calls
v_mapping = var_call_KY3zr1EsjUrymHTCg2iHf1ya
v_cpcdefs = var_call_y5KrkzNLsouHXbg6tlPGtOZM

# v_mapping may be a JSON string or a Python dict
if isinstance(v_mapping, str):
    mapping = json.loads(v_mapping)
else:
    mapping = v_mapping

# v_cpcdefs may be a JSON string or Python list
if isinstance(v_cpcdefs, str):
    cpc_defs = json.loads(v_cpcdefs)
else:
    cpc_defs = v_cpcdefs

symbol_to_title = {row['symbol']: row.get('titleFull') for row in cpc_defs}

result = []
for assignee, codes in mapping.get('assignee_to_codes', {}).items():
    titles = []
    for c in codes:
        titles.append({'code': c, 'titleFull': symbol_to_title.get(c)})
    result.append({'assignee': assignee, 'cpc_primary': titles})

print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_call_HmKEPxHFYVCDxkTNVoAewSKJ': 'file_storage/call_HmKEPxHFYVCDxkTNVoAewSKJ.json', 'var_call_KY3zr1EsjUrymHTCg2iHf1ya': {'assignee_to_codes': {'UNIV': ['A61K38/465', 'C12N15/102', 'C12N15/111', 'C12N15/907']}, 'codes': ['A61K38/465', 'C12N15/102', 'C12N15/111', 'C12N15/907']}, 'var_call_y5KrkzNLsouHXbg6tlPGtOZM': [{'symbol': 'A61K38/465', 'titleFull': 'Hydrolases (3) acting on ester bonds (3.1), e.g. lipases, ribonucleases'}, {'symbol': 'C12N15/907', 'titleFull': 'Stable introduction of foreign DNA into chromosome using homologous recombination in mammalian cells'}, {'symbol': 'C12N15/102', 'titleFull': 'Mutagenizing nucleic acids'}, {'symbol': 'C12N15/111', 'titleFull': 'General methods applicable to biologically active non-coding nucleic acids'}]}

exec(code, env_args)
