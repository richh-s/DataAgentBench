code = """import json
# load previous result mapping
res = json.loads(var_call_7rKgZnZ4NMOkeUn9FQHBtVC1)
# load cpc titles
cpc_rows = var_call_d8trxdAZQ0fCjmfczea8OOnz
cpc_map = {r['symbol']: r['titleFull'] for r in cpc_rows}

final = []
for assignee, codes in res.items():
    # clean assignee name: remove trailing context like 'AND HAS PUBLICATION...'
    name = assignee
    # heuristics: take portion before ' AND HAS ' or ' HOLDS ' or ' IS ' or ' WITH '
    for sep in [' AND HAS ', ' HOLDS ', ' IS HELD BY ', ' IS OWNED BY ', ' WITH PUBLICATION', ' WITH PUBLICATION NO', ' IS ']:
        if sep in name:
            name = name.split(sep)[0]
            break
    name = name.strip()
    if name.upper() in ('UNIV CALIFORNIA','UNIVERSITY OF CALIFORNIA'):
        continue
    for code in codes:
        title = cpc_map.get(code, '')
        final.append({'assignee': name, 'cpc_code': code, 'cpc_titleFull': title})

print('__RESULT__:')
print(json.dumps(final))"""

env_args = {'var_call_TbqAJZFKU2tYJY3RZLuEn1w5': 'file_storage/call_TbqAJZFKU2tYJY3RZLuEn1w5.json', 'var_call_69At5P7fh0Ou7fb0zFYvoQOh': [], 'var_call_E1sMXDo1vEG9H9KEBrJuUZmc': 'file_storage/call_E1sMXDo1vEG9H9KEBrJuUZmc.json', 'var_call_7rKgZnZ4NMOkeUn9FQHBtVC1': {'CALIFORNIA INST OF TECHN AND HAS PUBLICATION NUMBER US-2005165588-A1': ['G01V1/01'], 'THE US PATENT APPLICATION (NO. US-201715785968-A) IS HELD BY BLOOM ENERGY CORP AND HAS PUBLICATION NO. US-10615444-B2.': ['H01M4/9066', 'H01M8/2425'], 'CRYSTAL IS INC AND HAS PUBLICATION NO': ['C30B11/003', 'C30B25/10', 'C30B25/16'], 'SCHOWALTER LEO J HOLDS THE US APPLICATION (NUMBER US-2000608-A), WITH PUBLICATION NUMBER US-9437430-B2.': ['H01L21/0262']}, 'var_call_d8trxdAZQ0fCjmfczea8OOnz': [{'symbol': 'H01M4/9066', 'titleFull': 'Metals or alloys specially used in fuel cell operating at high temperature, e.g. SOFC of metal-ceramic composites or mixtures, e.g. cermets'}, {'symbol': 'H01L21/0262', 'titleFull': 'Reduction or decomposition of gaseous compounds, e.g. CVD'}, {'symbol': 'H01M8/2425', 'titleFull': 'High-temperature cells with solid electrolytes'}, {'symbol': 'C30B11/003', 'titleFull': 'Heating or cooling of the melt or the crystallised material'}, {'symbol': 'G01V1/01', 'titleFull': 'Measuring or predicting earthquakes'}, {'symbol': 'C30B25/10', 'titleFull': 'Heating of the reaction chamber or the substrate'}, {'symbol': 'C30B25/16', 'titleFull': 'Controlling or regulating'}]}

exec(code, env_args)
