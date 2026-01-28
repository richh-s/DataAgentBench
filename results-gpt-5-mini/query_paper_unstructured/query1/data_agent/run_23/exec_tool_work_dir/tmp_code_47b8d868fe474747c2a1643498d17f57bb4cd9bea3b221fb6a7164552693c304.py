code = """import json
# var_call_A7CHtCVCKI8GL03qPUpIj2kM is provided in storage and contains the path to the JSON file
fp = var_call_A7CHtCVCKI8GL03qPUpIj2kM
with open(fp, 'r', encoding='utf-8') as f:
    records = json.load(f)

# Filter records where 'food' appears in filename or text (case-insensitive)
matches = []
for r in records:
    fn = r.get('filename','')
    txt = r.get('text','')
    if 'food' in fn.lower() or 'food' in txt.lower():
        title = fn[:-4] if fn.lower().endswith('.txt') else fn
        matches.append(title)

# Deduplicate
matches = sorted(list(dict.fromkeys(matches)))
import json
print("__RESULT__:")
print(json.dumps(matches))"""

env_args = {'var_call_NyujfiVGojHluebXewte9Jj5': ['paper_docs'], 'var_call_damgR8rMM0yAZNofEpu1PxTE': ['Citations', 'sqlite_sequence'], 'var_call_A7CHtCVCKI8GL03qPUpIj2kM': 'file_storage/call_A7CHtCVCKI8GL03qPUpIj2kM.json'}

exec(code, env_args)
