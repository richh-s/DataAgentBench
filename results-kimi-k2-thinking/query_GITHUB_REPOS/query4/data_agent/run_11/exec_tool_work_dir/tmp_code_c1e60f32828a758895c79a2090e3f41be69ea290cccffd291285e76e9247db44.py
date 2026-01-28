code = """import json

# Read the full result from the file
result_file = var_functions.query_db_0
with open(result_file, 'r') as f:
    languages_data = json.load(f)

# Filter repositories whose main language is NOT Python
non_python_repos = []
for item in languages_data:
    repo_name = item['repo_name']
    language_description = item['language_description']
    
    # Check if Python is the main language
    # The description format is typically "The codebase includes: Python (X bytes), Other (Y bytes)"
    # or "This repository is mainly written in Python (X bytes), with additional code in Other (Y bytes)."
    if 'Python' not in language_description:
        non_python_repos.append(repo_name)
    else:
        # Extract the main language by looking for the language with highest bytes
        # This is a bit tricky with the natural language format
        # We'll check if Python appears first with the highest byte count
        import re
        
        # Find all language-byte pairs
        pattern = r'(\w+)\s*\((\d+)\s+bytes\)'
        matches = re.findall(pattern, language_description)
        
        if matches:
            # Find the language with max bytes
            max_lang = max(matches, key=lambda x: int(x[1]))[0]
            if max_lang != 'Python':
                non_python_repos.append(repo_name)
        else:
            # If we can't parse, check if Python is mentioned as "mainly written in"
            if "mainly written in Python" not in language_description:
                non_python_repos.append(repo_name)

print("__RESULT__:")
print(json.dumps(non_python_repos[:100]))  # Print first 100 for debugging"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json'}

exec(code, env_args)
