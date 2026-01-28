code = """import json, re
# var_call_cDHgvkQ2Jq8RatXF4NxUaL7o is a file path containing the JSON result from the contents query
fp = var_call_cDHgvkQ2Jq8RatXF4NxUaL7o
with open(fp, 'r', encoding='utf-8') as f:
    records = json.load(f)

# Filter Swift non-binary entries and extract copy counts from repo_data_description
pattern = re.compile(r"(\d+)\s*(?:times|time|copied|duplicated|appearing|appears|repeated)", re.IGNORECASE)
results = []
for r in records:
    path = r.get('sample_path','') or ''
    desc = r.get('repo_data_description','') or ''
    if path.lower().endswith('.swift') and 'non-binary' in desc.lower():
        m = pattern.search(desc)
        count = None
        if m:
            try:
                count = int(m.group(1))
            except:
                count = None
        results.append({'id': r.get('id'), 'sample_repo_name': r.get('sample_repo_name'), 'sample_path': path, 'repo_data_description': desc, 'parsed_count': count})

# Find max parsed_count
max_count = None
for r in results:
    c = r['parsed_count']
    if c is not None:
        if max_count is None or c > max_count:
            max_count = c

max_ids = [r for r in results if r['parsed_count'] == max_count]

out = {'max_count': max_count, 'max_ids': max_ids[:5]}  # limit for brevity

import json
print("__RESULT__:")
print(json.dumps(out))"""

env_args = {'var_call_UNXZXUASx9NP1eefdq11DOo8': [], 'var_call_DW1116ZDSQV61sNQVMzbX6mb': [{'id': 'a6fb31fa1e4b1647e8862580703add8c6205c6d1', 'copy_count': '4'}, {'id': 'd67714b2a25908fbc4e6b00531862cc62265bf75', 'copy_count': '2'}, {'id': '75c9123b0b91ca99402ed40efe80d21cb6bc3f90', 'copy_count': '2'}, {'id': '6066caa5e76b60fbd0f7bc2a096c6fd7c023609f', 'copy_count': '2'}, {'id': '731d202c0c486ce8daf377f2c6a7389cc9bc20fa', 'copy_count': '2'}, {'id': 'f260ac370354b6dc8e5fb92da276cf587dd2d4d7', 'copy_count': '2'}, {'id': 'a1615a71d1bdbb036d1dde0a94b8285fa8fca084', 'copy_count': '2'}, {'id': '0191f88060e6994e1095478da21798fd2c0a9dcb', 'copy_count': '2'}, {'id': '49f5eda9ac693bf61324ee7f65a15d704f7f3411', 'copy_count': '2'}, {'id': '8af9111216436874eecfaa475d5c2f3ac650e3bc', 'copy_count': '2'}, {'id': 'f64ee245678dcb26d658600708e2996a7608fc6e', 'copy_count': '2'}, {'id': '53496cde05c660feb3ab3335e825b363aa68a51a', 'copy_count': '2'}, {'id': '3252bbf919d2fb7d0f3fd9a3841f44f5f699c0c2', 'copy_count': '2'}, {'id': 'e94c45ffe619fbd39e7f5df78a590bd33893d64a', 'copy_count': '2'}, {'id': '5f34ae4f28cd2969f3ca3d5717e068e54e2dc4fb', 'copy_count': '1'}, {'id': '263647ddf1a48b46122b0cc6b1e959f542e37d39', 'copy_count': '1'}, {'id': '3db7a1eebb044e987b8a3d7724016584447936a2', 'copy_count': '1'}, {'id': '97b7ce1004877b0ea9eb01c6037494db144b237f', 'copy_count': '1'}, {'id': '542dc8f9a2c4a42107ca95a6da7a2c99cfe5f177', 'copy_count': '1'}, {'id': 'e0e158ea1c3a5fa3d6fc630f88d85da126737c3f', 'copy_count': '1'}], 'var_call_1Vdad0SNhCZFQXBjH48S0QDn': [], 'var_call_t4yf704qpmyo0vUhjAHVV1EZ': 'file_storage/call_t4yf704qpmyo0vUhjAHVV1EZ.json', 'var_call_l9kNuFdwCxrPJCObGE7hAsMr': [{'id': '71a17ce92451858f3eb01aa8082551e48bc5550d', 'copy_count': '1', 'sample_repo_name': 'SwiftAndroid/swift', 'sample_path': 'validation-test/compiler_crashers_fixed/27485-swift-bracestmt-create.swift', 'repo_data_description': 'It is a non-binary file of 470 bytes, repeated 23 times in the dataset under mode 33188.'}, {'id': 'cc41f22d46f21f11c9e716b30cbaeb11f4ef80fc', 'copy_count': '1', 'sample_repo_name': 'practicalswift/swift-compiler-crashes', 'sample_path': 'crashes-duplicates/22401-llvm-foldingset-swift-tupletype-nodeequals.swift', 'repo_data_description': 'This file has a size of 273 bytes, is non-binary, and appears 15 times with sample mode 33188.'}], 'var_call_cDHgvkQ2Jq8RatXF4NxUaL7o': 'file_storage/call_cDHgvkQ2Jq8RatXF4NxUaL7o.json'}

exec(code, env_args)
