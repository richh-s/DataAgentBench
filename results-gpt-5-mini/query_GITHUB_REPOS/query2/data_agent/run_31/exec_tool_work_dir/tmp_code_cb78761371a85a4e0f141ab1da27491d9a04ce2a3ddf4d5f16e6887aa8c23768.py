code = """import json, re
path = var_call_1L7UJ6UKvWrAguNX39s9kRNm
with open(path, 'r', encoding='utf-8') as f:
    data = json.load(f)

results = []
for r in data:
    sp = r.get('sample_path','') or ''
    desc = r.get('repo_data_description','') or ''
    if not sp.lower().endswith('.swift'):
        continue
    if 'binary' in desc.lower():
        continue
    desc_l = desc.lower()
    found = None
    patterns = [r"(\d+)\s*times",
                r"(?:copied|duplicated|appearing|appears|repeated|seen)\D{0,30}(\d+)",
                r"copied\D{0,30}(\d+)",
                r"appearing\D{0,30}(\d+)",
                r"duplicated\D{0,30}(\d+)",
                r"repeated\D{0,30}(\d+)",
                r"seen\D{0,30}(\d+)"]
    for p in patterns:
        m = re.search(p, desc_l)
        if m:
            try:
                val = int(m.group(1))
                found = val
                break
            except:
                continue
    # fallback: numbers present, pick largest <1000 maybe
    if found is None:
        nums = [int(x) for x in re.findall(r"\d+", desc_l)]
        # try to pick a number that is <= 500 and >1
        candidates = [x for x in nums if 1 < x < 1000]
        if candidates:
            # heuristic: if sentence contains 'bytes' then exclude numbers that likely are bytes > 1000
            if 'bytes' in desc_l:
                candidates2 = [x for x in candidates if x < 2000]
                if candidates2:
                    found = min(candidates2)
                else:
                    found = min(candidates)
            else:
                found = min(candidates)
    results.append({'id': r.get('id'), 'repo': r.get('sample_repo_name'), 'path': sp, 'desc': desc, 'copies': found})

# compute stats
with_copies = [e for e in results if e['copies'] is not None]
max_copies = max([e['copies'] for e in with_copies]) if with_copies else None
top = [e for e in with_copies if e['copies']==max_copies] if max_copies is not None else []

out = {'total_swift_nonbinary': len(results), 'with_extracted_copies': len(with_copies), 'max_copies': max_copies, 'top': top[:10]}
print('__RESULT__:')
print(json.dumps(out))"""

env_args = {'var_call_SDGQX18iUH8NYAOm5b9KcnF2': [], 'var_call_6rsNo2WRfbw8L1KylWqURcN9': [], 'var_call_39gQuW49foulPklZA7Mx8iO3': ['commits', 'contents', 'files'], 'var_call_JWQuMgg7VrdTv7VCwrisOm9A': [{'total_files': '1208'}], 'var_call_bT25wINgnqlapJwRt0hiNri1': [{'total_contents_swift': '105'}], 'var_call_1L7UJ6UKvWrAguNX39s9kRNm': 'file_storage/call_1L7UJ6UKvWrAguNX39s9kRNm.json', 'var_call_URM83RDoRV38Nz5sBVZIy5gc': {'max_copies': None, 'ids': []}, 'var_call_pIcSHWB2xCdTtA2TJmWHl27K': {'total_records': 105, 'first_10': [{'id': 'b03a39b4e07f98073fcf2fbe945bf1291cbfeca7', 'sample_repo_name': 'kostiakoval/WatchKit-Apps', 'sample_path': '5- Shared-CoreData/SharedKit/Record.swift', 'repo_data_description': 'With a file size of 290 bytes and sample mode 33188, this non-binary file is duplicated 8 times.'}, {'id': '3909cba31dd8c36766ee8efd9299c75a7e9f8721', 'sample_repo_name': 'slavapestov/swift', 'sample_path': 'validation-test/compiler_crashers_fixed/27617-swift-markasobjc.swift', 'repo_data_description': 'A 277-byte non-binary file appearing 8 times, with sample mode code 33188.'}, {'id': 'f7a67dcc0bda7a58e7e1a37d483bfd06e5ff9208', 'sample_repo_name': 'gmertk/BusyNavigationBar', 'sample_path': 'BusyNavigationBar/Example/AppDelegate.swift', 'repo_data_description': 'This file has a size of 2161 bytes, is non-binary, and appears 9 times with sample mode 33188.'}, {'id': '15492da9a0490415a84fa6c1a7957e473ebfa4db', 'sample_repo_name': 'practicalswift/swift-compiler-crashes', 'sample_path': 'crashes-duplicates/25255-swift-typechecker-checkinheritanceclause.swift', 'repo_data_description': 'With a file size of 240 bytes and sample mode 33188, this non-binary file is duplicated 10 times.'}, {'id': '41d65e7ae98cc15b6e5eacfd11568e1a851b6add', 'sample_repo_name': 'practicalswift/swift-compiler-crashes', 'sample_path': 'crashes-duplicates/26498-swift-sourcefile-lookupcache-lookupvalue.swift', 'repo_data_description': 'A 218-byte non-binary file appearing 10 times, with sample mode code 33188.'}, {'id': '117cee1262be7a8f9ffe72314c0395641169661d', 'sample_repo_name': 'firebase/quickstart-ios', 'sample_path': 'admob/AdMobExampleSwiftTests/AdMobExampleSwiftTests.swift', 'repo_data_description': 'A 1513-byte non-binary file appearing 12 times, with sample mode code 33188.'}, {'id': '679da520fd8ee30c041d816b15d74b14ec42ba75', 'sample_repo_name': 'MakeZL/MLSwiftBasic', 'sample_path': 'MLSwiftBasic/Classes/ProgressHUD/MLProgressHUD.swift', 'repo_data_description': 'The dataset includes this non-binary file, 6679 bytes in size and copied 12 times (mode: 33188).'}, {'id': '601d7b08677a1e95fcccea27fb1269c2110dc618', 'sample_repo_name': 'practicalswift/swift-compiler-crashes', 'sample_path': 'crashes-duplicates/23648-swift-modulefile-maybereadpattern.swift', 'repo_data_description': 'This file has a size of 262 bytes, is non-binary, and appears 14 times with sample mode 33188.'}, {'id': '98e288822bccf1c37b259164d3d5caa5b8c9f33d', 'sample_repo_name': 'practicalswift/swift-compiler-crashes', 'sample_path': 'crashes-duplicates/16041-swift-sourcemanager-getmessage.swift', 'repo_data_description': 'With a file size of 219 bytes and sample mode 33188, this non-binary file is duplicated 15 times.'}, {'id': 'cca8b7e8d35eccf1b5b46469b89d735b892dd316', 'sample_repo_name': 'practicalswift/swift-compiler-crashes', 'sample_path': 'crashes-duplicates/07465-swift-printingdiagnosticconsumer-handlediagnostic.swift', 'repo_data_description': 'With a file size of 344 bytes and sample mode 33188, this non-binary file is duplicated 15 times.'}]}, 'var_call_YhpQLU1Nrv70z0HJR6g83075': {'max_copies': None, 'top_ids': []}, 'var_call_bBr67Voa5K3ETIxYGrEdwkaN': {'max_copies': None, 'top': []}}

exec(code, env_args)
