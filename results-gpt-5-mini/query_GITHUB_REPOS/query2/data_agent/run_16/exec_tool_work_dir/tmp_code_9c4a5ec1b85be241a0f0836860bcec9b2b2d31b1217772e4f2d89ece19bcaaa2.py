code = """import json, re
# Load the large contents query result from the storage path
path = var_call_mIJxWXZE36V8bL2ZApfD6DxR
with open(path, 'r', encoding='utf-8') as f:
    records = json.load(f)

# Function to extract copies count from repo_data_description
def extract_copies(text):
    if not text:
        return None
    # look for patterns like 'copied 12 times', 'appears 15 times', 'repeated 23 times', 'duplicated 15 times', 'appearing 21 times'
    m = re.search(r"(copied|appears|appearing|repeated|duplicated|appears)\s+(\d+)\s+times", text, flags=re.I)
    if m:
        return int(m.group(2))
    m2 = re.search(r"(\d+)\s+times", text, flags=re.I)
    if m2:
        return int(m2.group(1))
    # fallback: any number preceding 'times' or 'time'
    m3 = re.search(r"(\d+)\s+time", text, flags=re.I)
    if m3:
        return int(m3.group(1))
    # fallback: 'appears N times' variations
    m4 = re.search(r"appears\s+(\d+)", text, flags=re.I)
    if m4:
        return int(m4.group(1))
    # last resort: any number in the string (but prefer larger meaningful ones)
    nums = re.findall(r"(\d+)", text)
    if nums:
        # choose the largest number found
        return max(int(x) for x in nums)
    return None

# Aggregate by id: take maximum reported copies among records for the same id
agg = {}
for r in records:
    rid = r.get('id')
    desc = r.get('repo_data_description') or ''
    copies = extract_copies(desc)
    if copies is None:
        continue
    if rid not in agg or copies > agg[rid]['copies']:
        agg[rid] = {'copies': copies, 'sample_repo_name': r.get('sample_repo_name'), 'sample_path': r.get('sample_path'), 'repo_data_description': desc}

# Find the id with maximum copies
if not agg:
    result = {'error': 'no non-binary swift records with copy counts found'}
else:
    top_id = max(agg.items(), key=lambda kv: kv[1]['copies'])[0]
    top_info = agg[top_id]
    result = {'top_id': top_id, 'copies': top_info['copies'], 'sample_repo_name': top_info.get('sample_repo_name'), 'sample_path': top_info.get('sample_path'), 'repo_data_description': top_info.get('repo_data_description')}

print("__RESULT__:")
print(json.dumps(result))"""

env_args = {'var_call_B3j02XKITg1goB7oFI3iaXv4': ['commits', 'contents', 'files'], 'var_call_i1c3dZQj2j15mdpQMk3t6JZA': [], 'var_call_amC0W07gJ0e62C8fqYbjgEbM': [{'id': '71a17ce92451858f3eb01aa8082551e48bc5550d', 'sample_path': 'validation-test/compiler_crashers_fixed/27485-swift-bracestmt-create.swift', 'copies': '1', 'repo_data_description_sample': 'It is a non-binary file of 470 bytes, repeated 23 times in the dataset under mode 33188.'}, {'id': 'cc41f22d46f21f11c9e716b30cbaeb11f4ef80fc', 'sample_path': 'crashes-duplicates/22401-llvm-foldingset-swift-tupletype-nodeequals.swift', 'copies': '1', 'repo_data_description_sample': 'This file has a size of 273 bytes, is non-binary, and appears 15 times with sample mode 33188.'}], 'var_call_mIJxWXZE36V8bL2ZApfD6DxR': 'file_storage/call_mIJxWXZE36V8bL2ZApfD6DxR.json', 'var_call_9lwKF9pCRYOVeMsoQq1hdOUx': [{'id': '71a17ce92451858f3eb01aa8082551e48bc5550d', 'copies': '1', 'sample_repo_name': 'SwiftAndroid/swift', 'sample_path': 'validation-test/compiler_crashers_fixed/27485-swift-bracestmt-create.swift', 'repo_data_description': 'It is a non-binary file of 470 bytes, repeated 23 times in the dataset under mode 33188.'}], 'var_call_Zwf1cTkrs2ZCiFbMNEgNbIcM': 'file_storage/call_Zwf1cTkrs2ZCiFbMNEgNbIcM.json', 'var_call_ZLuC53za7RvDkR8hmVkcU3QM': [{'id': '71a17ce92451858f3eb01aa8082551e48bc5550d', 'file_rows': '1', 'distinct_repos': '1', 'sample_repo': 'SwiftAndroid/swift', 'sample_path': 'validation-test/compiler_crashers_fixed/27485-swift-bracestmt-create.swift', 'repo_data_description': 'It is a non-binary file of 470 bytes, repeated 23 times in the dataset under mode 33188.'}, {'id': 'cc41f22d46f21f11c9e716b30cbaeb11f4ef80fc', 'file_rows': '1', 'distinct_repos': '1', 'sample_repo': 'practicalswift/swift-compiler-crashes', 'sample_path': 'crashes-duplicates/22401-llvm-foldingset-swift-tupletype-nodeequals.swift', 'repo_data_description': 'This file has a size of 273 bytes, is non-binary, and appears 15 times with sample mode 33188.'}]}

exec(code, env_args)
