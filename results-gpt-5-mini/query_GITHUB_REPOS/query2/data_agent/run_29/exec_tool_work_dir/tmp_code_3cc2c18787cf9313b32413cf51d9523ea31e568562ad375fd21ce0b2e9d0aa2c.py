code = """import re, json
# var_call_Jy9nwM0hHUCHJFHOACp3FKJa is available from storage
data = var_call_Jy9nwM0hHUCHJFHOACp3FKJa

results = []
for rec in data:
    desc = rec.get('repo_data_description') or ''
    # find all occurrences like '12 times' or 'appears 12 times' etc.
    m = re.findall(r"(\d+)\s+times", desc.lower())
    copies = None
    if m:
        # take the largest number found in the description
        copies = max(int(x) for x in m)
    else:
        # fallback: look for 'copied X' or 'appearing X' or 'repeated X' or standalone digits
        m2 = re.findall(r"(copied|appearing|repeated|appears)\s+(\d+)", desc.lower())
        if m2:
            copies = max(int(x[1]) for x in m2)
        else:
            m3 = re.findall(r"(\d+)", desc)
            if m3:
                copies = max(int(x) for x in m3)
    if copies is None:
        copies = 0
    results.append({
        'id': rec.get('id'),
        'sample_repo_name': rec.get('sample_repo_name'),
        'sample_path': rec.get('sample_path'),
        'copies': copies,
        'repo_data_description': desc
    })

# pick the record with max copies; if tie, pick the first
best = max(results, key=lambda r: r['copies']) if results else None
output = best or {}
print("__RESULT__:")
print(json.dumps(output))"""

