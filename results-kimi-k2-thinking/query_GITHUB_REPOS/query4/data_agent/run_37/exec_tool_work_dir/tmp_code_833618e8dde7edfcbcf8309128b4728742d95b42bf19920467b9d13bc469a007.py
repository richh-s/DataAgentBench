code = """import json
import re
from collections import defaultdict

# Load the languages data
languages_file = var_functions.query_db:4
with open(languages_file, 'r') as f:
    languages_data = json.load(f)

# Load the commits data
commits_file = var_functions.query_db:6
with open(commits_file, 'r') as f:
    commits_data = json.load(f)

# Function to extract main language from description
def get_main_language(description):
    # Look for patterns like "Ruby (22,438 bytes)" or "C++ (1000 bytes)"
    # The language with the highest byte count is the main language
    matches = re.findall(r'([A-Za-z+#]+)\s*\(([\d,]+)\s*bytes?\)', description)
    
    if not matches:
        return None
    
    # Convert to list of (language, bytes) tuples
    languages = []
    for lang, bytes_str in matches:
        # Remove commas and convert to int
        try:
            bytes_count = int(bytes_str.replace(',', ''))
            languages.append((lang, bytes_count))
        except ValueError:
            continue
    
    # Sort by byte count descending
    languages.sort(key=lambda x: x[1], reverse=True)
    
    return languages[0][0] if languages else None

# Filter repositories where main language is NOT Python
non_python_repos = set()
for item in languages_data:
    repo_name = item['repo_name']
    description = item['language_description']
    
    main_lang = get_main_language(description)
    if main_lang and main_lang.lower() != 'python':
        non_python_repos.add(repo_name)

# Count commits per repository from commits data
commit_counts = defaultdict(int)
for item in commits_data:
    repo_name = item['repo_name']
    if repo_name in non_python_repos:
        commit_counts[repo_name] += 1

# Sort repositories by commit count descending and get top 5
sorted_repos = sorted(commit_counts.items(), key=lambda x: x[1], reverse=True)
top_5_repos = sorted_repos[:5]

# Extract just the repository names
result = [repo for repo, count in top_5_repos]

print("__RESULT__:")
print(json.dumps(result))"""

env_args = {'var_functions.query_db:0': [{'repo_name': 'juliandunn/rackspacecloud', 'language_description': 'The codebase includes: Ruby (22,438 bytes), Shell (465 bytes).'}, {'repo_name': 'xMarkusSpringerx/coloranalyzer', 'language_description': 'This repository is mainly written in Ruby (1,897 bytes), with additional code in Shell (115 bytes).'}, {'repo_name': 'michaellihs/gitlab', 'language_description': 'The codebase includes: Ruby (162,002 bytes), Shell (168 bytes).'}, {'repo_name': 'vyorkin/xftp', 'language_description': 'The majority of the code is in Ruby (25,709 bytes), followed by Shell (115 bytes).'}, {'repo_name': 'airatshigapov/drophunter', 'language_description': 'The majority of the code is in Ruby (4,198 bytes), followed by Shell (115 bytes).'}, {'repo_name': 'tombruijn/chef-ruby-install', 'language_description': 'While most of the project is built in Ruby (10,174 bytes), it also incorporates Shell (716 bytes).'}, {'repo_name': 'SenseTecnic/stsplatform-lib-ruby', 'language_description': 'While most of the project is built in Ruby (17,195 bytes), it also incorporates Shell (115 bytes).'}, {'repo_name': 'procore/site-reliability-scripts', 'language_description': 'The majority of the code is in Ruby (12,891 bytes), followed by Shell (2,343 bytes).'}, {'repo_name': 'tibastral/web_motion', 'language_description': 'The majority of the code is in Ruby (5,324 bytes), followed by Shell (115 bytes).'}, {'repo_name': 'Haegin/stately', 'language_description': 'The codebase includes: Ruby (8,171 bytes), Shell (131 bytes).'}], 'var_functions.query_db:2': [{'repo_name': 'torvalds/linux', 'commit': '78e3f1f01d23c1a0d5828669d35afa2e7951987d'}, {'repo_name': 'torvalds/linux', 'commit': '4a4e07c1bdbbc24d905e4c266b92cada9371db5d'}, {'repo_name': 'torvalds/linux', 'commit': 'afe1bb73f8ed588ab6268c27c5a447fe0484e48f'}, {'repo_name': 'torvalds/linux', 'commit': 'b7ac233515c6263d6cb471d9e0f57bdd7ea36894'}, {'repo_name': 'torvalds/linux', 'commit': '71c11c378f46e42ca67c1e227646ce23bf43a8c6'}, {'repo_name': 'torvalds/linux', 'commit': '76cdd58e558669366adfaded436fda01b30cce3e'}, {'repo_name': 'torvalds/linux', 'commit': '2565409fc0303f3ab8d66b8326702a687962a29b'}, {'repo_name': 'torvalds/linux', 'commit': '7779d7bed950a7fb1af4f540c2f82a6b81b65901'}, {'repo_name': 'torvalds/linux', 'commit': '3443ad095fc330ace0ef23bf965354a56298bf58'}, {'repo_name': 'torvalds/linux', 'commit': '42e41c54d61e32e8a349943607daa53205324d7f'}], 'var_functions.query_db:4': 'file_storage/functions.query_db:4.json', 'var_functions.query_db:6': 'file_storage/functions.query_db:6.json'}

exec(code, env_args)
