code = """import json
import re

# Load metadata results (repos with Shell and Apache-2.0)
with open(locals()['var_function-call-4548573233453338920'], 'r') as f:
    repo_data = json.load(f)

# Filter for Shell (specifically "Shell", not "PowerShell")
valid_repos = set()
# Regex to match "Shell" as a whole word
# Since we are looking for "Shell" language usage, and the format is typically "Shell (bytes)"
# we can look for "Shell" where it is not preceded by a letter.
# Actually, the format is strict enough in the samples.
# Just ensuring it's not "PowerShell".
for entry in repo_data:
    desc = entry.get('language_description', '')
    # Check if "Shell" is present as a whole word.
    # \bShell\b matches "Shell" in "Shell (123)" but not "PowerShell"
    if re.search(r'\bShell\b', desc):
        valid_repos.add(entry['repo_name'])

# Load commits results (commits matching message criteria)
with open(locals()['var_function-call-5326938115670771413'], 'r') as f:
    commits_data = json.load(f)

# Count commits that belong to valid repos
count = 0
for commit in commits_data:
    if commit['repo_name'] in valid_repos:
        count += 1

print("__RESULT__:")
print(count)"""

env_args = {'var_function-call-12666756499218807487': [{'repo_name': 'juliandunn/rackspacecloud', 'language_description': 'The codebase includes: Ruby (22,438 bytes), Shell (465 bytes).'}, {'repo_name': 'xMarkusSpringerx/coloranalyzer', 'language_description': 'This repository is mainly written in Ruby (1,897 bytes), with additional code in Shell (115 bytes).'}, {'repo_name': 'michaellihs/gitlab', 'language_description': 'The codebase includes: Ruby (162,002 bytes), Shell (168 bytes).'}, {'repo_name': 'vyorkin/xftp', 'language_description': 'The majority of the code is in Ruby (25,709 bytes), followed by Shell (115 bytes).'}, {'repo_name': 'airatshigapov/drophunter', 'language_description': 'The majority of the code is in Ruby (4,198 bytes), followed by Shell (115 bytes).'}], 'var_function-call-6198626166745145075': [{'repo_name': 'benstreb/os-test-harness', 'license': 'isc'}, {'repo_name': 'hanklords/sftpd', 'license': 'isc'}, {'repo_name': 'ivoreis/trine', 'license': 'isc'}, {'repo_name': 'dega37/VIRL2', 'license': 'isc'}, {'repo_name': 'mcgrof/compat-user', 'license': 'isc'}], 'var_function-call-8952076935394127844': [{'COUNT(*)': '114972'}], 'var_function-call-5999132861061876696': [{'count_star()': '17976'}], 'var_function-call-14076290995272721153': [{'language_description': 'While most of the project is built in C# (133,913 bytes), it also incorporates Java (22,737 bytes), ANTLR (21,320 bytes), PowerShell (905 bytes), Shell (58 bytes).'}, {'language_description': 'The codebase includes: C# (146,362 bytes), ANTLR (9,017 bytes), PowerShell (6,205 bytes).'}, {'language_description': 'The majority of the code is in Java (13,914,043 bytes), followed by HTML (2,676,449 bytes), ANTLR (1,483,189 bytes), VHDL (401,678 bytes), GAP (226,361 bytes), Objective-C (134,542 bytes), Assembly (134,524 bytes), JavaScript (104,216 bytes), C (103,168 bytes), Swift (83,207 bytes), PLpgSQL (35,862 bytes), SQLPL (31,877 bytes), C# (22,932 bytes), Pascal (13,808 bytes), PLSQL (8,695 bytes), Python (8,598 bytes), PHP (8,070 bytes), PowerShell (6,138 bytes), M (5,739 bytes), CSS (3,886 bytes), Shell (2,317 bytes), Erlang (2,303 bytes), CMake (1,930 bytes), Ruby (1,715 bytes), Visual Basic (1,564 bytes), TypeScript (1,174 bytes), Batchfile (491 bytes), Makefile (417 bytes), C++ (367 bytes), Lua (278 bytes), Awk (251 bytes), R (61 bytes), Matlab (23 bytes), Smalltalk (19 bytes).'}, {'language_description': 'While most of the project is built in C# (7,177,294 bytes), it also incorporates C (217,258 bytes), Visual Basic (164,462 bytes), Inno Setup (75,557 bytes), ANTLR (50,375 bytes), C++ (35,730 bytes), PowerShell (14,705 bytes), Batchfile (186 bytes).'}, {'language_description': 'The codebase includes: Java (5,768,297 bytes), C# (1,460,309 bytes), Python (1,410,962 bytes), JavaScript (443,990 bytes), GAP (110,837 bytes), ANTLR (72,606 bytes), C (9,558 bytes), PowerShell (6,138 bytes), Batchfile (139 bytes).'}], 'var_function-call-4548573233453338920': 'file_storage/function-call-4548573233453338920.json', 'var_function-call-5326938115670771413': 'file_storage/function-call-5326938115670771413.json'}

exec(code, env_args)
