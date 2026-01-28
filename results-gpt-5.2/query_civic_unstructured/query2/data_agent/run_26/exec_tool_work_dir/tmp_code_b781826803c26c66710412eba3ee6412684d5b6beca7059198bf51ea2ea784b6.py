code = """import json, re

def load_tool_result(x):
    if isinstance(x, str) and x.endswith('.json'):
        with open(x,'r',encoding='utf-8') as f:
            return json.load(f)
    return x

docs=load_tool_result(var_call_UCJq4gDEzfiZVQPH44VuWTPI)
text0=docs[0]['text']
lines=[ln.strip() for ln in text0.splitlines()]
ln=lines[314]
print('__RESULT__:')
print(json.dumps({'line':ln,'match_construction_completed':bool(re.search(r'construction was completed', ln, re.I)),'has_2022':bool(re.search(r'2022', ln))}))"""

env_args = {'var_call_hXf50YBfCrrwm4VISQMICNsZ': ['Funding'], 'var_call_SxtnxuThncsmTRlN1JT8h0Dx': ['civic_docs'], 'var_call_UCJq4gDEzfiZVQPH44VuWTPI': 'file_storage/call_UCJq4gDEzfiZVQPH44VuWTPI.json', 'var_call_QZtCO6cQtvO8QTD4wdb2dF3L': 'file_storage/call_QZtCO6cQtvO8QTD4wdb2dF3L.json', 'var_call_daScurDCWm3lCH5Z7VUW1soU': {'projects_completed_2022_park': [], 'matched_projects': [], 'total_funding': 0}, 'var_call_jx825yvGj5t1RO9j1r5BxfCm': [{'i': 137, 'line': '(cid:131) Plans and specifications have been completed', 'context': ['(cid:190) Updates:', '', '(cid:131) Plans and specifications have been completed', '(cid:131) Awaiting final FEMA/CalOES approval for scope modification', '']}, {'i': 149, 'line': '(cid:131) Field data collection has been completed and storm drain inventory has', 'context': ['(cid:190) Updates:', '', '(cid:131) Field data collection has been completed and storm drain inventory has', '', 'been finalized and incorporated into GIS.']}, {'i': 314, 'line': '(cid:190) Updates: Construction was completed November 2022. Notice of completion', 'context': ['Bluffs Park Shade Structure', '', '(cid:190) Updates: Construction was completed November 2022. Notice of completion', '', 'filed January 2023']}, {'i': 335, 'line': '(cid:131) Construction was completed, January 2023', 'context': ['(cid:190) Updates:', '', '(cid:131) Construction was completed, January 2023', '(cid:131) Scheduled for Council acceptance on April 24, 2023', '']}, {'i': 342, 'line': '(cid:131) Construction was completed, November 2022', 'context': ['(cid:190) Updates:', '', '(cid:131) Construction was completed, November 2022', '(cid:131) Notice of completion filed January 2023', '']}, {'i': 348, 'line': '(cid:131) Construction was completed, November 2022', 'context': ['(cid:190) Updates:', '', '(cid:131) Construction was completed, November 2022', '(cid:131) Notice of completion filed January 2023', '']}], 'var_call_SW73zavkufIUTTcjJF3JGvZs': {'projects': [], 'total_funding': 0, 'matched': []}, 'var_call_EzTxSsaG4wvDCAsUvus10f6V': {'name': 'Bluffs Park Shade Structure', 'window': '(cid:190) Project Schedule:  (cid:131) Begin construction: Summer 2023 (cid:131) Complete Construction: Summer 2023  Bluffs Park Shade Structure  (cid:190) Updates: Construction was completed November 2022. Notice of completion  filed January 2023  Page 4 of 6'}}

exec(code, env_args)
