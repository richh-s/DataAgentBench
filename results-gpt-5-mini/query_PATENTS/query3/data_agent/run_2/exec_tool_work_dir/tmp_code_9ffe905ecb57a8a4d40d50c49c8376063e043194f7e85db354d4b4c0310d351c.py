code = """import json
import re

pairs = var_call_nc23yghwdUjKoox7Sc1dMC7d
cpc_defs = var_call_lhKmMBTia4VPyM1dQVnsIjqi

# helper to lookup title
def lookup(code):
    for r in cpc_defs:
        if r['symbol']==code:
            return r['titleFull']
    return ''

# clean assignee
def clean_assignee(s):
    s = s.strip()
    up = s.upper()
    if 'OWNED BY' in up:
        idx = up.find('OWNED BY') + len('OWNED BY')
        rest = s[idx:].strip()
        rest_up = rest.upper()
        for sep in [' AND HAS', ' AND HAVE', ' AND HAS PUBLICATION', ' AND ']:
            if sep in rest_up:
                rest = rest[:rest_up.find(sep)].strip()
                break
        return rest
    # remove trailing 'AND HAS PUBLICATION' parts
    try:
        s = re.split(r'\bAND HAS PUBLICATION\b', s, flags=re.I)[0].strip()
    except Exception:
        pass
    s = re.sub(r'\bHAS PUBLICATION NUMBER\b.*', '', s, flags=re.I).strip()
    s = re.sub(r'\bHAS PUBLICATION NO\.?\b.*', '', s, flags=re.I).strip()
    if up.startswith('THE US APPLICATION') and 'OWNED BY' in up:
        idx = up.find('OWNED BY') + len('OWNED BY')
        rest = s[idx:].strip()
        rest = re.split(r'\bAND\b', rest, flags=re.I)[0].strip()
        return rest
    return s

output_lines = []
for p in pairs:
    asg = p['assignee']
    code = p['cpc_code']
    title = lookup(code)
    cleaned = clean_assignee(asg)
    output_lines.append(f"{cleaned} — {title}")

final_text = '\n'.join(output_lines)

import json as _json
print('__RESULT__:')
print(_json.dumps(final_text))"""

env_args = {'var_call_5Sz553TW5TdZm9NFNJo3EnYY': 'file_storage/call_5Sz553TW5TdZm9NFNJo3EnYY.json', 'var_call_nc23yghwdUjKoox7Sc1dMC7d': [{'assignee': 'CALIFORNIA INST OF TECHN AND HAS PUBLICATION NUMBER US-2005165588-A1', 'cpc_code': 'G01V1/01'}, {'assignee': 'SCHOWALTER LEO J', 'cpc_code': 'H01L21/0262'}, {'assignee': 'THE US APPLICATION (ID US-201414520615-A) IS OWNED BY CRYSTAL IS INC AND HAS PUBLICATION NO. US-9447521-B2.', 'cpc_code': 'C30B11/003'}], 'var_call_lhKmMBTia4VPyM1dQVnsIjqi': [{'symbol': 'G01V1/01', 'titleFull': 'Measuring or predicting earthquakes'}, {'symbol': 'H01L21/0262', 'titleFull': 'Reduction or decomposition of gaseous compounds, e.g. CVD'}, {'symbol': 'C30B11/003', 'titleFull': 'Heating or cooling of the melt or the crystallised material'}]}

exec(code, env_args)
