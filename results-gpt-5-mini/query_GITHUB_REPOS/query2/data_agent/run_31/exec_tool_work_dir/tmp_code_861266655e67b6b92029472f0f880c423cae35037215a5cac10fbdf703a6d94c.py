code = """import json, re
path = var_call_1L7UJ6UKvWrAguNX39s9kRNm
with open(path, 'r', encoding='utf-8') as f:
    data = json.load(f)

keywords = ['times','copied','duplicated','appearing','appears','repeated','seen','appears','appearing']

results = []
for r in data:
    sp = (r.get('sample_path') or '')
    desc = (r.get('repo_data_description') or '')
    if not sp.lower().endswith('.swift'):
        continue
    if 'binary' in desc.lower():
        continue
    desc_l = desc
    nums = [(m.group(0), m.start(), m.end()) for m in re.finditer(r'\d+', desc_l)]
    found_vals = []
    for num, s, e in nums:
        val = int(num)
        window = desc_l[max(0, s-40):min(len(desc_l), e+40)].lower()
        # if window has any keyword, accept
        if any(k in window for k in keywords):
            found_vals.append((val, window))
        # else if 'bytes' in window and val > 1000, it's likely size, skip
    # if none found via keyword, try patterns like 'copied N times' where N may be elsewhere
    if not found_vals:
        # search patterns
        patterns = [r'copied\s+(\d+)', r'duplicated\s+(\d+)', r'appearing\s+(\d+)', r'appears\s+(\d+)', r'repeated\s+(\d+)', r'seen\s+(\d+)', r'(\d+)\s+times']
        for p in patterns:
            m = re.search(p, desc_l, flags=re.IGNORECASE)
            if m:
                found_vals.append((int(m.group(1)), desc_l))
    # fallback: consider any small integers under 1000 excluding those in 'bytes' contexts larger than 2000
    if not found_vals:
        candidates = []
        for num, s, e in nums:
            val = int(num)
            window = desc_l[max(0, s-20):min(len(desc_l), e+20)].lower()
            if 'byte' in window and val > 2000:
                continue
            if 1 <= val <= 10000:
                candidates.append((val, window))
        if candidates:
            # choose the candidate whose window contains any keyword, else smallest
            for val, window in candidates:
                if any(k in window for k in keywords):
                    found_vals.append((val, window))
                    break
            if not found_vals:
                # take smallest
                found_vals.append(min(candidates, key=lambda x: x[0]))
    copies = None
    if found_vals:
        # pick the most plausible: if multiple, pick the one with keyword 'times' or 'copied' priority
        # prioritize values where window contains 'times' or 'copied' or 'appearing'
        priority = None
        for val, window in found_vals:
            if 'times' in window or 'copied' in window or 'appearing' in window or 'appears' in window:
                priority = val
                break
        copies = priority if priority is not None else found_vals[0][0]
    results.append({'id': r.get('id'), 'sample_repo_name': r.get('sample_repo_name'), 'sample_path': sp, 'desc': desc, 'copies': copies})

# compute max
with_copies = [e for e in results if e['copies'] is not None]
if not with_copies:
    out = {'error': 'no entries with copies extracted'}
else:
    max_c = max(e['copies'] for e in with_copies)
    tops = [e for e in with_copies if e['copies']==max_c]
    out = {'max_copies': max_c, 'top_entries': tops, 'count_total_swift_nonbinary': len(results)}

print('__RESULT__:')
print(json.dumps(out))"""

