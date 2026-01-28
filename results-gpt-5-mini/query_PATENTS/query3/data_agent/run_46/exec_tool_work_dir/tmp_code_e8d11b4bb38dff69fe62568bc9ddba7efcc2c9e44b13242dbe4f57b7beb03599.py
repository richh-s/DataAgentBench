code = """import json

# Load previous processed mapping
var1 = json.loads(open(var_call_KY3zr1EsjUrymHTCg2iHf1ya, 'r', encoding='utf-8').read())
assignee_to_codes = var1['assignee_to_codes']

# Load cpc definitions
cpc_defs = json.load(open(var_call_y5KrkzNLsouHXbg6tlPGtOZM, 'r', encoding='utf-8'))
symbol_to_title = {row['symbol']: row['titleFull'] for row in cpc_defs}

# Build final mapping: each assignee to list of titles for their primary CPC codes
result = []
for assignee, codes in assignee_to_codes.items():
    titles = []
    for c in codes:
        title = symbol_to_title.get(c)
        if not title:
            title = None
        titles.append({'code': c, 'titleFull': title})
    result.append({'assignee': assignee, 'cpc_primary': titles})

print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_call_HmKEPxHFYVCDxkTNVoAewSKJ': 'file_storage/call_HmKEPxHFYVCDxkTNVoAewSKJ.json', 'var_call_KY3zr1EsjUrymHTCg2iHf1ya': {'assignee_to_codes': {'UNIV': ['A61K38/465', 'C12N15/102', 'C12N15/111', 'C12N15/907']}, 'codes': ['A61K38/465', 'C12N15/102', 'C12N15/111', 'C12N15/907']}, 'var_call_y5KrkzNLsouHXbg6tlPGtOZM': [{'symbol': 'A61K38/465', 'titleFull': 'Hydrolases (3) acting on ester bonds (3.1), e.g. lipases, ribonucleases'}, {'symbol': 'C12N15/907', 'titleFull': 'Stable introduction of foreign DNA into chromosome using homologous recombination in mammalian cells'}, {'symbol': 'C12N15/102', 'titleFull': 'Mutagenizing nucleic acids'}, {'symbol': 'C12N15/111', 'titleFull': 'General methods applicable to biologically active non-coding nucleic acids'}]}

exec(code, env_args)
