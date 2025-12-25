code = """import json
import re

# Load repos with descriptions
with open(locals()['var_function-call-14802464829231452440'], 'r') as f:
    repos_data = json.load(f)

# Filter for explicit "Shell"
valid_repos_set = set()
pattern = re.compile(r'\bShell\b')

for r in repos_data:
    if pattern.search(r['language_description']):
        valid_repos_set.add(r['repo_name'])

print(f"Total repos after strict Shell check: {len(valid_repos_set)}")

# Load commits data
with open(locals()['var_function-call-11876841047574768394'], 'r') as f:
    commits_data = json.load(f)

# Count matching commits
count = 0
for c in commits_data:
    if c['repo_name'] in valid_repos_set:
        count += 1

print("__RESULT__:")
print(count)"""

env_args = {'var_function-call-17537969500786155242': ['languages', 'repos', 'licenses'], 'var_function-call-8644759848828647209': [{'repo_name': 'juliandunn/rackspacecloud', 'language_description': 'The codebase includes: Ruby (22,438 bytes), Shell (465 bytes).'}, {'repo_name': 'xMarkusSpringerx/coloranalyzer', 'language_description': 'This repository is mainly written in Ruby (1,897 bytes), with additional code in Shell (115 bytes).'}, {'repo_name': 'michaellihs/gitlab', 'language_description': 'The codebase includes: Ruby (162,002 bytes), Shell (168 bytes).'}, {'repo_name': 'vyorkin/xftp', 'language_description': 'The majority of the code is in Ruby (25,709 bytes), followed by Shell (115 bytes).'}, {'repo_name': 'airatshigapov/drophunter', 'language_description': 'The majority of the code is in Ruby (4,198 bytes), followed by Shell (115 bytes).'}], 'var_function-call-2812382068649453778': [{'repo_name': 'benstreb/os-test-harness', 'license': 'isc'}, {'repo_name': 'hanklords/sftpd', 'license': 'isc'}, {'repo_name': 'ivoreis/trine', 'license': 'isc'}, {'repo_name': 'dega37/VIRL2', 'license': 'isc'}, {'repo_name': 'mcgrof/compat-user', 'license': 'isc'}], 'var_function-call-12620747423359288603': 'file_storage/function-call-12620747423359288603.json', 'var_function-call-7792020106097816291': 'file_storage/function-call-7792020106097816291.json', 'var_function-call-12633256304448615475': 114972, 'var_function-call-13634301978280679600': [{'count_star()': '17976'}], 'var_function-call-11876841047574768394': 'file_storage/function-call-11876841047574768394.json', 'var_function-call-7017832902310679063': 1077, 'var_function-call-13689173762122494810': [{'language_description': 'While most of the project is built in C# (133,913 bytes), it also incorporates Java (22,737 bytes), ANTLR (21,320 bytes), PowerShell (905 bytes), Shell (58 bytes).'}, {'language_description': 'The codebase includes: C# (146,362 bytes), ANTLR (9,017 bytes), PowerShell (6,205 bytes).'}, {'language_description': 'The majority of the code is in Java (13,914,043 bytes), followed by HTML (2,676,449 bytes), ANTLR (1,483,189 bytes), VHDL (401,678 bytes), GAP (226,361 bytes), Objective-C (134,542 bytes), Assembly (134,524 bytes), JavaScript (104,216 bytes), C (103,168 bytes), Swift (83,207 bytes), PLpgSQL (35,862 bytes), SQLPL (31,877 bytes), C# (22,932 bytes), Pascal (13,808 bytes), PLSQL (8,695 bytes), Python (8,598 bytes), PHP (8,070 bytes), PowerShell (6,138 bytes), M (5,739 bytes), CSS (3,886 bytes), Shell (2,317 bytes), Erlang (2,303 bytes), CMake (1,930 bytes), Ruby (1,715 bytes), Visual Basic (1,564 bytes), TypeScript (1,174 bytes), Batchfile (491 bytes), Makefile (417 bytes), C++ (367 bytes), Lua (278 bytes), Awk (251 bytes), R (61 bytes), Matlab (23 bytes), Smalltalk (19 bytes).'}, {'language_description': 'While most of the project is built in C# (7,177,294 bytes), it also incorporates C (217,258 bytes), Visual Basic (164,462 bytes), Inno Setup (75,557 bytes), ANTLR (50,375 bytes), C++ (35,730 bytes), PowerShell (14,705 bytes), Batchfile (186 bytes).'}, {'language_description': 'The codebase includes: Java (5,768,297 bytes), C# (1,460,309 bytes), Python (1,410,962 bytes), JavaScript (443,990 bytes), GAP (110,837 bytes), ANTLR (72,606 bytes), C (9,558 bytes), PowerShell (6,138 bytes), Batchfile (139 bytes).'}], 'var_function-call-14802464829231452440': 'file_storage/function-call-14802464829231452440.json'}

exec(code, env_args)