env_args = {'var_call_SDGQX18iUH8NYAOm5b9KcnF2': [], 'var_call_6rsNo2WRfbw8L1KylWqURcN9': [], 'var_call_39gQuW49foulPklZA7Mx8iO3': ['commits', 'contents', 'files'], 'var_call_JWQuMgg7VrdTv7VCwrisOm9A': [{'total_files': '1208'}], 'var_call_bT25wINgnqlapJwRt0hiNri1': [{'total_contents_swift': '105'}], 'var_call_1L7UJ6UKvWrAguNX39s9kRNm': 'file_storage/call_1L7UJ6UKvWrAguNX39s9kRNm.json', 'var_call_URM83RDoRV38Nz5sBVZIy5gc': {'max_copies': None, 'ids': []}, 'var_call_pIcSHWB2xCdTtA2TJmWHl27K': {'total_records': 105, 'first_10': [{'id': 'b03a39b4e07f98073fcf2fbe945bf1291cbfeca7', 'sample_repo_name': 'kostiakoval/WatchKit-Apps', 'sample_path': '5- Shared-CoreData/SharedKit/Record.swift', 'repo_data_description': 'With a file size of 290 bytes and sample mode 33188, this non-binary file is duplicated 8 times.'}, {'id': '3909cba31dd8c36766ee8efd9299c75a7e9f8721', 'sample_repo_name': 'slavapestov/swift', 'sample_path': 'validation-test/compiler_crashers_fixed/27617-swift-markasobjc.swift', 'repo_data_description': 'A 277-byte non-binary file appearing 8 times, with sample mode code 33188.'}, {'id': 'f7a67dcc0bda7a58e7e1a37d483bfd06e5ff9208', 'sample_repo_name': 'gmertk/BusyNavigationBar', 'sample_path': 'BusyNavigationBar/Example/AppDelegate.swift', 'repo_data_description': 'This file has a size of 2161 bytes, is non-binary, and appears 9 times with sample mode 33188.'}, {'id': '15492da9a0490415a84fa6c1a7957e473ebfa4db', 'sample_repo_name': 'practicalswift/swift-compiler-crashes', 'sample_path': 'crashes-duplicates/25255-swift-typechecker-checkinheritanceclause.swift', 'repo_data_description': 'With a file size of 240 bytes and sample mode 33188, this non-binary file is duplicated 10 times.'}, {'id': '41d65e7ae98cc15b6e5eacfd11568e1a851b6add', 'sample_repo_name': 'practicalswift/swift-compiler-crashes', 'sample_path': 'crashes-duplicates/26498-swift-sourcefile-lookupcache-lookupvalue.swift', 'repo_data_description': 'A 218-byte non-binary file appearing 10 times, with sample mode code 33188.'}, {'id': '117cee1262be7a8f9ffe72314c0395641169661d', 'sample_repo_name': 'firebase/quickstart-ios', 'sample_path': 'admob/AdMobExampleSwiftTests/AdMobExampleSwiftTests.swift', 'repo_data_description': 'A 1513-byte non-binary file appearing 12 times, with sample mode code 33188.'}, {'id': '679da520fd8ee30c041d816b15d74b14ec42ba75', 'sample_repo_name': 'MakeZL/MLSwiftBasic', 'sample_path': 'MLSwiftBasic/Classes/ProgressHUD/MLProgressHUD.swift', 'repo_data_description': 'The dataset includes this non-binary file, 6679 bytes in size and copied 12 times (mode: 33188).'}, {'id': '601d7b08677a1e95fcccea27fb1269c2110dc618', 'sample_repo_name': 'practicalswift/swift-compiler-crashes', 'sample_path': 'crashes-duplicates/23648-swift-modulefile-maybereadpattern.swift', 'repo_data_description': 'This file has a size of 262 bytes, is non-binary, and appears 14 times with sample mode 33188.'}, {'id': '98e288822bccf1c37b259164d3d5caa5b8c9f33d', 'sample_repo_name': 'practicalswift/swift-compiler-crashes', 'sample_path': 'crashes-duplicates/16041-swift-sourcemanager-getmessage.swift', 'repo_data_description': 'With a file size of 219 bytes and sample mode 33188, this non-binary file is duplicated 15 times.'}, {'id': 'cca8b7e8d35eccf1b5b46469b89d735b892dd316', 'sample_repo_name': 'practicalswift/swift-compiler-crashes', 'sample_path': 'crashes-duplicates/07465-swift-printingdiagnosticconsumer-handlediagnostic.swift', 'repo_data_description': 'With a file size of 344 bytes and sample mode 33188, this non-binary file is duplicated 15 times.'}]}, 'var_call_YhpQLU1Nrv70z0HJR6g83075': {'max_copies': None, 'top_ids': []}, 'var_call_bBr67Voa5K3ETIxYGrEdwkaN': {'max_copies': None, 'top': []}, 'var_call_Z6q0XmsZhewnGOczECijydmT': {'total_swift_nonbinary': 0, 'with_extracted_copies': 0, 'max_copies': None, 'top': []}, 'var_call_FjPngB51KJkbG1Ds36WCxHHv': [{'sample_path': '5- Shared-CoreData/SharedKit/Record.swift', 'repo_data_description': 'With a file size of 290 bytes and sample mode 33188, this non-binary file is duplicated 8 times.'}, {'sample_path': 'validation-test/compiler_crashers_fixed/27617-swift-markasobjc.swift', 'repo_data_description': 'A 277-byte non-binary file appearing 8 times, with sample mode code 33188.'}, {'sample_path': 'BusyNavigationBar/Example/AppDelegate.swift', 'repo_data_description': 'This file has a size of 2161 bytes, is non-binary, and appears 9 times with sample mode 33188.'}, {'sample_path': 'crashes-duplicates/25255-swift-typechecker-checkinheritanceclause.swift', 'repo_data_description': 'With a file size of 240 bytes and sample mode 33188, this non-binary file is duplicated 10 times.'}, {'sample_path': 'crashes-duplicates/26498-swift-sourcefile-lookupcache-lookupvalue.swift', 'repo_data_description': 'A 218-byte non-binary file appearing 10 times, with sample mode code 33188.'}, {'sample_path': 'admob/AdMobExampleSwiftTests/AdMobExampleSwiftTests.swift', 'repo_data_description': 'A 1513-byte non-binary file appearing 12 times, with sample mode code 33188.'}, {'sample_path': 'MLSwiftBasic/Classes/ProgressHUD/MLProgressHUD.swift', 'repo_data_description': 'The dataset includes this non-binary file, 6679 bytes in size and copied 12 times (mode: 33188).'}, {'sample_path': 'crashes-duplicates/23648-swift-modulefile-maybereadpattern.swift', 'repo_data_description': 'This file has a size of 262 bytes, is non-binary, and appears 14 times with sample mode 33188.'}, {'sample_path': 'crashes-duplicates/16041-swift-sourcemanager-getmessage.swift', 'repo_data_description': 'With a file size of 219 bytes and sample mode 33188, this non-binary file is duplicated 15 times.'}, {'sample_path': 'crashes-duplicates/07465-swift-printingdiagnosticconsumer-handlediagnostic.swift', 'repo_data_description': 'With a file size of 344 bytes and sample mode 33188, this non-binary file is duplicated 15 times.'}, {'sample_path': 'fixed/01682-swift-parser-parsedecl.swift', 'repo_data_description': 'The dataset includes this non-binary file, 211 bytes in size and copied 15 times (mode: 33188).'}, {'sample_path': 'crashes-duplicates/15025-swift-sourcemanager-getmessage.swift', 'repo_data_description': 'A 221-byte non-binary file appearing 15 times, with sample mode code 33188.'}, {'sample_path': 'crashes-duplicates/18368-swift-sourcemanager-getmessage.swift', 'repo_data_description': 'The dataset includes this non-binary file, 226 bytes in size and copied 15 times (mode: 33188).'}, {'sample_path': 'fixed/01847-std-function-func-swift-type-subst.swift', 'repo_data_description': 'Non-binary content file (215 bytes) seen 15 times, using sample mode 33188.'}, {'sample_path': 'crashes-duplicates/08505-swift-typechecker-conformstoprotocol.swift', 'repo_data_description': 'With a file size of 247 bytes and sample mode 33188, this non-binary file is duplicated 15 times.'}, {'sample_path': 'fixed/00118-swift-dependentgenerictyperesolver-resolvegenerictypeparamtype.swift', 'repo_data_description': 'It is a non-binary file of 306 bytes, repeated 15 times in the dataset under mode 33188.'}, {'sample_path': 'crashes-duplicates/22401-llvm-foldingset-swift-tupletype-nodeequals.swift', 'repo_data_description': 'This file has a size of 273 bytes, is non-binary, and appears 15 times with sample mode 33188.'}, {'sample_path': 'crashes-duplicates/15704-no-stacktrace.swift', 'repo_data_description': 'It is a non-binary file of 243 bytes, repeated 15 times in the dataset under mode 33188.'}, {'sample_path': 'crashes-duplicates/04574-swift-sourcemanager-getmessage.swift', 'repo_data_description': 'This file has a size of 241 bytes, is non-binary, and appears 15 times with sample mode 33188.'}, {'sample_path': 'crashes-duplicates/02484-swift-sourcemanager-getmessage.swift', 'repo_data_description': 'With a file size of 226 bytes and sample mode 33188, this non-binary file is duplicated 15 times.'}, {'sample_path': 'crashes-duplicates/11691-swift-typechecker-checksubstitutions.swift', 'repo_data_description': 'With a file size of 248 bytes and sample mode 33188, this non-binary file is duplicated 15 times.'}, {'sample_path': 'crashes-duplicates/07164-swift-sourcemanager-getmessage.swift', 'repo_data_description': 'The dataset includes this non-binary file, 323 bytes in size and copied 15 times (mode: 33188).'}, {'sample_path': 'test/Misc/tbi.swift', 'repo_data_description': 'The dataset includes this non-binary file, 771 bytes in size and copied 17 times (mode: 33188).'}, {'sample_path': 'validation-test/compiler_crashers_fixed/25612-swift-patternbindingdecl-create.swift', 'repo_data_description': 'A 273-byte non-binary file appearing 20 times, with sample mode code 33188.'}, {'sample_path': 'test/Interpreter/SDK/Quartz_without_Foundation.swift', 'repo_data_description': 'It is a non-binary file of 241 bytes, repeated 20 times in the dataset under mode 33188.'}, {'sample_path': 'validation-test/compiler_crashers_fixed/02103-swift-typebase-getcanonicaltype.swift', 'repo_data_description': 'It is a non-binary file of 481 bytes, repeated 21 times in the dataset under mode 33188.'}, {'sample_path': 'validation-test/compiler_crashers_fixed/00354-swift-modulefile-maybereadpattern.swift', 'repo_data_description': 'Non-binary content file (398 bytes) seen 21 times, using sample mode 33188.'}, {'sample_path': 'validation-test/compiler_crashers_fixed/00501-resolvetypedecl.swift', 'repo_data_description': 'A 259-byte non-binary file appearing 21 times, with sample mode code 33188.'}, {'sample_path': 'validation-test/compiler_crashers_fixed/00602-swift-modulefile-gettype.swift', 'repo_data_description': 'A 286-byte non-binary file appearing 21 times, with sample mode code 33188.'}, {'sample_path': 'test/IDE/complete_overridden_decls.swift', 'repo_data_description': 'With a file size of 4470 bytes and sample mode 33188, this non-binary file is duplicated 21 times.'}], 'var_call_llms9eJCOLYwQfF7QuIZkdmy': {'error': 'no entries with copies extracted'}}

exec(code, env_args)
