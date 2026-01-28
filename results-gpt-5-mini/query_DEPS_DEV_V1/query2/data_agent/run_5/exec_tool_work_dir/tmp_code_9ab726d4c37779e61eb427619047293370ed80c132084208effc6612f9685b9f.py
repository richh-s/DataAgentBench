code = """import json
path = var_call_Jk6uPPy5uSFPQDeh4DmIsxXL
with open(path, 'r', encoding='utf-8') as f:
    rows = json.load(f)
project_names = [r['ProjectName'] for r in rows if r.get('ProjectName')]
unique = sorted(set(project_names))
print("__RESULT__:")
print(json.dumps({"total_mappings": len(rows), "unique_projects": len(unique), "sample_projects": unique[:50]}))"""

env_args = {'var_call_SPpf6OTIy2suP5I0T2HqEXjg': ['packageinfo'], 'var_call_i6hRKgFEWzpOJz5Z6LugaNNc': ['project_info', 'project_packageversion'], 'var_call_4QBHnENUNKnmttDHTGhGVb3H': 'file_storage/call_4QBHnENUNKnmttDHTGhGVb3H.json', 'var_call_0WCxbMuTxQGRvEiIxdI5oYtN': 'file_storage/call_0WCxbMuTxQGRvEiIxdI5oYtN.json', 'var_call_j0C5oPHpfXCyprf5Yum5tvPX': 'file_storage/call_j0C5oPHpfXCyprf5Yum5tvPX.json', 'var_call_Jk6uPPy5uSFPQDeh4DmIsxXL': 'file_storage/call_Jk6uPPy5uSFPQDeh4DmIsxXL.json'}

exec(code, env_args)
