code = """import json

pairs = var_call_nc23yghwdUjKoox7Sc1dMC7d
cpc_defs = var_call_lhKmMBTia4VPyM1dQVnsIjqi

# lookup title
def lookup(code):
    for r in cpc_defs:
        if r.get('symbol') == code:
            return r.get('titleFull','')
    return ''

# clean assignee string
def clean_assignee(s):
    if not s:
        return s
    s = s.strip()
    up = s.upper()
    if 'OWNED BY' in up:
        idx = up.find('OWNED BY') + len('OWNED BY')
        rest = s[idx:].strip()
        # truncate at common separators
        for sep in [' AND HAS', ' AND HAVE', ' AND HAS PUBLICATION', ' AND HAS PUBLICATION NUMBER', ' AND HAS PUBLICATION NO', ' AND HAS PUBLICATION NO.',' AND HAS', ' AND ']:
            pos = rest.upper().find(sep)
            if pos != -1:
                rest = rest[:pos].strip()
        return rest
    # remove 'HAS PUBLICATION' clauses
    up = s.upper()
    if 'HAS PUBLICATION' in up:
        s = s[:up.find('HAS PUBLICATION')].strip()
    if 'HAS PUBLICATION NUMBER' in up:
        s = s[:up.find('HAS PUBLICATION NUMBER')].strip()
    if 'HAS PUBLICATION NO' in up:
        s = s[:up.find('HAS PUBLICATION NO')].strip()
    # remove leading descriptors like 'THE US APPLICATION (ID ...) IS OWNED BY X'
    if up.startswith('THE US APPLICATION') and 'OWNED BY' in up:
        idx = up.find('OWNED BY') + len('OWNED BY')
        rest = s[idx:].strip()
        # cut off trailing bits after first 'AND'
        if ' AND ' in rest.upper():
            rest = rest[:rest.upper().find(' AND ')].strip()
        return rest
    return s

output = []
for p in pairs:
    asg = p.get('assignee','')
    code = p.get('cpc_code','')
    title = lookup(code)
    cleaned = clean_assignee(asg)
    output.append({'assignee': cleaned, 'cpc_titleFull': title})

print('__RESULT__:')
print(json.dumps(output))"""

env_args = {'var_call_5Sz553TW5TdZm9NFNJo3EnYY': 'file_storage/call_5Sz553TW5TdZm9NFNJo3EnYY.json', 'var_call_nc23yghwdUjKoox7Sc1dMC7d': [{'assignee': 'CALIFORNIA INST OF TECHN AND HAS PUBLICATION NUMBER US-2005165588-A1', 'cpc_code': 'G01V1/01'}, {'assignee': 'SCHOWALTER LEO J', 'cpc_code': 'H01L21/0262'}, {'assignee': 'THE US APPLICATION (ID US-201414520615-A) IS OWNED BY CRYSTAL IS INC AND HAS PUBLICATION NO. US-9447521-B2.', 'cpc_code': 'C30B11/003'}], 'var_call_lhKmMBTia4VPyM1dQVnsIjqi': [{'symbol': 'G01V1/01', 'titleFull': 'Measuring or predicting earthquakes'}, {'symbol': 'H01L21/0262', 'titleFull': 'Reduction or decomposition of gaseous compounds, e.g. CVD'}, {'symbol': 'C30B11/003', 'titleFull': 'Heating or cooling of the melt or the crystallised material'}]}

exec(code, env_args)
