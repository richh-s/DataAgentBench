code = """import json
import re

languages_data = json.load(open(locals()['var_function-call-11839730805232868770']))

swift_repos = []

for entry in languages_data:
    repo_name = entry['repo_name']
    desc = entry['language_description']
    
    # Extract languages and bytes
    # Pattern: "Language (bytes)" or "Language (bytes),"
    # But the text is natural language. e.g. "The codebase includes: Ruby (22,438 bytes), Shell (465 bytes)."
    # Regex to find all "Language (N bytes)"
    matches = re.findall(r'([A-Za-z]+) \(([\d,]+) bytes\)', desc)
    
    if not matches:
        continue
        
    stats = {}
    for lang, bytes_str in matches:
        bytes_val = int(bytes_str.replace(',', ''))
        stats[lang] = bytes_val
        
    # Check if Swift is the primary language
    if 'Swift' in stats:
        max_lang = max(stats, key=stats.get)
        if max_lang == 'Swift':
            swift_repos.append(repo_name)

print(f"Found {len(swift_repos)} Swift repositories.")
print("__RESULT__:")
print(json.dumps(swift_repos))"""

env_args = {'var_function-call-2393945165568935876': ['languages', 'repos', 'licenses'], 'var_function-call-2393945165568936765': ['commits', 'contents', 'files'], 'var_function-call-13436992224161459324': 'file_storage/function-call-13436992224161459324.json', 'var_function-call-13436992224161456667': [{'repo_name': 'juliandunn/rackspacecloud', 'language_description': 'The codebase includes: Ruby (22,438 bytes), Shell (465 bytes).'}, {'repo_name': 'xMarkusSpringerx/coloranalyzer', 'language_description': 'This repository is mainly written in Ruby (1,897 bytes), with additional code in Shell (115 bytes).'}, {'repo_name': 'michaellihs/gitlab', 'language_description': 'The codebase includes: Ruby (162,002 bytes), Shell (168 bytes).'}, {'repo_name': 'vyorkin/xftp', 'language_description': 'The majority of the code is in Ruby (25,709 bytes), followed by Shell (115 bytes).'}, {'repo_name': 'airatshigapov/drophunter', 'language_description': 'The majority of the code is in Ruby (4,198 bytes), followed by Shell (115 bytes).'}], 'var_function-call-11839730805232868770': 'file_storage/function-call-11839730805232868770.json'}

exec(code, env_args)
