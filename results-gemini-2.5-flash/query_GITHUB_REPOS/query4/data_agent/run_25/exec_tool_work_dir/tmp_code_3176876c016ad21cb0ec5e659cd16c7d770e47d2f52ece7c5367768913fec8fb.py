code = """import json
import re

language_data = json.load(open(locals()['var_function-call-13215391144481791493'], 'r'))

non_python_repos = []

for entry in language_data:
    repo_name = entry["repo_name"]
    language_description = entry["language_description"]
    
    # Regex to extract language and bytes. It handles different phrasing and multiple languages.
    # It looks for patterns like "Language (bytes)" or "Language (bytes), Language (bytes)"
    # or "mainly written in Language (bytes), with additional code in Language (bytes)"
    
    matches = re.findall(r"([A-Za-z0-9+#]+)\s*\(([0-9,]+)\s*bytes\)", language_description)
    
    if not matches: # Try another pattern if the first one fails
        matches = re.findall(r"([A-Za-z0-9+#]+)\s*\(([0-9,]+)\s*bytes\)", language_description.split("The codebase includes:")[-1])
    
    if not matches: # Try another pattern if the second one fails
        matches = re.findall(r"([A-Za-z0-9+#]+)\s*\(([0-9,]+)\s*bytes\)", language_description.split("The majority of the code is in")[-1])
    
    if not matches: # Try another pattern if the third one fails
        matches = re.findall(r"([A-Za-z0-9+#]+)\s*\(([0-9,]+)\s*bytes\)", language_description.split("This repository is mainly written in")[-1])

    main_language = None
    max_bytes = -1

    for lang, bytes_str in matches:
        bytes_count = int(bytes_str.replace(",", ""))
        if bytes_count > max_bytes:
            max_bytes = bytes_count
            main_language = lang

    if main_language and main_language.lower() != "python":
        non_python_repos.append(repo_name)

print("__RESULT__:")
print(json.dumps(non_python_repos))"""

env_args = {'var_function-call-13215391144481791493': 'file_storage/function-call-13215391144481791493.json'}

exec(code, env_args)
