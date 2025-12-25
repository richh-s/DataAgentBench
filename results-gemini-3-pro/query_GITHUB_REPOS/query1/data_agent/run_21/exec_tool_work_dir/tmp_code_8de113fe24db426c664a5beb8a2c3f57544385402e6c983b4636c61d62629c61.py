code = """import json

# Load data
with open(locals()['var_function-call-16559173715773755267'], 'r') as f:
    readme_data = json.load(f)

# unique repos
repo_names = list(set([item['sample_repo_name'] for item in readme_data]))

print(f"Total READMEs: {len(readme_data)}")
print(f"Unique repos: {len(repo_names)}")

# I will chunk the repo names if too many, but 204 is fine for one query.
# Format for SQL IN clause
repo_list_str = ", ".join([f"'{name}'" for name in repo_names])

print("__RESULT__:")
print(json.dumps(repo_list_str))"""

env_args = {'var_function-call-13677778010895943402': [{'repo_name': 'juliandunn/rackspacecloud', 'language_description': 'The codebase includes: Ruby (22,438 bytes), Shell (465 bytes).'}, {'repo_name': 'xMarkusSpringerx/coloranalyzer', 'language_description': 'This repository is mainly written in Ruby (1,897 bytes), with additional code in Shell (115 bytes).'}, {'repo_name': 'michaellihs/gitlab', 'language_description': 'The codebase includes: Ruby (162,002 bytes), Shell (168 bytes).'}, {'repo_name': 'vyorkin/xftp', 'language_description': 'The majority of the code is in Ruby (25,709 bytes), followed by Shell (115 bytes).'}, {'repo_name': 'airatshigapov/drophunter', 'language_description': 'The majority of the code is in Ruby (4,198 bytes), followed by Shell (115 bytes).'}], 'var_function-call-9760931169711847301': [{'COUNT(*)': '3325634'}], 'var_function-call-16478506448492513366': [{'count_star()': '524077'}], 'var_function-call-12904064769800451095': [{'count(DISTINCT repo_name)': '59686'}], 'var_function-call-4301828507115235792': [{'path': 'README.md', 'count_star()': '1059'}, {'path': 'README.rst', 'count_star()': '56'}, {'path': 'README', 'count_star()': '47'}, {'path': 'readme.md', 'count_star()': '27'}, {'path': 'README.markdown', 'count_star()': '10'}, {'path': 'docs/README.md', 'count_star()': '8'}, {'path': 'Readme.md', 'count_star()': '8'}, {'path': 'example/README.md', 'count_star()': '6'}, {'path': 'README.txt', 'count_star()': '6'}, {'path': 'drivers/staging/slicoss/README', 'count_star()': '6'}], 'var_function-call-18398660009715640193': [{'repo_name': 'waydelyle/openfund', 'has_copyright': '1'}, {'repo_name': 'briancavalier/todomvc-fab', 'has_copyright': '0'}, {'repo_name': 'rgardler/azure-quickstart-templates', 'has_copyright': '0'}, {'repo_name': 'DaMSL/K3', 'has_copyright': '0'}], 'var_function-call-1502578823372228115': ['briancavalier/todomvc-fab', 'waydelyle/openfund', 'DaMSL/K3', 'rgardler/azure-quickstart-templates'], 'var_function-call-362295928800951001': [{'count_star()': '24286'}], 'var_function-call-16623598251868077292': [{'id': '100b93820ade4c16225673b4ca62bb3ade63c313'}, {'id': '9ed04c6e74db0e3606e716e64e1d7190d5027b15'}, {'id': '5f0d4f75fdb2cf3b303d312d6898d3413fccfca7'}, {'id': '4e1d480f9228a40af4e3e4c507b38d593e3e588b'}, {'id': 'e75de9d29f2af646ae811eb662be95f7f3dc6cc2'}], 'var_function-call-16847896288229096354': [], 'var_function-call-15204758217568640510': 'file_storage/function-call-15204758217568640510.json', 'var_function-call-8376599495387671806': [{'count_star()': '204'}], 'var_function-call-16559173715773755267': 'file_storage/function-call-16559173715773755267.json'}

exec(code, env_args)
