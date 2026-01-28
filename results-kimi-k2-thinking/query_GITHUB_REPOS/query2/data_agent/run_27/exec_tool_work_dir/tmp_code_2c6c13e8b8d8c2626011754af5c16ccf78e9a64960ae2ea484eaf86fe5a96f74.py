code = """import json
import re

# Read the Swift repositories from the file
swift_repos_file = locals()['var_functions.query_db:6']
swift_repos = []

if isinstance(swift_repos_file, str) and swift_repos_file.endswith('.json'):
    with open(swift_repos_file, 'r') as f:
        swift_repos = json.load(f)
else:
    swift_repos = swift_repos_file

print(f"Total Swift-related repositories: {len(swift_repos)}")

# Parse language descriptions to extract Swift bytes and confirm it's the main language
swift_repos_parsed = []
for repo in swift_repos:
    desc = repo['language_description']
    repo_name = repo['repo_name']
    
    # Extract Swift bytes using regex
    swift_match = re.search(r'Swift\s*\(\s*([\d,]+)\s*bytes\s*\)', desc)
    if swift_match:
        swift_bytes = int(swift_match.group(1).replace(',', ''))
        
        # Check if Swift is the main language (largest byte count)
        # Extract all language byte counts
        all_langs = re.findall(r'(\w+)\s*\(\s*([\d,]+)\s*bytes\s*\)', desc)
        max_bytes = 0
        is_main_lang = False
        
        for lang, bytes_str in all_langs:
            lang_bytes = int(bytes_str.replace(',', ''))
            if lang_bytes > max_bytes:
                max_bytes = lang_bytes
                is_main_lang = (lang == 'Swift')
        
        if is_main_lang:
            swift_repos_parsed.append({
                'repo_name': repo_name,
                'swift_bytes': swift_bytes,
                'language_description': desc
            })

print(f"Repositories where Swift is the main language: {len(swift_repos_parsed)}")
print(f"Sample repos: {[r['repo_name'] for r in swift_repos_parsed[:5]]}")

# Store the parsed repos for later use
result = {
    'swift_repo_count': len(swift_repos_parsed),
    'swift_repos': swift_repos_parsed[:10]  # Sample for verification
}

print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.query_db:0': [{'repo_name': 'e-Sixt/Swen', 'language_description': 'This repository is mainly written in Swift (16,364 bytes), with additional code in Ruby (7,243 bytes), Shell (94 bytes).'}, {'repo_name': 'ApplauseOSS/Swifjection', 'language_description': 'The codebase includes: Swift (109,540 bytes), Ruby (3,068 bytes), Shell (762 bytes).'}, {'repo_name': 'vizifit/GenericPasswordRow', 'language_description': 'The codebase includes: Swift (18,238 bytes), Ruby (716 bytes), Shell (211 bytes).'}, {'repo_name': 'cxy921126/SoftSwift', 'language_description': 'The majority of the code is in Swift (1,723,695 bytes), followed by Shell (17,716 bytes), Ruby (297 bytes).'}, {'repo_name': 'cwwise/CWWeChat', 'language_description': 'While most of the project is built in Swift (585,714 bytes), it also incorporates Ruby (3,447 bytes), Shell (190 bytes).'}], 'var_functions.list_db:2': ['commits', 'contents', 'files'], 'var_functions.query_db:6': 'file_storage/functions.query_db:6.json'}

exec(code, env_args)
