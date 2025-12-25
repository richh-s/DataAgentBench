code = """import json
import re

file_path = locals()['var_function-call-16194117252138062191']
with open(file_path, 'r') as f:
    repos = json.load(f)

valid_repos = []
debug_info = []

# Regex test
pattern = r'(?:^|[^a-zA-Z0-9])Shell(?:$|[^a-zA-Z0-9])'

count = 0
for r in repos:
    desc = r['language_description']
    if re.search(pattern, desc):
        valid_repos.append(r['repo_name'])
        if count < 5:
            debug_info.append(f"MATCH: {desc}")
    else:
        if count < 5:
            debug_info.append(f"NO MATCH: {repr(desc)}")
    count += 1

result = {
    "total_input": len(repos),
    "filtered_count": len(valid_repos),
    "debug_samples": debug_info,
    "valid_repos_preview": valid_repos[:10]
}

print("__RESULT__:")
print(json.dumps(result))"""

env_args = {'var_function-call-6809914395948221963': [{'repo_name': 'juliandunn/rackspacecloud', 'language_description': 'The codebase includes: Ruby (22,438 bytes), Shell (465 bytes).'}, {'repo_name': 'xMarkusSpringerx/coloranalyzer', 'language_description': 'This repository is mainly written in Ruby (1,897 bytes), with additional code in Shell (115 bytes).'}, {'repo_name': 'michaellihs/gitlab', 'language_description': 'The codebase includes: Ruby (162,002 bytes), Shell (168 bytes).'}, {'repo_name': 'vyorkin/xftp', 'language_description': 'The majority of the code is in Ruby (25,709 bytes), followed by Shell (115 bytes).'}, {'repo_name': 'airatshigapov/drophunter', 'language_description': 'The majority of the code is in Ruby (4,198 bytes), followed by Shell (115 bytes).'}], 'var_function-call-6809914395948221246': [{'repo_name': 'benstreb/os-test-harness', 'license': 'isc'}, {'repo_name': 'hanklords/sftpd', 'license': 'isc'}, {'repo_name': 'ivoreis/trine', 'license': 'isc'}, {'repo_name': 'dega37/VIRL2', 'license': 'isc'}, {'repo_name': 'mcgrof/compat-user', 'license': 'isc'}], 'var_function-call-11773527770620018970': [{'COUNT(*)': '3325634'}], 'var_function-call-11773527770620019115': [{'COUNT(*)': '3325634'}], 'var_function-call-11773527770620019260': [{'license': 'apache-2.0'}], 'var_function-call-7383299967845310022': [{'COUNT(*)': '112656'}], 'var_function-call-7383299967845308495': [{'language_description': 'Nearly all of the code is in Shell, totaling 100,389 bytes.'}, {'language_description': 'Nearly all of the code is in Shell, totaling 2,381 bytes.'}, {'language_description': 'Nearly all of the code is in Shell, totaling 1,079 bytes.'}, {'language_description': 'Nearly all of the code is in Shell, totaling 946 bytes.'}, {'language_description': 'Nearly all of the code is in Shell, totaling 5,370 bytes.'}, {'language_description': 'Nearly all of the code is in Shell, totaling 30,437 bytes.'}, {'language_description': 'Nearly all of the code is in Shell, totaling 6,690 bytes.'}, {'language_description': 'Nearly all of the code is in Shell, totaling 8,224 bytes.'}, {'language_description': 'Nearly all of the code is in Shell, totaling 19,499 bytes.'}, {'language_description': 'Nearly all of the code is in Shell, totaling 2,627 bytes.'}], 'var_function-call-17570289864634806236': [{'language_description': 'While most of the project is built in C# (133,913 bytes), it also incorporates Java (22,737 bytes), ANTLR (21,320 bytes), PowerShell (905 bytes), Shell (58 bytes).'}, {'language_description': 'The codebase includes: C# (146,362 bytes), ANTLR (9,017 bytes), PowerShell (6,205 bytes).'}, {'language_description': 'The majority of the code is in Java (13,914,043 bytes), followed by HTML (2,676,449 bytes), ANTLR (1,483,189 bytes), VHDL (401,678 bytes), GAP (226,361 bytes), Objective-C (134,542 bytes), Assembly (134,524 bytes), JavaScript (104,216 bytes), C (103,168 bytes), Swift (83,207 bytes), PLpgSQL (35,862 bytes), SQLPL (31,877 bytes), C# (22,932 bytes), Pascal (13,808 bytes), PLSQL (8,695 bytes), Python (8,598 bytes), PHP (8,070 bytes), PowerShell (6,138 bytes), M (5,739 bytes), CSS (3,886 bytes), Shell (2,317 bytes), Erlang (2,303 bytes), CMake (1,930 bytes), Ruby (1,715 bytes), Visual Basic (1,564 bytes), TypeScript (1,174 bytes), Batchfile (491 bytes), Makefile (417 bytes), C++ (367 bytes), Lua (278 bytes), Awk (251 bytes), R (61 bytes), Matlab (23 bytes), Smalltalk (19 bytes).'}, {'language_description': 'While most of the project is built in C# (7,177,294 bytes), it also incorporates C (217,258 bytes), Visual Basic (164,462 bytes), Inno Setup (75,557 bytes), ANTLR (50,375 bytes), C++ (35,730 bytes), PowerShell (14,705 bytes), Batchfile (186 bytes).'}, {'language_description': 'The codebase includes: Java (5,768,297 bytes), C# (1,460,309 bytes), Python (1,410,962 bytes), JavaScript (443,990 bytes), GAP (110,837 bytes), ANTLR (72,606 bytes), C (9,558 bytes), PowerShell (6,138 bytes), Batchfile (139 bytes).'}], 'var_function-call-4977993716473716283': [{'COUNT(*)': '495134'}], 'var_function-call-16194117252138062191': 'file_storage/function-call-16194117252138062191.json', 'var_function-call-6490343147593444872': [], 'var_function-call-1761513205434522544': {'total_input': 114972, 'filtered_count': 0, 'debug_samples': ['NO MATCH: The majority of the code is in Java (137,502 bytes), followed by HTML (2,371 bytes), JavaScript (2,187 bytes), Shell (755 bytes).', 'NO MATCH: The codebase includes: C# (425,267 bytes), PowerShell (2,088 bytes), ApacheConf (1,276 bytes).', 'NO MATCH: While most of the project is built in Java (31,960 bytes), it also incorporates Shell (99 bytes).', 'NO MATCH: While most of the project is built in Java (65,290 bytes), it also incorporates Shell (1,232 bytes).', 'NO MATCH: This repository is mainly written in Shell (3,622 bytes).'], 'valid_repos': []}}

exec(code, env_args)
