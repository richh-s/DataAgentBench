code = """import json, re
# var_call_If4ehbktY9sxOq7H7rpUgWfW is a filepath containing the full JSON result
p = var_call_If4ehbktY9sxOq7H7rpUgWfW
with open(p, 'r') as f:
    data = json.load(f)
# Extract copies from repo_data_description
results = []
for rec in data:
    rid = rec.get('id')
    desc = rec.get('repo_data_description','')
    m = re.search(r"(copied|duplicated|appearing|appears|appears|appearing|repeated)\s+(\d+)\s+times", desc)
    if not m:
        # fallback: find any number followed by 'times'
        m2 = re.search(r"(\d+)\s+times", desc)
        num = int(m2.group(1)) if m2 else None
    else:
        num = int(m.group(2))
    results.append({'id': rid, 'copies': num, 'sample_repo_name': rec.get('sample_repo_name'), 'sample_path': rec.get('sample_path'), 'repo_data_description': desc})
# Filter None copies
results = [r for r in results if r['copies'] is not None]
# Find max
if not results:
    out = {'error': 'no entries with copies extracted'}
else:
    max_copies = max(r['copies'] for r in results)
    top = [r for r in results if r['copies']==max_copies]
    out = {'max_copies': max_copies, 'top_ids': top}

import json
print("__RESULT__:")
print(json.dumps(out))"""

env_args = {'var_call_lIqcEnv7ktQyMUO90EE08cGK': [], 'var_call_8bVUV3mhn3LzrWwDkYZklSDb': [], 'var_call_iWNphutg9QKUtxvyxLaaRltk': [{'cnt': '1208'}], 'var_call_YKGHnLLQjAxWeZSpcppdMzdY': [{'id': '71a17ce92451858f3eb01aa8082551e48bc5550d', 'copies': '1', 'any_repo': 'SwiftAndroid/swift', 'sample_path': 'validation-test/compiler_crashers_fixed/27485-swift-bracestmt-create.swift'}, {'id': 'cc41f22d46f21f11c9e716b30cbaeb11f4ef80fc', 'copies': '1', 'any_repo': 'practicalswift/swift-compiler-crashes', 'sample_path': 'crashes-duplicates/22401-llvm-foldingset-swift-tupletype-nodeequals.swift'}], 'var_call_If4ehbktY9sxOq7H7rpUgWfW': 'file_storage/call_If4ehbktY9sxOq7H7rpUgWfW.json', 'var_call_HbymTN5eMGYcT45CdgCsPtFS': []}

exec(code, env_args)
