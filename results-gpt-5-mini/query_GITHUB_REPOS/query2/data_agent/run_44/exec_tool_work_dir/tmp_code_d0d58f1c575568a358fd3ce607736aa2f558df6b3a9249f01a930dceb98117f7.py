code = """import json, re
# var_call_MgZSuSkC8mbtVOtyblGuwShM is a path to the JSON file with contents query results
p = var_call_MgZSuSkC8mbtVOtyblGuwShM
with open(p, 'r', encoding='utf-8') as f:
    data = json.load(f)

# Parse repo_data_description to extract copies count
results = {}
for entry in data:
    id_ = entry.get('id')
    desc = entry.get('repo_data_description') or ''
    # find patterns like 'copied 12 times', 'duplicated 8 times', 'appearing 8 times', 'repeated 23 times', 'seen 15 times'
    m = re.search(r'(\d+)\s+times', desc)
    copies = int(m.group(1)) if m else None
    if copies is None:
        m2 = re.search(r'repeated\s+(\d+)', desc)
        if m2:
            copies = int(m2.group(1))
    if copies is None:
        m3 = re.search(r'copied\s+(\d+)', desc)
        if m3:
            copies = int(m3.group(1))
    if copies is None:
        # fallback: any number in description
        m4 = re.search(r'(\d+)', desc)
        if m4:
            copies = int(m4.group(1))
    if copies is None:
        continue
    # store max copies per id
    if id_ not in results or copies > results[id_]['copies']:
        results[id_] = {
            'id': id_,
            'copies': copies,
            'sample_repo_name': entry.get('sample_repo_name'),
            'sample_path': entry.get('sample_path'),
            'repo_data_description': desc
        }

# find id with max copies
max_entry = max(results.values(), key=lambda x: x['copies'])
out = max_entry
import json
print("__RESULT__:")
print(json.dumps(out))"""

env_args = {'var_call_JAetpcNkDsF8xGU27jjUD1jc': 'file_storage/call_JAetpcNkDsF8xGU27jjUD1jc.json', 'var_call_PE0L8PjXt835cxTEIFwb6UAq': [{'id': '71a17ce92451858f3eb01aa8082551e48bc5550d', 'copies': '1', 'sample_repo_name': 'SwiftAndroid/swift', 'sample_path': 'validation-test/compiler_crashers_fixed/27485-swift-bracestmt-create.swift', 'repo_data_description': 'It is a non-binary file of 470 bytes, repeated 23 times in the dataset under mode 33188.'}, {'id': 'cc41f22d46f21f11c9e716b30cbaeb11f4ef80fc', 'copies': '1', 'sample_repo_name': 'practicalswift/swift-compiler-crashes', 'sample_path': 'crashes-duplicates/22401-llvm-foldingset-swift-tupletype-nodeequals.swift', 'repo_data_description': 'This file has a size of 273 bytes, is non-binary, and appears 15 times with sample mode 33188.'}], 'var_call_gA0u8kgyhT5jqF6JzH9W6ZCm': [{'id': '71a17ce92451858f3eb01aa8082551e48bc5550d', 'copies': '1'}, {'id': 'cc41f22d46f21f11c9e716b30cbaeb11f4ef80fc', 'copies': '1'}], 'var_call_QwHzqfw14yd1bVFO3TffKJSe': [{'id': '71a17ce92451858f3eb01aa8082551e48bc5550d', 'copies': '1', 'sample_path': 'validation-test/compiler_crashers_fixed/27485-swift-bracestmt-create.swift', 'repo_data_description': 'It is a non-binary file of 470 bytes, repeated 23 times in the dataset under mode 33188.', 'repo_list': 'SwiftAndroid/swift'}, {'id': 'cc41f22d46f21f11c9e716b30cbaeb11f4ef80fc', 'copies': '1', 'sample_path': 'crashes-duplicates/22401-llvm-foldingset-swift-tupletype-nodeequals.swift', 'repo_data_description': 'This file has a size of 273 bytes, is non-binary, and appears 15 times with sample mode 33188.', 'repo_list': 'practicalswift/swift-compiler-crashes'}], 'var_call_MgZSuSkC8mbtVOtyblGuwShM': 'file_storage/call_MgZSuSkC8mbtVOtyblGuwShM.json'}

exec(code, env_args)
