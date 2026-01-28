code = """import json, re
path = var_call_mB4p9sAq4lpFrwci3VV5sX6H
with open(path, 'r', encoding='utf-8') as f:
    records = json.load(f)

debug = []
for i, r in enumerate(records[:10]):
    filename = r.get('filename','')
    text = r.get('text','')
    emp = bool(re.search(r'\bempirical\b', text, re.IGNORECASE))
    # search for 2017-2024
    m = re.search(r'20(1[7-9]|2[0-4])', text)
    year = int(m.group(0)) if m else None
    preview = text[:200]
    debug.append({'filename': filename, 'empirical_found': emp, 'year_found': year, 'preview': preview})

print('__RESULT__:')
print(json.dumps(debug))"""

env_args = {'var_call_a50SROerJh7cg2CaFPe5HUSq': ['paper_docs'], 'var_call_8DV18aV221C1QGLy9PTJoWRD': ['Citations', 'sqlite_sequence'], 'var_call_qdPezJyiGQ882BWNhhrL3cAR': 'file_storage/call_qdPezJyiGQ882BWNhhrL3cAR.json', 'var_call_bMZXN2lTUc5GRRtVj2EHltEd': [], 'var_call_mB4p9sAq4lpFrwci3VV5sX6H': 'file_storage/call_mB4p9sAq4lpFrwci3VV5sX6H.json', 'var_call_HGxkZwdlqYp7msjXWFNaJEEP': []}

exec(code, env_args)
