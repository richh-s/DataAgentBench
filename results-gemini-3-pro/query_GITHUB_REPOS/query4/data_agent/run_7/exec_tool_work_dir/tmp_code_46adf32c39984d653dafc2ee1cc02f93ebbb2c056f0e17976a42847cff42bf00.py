code = """import json
import re

commits_data = locals()['var_function-call-15279119177356948517']
languages_file_path = locals()['var_function-call-15657998434769201345']
with open(languages_file_path, 'r') as f:
    languages_data = json.load(f)

lang_dict = {item['repo_name']: item['language_description'] for item in languages_data}

def get_main_language(description):
    if not description:
        return None
    matches = re.findall(r'([A-Za-z0-9\+\-\#\.\s]+)\s\(([0-9,]+)\sbytes\)', description)
    if not matches:
        return None
    lang_stats = []
    for lang_str, bytes_str in matches:
        # Simplistic parsing: take last word of the captured text before space
        # This works for "Ruby", "Shell", "C++", "C", "Objective-C", "Go", "Java", "JavaScript", "TypeScript", "Python"
        # Might fail for "Visual Basic" -> "Basic".
        
        # Clean the lang_str
        # It captures "The codebase includes: Ruby"
        # Split by space and take last word.
        words = lang_str.split()
        if not words: continue
        name = words[-1]
        
        # Correction for common multi-word languages if necessary?
        # In GitHub data, usually "Emacs Lisp", "Visual Basic".
        # But "Python" is single word.
        
        bytes_val = int(bytes_str.replace(',', ''))
        lang_stats.append((name, bytes_val))
    
    if not lang_stats:
        return None
        
    lang_stats.sort(key=lambda x: x[1], reverse=True)
    return lang_stats[0][0]

debug_info = {}
for repo_dict in commits_data:
    name = repo_dict['repo_name']
    desc = lang_dict.get(name, "No Desc")
    main_lang = get_main_language(desc)
    debug_info[name] = main_lang

print("__RESULT__:")
print(json.dumps(debug_info))"""

env_args = {'var_function-call-5286727036878620176': [{'repo_name': 'juliandunn/rackspacecloud', 'language_description': 'The codebase includes: Ruby (22,438 bytes), Shell (465 bytes).'}, {'repo_name': 'xMarkusSpringerx/coloranalyzer', 'language_description': 'This repository is mainly written in Ruby (1,897 bytes), with additional code in Shell (115 bytes).'}, {'repo_name': 'michaellihs/gitlab', 'language_description': 'The codebase includes: Ruby (162,002 bytes), Shell (168 bytes).'}, {'repo_name': 'vyorkin/xftp', 'language_description': 'The majority of the code is in Ruby (25,709 bytes), followed by Shell (115 bytes).'}, {'repo_name': 'airatshigapov/drophunter', 'language_description': 'The majority of the code is in Ruby (4,198 bytes), followed by Shell (115 bytes).'}], 'var_function-call-15279119177356948517': [{'repo_name': 'facebook/react', 'commit_count': '178'}, {'repo_name': 'tensorflow/tensorflow', 'commit_count': '156'}, {'repo_name': 'Microsoft/vscode', 'commit_count': '190'}, {'repo_name': 'apple/swift', 'commit_count': '1051'}, {'repo_name': 'twbs/bootstrap', 'commit_count': '340'}, {'repo_name': 'torvalds/linux', 'commit_count': '16061'}], 'var_function-call-15657998434769201345': 'file_storage/function-call-15657998434769201345.json', 'var_function-call-16388981185822219975': ['torvalds/linux', 'apple/swift', 'twbs/bootstrap', 'Microsoft/vscode', 'facebook/react']}

exec(code, env_args)
