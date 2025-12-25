code = """import json

languages_file_path = locals()['var_function-call-15657998434769201345']
with open(languages_file_path, 'r') as f:
    languages_data = json.load(f)

# Search for torvalds
matches = [item['repo_name'] for item in languages_data if 'torvalds' in item['repo_name']]
print("__RESULT__:")
print(json.dumps(matches))"""

env_args = {'var_function-call-5286727036878620176': [{'repo_name': 'juliandunn/rackspacecloud', 'language_description': 'The codebase includes: Ruby (22,438 bytes), Shell (465 bytes).'}, {'repo_name': 'xMarkusSpringerx/coloranalyzer', 'language_description': 'This repository is mainly written in Ruby (1,897 bytes), with additional code in Shell (115 bytes).'}, {'repo_name': 'michaellihs/gitlab', 'language_description': 'The codebase includes: Ruby (162,002 bytes), Shell (168 bytes).'}, {'repo_name': 'vyorkin/xftp', 'language_description': 'The majority of the code is in Ruby (25,709 bytes), followed by Shell (115 bytes).'}, {'repo_name': 'airatshigapov/drophunter', 'language_description': 'The majority of the code is in Ruby (4,198 bytes), followed by Shell (115 bytes).'}], 'var_function-call-15279119177356948517': [{'repo_name': 'facebook/react', 'commit_count': '178'}, {'repo_name': 'tensorflow/tensorflow', 'commit_count': '156'}, {'repo_name': 'Microsoft/vscode', 'commit_count': '190'}, {'repo_name': 'apple/swift', 'commit_count': '1051'}, {'repo_name': 'twbs/bootstrap', 'commit_count': '340'}, {'repo_name': 'torvalds/linux', 'commit_count': '16061'}], 'var_function-call-15657998434769201345': 'file_storage/function-call-15657998434769201345.json', 'var_function-call-16388981185822219975': ['torvalds/linux', 'apple/swift', 'twbs/bootstrap', 'Microsoft/vscode', 'facebook/react'], 'var_function-call-2401095629380330759': {'facebook/react': 'JavaScript', 'tensorflow/tensorflow': 'C++', 'Microsoft/vscode': 'TypeScript', 'apple/swift': 'C++', 'twbs/bootstrap': 'JavaScript', 'torvalds/linux': None}, 'var_function-call-8956986662958048820': 'Not Found'}

exec(code, env_args)
