code = """import json
import re

with open(locals()['var_function-call-513243052492864742']) as f:
    swift_repos_raw = json.load(f)
swift_repos = set(r['repo_name'] for r in swift_repos_raw)

with open(locals()['var_function-call-513243052492863773']) as f:
    contents = json.load(f)

def parse_count(desc):
    match = re.search(r'(?:seen|duplicated|appearing|copied|repeated)\s+(\d+)\s+times', desc)
    if match:
        return int(match.group(1))
    return 0

def is_non_binary(desc):
    return "non-binary" in desc.lower()

candidates = []
for c in contents:
    desc = c.get('repo_data_description', '')
    if is_non_binary(desc):
        count = parse_count(desc)
        candidates.append({
            'id': c['id'],
            'count': count,
            'repo': c.get('sample_repo_name'),
            'path': c.get('sample_path'),
            'is_swift_repo': c.get('sample_repo_name') in swift_repos
        })

candidates.sort(key=lambda x: x['count'], reverse=True)

print("__RESULT__:")
print(json.dumps(candidates[:10]))"""

env_args = {'var_function-call-11059177960452465386': ['languages', 'repos', 'licenses'], 'var_function-call-11059177960452467955': ['commits', 'contents', 'files'], 'var_function-call-6869508518099835213': [{'repo_name': 'juliandunn/rackspacecloud', 'language_description': 'The codebase includes: Ruby (22,438 bytes), Shell (465 bytes).'}, {'repo_name': 'xMarkusSpringerx/coloranalyzer', 'language_description': 'This repository is mainly written in Ruby (1,897 bytes), with additional code in Shell (115 bytes).'}, {'repo_name': 'michaellihs/gitlab', 'language_description': 'The codebase includes: Ruby (162,002 bytes), Shell (168 bytes).'}, {'repo_name': 'vyorkin/xftp', 'language_description': 'The majority of the code is in Ruby (25,709 bytes), followed by Shell (115 bytes).'}, {'repo_name': 'airatshigapov/drophunter', 'language_description': 'The majority of the code is in Ruby (4,198 bytes), followed by Shell (115 bytes).'}], 'var_function-call-6869508518099833804': 'file_storage/function-call-6869508518099833804.json', 'var_function-call-6869508518099836491': [{'repo_name': 'np/ling', 'ref': 'refs/heads/master', 'path': 'fixtures/strict-par-success/fun1_to_proc_par2.ll', 'mode': '40960', 'id': '316ad972693d0355c3504729fff14287419e004d', 'symlink_target': '../all/fun1_to_proc_par2.ll'}, {'repo_name': 'np/ling', 'ref': 'refs/heads/master', 'path': 'tests/failure/wrong_order_par_seq_middle.t/wrong_order_par_seq_middle.ll', 'mode': '40960', 'id': 'daa40d563068ee94f01b1e87952d607a6588a589', 'symlink_target': '../../../fixtures/all/wrong_order_par_seq_middle.ll'}, {'repo_name': 'np/ling', 'ref': 'refs/heads/master', 'path': 'fixtures/strict-par-success/layout_case.ll', 'mode': '40960', 'id': '6bd679ec4ff94d8149986d49b8e789d1b4d6a44a', 'symlink_target': '../all/layout_case.ll'}, {'repo_name': 'np/ling', 'ref': 'refs/heads/master', 'path': 'fixtures/strict-par-success/merger_loli_Sort.ll', 'mode': '40960', 'id': '0cfcfb70b14958a8ba30cb83808c9bcc25516969', 'symlink_target': '../all/merger_loli_Sort.ll'}, {'repo_name': 'np/ling', 'ref': 'refs/heads/master', 'path': 'fixtures/failure/infer_recv.ll', 'mode': '40960', 'id': 'de516c994d6cc8b7bcc1fb6bf986699fced404f6', 'symlink_target': '../all/infer_recv.ll'}], 'var_function-call-11564613498295059514': [{'count(*)': '42605'}], 'var_function-call-437346317383943467': [{'id': 'a6fb31fa1e4b1647e8862580703add8c6205c6d1', 'cnt': '4'}, {'id': 'e94c45ffe619fbd39e7f5df78a590bd33893d64a', 'cnt': '2'}, {'id': 'a1615a71d1bdbb036d1dde0a94b8285fa8fca084', 'cnt': '2'}, {'id': '49f5eda9ac693bf61324ee7f65a15d704f7f3411', 'cnt': '2'}, {'id': '75c9123b0b91ca99402ed40efe80d21cb6bc3f90', 'cnt': '2'}, {'id': '0191f88060e6994e1095478da21798fd2c0a9dcb', 'cnt': '2'}, {'id': '6066caa5e76b60fbd0f7bc2a096c6fd7c023609f', 'cnt': '2'}, {'id': 'd1b6baa8d0bd3ac28e0765482e204e33340ccf8c', 'cnt': '2'}, {'id': 'd67714b2a25908fbc4e6b00531862cc62265bf75', 'cnt': '2'}, {'id': 'f64ee245678dcb26d658600708e2996a7608fc6e', 'cnt': '2'}], 'var_function-call-3672695489722118154': [], 'var_function-call-16610468603399776870': [{'id': 'b03a39b4e07f98073fcf2fbe945bf1291cbfeca7', 'sample_path': '5- Shared-CoreData/SharedKit/Record.swift', 'repo_data_description': 'With a file size of 290 bytes and sample mode 33188, this non-binary file is duplicated 8 times.'}, {'id': '3909cba31dd8c36766ee8efd9299c75a7e9f8721', 'sample_path': 'validation-test/compiler_crashers_fixed/27617-swift-markasobjc.swift', 'repo_data_description': 'A 277-byte non-binary file appearing 8 times, with sample mode code 33188.'}, {'id': 'f7a67dcc0bda7a58e7e1a37d483bfd06e5ff9208', 'sample_path': 'BusyNavigationBar/Example/AppDelegate.swift', 'repo_data_description': 'This file has a size of 2161 bytes, is non-binary, and appears 9 times with sample mode 33188.'}, {'id': '15492da9a0490415a84fa6c1a7957e473ebfa4db', 'sample_path': 'crashes-duplicates/25255-swift-typechecker-checkinheritanceclause.swift', 'repo_data_description': 'With a file size of 240 bytes and sample mode 33188, this non-binary file is duplicated 10 times.'}, {'id': '41d65e7ae98cc15b6e5eacfd11568e1a851b6add', 'sample_path': 'crashes-duplicates/26498-swift-sourcefile-lookupcache-lookupvalue.swift', 'repo_data_description': 'A 218-byte non-binary file appearing 10 times, with sample mode code 33188.'}, {'id': '117cee1262be7a8f9ffe72314c0395641169661d', 'sample_path': 'admob/AdMobExampleSwiftTests/AdMobExampleSwiftTests.swift', 'repo_data_description': 'A 1513-byte non-binary file appearing 12 times, with sample mode code 33188.'}, {'id': '679da520fd8ee30c041d816b15d74b14ec42ba75', 'sample_path': 'MLSwiftBasic/Classes/ProgressHUD/MLProgressHUD.swift', 'repo_data_description': 'The dataset includes this non-binary file, 6679 bytes in size and copied 12 times (mode: 33188).'}, {'id': '601d7b08677a1e95fcccea27fb1269c2110dc618', 'sample_path': 'crashes-duplicates/23648-swift-modulefile-maybereadpattern.swift', 'repo_data_description': 'This file has a size of 262 bytes, is non-binary, and appears 14 times with sample mode 33188.'}, {'id': '98e288822bccf1c37b259164d3d5caa5b8c9f33d', 'sample_path': 'crashes-duplicates/16041-swift-sourcemanager-getmessage.swift', 'repo_data_description': 'With a file size of 219 bytes and sample mode 33188, this non-binary file is duplicated 15 times.'}, {'id': 'cca8b7e8d35eccf1b5b46469b89d735b892dd316', 'sample_path': 'crashes-duplicates/07465-swift-printingdiagnosticconsumer-handlediagnostic.swift', 'repo_data_description': 'With a file size of 344 bytes and sample mode 33188, this non-binary file is duplicated 15 times.'}], 'var_function-call-15247824621466758386': [], 'var_function-call-7542092825191643099': [{'count_star()': '105'}], 'var_function-call-513243052492864742': 'file_storage/function-call-513243052492864742.json', 'var_function-call-513243052492863773': 'file_storage/function-call-513243052492863773.json', 'var_function-call-2421369311634029309': {'id': '6f4cdb70f044b0486a24a07403600cb964a02672', 'count': 38, 'repo': 'uacaps/PageMenu', 'path': 'Demos/Demo 4/PageMenuDemoTabbar/PageMenuDemoTabbar/ContactTableViewCell.swift'}}

exec(code, env_args)
