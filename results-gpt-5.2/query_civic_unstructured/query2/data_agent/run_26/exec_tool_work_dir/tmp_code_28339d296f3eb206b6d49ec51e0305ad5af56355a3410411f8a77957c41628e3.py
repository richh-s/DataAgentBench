code = """import json, re

def load_tool_result(x):
    if isinstance(x, str) and x.endswith('.json'):
        with open(x,'r',encoding='utf-8') as f:
            return json.load(f)
    return x

docs = load_tool_result(var_call_UCJq4gDEzfiZVQPH44VuWTPI)

text0 = docs[0]['text']
lines = [ln.strip() for ln in text0.splitlines()]
# find lines with 'completed' and show surrounding
hits=[]
for i,ln in enumerate(lines):
    if re.search(r'completed', ln, re.I):
        hits.append({'i':i,'line':ln,'context':lines[max(0,i-2):i+3]})
print('__RESULT__:')
print(json.dumps(hits[:20]))"""

env_args = {'var_call_hXf50YBfCrrwm4VISQMICNsZ': ['Funding'], 'var_call_SxtnxuThncsmTRlN1JT8h0Dx': ['civic_docs'], 'var_call_UCJq4gDEzfiZVQPH44VuWTPI': 'file_storage/call_UCJq4gDEzfiZVQPH44VuWTPI.json', 'var_call_QZtCO6cQtvO8QTD4wdb2dF3L': 'file_storage/call_QZtCO6cQtvO8QTD4wdb2dF3L.json', 'var_call_daScurDCWm3lCH5Z7VUW1soU': {'projects_completed_2022_park': [], 'matched_projects': [], 'total_funding': 0}}

exec(code, env_args)
