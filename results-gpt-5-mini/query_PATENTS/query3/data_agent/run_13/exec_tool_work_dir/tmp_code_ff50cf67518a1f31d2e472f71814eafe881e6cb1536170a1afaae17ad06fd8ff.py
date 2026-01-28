code = """import json

cpc_defs = json.loads(open(var_call_jdqbAsxXwsQrGXO3rjfwgMpn).read())
parse_res = json.loads(open(var_call_5paADsIoJRDGKWDuXLRFjb7W).read())
ass_to_codes = parse_res['assignee_to_codes']

# build mapping code->title
code_title = {r['symbol']: r['titleFull'] for r in cpc_defs}

final = []
for assignee, codes in ass_to_codes.items():
    for code in codes:
        title = code_title.get(code, None)
        final.append({'assignee': assignee, 'cpc': code, 'titleFull': title})

print('__RESULT__:')
print(json.dumps(final))"""

env_args = {'var_call_RQE78oOVxD82z54dvi4GCBdC': 'file_storage/call_RQE78oOVxD82z54dvi4GCBdC.json', 'var_call_WQS6C0FIkO1PLo7yWplRnL1r': 'file_storage/call_WQS6C0FIkO1PLo7yWplRnL1r.json', 'var_call_e9K9FC2cSeE9c7PgDhih3Vwy': 'file_storage/call_e9K9FC2cSeE9c7PgDhih3Vwy.json', 'var_call_0iVQSPpbanCFSC8TDBFm8T8y': 'file_storage/call_0iVQSPpbanCFSC8TDBFm8T8y.json', 'var_call_5paADsIoJRDGKWDuXLRFjb7W': {'assignee_to_codes': {'THE US PATENT FILING (APPLICATION NUMBER US-4007205-A)': ['G01V1/01'], 'THE US PATENT APPLICATION (NO. US-201715785968-A) IS': ['H01M4/9066', 'H01M8/2425'], 'THE US APPLICATION (ID US-201414520615-A)': ['C30B11/003', 'C30B25/10', 'C30B25/16'], 'SCHOWALTER LEO J': ['H01L21/0262']}, 'codes': ['C30B11/003', 'C30B25/10', 'C30B25/16', 'G01V1/01', 'H01L21/0262', 'H01M4/9066', 'H01M8/2425']}, 'var_call_jdqbAsxXwsQrGXO3rjfwgMpn': [{'symbol': 'H01M4/9066', 'titleFull': 'Metals or alloys specially used in fuel cell operating at high temperature, e.g. SOFC of metal-ceramic composites or mixtures, e.g. cermets'}, {'symbol': 'H01L21/0262', 'titleFull': 'Reduction or decomposition of gaseous compounds, e.g. CVD'}, {'symbol': 'C30B25/10', 'titleFull': 'Heating of the reaction chamber or the substrate'}, {'symbol': 'C30B25/16', 'titleFull': 'Controlling or regulating'}, {'symbol': 'G01V1/01', 'titleFull': 'Measuring or predicting earthquakes'}, {'symbol': 'C30B11/003', 'titleFull': 'Heating or cooling of the melt or the crystallised material'}, {'symbol': 'H01M8/2425', 'titleFull': 'High-temperature cells with solid electrolytes'}]}

exec(code, env_args)
