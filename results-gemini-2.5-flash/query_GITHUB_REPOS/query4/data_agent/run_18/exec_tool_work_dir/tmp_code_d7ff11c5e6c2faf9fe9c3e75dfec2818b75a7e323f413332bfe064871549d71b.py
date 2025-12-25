code = """import pandas as pd
import re
import json

def parse_language_description(description):
    if not description:
        return None
    
    # Split by comma or "with additional code in" or "and" for multiple language entries
    entries = re.split(r", | with additional code in | and ", description)
    
    main_language = None
    max_bytes = -1

    for entry in entries:
        # Clean up the entry string
        entry = entry.replace("The codebase includes: ", "").replace("This repository is mainly written in ", "").replace("While most of the project is built in ", "").replace("The majority of the code is in ", "").strip()
        
        # Extract language and bytes using regex
        match = re.search(r"([a-zA-Z0-9+#-]+) \((\d{1,3}(?:,\d{3})*|\d+) bytes\)", entry)
        if match:
            language = match.group(1)
            bytes_str = match.group(2).replace(",", "")
            bytes_value = int(bytes_str)
            
            if bytes_value > max_bytes:
                max_bytes = bytes_value
                main_language = language
    return main_language

# Load the language data from the file
with open(locals()['var_function-call-11757029296570613446'], 'r') as f:
    language_data = json.load(f)


df_languages = pd.DataFrame(language_data)
df_languages['main_language'] = df_languages['language_description'].apply(parse_language_description)


non_python_repos = df_languages[df_languages['main_language'] != 'Python']['repo_name'].tolist()

print("__RESULT__:")
print(json.dumps(non_python_repos))"""

env_args = {'var_function-call-2408604976084049323': [{'language_description': 'The codebase includes: Ruby (22,438 bytes), Shell (465 bytes).'}, {'language_description': 'This repository is mainly written in Ruby (1,897 bytes), with additional code in Shell (115 bytes).'}, {'language_description': 'The codebase includes: Ruby (162,002 bytes), Shell (168 bytes).'}, {'language_description': 'The majority of the code is in Ruby (25,709 bytes), followed by Shell (115 bytes).'}, {'language_description': 'The majority of the code is in Ruby (4,198 bytes), followed by Shell (115 bytes).'}, {'language_description': 'While most of the project is built in Ruby (10,174 bytes), it also incorporates Shell (716 bytes).'}, {'language_description': 'While most of the project is built in Ruby (17,195 bytes), it also incorporates Shell (115 bytes).'}, {'language_description': 'The majority of the code is in Ruby (12,891 bytes), followed by Shell (2,343 bytes).'}, {'language_description': 'The majority of the code is in Ruby (5,324 bytes), followed by Shell (115 bytes).'}, {'language_description': 'The codebase includes: Ruby (8,171 bytes), Shell (131 bytes).'}], 'var_function-call-11757029296570613446': 'file_storage/function-call-11757029296570613446.json'}

exec(code, env_args)
