code = """import json

# Paths to the files from previous tool calls
non_python_file = locals()['var_function-call-7539022283214477356']
readme_file = locals()['var_function-call-1419511176935753042']

# Load non-python repos
try:
    with open(non_python_file, 'r') as f:
        # The file contains a JSON array of objects
        non_python_data = json.load(f)
        non_python_repos = set(item['repo_name'] for item in non_python_data)
except Exception as e:
    print(f"Error loading non-python repos: {e}")
    non_python_repos = set()

# Load README info
try:
    with open(readme_file, 'r') as f:
        readme_data = json.load(f)
except Exception as e:
    print(f"Error loading readme data: {e}")
    readme_data = []

# Filter and count
numerator = 0
denominator = 0

matched_repos = []

for item in readme_data:
    repo_name = item.get('sample_repo_name')
    has_copyright = item.get('has_copyright')
    
    # Check if this repo is in the non-python set
    if repo_name in non_python_repos:
        denominator += 1
        if has_copyright == '1' or has_copyright == 1:
            numerator += 1
            matched_repos.append(repo_name)

# Calculate proportion
if denominator > 0:
    proportion = numerator / denominator
else:
    proportion = 0.0

result = {
    "numerator": numerator,
    "denominator": denominator,
    "proportion": proportion,
    "matched_repos_sample": matched_repos[:10]
}

print("__RESULT__:")
print(json.dumps(result))"""

env_args = {'var_function-call-15624214722374368654': ['languages', 'repos', 'licenses'], 'var_function-call-10657861898927910422': [{'repo_name': 'juliandunn/rackspacecloud', 'language_description': 'The codebase includes: Ruby (22,438 bytes), Shell (465 bytes).'}, {'repo_name': 'xMarkusSpringerx/coloranalyzer', 'language_description': 'This repository is mainly written in Ruby (1,897 bytes), with additional code in Shell (115 bytes).'}, {'repo_name': 'michaellihs/gitlab', 'language_description': 'The codebase includes: Ruby (162,002 bytes), Shell (168 bytes).'}, {'repo_name': 'vyorkin/xftp', 'language_description': 'The majority of the code is in Ruby (25,709 bytes), followed by Shell (115 bytes).'}, {'repo_name': 'airatshigapov/drophunter', 'language_description': 'The majority of the code is in Ruby (4,198 bytes), followed by Shell (115 bytes).'}], 'var_function-call-18410543153073337604': ['commits', 'contents', 'files'], 'var_function-call-14618881362859472868': 'file_storage/function-call-14618881362859472868.json', 'var_function-call-9159591592004922589': [{'COUNT(*)': '3325634'}], 'var_function-call-17047997568710732690': [{'count_star()': '195'}], 'var_function-call-13067955104841607686': [{'count_star()': '2743'}], 'var_function-call-8638297394484339896': [{'count(DISTINCT repo_name)': '59686'}], 'var_function-call-3882056426990325412': [{'repo_name': 'waydelyle/openfund', 'has_copyright': '1'}, {'repo_name': 'rgardler/azure-quickstart-templates', 'has_copyright': '0'}, {'repo_name': 'briancavalier/todomvc-fab', 'has_copyright': '0'}, {'repo_name': 'DaMSL/K3', 'has_copyright': '0'}], 'var_function-call-5704319191726728268': [{'count_star()': '4'}], 'var_function-call-7546815921480190686': [{'count_star()': '24286'}], 'var_function-call-14128907459357650008': [{'id': '316ad972693d0355c3504729fff14287419e004d'}, {'id': 'daa40d563068ee94f01b1e87952d607a6588a589'}, {'id': '6bd679ec4ff94d8149986d49b8e789d1b4d6a44a'}, {'id': '0cfcfb70b14958a8ba30cb83808c9bcc25516969'}, {'id': 'de516c994d6cc8b7bcc1fb6bf986699fced404f6'}], 'var_function-call-340646399112960349': [{'id': '6ba8b7a1ad72449bed2c27c18dc09fdfdc902f4f'}, {'id': '2808cc7dad1e963456a33387816a60edcd14e3c2'}, {'id': '9ba1cd853975d7412462af7426bfff682bf12171'}, {'id': 'b5d98c4d7b90b473fdf470a29b2562c7c6b70c67'}, {'id': 'feb55b7e02a74beed6b06ed165c8ba65cb76bd75'}], 'var_function-call-1419511176935753042': 'file_storage/function-call-1419511176935753042.json', 'var_function-call-4841662331472719430': 'file_storage/function-call-4841662331472719430.json', 'var_function-call-7539022283214477356': 'file_storage/function-call-7539022283214477356.json'}

exec(code, env_args)