env_args = {'var_call_fcgaYFMKd48OlW1pwwWI4sob': [], 'var_call_b7AXjaKp3RkMRwTnEFecIyZc': ['commits', 'contents', 'files'], 'var_call_bKSkaYI5c8pi7D060B2PCkwe': [], 'var_call_Jy9nwM0hHUCHJFHOACp3FKJa': [{'id': 'b03a39b4e07f98073fcf2fbe945bf1291cbfeca7', 'sample_repo_name': 'kostiakoval/WatchKit-Apps', 'sample_path': '5- Shared-CoreData/SharedKit/Record.swift', 'repo_data_description': 'With a file size of 290 bytes and sample mode 33188, this non-binary file is duplicated 8 times.'}, {'id': '3909cba31dd8c36766ee8efd9299c75a7e9f8721', 'sample_repo_name': 'slavapestov/swift', 'sample_path': 'validation-test/compiler_crashers_fixed/27617-swift-markasobjc.swift', 'repo_data_description': 'A 277-byte non-binary file appearing 8 times, with sample mode code 33188.'}, {'id': 'f7a67dcc0bda7a58e7e1a37d483bfd06e5ff9208', 'sample_repo_name': 'gmertk/BusyNavigationBar', 'sample_path': 'BusyNavigationBar/Example/AppDelegate.swift', 'repo_data_description': 'This file has a size of 2161 bytes, is non-binary, and appears 9 times with sample mode 33188.'}, {'id': '15492da9a0490415a84fa6c1a7957e473ebfa4db', 'sample_repo_name': 'practicalswift/swift-compiler-crashes', 'sample_path': 'crashes-duplicates/25255-swift-typechecker-checkinheritanceclause.swift', 'repo_data_description': 'With a file size of 240 bytes and sample mode 33188, this non-binary file is duplicated 10 times.'}, {'id': '41d65e7ae98cc15b6e5eacfd11568e1a851b6add', 'sample_repo_name': 'practicalswift/swift-compiler-crashes', 'sample_path': 'crashes-duplicates/26498-swift-sourcefile-lookupcache-lookupvalue.swift', 'repo_data_description': 'A 218-byte non-binary file appearing 10 times, with sample mode code 33188.'}, {'id': '117cee1262be7a8f9ffe72314c0395641169661d', 'sample_repo_name': 'firebase/quickstart-ios', 'sample_path': 'admob/AdMobExampleSwiftTests/AdMobExampleSwiftTests.swift', 'repo_data_description': 'A 1513-byte non-binary file appearing 12 times, with sample mode code 33188.'}, {'id': '679da520fd8ee30c041d816b15d74b14ec42ba75', 'sample_repo_name': 'MakeZL/MLSwiftBasic', 'sample_path': 'MLSwiftBasic/Classes/ProgressHUD/MLProgressHUD.swift', 'repo_data_description': 'The dataset includes this non-binary file, 6679 bytes in size and copied 12 times (mode: 33188).'}, {'id': '601d7b08677a1e95fcccea27fb1269c2110dc618', 'sample_repo_name': 'practicalswift/swift-compiler-crashes', 'sample_path': 'crashes-duplicates/23648-swift-modulefile-maybereadpattern.swift', 'repo_data_description': 'This file has a size of 262 bytes, is non-binary, and appears 14 times with sample mode 33188.'}, {'id': '98e288822bccf1c37b259164d3d5caa5b8c9f33d', 'sample_repo_name': 'practicalswift/swift-compiler-crashes', 'sample_path': 'crashes-duplicates/16041-swift-sourcemanager-getmessage.swift', 'repo_data_description': 'With a file size of 219 bytes and sample mode 33188, this non-binary file is duplicated 15 times.'}, {'id': 'cca8b7e8d35eccf1b5b46469b89d735b892dd316', 'sample_repo_name': 'practicalswift/swift-compiler-crashes', 'sample_path': 'crashes-duplicates/07465-swift-printingdiagnosticconsumer-handlediagnostic.swift', 'repo_data_description': 'With a file size of 344 bytes and sample mode 33188, this non-binary file is duplicated 15 times.'}, {'id': 'c86b30ad42a5299ccb8907a949ad9248eadc0204', 'sample_repo_name': 'practicalswift/swift-compiler-crashes', 'sample_path': 'fixed/01682-swift-parser-parsedecl.swift', 'repo_data_description': 'The dataset includes this non-binary file, 211 bytes in size and copied 15 times (mode: 33188).'}, {'id': '30b20e2d80706fd2381dc51eec2f1c22e71ecacf', 'sample_repo_name': 'practicalswift/swift-compiler-crashes', 'sample_path': 'crashes-duplicates/15025-swift-sourcemanager-getmessage.swift', 'repo_data_description': 'A 221-byte non-binary file appearing 15 times, with sample mode code 33188.'}, {'id': 'b350eee519227d356704648c868c896ff3a93048', 'sample_repo_name': 'practicalswift/swift-compiler-crashes', 'sample_path': 'crashes-duplicates/18368-swift-sourcemanager-getmessage.swift', 'repo_data_description': 'The dataset includes this non-binary file, 226 bytes in size and copied 15 times (mode: 33188).'}, {'id': '1ad86cf8e815fce652aa101d654485fea8033954', 'sample_repo_name': 'practicalswift/swift-compiler-crashes', 'sample_path': 'fixed/01847-std-function-func-swift-type-subst.swift', 'repo_data_description': 'Non-binary content file (215 bytes) seen 15 times, using sample mode 33188.'}, {'id': '3c92bfc55f392146da4902bc252fd216cd3f2efd', 'sample_repo_name': 'practicalswift/swift-compiler-crashes', 'sample_path': 'crashes-duplicates/08505-swift-typechecker-conformstoprotocol.swift', 'repo_data_description': 'With a file size of 247 bytes and sample mode 33188, this non-binary file is duplicated 15 times.'}, {'id': '3d42ac2c0fad831225f80a9355a196027e6ccc3e', 'sample_repo_name': 'practicalswift/swift-compiler-crashes', 'sample_path': 'fixed/00118-swift-dependentgenerictyperesolver-resolvegenerictypeparamtype.swift', 'repo_data_description': 'It is a non-binary file of 306 bytes, repeated 15 times in the dataset under mode 33188.'}, {'id': 'cc41f22d46f21f11c9e716b30cbaeb11f4ef80fc', 'sample_repo_name': 'practicalswift/swift-compiler-crashes', 'sample_path': 'crashes-duplicates/22401-llvm-foldingset-swift-tupletype-nodeequals.swift', 'repo_data_description': 'This file has a size of 273 bytes, is non-binary, and appears 15 times with sample mode 33188.'}, {'id': 'be6be234f9d404b0251c9a3626d644104cfe359b', 'sample_repo_name': 'practicalswift/swift-compiler-crashes', 'sample_path': 'crashes-duplicates/15704-no-stacktrace.swift', 'repo_data_description': 'It is a non-binary file of 243 bytes, repeated 15 times in the dataset under mode 33188.'}, {'id': 'b8223ce270293582721ad59ebe08f0ca2c068ed8', 'sample_repo_name': 'practicalswift/swift-compiler-crashes', 'sample_path': 'crashes-duplicates/04574-swift-sourcemanager-getmessage.swift', 'repo_data_description': 'This file has a size of 241 bytes, is non-binary, and appears 15 times with sample mode 33188.'}, {'id': 'cc4de346f66613edef22d12b73c44fc2c8834acd', 'sample_repo_name': 'practicalswift/swift-compiler-crashes', 'sample_path': 'crashes-duplicates/02484-swift-sourcemanager-getmessage.swift', 'repo_data_description': 'With a file size of 226 bytes and sample mode 33188, this non-binary file is duplicated 15 times.'}], 'var_call_KZSwmnpkWPg5k9tqRC8B0sj9': []}

exec(code, env_args)
