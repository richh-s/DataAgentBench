code = """import json
import re

contents_data = json.load(open(locals()['var_function-call-10962614403597425214']))

top_file = None
max_copies = -1

# Regex to extract copy count
# Examples:
# "seen 8 times"
# "duplicated 8 times"
# "appearing 8 times"
# "repeated 15 times"
# "copied 12 times"
regex = re.compile(r'(?:seen|duplicated|appearing|repeated|copied)\s+(\d+)\s+times')

for entry in contents_data:
    desc = entry['repo_data_description']
    match = regex.search(desc)
    if match:
        copies = int(match.group(1))
        if copies > max_copies:
            max_copies = copies
            top_file = entry
    else:
        # Fallback or log if needed, but assuming most follow the pattern
        pass

print("__RESULT__:")
print(json.dumps({"top_file_id": top_file['id'], "max_copies": max_copies, "sample_repo": top_file['sample_repo_name']}))"""

env_args = {'var_function-call-2393945165568935876': ['languages', 'repos', 'licenses'], 'var_function-call-2393945165568936765': ['commits', 'contents', 'files'], 'var_function-call-13436992224161459324': 'file_storage/function-call-13436992224161459324.json', 'var_function-call-13436992224161456667': [{'repo_name': 'juliandunn/rackspacecloud', 'language_description': 'The codebase includes: Ruby (22,438 bytes), Shell (465 bytes).'}, {'repo_name': 'xMarkusSpringerx/coloranalyzer', 'language_description': 'This repository is mainly written in Ruby (1,897 bytes), with additional code in Shell (115 bytes).'}, {'repo_name': 'michaellihs/gitlab', 'language_description': 'The codebase includes: Ruby (162,002 bytes), Shell (168 bytes).'}, {'repo_name': 'vyorkin/xftp', 'language_description': 'The majority of the code is in Ruby (25,709 bytes), followed by Shell (115 bytes).'}, {'repo_name': 'airatshigapov/drophunter', 'language_description': 'The majority of the code is in Ruby (4,198 bytes), followed by Shell (115 bytes).'}], 'var_function-call-11839730805232868770': 'file_storage/function-call-11839730805232868770.json', 'var_function-call-13175564607764114620': 'file_storage/function-call-13175564607764114620.json', 'var_function-call-10962614403597425214': 'file_storage/function-call-10962614403597425214.json'}

exec(code, env_args)
