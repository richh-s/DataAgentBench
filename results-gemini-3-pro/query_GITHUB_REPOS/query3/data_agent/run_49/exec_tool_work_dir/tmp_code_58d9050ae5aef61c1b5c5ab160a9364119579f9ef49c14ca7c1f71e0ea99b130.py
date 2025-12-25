code = """import json
import re

with open(locals()['var_function-call-13275413109263088104'], 'r') as f:
    shell_repos_data = json.load(f)

desc = shell_repos_data[0]['language_description']
print("__RESULT__:")
print(json.dumps({
    "desc": desc,
    "repr": repr(desc),
    "has_Shell": "Shell" in desc,
    "re_Shell": bool(re.search(r'Shell', desc)),
    "re_bShellb": bool(re.search(r'\bShell\b', desc)),
    "re_spaceShell": bool(re.search(r' Shell', desc))
}))"""

env_args = {'var_function-call-13275413109263088104': 'file_storage/function-call-13275413109263088104.json', 'var_function-call-13275413109263086351': 'file_storage/function-call-13275413109263086351.json', 'var_function-call-12889226768733389097': 'file_storage/function-call-12889226768733389097.json', 'var_function-call-14486139235551259839': 114972, 'var_function-call-1955957542433666088': [{'count_star()': '15016'}], 'var_function-call-3442467327927111626': 'file_storage/function-call-3442467327927111626.json', 'var_function-call-15496216609529752315': 1077, 'var_function-call-15000476436529302927': [{'language_description': 'While most of the project is built in C# (133,913 bytes), it also incorporates Java (22,737 bytes), ANTLR (21,320 bytes), PowerShell (905 bytes), Shell (58 bytes).'}, {'language_description': 'The codebase includes: C# (146,362 bytes), ANTLR (9,017 bytes), PowerShell (6,205 bytes).'}, {'language_description': 'The majority of the code is in Java (13,914,043 bytes), followed by HTML (2,676,449 bytes), ANTLR (1,483,189 bytes), VHDL (401,678 bytes), GAP (226,361 bytes), Objective-C (134,542 bytes), Assembly (134,524 bytes), JavaScript (104,216 bytes), C (103,168 bytes), Swift (83,207 bytes), PLpgSQL (35,862 bytes), SQLPL (31,877 bytes), C# (22,932 bytes), Pascal (13,808 bytes), PLSQL (8,695 bytes), Python (8,598 bytes), PHP (8,070 bytes), PowerShell (6,138 bytes), M (5,739 bytes), CSS (3,886 bytes), Shell (2,317 bytes), Erlang (2,303 bytes), CMake (1,930 bytes), Ruby (1,715 bytes), Visual Basic (1,564 bytes), TypeScript (1,174 bytes), Batchfile (491 bytes), Makefile (417 bytes), C++ (367 bytes), Lua (278 bytes), Awk (251 bytes), R (61 bytes), Matlab (23 bytes), Smalltalk (19 bytes).'}, {'language_description': 'While most of the project is built in C# (7,177,294 bytes), it also incorporates C (217,258 bytes), Visual Basic (164,462 bytes), Inno Setup (75,557 bytes), ANTLR (50,375 bytes), C++ (35,730 bytes), PowerShell (14,705 bytes), Batchfile (186 bytes).'}, {'language_description': 'The codebase includes: Java (5,768,297 bytes), C# (1,460,309 bytes), Python (1,410,962 bytes), JavaScript (443,990 bytes), GAP (110,837 bytes), ANTLR (72,606 bytes), C (9,558 bytes), PowerShell (6,138 bytes), Batchfile (139 bytes).'}], 'var_function-call-5610714206803632047': [{'COUNT(*)': '3325634'}], 'var_function-call-13964834016212180676': 0, 'var_function-call-16946634622781234878': {'len_shell_original': 659616, 'len_shell_strict': 0, 'len_apache': 495134, 'len_intersection': 0}, 'var_function-call-191082852464816019': [['The codebase includes: Ruby (22,438 bytes), Shell (465 bytes).', False], ['This repository is mainly written in Ruby (1,897 bytes), with additional code in Shell (115 bytes).', False], ['The codebase includes: Ruby (162,002 bytes), Shell (168 bytes).', False], ['The majority of the code is in Ruby (25,709 bytes), followed by Shell (115 bytes).', False], ['The majority of the code is in Ruby (4,198 bytes), followed by Shell (115 bytes).', False]]}

exec(code, env_args)
