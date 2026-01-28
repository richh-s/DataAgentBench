code = """import json
p = var_call_BQYWUevYFUky85OvPZGvHJRC
with open(p, 'r', encoding='utf-8') as f:
    data = json.load(f)

# we will load into dict mapping title->total_citations (int)
cit = {}
for r in data:
    t = r.get('title')
    v = r.get('total_citations')
    try:
        cit[t] = int(v)
    except:
        try:
            cit[t] = int(float(v))
        except:
            cit[t] = None

print('__RESULT__:')
print(json.dumps(cit))"""

env_args = {'var_call_UeAwGvyL4BRgCq5TsBDxPehn': 'file_storage/call_UeAwGvyL4BRgCq5TsBDxPehn.json', 'var_call_dtnwJdFJIovt8fdBMoCOC9Z5': [], 'var_call_40G8suqyORvGvH2VqbbBEhkO': 'file_storage/call_40G8suqyORvGvH2VqbbBEhkO.json', 'var_call_jokn9ejj3SySQh0YVLoqQrID': [], 'var_call_GCWkR1OFB2vPEOsJxlXZD4wx': [], 'var_call_On7oCux1AjpCpaT2jkfydY5j': 'file_storage/call_On7oCux1AjpCpaT2jkfydY5j.json', 'var_call_z3BmMZCV2zNwBJd3OBhZLJql': ['paper_docs'], 'var_call_9PGGGyYeJkpVGL7Mt4nLr2dm': ['Citations', 'sqlite_sequence'], 'var_call_BQYWUevYFUky85OvPZGvHJRC': 'file_storage/call_BQYWUevYFUky85OvPZGvHJRC.json'}

exec(code, env_args)
