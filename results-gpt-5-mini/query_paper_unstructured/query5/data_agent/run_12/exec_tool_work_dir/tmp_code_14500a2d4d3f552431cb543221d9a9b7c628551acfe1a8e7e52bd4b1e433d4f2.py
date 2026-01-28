code = """import json, re
path_papers = var_call_kcMrujPTFLPyK4epIvakeN2T
with open(path_papers, 'r', encoding='utf-8') as f:
    papers = json.load(f)

patterns = [r"CHI", r"SIGCHI", r"Human Factors in Computing Systems", r"Proceedings of the.*CHI", r"ACM CHI", r"CHI Conference"]

matches = []
for doc in papers:
    filename = doc.get('filename','')
    title = filename[:-4] if filename.lower().endswith('.txt') else filename
    text = doc.get('text','')
    found = []
    for p in patterns:
        if re.search(p, text, flags=re.IGNORECASE):
            found.append(p)
    if found:
        matches.append({'title': title, 'matches': found[:5]})

# show counts and first 20 matches
out = {'num_matching_docs': len(matches), 'sample_matches': matches[:20]}
print("__RESULT__:")
print(json.dumps(out))"""

env_args = {'var_call_gFwFvyf3mPGfKL0vFQmrcJZX': 'file_storage/call_gFwFvyf3mPGfKL0vFQmrcJZX.json', 'var_call_kcMrujPTFLPyK4epIvakeN2T': 'file_storage/call_kcMrujPTFLPyK4epIvakeN2T.json', 'var_call_vp4xBBEe2kesakgiwy8DfF37': {'papers': [], 'total_citations': 0, 'num_papers': 0}}

exec(code, env_args)
