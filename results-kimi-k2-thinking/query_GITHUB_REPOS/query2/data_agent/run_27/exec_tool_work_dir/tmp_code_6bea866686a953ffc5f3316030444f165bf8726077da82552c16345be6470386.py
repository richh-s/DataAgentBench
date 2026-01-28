code = """# Let's explore the data structure
import json

# First, let's see what the language_description looks like for Swift repos
swift_repos = locals().get('var_functions.query_db:0', [])
print(f"Number of Swift repos in sample: {len(swift_repos)}")
for repo in swift_repos[:3]:
    print(f"Repo: {repo['repo_name']}")
    print(f"Language desc: {repo['language_description']}")
    print("---")

# Let's check if the result is a full list or a file path
if isinstance(swift_repos, str) and swift_repos.endswith('.json'):
    with open(swift_repos, 'r') as f:
        swift_repos = json.load(f)
    print(f"Loaded {len(swift_repos)} Swift repos from file")

# Get all Swift repositories from metadata_database
# We need to parse language_description to confirm Swift is the main language
print("Getting all repositories...")"""

env_args = {'var_functions.query_db:0': [{'repo_name': 'e-Sixt/Swen', 'language_description': 'This repository is mainly written in Swift (16,364 bytes), with additional code in Ruby (7,243 bytes), Shell (94 bytes).'}, {'repo_name': 'ApplauseOSS/Swifjection', 'language_description': 'The codebase includes: Swift (109,540 bytes), Ruby (3,068 bytes), Shell (762 bytes).'}, {'repo_name': 'vizifit/GenericPasswordRow', 'language_description': 'The codebase includes: Swift (18,238 bytes), Ruby (716 bytes), Shell (211 bytes).'}, {'repo_name': 'cxy921126/SoftSwift', 'language_description': 'The majority of the code is in Swift (1,723,695 bytes), followed by Shell (17,716 bytes), Ruby (297 bytes).'}, {'repo_name': 'cwwise/CWWeChat', 'language_description': 'While most of the project is built in Swift (585,714 bytes), it also incorporates Ruby (3,447 bytes), Shell (190 bytes).'}], 'var_functions.list_db:2': ['commits', 'contents', 'files']}

exec(code, env_args)
