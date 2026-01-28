code = """import json
import re
from collections import defaultdict

# Load languages data
if isinstance(var_functions.query_db:6, str):
    with open(var_functions.query_db:6, 'r') as f:
        languages_data = json.load(f)
else:
    languages_data = var_functions.query_db:6

# Load commits data
if isinstance(var_functions.query_db:9, str):
    with open(var_functions.query_db:9, 'r') as f:
        commits_data = json.load(f)
else:
    commits_data = var_functions.query_db:9

print(f"Total language records: {len(languages_data)}")
print(f"Total commit records: {len(commits_data)}")
print(f"Sample language record: {languages_data[0] if languages_data else 'None'}")
print(f"Sample commit record: {commits_data[0] if commits_data else 'None'}")

# Parse main language from language_description
def extract_main_language(lang_desc):
    """Extract the main language and its bytes from language_description"""
    if not lang_desc:
        return None, 0
    
    # Pattern to match language names and byte counts
    pattern = r'([A-Za-z\+#]+)\s*\((\d+(?:,\d+)*)\s*bytes\)'
    matches = re.findall(pattern, lang_desc)
    
    if not matches:
        return None, 0
    
    # Convert bytes to integers and find the language with max bytes
    max_bytes = 0
    main_lang = None
    
    for lang, bytes_str in matches:
        try:
            bytes_val = int(bytes_str.replace(',', ''))
            if bytes_val > max_bytes:
                max_bytes = bytes_val
                main_lang = lang
        except:
            continue
    
    return main_lang, max_bytes

# Test parsing on sample data
sample_langs = [
    "The codebase includes: Ruby (22,438 bytes), Shell (465 bytes).",
    "This repository is mainly written in Ruby (1,897 bytes), with additional code in Shell (115 bytes).",
    "The majority of the code is in Ruby (25,709 bytes), followed by Shell (115 bytes).",
    "The majority of the code is in Shell (3,715 bytes), followed by Ruby (931 bytes)."
]

for desc in sample_langs:
    lang, bytes_val = extract_main_language(desc)
    print(f"Description: {desc}")
    print(f"Main language: {lang}, Bytes: {bytes_val}")
    print("---")

print("__RESULT__:")
print(json.dumps({"status": "parsing_test_complete"}))"""

env_args = {'var_functions.list_db:0': ['languages', 'repos', 'licenses'], 'var_functions.query_db:2': [{'repo_name': 'juliandunn/rackspacecloud', 'language_description': 'The codebase includes: Ruby (22,438 bytes), Shell (465 bytes).'}, {'repo_name': 'xMarkusSpringerx/coloranalyzer', 'language_description': 'This repository is mainly written in Ruby (1,897 bytes), with additional code in Shell (115 bytes).'}, {'repo_name': 'michaellihs/gitlab', 'language_description': 'The codebase includes: Ruby (162,002 bytes), Shell (168 bytes).'}, {'repo_name': 'vyorkin/xftp', 'language_description': 'The majority of the code is in Ruby (25,709 bytes), followed by Shell (115 bytes).'}, {'repo_name': 'airatshigapov/drophunter', 'language_description': 'The majority of the code is in Ruby (4,198 bytes), followed by Shell (115 bytes).'}], 'var_functions.list_db:4': ['commits', 'contents', 'files'], 'var_functions.query_db:6': 'file_storage/functions.query_db:6.json', 'var_functions.query_db:9': 'file_storage/functions.query_db:9.json'}

exec(code, env_args)
