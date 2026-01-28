code = """import json
import re

# Read the query result from file
result_file = "var_functions.query_db:9"
with open(result_file, 'r') as f:
    swift_repos = json.load(f)

# Extract repo names where Swift is the primary language
swift_primary_repos = []

for repo in swift_repos:
    desc = repo['language_description'].lower()
    # Look for patterns indicating Swift is primary
    if 'mainly written in swift' in desc or 'majority of the code is in swift' in desc:
        swift_primary_repos.append(repo['repo_name'])
    elif 'the codebase includes: swift' in desc:
        # Check if Swift has the highest byte count
        # Extract byte counts
        swift_match = re.search(r'swift \(([\d,]+) bytes\)', desc)
        if swift_match:
            swift_bytes = int(swift_match.group(1).replace(',', ''))
            # Check for other major languages
            ruby_match = re.search(r'ruby \(([\d,]+) bytes\)', desc)
            shell_match = re.search(r'shell \(([\d,]+) bytes\)', desc)
            
            ruby_bytes = int(ruby_match.group(1).replace(',', '')) if ruby_match else 0
            shell_bytes = int(shell_match.group(1).replace(',', '')) if shell_match else 0
            
            if swift_bytes > ruby_bytes and swift_bytes > shell_bytes:
                swift_primary_repos.append(repo['repo_name'])

print('__RESULT__:')
print(json.dumps({
    'swift_primary_repos': swift_primary_repos,
    'count': len(swift_primary_repos)
}))"""

env_args = {'var_functions.list_db:0': ['languages', 'repos', 'licenses'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.list_db:5': ['commits', 'contents', 'files'], 'var_functions.query_db:9': [{'repo_name': 'e-Sixt/Swen', 'language_description': 'This repository is mainly written in Swift (16,364 bytes), with additional code in Ruby (7,243 bytes), Shell (94 bytes).'}, {'repo_name': 'ApplauseOSS/Swifjection', 'language_description': 'The codebase includes: Swift (109,540 bytes), Ruby (3,068 bytes), Shell (762 bytes).'}, {'repo_name': 'vizifit/GenericPasswordRow', 'language_description': 'The codebase includes: Swift (18,238 bytes), Ruby (716 bytes), Shell (211 bytes).'}, {'repo_name': 'cxy921126/SoftSwift', 'language_description': 'The majority of the code is in Swift (1,723,695 bytes), followed by Shell (17,716 bytes), Ruby (297 bytes).'}, {'repo_name': 'cwwise/CWWeChat', 'language_description': 'While most of the project is built in Swift (585,714 bytes), it also incorporates Ruby (3,447 bytes), Shell (190 bytes).'}, {'repo_name': 'Apemb/Compass', 'language_description': 'The codebase includes: Swift (33,632 bytes), Shell (711 bytes), Ruby (434 bytes).'}, {'repo_name': 'toggl/superday', 'language_description': 'The majority of the code is in Swift (747,765 bytes), followed by Ruby (3,949 bytes), Shell (393 bytes).'}, {'repo_name': 'malcommac/SwiftDate', 'language_description': 'While most of the project is built in Swift (419,579 bytes), it also incorporates Ruby (767 bytes), Shell (169 bytes).'}, {'repo_name': 'chronotruck/CTKFlagPhoneNumber', 'language_description': 'While most of the project is built in Swift (87,439 bytes), it also incorporates Ruby (2,165 bytes), Shell (65 bytes).'}, {'repo_name': 'zendobk/SwiftUtils', 'language_description': 'While most of the project is built in Swift (71,711 bytes), it also incorporates Shell (3,156 bytes), Ruby (3,009 bytes).'}, {'repo_name': 'binarylevel/Riseset', 'language_description': 'The codebase includes: Swift (55,000 bytes), Ruby (533 bytes), Shell (193 bytes).'}, {'repo_name': 'Raizlabs/Anchorage', 'language_description': 'This repository is mainly written in Swift (99,834 bytes), with additional code in Ruby (6,219 bytes), Shell (5,846 bytes).'}, {'repo_name': 'mweibel/esrscan', 'language_description': 'While most of the project is built in Swift (46,819 bytes), it also incorporates Ruby (761 bytes), Shell (102 bytes).'}, {'repo_name': 'magmajo/nmagma-ios', 'language_description': 'The codebase includes: Swift (8,672 bytes), Ruby (6,468 bytes), Shell (1,308 bytes).'}, {'repo_name': 'elpassion/el-space-ios', 'language_description': 'While most of the project is built in Swift (366,580 bytes), it also incorporates Ruby (11,529 bytes), Shell (132 bytes).'}, {'repo_name': 'steveholt55/BLJGameButton', 'language_description': 'While most of the project is built in Swift (6,873 bytes), it also incorporates Ruby (577 bytes), Shell (28 bytes).'}, {'repo_name': 'truemetal/vapor-2-heroku-auth-template', 'language_description': 'This repository is mainly written in Swift (11,040 bytes), with additional code in Ruby (880 bytes), Shell (304 bytes).'}, {'repo_name': 'DenHeadless/DTCollectionViewManager', 'language_description': 'The codebase includes: Swift (264,900 bytes), Ruby (9,909 bytes), Shell (724 bytes).'}, {'repo_name': 'fizx/jane', 'language_description': 'The codebase includes: Swift (36,767 bytes), Ruby (6,457 bytes), Shell (1,823 bytes).'}, {'repo_name': 'ostatnicky/kancional-ios', 'language_description': 'While most of the project is built in Swift (147,485 bytes), it also incorporates Ruby (422 bytes), Shell (74 bytes).'}]}

exec(code, env_args)
