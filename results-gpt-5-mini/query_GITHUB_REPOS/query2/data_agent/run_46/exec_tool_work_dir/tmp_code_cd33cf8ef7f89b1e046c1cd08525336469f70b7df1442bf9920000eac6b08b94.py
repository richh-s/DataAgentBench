code = """import json, re, os
# var_call_xLwnIE9BbSQYIbguSImjpHTo contains the large result file path or list
data_var = var_call_xLwnIE9BbSQYIbguSImjpHTo
if isinstance(data_var, str) and os.path.exists(data_var):
    with open(data_var, 'r', encoding='utf-8') as f:
        records = json.load(f)
else:
    records = data_var

# Filter for .swift files and non-binary mentioned (should already be filtered)
swift_records = [r for r in records if 'sample_path' in r and r['sample_path'] and r['sample_path'].lower().endswith('.swift')]

# Function to extract copies count from repo_data_description
def extract_count(desc):
    if not desc:
        return 0
    m = re.search(r'(?:duplicated|repeated|appears|appearing|appears|copied|seen|seen|repeated)\s+(\d+)\s+times', desc, re.IGNORECASE)
    if not m:
        # fallback: find first number followed by 'times' or 'time'
        m = re.search(r'(\d+)\s+times?', desc, re.IGNORECASE)
    if m:
        return int(m.group(1))
    # sometimes phrasing like 'repeated 21 times' handled above; else check for 'repeated 21'
    m = re.search(r'(?:duplicated|repeated|appears|appearing|copied|seen)\s+(\d+)', desc, re.IGNORECASE)
    if m:
        return int(m.group(1))
    return 0

# Build mapping id -> best record (max count)
best_by_id = {}
for r in swift_records:
    rid = r.get('id')
    cnt = extract_count(r.get('repo_data_description',''))
    if rid is None:
        continue
    if rid not in best_by_id or cnt > best_by_id[rid]['copies']:
        best_by_id[rid] = {'id': rid, 'copies': cnt, 'sample_repo_name': r.get('sample_repo_name'), 'sample_path': r.get('sample_path'), 'repo_data_description': r.get('repo_data_description')}

# Find the id with maximum copies
if not best_by_id:
    result = {'error': 'no swift records found'}
else:
    top = max(best_by_id.values(), key=lambda x: x['copies'])
    result = top

print("__RESULT__:")
print(json.dumps(result))"""

env_args = {'var_call_P7VtPWPYq8w71gstcj2ttIBw': 'file_storage/call_P7VtPWPYq8w71gstcj2ttIBw.json', 'var_call_I5ENV28yTlXCAUN5SkQiEluA': [{'id': '71a17ce92451858f3eb01aa8082551e48bc5550d', 'copies': '1', 'sample_path': 'validation-test/compiler_crashers_fixed/27485-swift-bracestmt-create.swift', 'repo_data_description': 'It is a non-binary file of 470 bytes, repeated 23 times in the dataset under mode 33188.', 'sample_repo_name': 'SwiftAndroid/swift'}, {'id': 'cc41f22d46f21f11c9e716b30cbaeb11f4ef80fc', 'copies': '1', 'sample_path': 'crashes-duplicates/22401-llvm-foldingset-swift-tupletype-nodeequals.swift', 'repo_data_description': 'This file has a size of 273 bytes, is non-binary, and appears 15 times with sample mode 33188.', 'sample_repo_name': 'practicalswift/swift-compiler-crashes'}], 'var_call_xLwnIE9BbSQYIbguSImjpHTo': 'file_storage/call_xLwnIE9BbSQYIbguSImjpHTo.json', 'var_call_HPlsvA1gXYnRpSLDScMaIvkn': [{'id': '71a17ce92451858f3eb01aa8082551e48bc5550d', 'copies': '1', 'sample_path': 'validation-test/compiler_crashers_fixed/27485-swift-bracestmt-create.swift', 'sample_repo_name': 'SwiftAndroid/swift', 'repo_data_description': 'It is a non-binary file of 470 bytes, repeated 23 times in the dataset under mode 33188.'}, {'id': 'cc41f22d46f21f11c9e716b30cbaeb11f4ef80fc', 'copies': '1', 'sample_path': 'crashes-duplicates/22401-llvm-foldingset-swift-tupletype-nodeequals.swift', 'sample_repo_name': 'practicalswift/swift-compiler-crashes', 'repo_data_description': 'This file has a size of 273 bytes, is non-binary, and appears 15 times with sample mode 33188.'}], 'var_call_3ixnJvHO0jcwFXPRIy1KSrEe': [{'id': 'cc41f22d46f21f11c9e716b30cbaeb11f4ef80fc', 'repo_count': '1', 'sample_path': 'crashes-duplicates/22401-llvm-foldingset-swift-tupletype-nodeequals.swift', 'sample_repo_name': 'practicalswift/swift-compiler-crashes', 'repo_data_description': 'This file has a size of 273 bytes, is non-binary, and appears 15 times with sample mode 33188.'}, {'id': '71a17ce92451858f3eb01aa8082551e48bc5550d', 'repo_count': '1', 'sample_path': 'validation-test/compiler_crashers_fixed/27485-swift-bracestmt-create.swift', 'sample_repo_name': 'SwiftAndroid/swift', 'repo_data_description': 'It is a non-binary file of 470 bytes, repeated 23 times in the dataset under mode 33188.'}]}

exec(code, env_args)
