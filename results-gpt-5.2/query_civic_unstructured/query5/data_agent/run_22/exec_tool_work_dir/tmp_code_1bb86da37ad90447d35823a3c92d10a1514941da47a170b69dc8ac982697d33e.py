code = """import json, re

def load_records(v):
    if isinstance(v, str) and v.endswith('.json'):
        with open(v, 'r', encoding='utf-8') as f:
            return json.load(f)
    return v

docs = load_records(var_call_pvJShtqIdgjHoyyWmysUP8iU)
# find docs that have a section header exactly 'Disaster Recovery Projects' line
matches=[]
for d in docs:
    t=d.get('text','')
    if 'Disaster Recovery Projects (Design)' in t or '\nDisaster Recovery Projects\n' in t:
        matches.append(d.get('filename'))
    if len(matches)>=20:
        break
print('__RESULT__:')
print(json.dumps(matches))"""

env_args = {'var_call_WforWNGckDLZNcgvbG8AKAU6': ['Funding'], 'var_call_QfAvDZ3qPtBCuw0ojwVBpNT6': ['civic_docs'], 'var_call_pvJShtqIdgjHoyyWmysUP8iU': 'file_storage/call_pvJShtqIdgjHoyyWmysUP8iU.json', 'var_call_9cXbeBzbNaOXIHYfXpfQYeX9': 'file_storage/call_9cXbeBzbNaOXIHYfXpfQYeX9.json', 'var_call_SQoTkmoTWIbOJzh1MoSBeDNQ': [], 'var_call_GJsuDFVB0bTNRESDDnW2BAs3': {'filename': 'malibucity_agenda_03222023-2060.txt', 'has_phrase': True, 'snippet': 'Disaster Recovery Projects Status\nReport\n\nRECOMMENDED ACTION: Receive and file report on the status of the City’s current and\nupcoming Capital Improvement Projects and Disaster Recovery Projects.\n\nDISCUSSION: Staff will provide a status update on the following active projects in the\nFiscal Year 2022-2023 Capital Improvement Program:\n\nCapital Improvement Projects (Design)\n\n2022 Morning View Resurfacing & Storm Drain Improvements\n\n(cid:190) Updates:\n\n(cid:131) Staff is working with the consultant '}}

exec(code, env_args)
