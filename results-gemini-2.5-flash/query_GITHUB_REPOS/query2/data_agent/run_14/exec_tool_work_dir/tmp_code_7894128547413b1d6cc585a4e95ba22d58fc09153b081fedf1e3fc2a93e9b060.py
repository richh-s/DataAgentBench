code = """import pandas as pd
import json
import re

# Load Swift repository names
swift_repos_json_path = locals()['var_function-call-6031568542258250922']
with open(swift_repos_json_path, 'r') as f:
    swift_repos_data = pd.read_json(f)
swift_repo_names = swift_repos_data['repo_name'].tolist()

# Load contents data
contents_json_path = locals()['var_function-call-1814398536932392220']
with open(contents_json_path, 'r') as f:
    contents_data = pd.read_json(f)

# Filter for Swift repositories
swift_files = contents_data[contents_data['sample_repo_name'].isin(swift_repo_names)].copy()

# Filter for non-binary files
non_binary_swift_files = swift_files[~swift_files['repo_data_description'].str.contains('binary', case=False, na=False)].copy()

# Inspect descriptions that should contain copy info
# Let's sample some descriptions to see the pattern.
sample_descriptions = non_binary_swift_files['repo_data_description'].sample(min(10, len(non_binary_swift_files))).tolist()

print('__RESULT__:')
print(json.dumps(sample_descriptions))"""

env_args = {'var_function-call-2850923003014532866': 'file_storage/function-call-2850923003014532866.json', 'var_function-call-1766463442254537415': 'file_storage/function-call-1766463442254537415.json', 'var_function-call-713632137538016356': 'file_storage/function-call-713632137538016356.json', 'var_function-call-13432594123923521291': [], 'var_function-call-16997509447462690496': 'file_storage/function-call-16997509447462690496.json', 'var_function-call-10092827166527856325': 'file_storage/function-call-10092827166527856325.json', 'var_function-call-15912791102461805296': 'file_storage/function-call-15912791102461805296.json', 'var_function-call-3073793350228249034': 'file_storage/function-call-3073793350228249034.json', 'var_function-call-6570015369607869120': 'file_storage/function-call-6570015369607869120.json', 'var_function-call-9900618962137091359': 'No non-binary Swift file with copy information found.', 'var_function-call-1573539438079082201': 'file_storage/function-call-1573539438079082201.json', 'var_function-call-11835150289539032062': 'No non-binary Swift files found in specified repositories.', 'var_function-call-6031568542258250922': 'file_storage/function-call-6031568542258250922.json', 'var_function-call-9943881458440075688': 'No non-binary Swift file with valid copy information found.', 'var_function-call-12906077147604428302': 'file_storage/function-call-12906077147604428302.json', 'var_function-call-1814398536932392220': 'file_storage/function-call-1814398536932392220.json'}

exec(code, env_args)
