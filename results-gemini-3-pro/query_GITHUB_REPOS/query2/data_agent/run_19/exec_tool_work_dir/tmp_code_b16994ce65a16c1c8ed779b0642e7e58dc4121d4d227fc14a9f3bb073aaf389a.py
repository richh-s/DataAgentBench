code = """import json
import re

contents_data = json.load(open(locals()['var_function-call-10962614403597425214']))

top_file = None
max_copies = -1

# Regex to extract copy count
# Expanded keywords: seen, duplicated, appearing, appears, repeated, copied
# Also handle "duplicated X times" where X is int.
regex = re.compile(r'(?:seen|duplicated|appearing|appears|repeated|copied)\s+(\d+)\s+times')

for entry in contents_data:
    desc = entry['repo_data_description']
    match = regex.search(desc)
    if match:
        copies = int(match.group(1))
        if copies > max_copies:
            max_copies = copies
            top_file = entry

print("__RESULT__:")
print(json.dumps({"top_file_id": top_file['id'] if top_file else None, "max_copies": max_copies, "sample_repo": top_file['sample_repo_name'] if top_file else None}))"""

env_args = {'var_function-call-2393945165568935876': ['languages', 'repos', 'licenses'], 'var_function-call-2393945165568936765': ['commits', 'contents', 'files'], 'var_function-call-13436992224161459324': 'file_storage/function-call-13436992224161459324.json', 'var_function-call-13436992224161456667': [{'repo_name': 'juliandunn/rackspacecloud', 'language_description': 'The codebase includes: Ruby (22,438 bytes), Shell (465 bytes).'}, {'repo_name': 'xMarkusSpringerx/coloranalyzer', 'language_description': 'This repository is mainly written in Ruby (1,897 bytes), with additional code in Shell (115 bytes).'}, {'repo_name': 'michaellihs/gitlab', 'language_description': 'The codebase includes: Ruby (162,002 bytes), Shell (168 bytes).'}, {'repo_name': 'vyorkin/xftp', 'language_description': 'The majority of the code is in Ruby (25,709 bytes), followed by Shell (115 bytes).'}, {'repo_name': 'airatshigapov/drophunter', 'language_description': 'The majority of the code is in Ruby (4,198 bytes), followed by Shell (115 bytes).'}], 'var_function-call-11839730805232868770': 'file_storage/function-call-11839730805232868770.json', 'var_function-call-13175564607764114620': 'file_storage/function-call-13175564607764114620.json', 'var_function-call-10962614403597425214': 'file_storage/function-call-10962614403597425214.json', 'var_function-call-15512567175214681860': {'top_file_id': '6f4cdb70f044b0486a24a07403600cb964a02672', 'max_copies': 38, 'sample_repo': 'uacaps/PageMenu'}, 'var_function-call-7668030732099369117': [], 'var_function-call-1764687196318036265': [{'repo_name': 'np/ling', 'ref': 'refs/heads/master', 'path': 'fixtures/strict-par-success/fun1_to_proc_par2.ll', 'mode': '40960', 'id': '316ad972693d0355c3504729fff14287419e004d', 'symlink_target': '../all/fun1_to_proc_par2.ll'}, {'repo_name': 'np/ling', 'ref': 'refs/heads/master', 'path': 'tests/failure/wrong_order_par_seq_middle.t/wrong_order_par_seq_middle.ll', 'mode': '40960', 'id': 'daa40d563068ee94f01b1e87952d607a6588a589', 'symlink_target': '../../../fixtures/all/wrong_order_par_seq_middle.ll'}, {'repo_name': 'np/ling', 'ref': 'refs/heads/master', 'path': 'fixtures/strict-par-success/layout_case.ll', 'mode': '40960', 'id': '6bd679ec4ff94d8149986d49b8e789d1b4d6a44a', 'symlink_target': '../all/layout_case.ll'}, {'repo_name': 'np/ling', 'ref': 'refs/heads/master', 'path': 'fixtures/strict-par-success/merger_loli_Sort.ll', 'mode': '40960', 'id': '0cfcfb70b14958a8ba30cb83808c9bcc25516969', 'symlink_target': '../all/merger_loli_Sort.ll'}, {'repo_name': 'np/ling', 'ref': 'refs/heads/master', 'path': 'fixtures/failure/infer_recv.ll', 'mode': '40960', 'id': 'de516c994d6cc8b7bcc1fb6bf986699fced404f6', 'symlink_target': '../all/infer_recv.ll'}], 'var_function-call-1764687196318036888': [], 'var_function-call-14878134688874249732': [{'repo_name': 'uacaps/PageMenu', 'watch_count': '487'}], 'var_function-call-14878134688874246835': [], 'var_function-call-9725443235258778393': [{'repo_name': 'uacaps/PageMenu', 'language_description': 'The codebase includes: Swift (56,461 bytes), Objective-C (51,756 bytes), Ruby (5,999 bytes).'}], 'var_function-call-9725443235258780660': [{'repo_name': 'SRsim/simulator'}, {'repo_name': 'SamSaffron/pups'}, {'repo_name': 'Samsung/GearVRf'}, {'repo_name': 'ScyDev/reaction'}, {'repo_name': 'Sellegit/j2objc'}, {'repo_name': 'SkyLined/alpha3'}, {'repo_name': 'Stephane-D/SGDK'}, {'repo_name': 'TACC/tacc_stats'}, {'repo_name': 'TeaMeow/TocasUI'}, {'repo_name': 'Teradata/presto'}, {'repo_name': 'Thomas101/wmail'}, {'repo_name': 'TigerKid001/Owl'}, {'repo_name': 'Transitime/core'}, {'repo_name': 'a-palchikov/wmi'}, {'repo_name': 'aFarkas/webshim'}, {'repo_name': 'adonley/BitMesh'}, {'repo_name': 'akheron/jansson'}, {'repo_name': 'alvinhkh/buseta'}, {'repo_name': 'amplab/keystone'}, {'repo_name': 'andforce/iBeebo'}], 'var_function-call-17658025397188436335': []}

exec(code, env_args)
