code = """import json
import re

# Read the languages data from the file
lang_file = var_functions.query_db:0
with open(lang_file, 'r') as f:
    languages_data = json.load(f)

# Parse language descriptions to find the main language for each repo
repo_main_lang = {}

for item in languages_data:
    repo_name = item['repo_name']
    lang_desc = item['language_description']
    
    # Extract language-byte pairs using regex
    # Look for patterns like "Language (bytes)"
    lang_bytes = re.findall(r'(\w+)\s*\((\d+)\s*bytes?\)', lang_desc)
    
    if lang_bytes:
        # Convert to dict and find the language with max bytes
        lang_dict = {lang: int(bytes_count) for lang, bytes_count in lang_bytes}
        main_lang = max(lang_dict, key=lang_dict.get)
        repo_main_lang[repo_name] = main_lang
    else:
        # If no pattern matches, skip
        continue

# Count repos by main language for debugging
lang_counts = {}
for lang in repo_main_lang.values():
    lang_counts[lang] = lang_counts.get(lang, 0) + 1

print('__RESULT__:')
print(json.dumps({
    'total_repos': len(repo_main_lang),
    'language_counts': lang_counts,
    'sample_repos': list(repo_main_lang.items())[:10]
}))"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json'}

exec(code, env_args)
