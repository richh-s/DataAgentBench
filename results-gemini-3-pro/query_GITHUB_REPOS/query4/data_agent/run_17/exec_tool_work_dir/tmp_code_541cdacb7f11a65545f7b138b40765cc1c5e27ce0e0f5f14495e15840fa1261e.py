code = """import json
import re

commits_data = locals()['var_function-call-507962262134349788']
languages_file_path = locals()['var_function-call-507962262134348277']

with open(languages_file_path, 'r') as f:
    languages_data = json.load(f)

languages_map = {item['repo_name']: item['language_description'] for item in languages_data}

target_repos = [
    "apple/swift", 
    "twbs/bootstrap", 
    "Microsoft/vscode", 
    "facebook/react", 
    "tensorflow/tensorflow"
]

def parse_languages(description):
    # Regex to capture "Language (bytes)"
    # We will iterate over all matches
    matches = re.findall(r'([a-zA-Z0-9\+\#\.\-]+(?: [a-zA-Z0-9\+\#\.\-]+)*) \(([\d,]+) bytes\)', description)
    
    parsed = []
    for lang, bytes_str in matches:
        # Clean up language name
        # Remove common prefixes
        clean_lang = lang
        prefixes = [
            "The codebase includes:", 
            "This repository is mainly written in", 
            "The majority of the code is in", 
            "While most of the project is built in",
            "followed by", 
            "with additional code in", 
            "it also incorporates",
            "includes:"
        ]
        for p in prefixes:
            if p in clean_lang:
                clean_lang = clean_lang.replace(p, "")
        
        clean_lang = clean_lang.strip()
        # Remove leading comma if present (from previous split)
        if clean_lang.startswith(","):
            clean_lang = clean_lang[1:].strip()
            
        bytes_count = int(bytes_str.replace(',', ''))
        parsed.append((clean_lang, bytes_count))
        
    return parsed

results = {}
for name in target_repos:
    desc = languages_map.get(name)
    if desc:
        langs = parse_languages(desc)
        # Sort by bytes desc
        langs.sort(key=lambda x: x[1], reverse=True)
        main_lang = langs[0][0] if langs else None
        results[name] = {"main": main_lang, "all": langs, "raw": desc}
    else:
        results[name] = "NOT FOUND"

print("__RESULT__:")
print(json.dumps(results))"""

env_args = {'var_function-call-13619765481203691763': ['commits', 'contents', 'files'], 'var_function-call-13619765481203693066': ['languages', 'repos', 'licenses'], 'var_function-call-507962262134349788': [{'repo_name': 'torvalds/linux', 'commit_count': '16061'}, {'repo_name': 'apple/swift', 'commit_count': '1051'}, {'repo_name': 'twbs/bootstrap', 'commit_count': '340'}, {'repo_name': 'Microsoft/vscode', 'commit_count': '190'}, {'repo_name': 'facebook/react', 'commit_count': '178'}, {'repo_name': 'tensorflow/tensorflow', 'commit_count': '156'}], 'var_function-call-507962262134348277': 'file_storage/function-call-507962262134348277.json', 'var_function-call-7988308145770392283': ['apple/swift', 'twbs/bootstrap', 'Microsoft/vscode', 'facebook/react', 'tensorflow/tensorflow'], 'var_function-call-4083187669836648844': {'torvalds/linux': 'NOT FOUND', 'tensorflow/tensorflow': 'While most of the project is built in C++'}, 'var_function-call-13926318793127652167': [], 'var_function-call-8320602802895006229': 6}

exec(code, env_args)
