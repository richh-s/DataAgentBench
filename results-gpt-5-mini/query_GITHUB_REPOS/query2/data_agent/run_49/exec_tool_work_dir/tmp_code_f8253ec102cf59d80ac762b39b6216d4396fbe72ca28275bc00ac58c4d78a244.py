code = """import json, re

# Load the large contents result from artifacts query
path = var_call_3UelDehUAelNvswApPQl0kLP
with open(path, 'r') as f:
    data = json.load(f)

results = []

patterns = [
    re.compile(r"appears\s+(\d+)\s+times"),
    re.compile(r"appearing\s+(\d+)\s+times"),
    re.compile(r"copied\s+(\d+)\s+times"),
    re.compile(r"repeated\s+(\d+)\s+times"),
    re.compile(r"seen\s+(\d+)\s+times"),
    re.compile(r"appear[s|ing]*\s+(\d+)"),
    re.compile(r"(\d+)\s+times"),
    re.compile(r"(\d+)\s+time")
]

for rec in data:
    path_lower = rec.get('sample_path','').lower()
    desc = rec.get('repo_data_description','').lower()
    if not path_lower.endswith('.swift'):
        continue
    if 'non-binary' not in desc:
        continue
    copies = None
    for p in patterns:
        m = p.search(desc)
        if m:
            # find first non-None group
            for g in m.groups():
                if g:
                    copies = int(g)
                    break
        if copies is not None:
            break
    if copies is None:
        # fallback: find all integers and pick one that seems like copies (<=1000 and <= file size maybe)
        nums = [int(x) for x in re.findall(r"(\d+)", desc)]
        if nums:
            # choose the smallest number greater than 1 (since copies>1 usually) or the last one
            cand = [n for n in nums if n>1]
            copies = cand[0] if cand else nums[-1]
    if copies is None:
        continue
    results.append({
        'id': rec.get('id'),
        'copies': copies,
        'sample_repo_name': rec.get('sample_repo_name'),
        'sample_path': rec.get('sample_path')
    })

# Deduplicate by id (keep first occurrence)
seen = set()
uniq = []
for r in results:
    if r['id'] in seen:
        continue
    seen.add(r['id'])
    uniq.append(r)

# Sort by copies desc
uniq_sorted = sorted(uniq, key=lambda x: x['copies'], reverse=True)

# Keep top 100
top = uniq_sorted[:100]

import json
print("__RESULT__:")
print(json.dumps(top))"""

env_args = {'var_call_3UelDehUAelNvswApPQl0kLP': 'file_storage/call_3UelDehUAelNvswApPQl0kLP.json', 'var_call_updXhoAa20BHfBBtltrMhyhy': [{'id': 'cc41f22d46f21f11c9e716b30cbaeb11f4ef80fc', 'copies': '1', 'sample_repo_name': 'practicalswift/swift-compiler-crashes', 'sample_path': 'crashes-duplicates/22401-llvm-foldingset-swift-tupletype-nodeequals.swift'}, {'id': '71a17ce92451858f3eb01aa8082551e48bc5550d', 'copies': '1', 'sample_repo_name': 'SwiftAndroid/swift', 'sample_path': 'validation-test/compiler_crashers_fixed/27485-swift-bracestmt-create.swift'}], 'var_call_fw6ZNnXxYw1PusmoMww4IpWl': [{'id': 'cc41f22d46f21f11c9e716b30cbaeb11f4ef80fc', 'copies': '1', 'sample_repo_name': 'practicalswift/swift-compiler-crashes', 'sample_path': 'crashes-duplicates/22401-llvm-foldingset-swift-tupletype-nodeequals.swift', 'repo_data_description': 'This file has a size of 273 bytes, is non-binary, and appears 15 times with sample mode 33188.'}, {'id': '71a17ce92451858f3eb01aa8082551e48bc5550d', 'copies': '1', 'sample_repo_name': 'SwiftAndroid/swift', 'sample_path': 'validation-test/compiler_crashers_fixed/27485-swift-bracestmt-create.swift', 'repo_data_description': 'It is a non-binary file of 470 bytes, repeated 23 times in the dataset under mode 33188.'}]}

exec(code, env_args)
