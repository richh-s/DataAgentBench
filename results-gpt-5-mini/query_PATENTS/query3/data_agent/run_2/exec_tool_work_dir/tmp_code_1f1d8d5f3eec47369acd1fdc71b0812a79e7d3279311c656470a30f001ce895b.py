code = """import json
# load previous python result
path = var_call_nc23yghwdUjKoox7Sc1dMC7d
with open(path, 'r', encoding='utf-8') as f:
    pairs = json.load(f)

# load cpc definitions
cpc_defs = var_call_lhKmMBTia4VPyM1dQVnsIjqi

def lookup(code):
    for r in cpc_defs:
        if r['symbol']==code:
            return r['titleFull']
    return None

output = []
for p in pairs:
    title = lookup(p['cpc_code'])
    output.append({'assignee': p['assignee'], 'cpc_titleFull': title or ''})

import json as _json
print('__RESULT__:')
print(_json.dumps(output))"""

env_args = {'var_call_5Sz553TW5TdZm9NFNJo3EnYY': 'file_storage/call_5Sz553TW5TdZm9NFNJo3EnYY.json', 'var_call_nc23yghwdUjKoox7Sc1dMC7d': [{'assignee': 'CALIFORNIA INST OF TECHN AND HAS PUBLICATION NUMBER US-2005165588-A1', 'cpc_code': 'G01V1/01'}, {'assignee': 'SCHOWALTER LEO J', 'cpc_code': 'H01L21/0262'}, {'assignee': 'THE US APPLICATION (ID US-201414520615-A) IS OWNED BY CRYSTAL IS INC AND HAS PUBLICATION NO. US-9447521-B2.', 'cpc_code': 'C30B11/003'}], 'var_call_lhKmMBTia4VPyM1dQVnsIjqi': [{'symbol': 'G01V1/01', 'titleFull': 'Measuring or predicting earthquakes'}, {'symbol': 'H01L21/0262', 'titleFull': 'Reduction or decomposition of gaseous compounds, e.g. CVD'}, {'symbol': 'C30B11/003', 'titleFull': 'Heating or cooling of the melt or the crystallised material'}]}

exec(code, env_args)
