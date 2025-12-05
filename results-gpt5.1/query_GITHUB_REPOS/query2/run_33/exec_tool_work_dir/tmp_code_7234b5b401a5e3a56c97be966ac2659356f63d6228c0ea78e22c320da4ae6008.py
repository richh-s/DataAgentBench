code = """import re, json
rows = var_call_ryPd04Z5IMKX8asxGcyUXeh7
max_copies = -1
best = None
for r in rows:
    m = re.search(r"copied (\d+) times", r['repo_data_description'])
    if not m:
        continue
    c = int(m.group(1))
    if c > max_copies:
        max_copies = c
        best = {'id': r['id'], 'sample_repo_name': r['sample_repo_name'], 'copies': c}
result = json.dumps(best)
print("__RESULT__:")
print(result)"""

env_args = {'var_call_rybY8IL1Rl2nlDWrBjGKFL4X': [], 'var_call_ryPd04Z5IMKX8asxGcyUXeh7': [{'id': '679da520fd8ee30c041d816b15d74b14ec42ba75', 'sample_repo_name': 'MakeZL/MLSwiftBasic', 'repo_data_description': 'The dataset includes this non-binary file, 6679 bytes in size and copied 12 times (mode: 33188).'}, {'id': 'c86b30ad42a5299ccb8907a949ad9248eadc0204', 'sample_repo_name': 'practicalswift/swift-compiler-crashes', 'repo_data_description': 'The dataset includes this non-binary file, 211 bytes in size and copied 15 times (mode: 33188).'}, {'id': 'b350eee519227d356704648c868c896ff3a93048', 'sample_repo_name': 'practicalswift/swift-compiler-crashes', 'repo_data_description': 'The dataset includes this non-binary file, 226 bytes in size and copied 15 times (mode: 33188).'}, {'id': '5fb353bfd251866214a3550d1f4bd33f2bc23333', 'sample_repo_name': 'practicalswift/swift-compiler-crashes', 'repo_data_description': 'The dataset includes this non-binary file, 323 bytes in size and copied 15 times (mode: 33188).'}, {'id': 'df3a20f577629bc8c49fd9a837837a6b45782c74', 'sample_repo_name': 'apple/swift', 'repo_data_description': 'The dataset includes this non-binary file, 771 bytes in size and copied 17 times (mode: 33188).'}, {'id': '4878324085d3c0bb299768377ba1750d5351ec82', 'sample_repo_name': 'SwiftAndroid/swift', 'repo_data_description': 'The dataset includes this non-binary file, 477 bytes in size and copied 23 times (mode: 33188).'}, {'id': '437d4a8638c1971be781cc55171aed646d733c70', 'sample_repo_name': 'apple/swift', 'repo_data_description': 'The dataset includes this non-binary file, 478 bytes in size and copied 23 times (mode: 33188).'}, {'id': 'a34c3d906831a12ffffa1b5d0fc30505126e9b69', 'sample_repo_name': 'kostiakoval/Mirror', 'repo_data_description': 'The dataset includes this non-binary file, 1848 bytes in size and copied 35 times (mode: 33188).'}, {'id': 'f2a35422a5bf04eba40c03e05adb0f15db319cf8', 'sample_repo_name': 'gregttn/GTToast', 'repo_data_description': 'The dataset includes this non-binary file, 7324 bytes in size and copied 1 times (mode: 33188).'}, {'id': '19f7d597fe480929b453e0603e5bbfc92679c0da', 'sample_repo_name': 'pop2ones/BallDown', 'repo_data_description': 'The dataset includes this non-binary file, 115 bytes in size and copied 2 times (mode: 33188).'}, {'id': 'a452f93131f16c5ea7978582b8253046d6a36f63', 'sample_repo_name': 'apple/swift-corelibs-foundation', 'repo_data_description': 'The dataset includes this non-binary file, 1416 bytes in size and copied 1 times (mode: 33188).'}, {'id': 'ba3c375f83c7a5307a6ac898ce7e020f3c58d619', 'sample_repo_name': 'domenicosolazzo/practice-swift', 'repo_data_description': 'The dataset includes this non-binary file, 902 bytes in size and copied 3 times (mode: 33188).'}, {'id': 'e781e95c03289f1f1cf7c2aed24c15ea5fd7e92e', 'sample_repo_name': 'SwiftAndroid/swift', 'repo_data_description': 'The dataset includes this non-binary file, 19263 bytes in size and copied 5 times (mode: 33188).'}]}

exec(code, env_args)
