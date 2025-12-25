code = """import pandas as pd
import json
import re

# Load Swift repository names
swift_repos_json_path = locals()['var_function-call-16997509447462690496']
with open(swift_repos_json_path, 'r') as f:
    swift_repos_data = pd.read_json(f)
swift_repo_names = swift_repos_data['repo_name'].tolist()

# Load contents data
contents_json_path = locals()['var_function-call-6570015369607869120']
with open(contents_json_path, 'r') as f:
    contents_data = pd.read_json(f)

# Filter for Swift repositories and non-binary files
filtered_contents = contents_data[
    contents_data['sample_repo_name'].isin(swift_repo_names) & 
    ~contents_data['repo_data_description'].str.contains('binary', case=False, na=False)
].copy()

# Extract copy count
def extract_copy_count(description):
    match = re.search(r'(?:seen|copied|appearing)\s+(\d+)\s+times', description, re.IGNORECASE)
    return int(match.group(1)) if match else 0

filtered_contents['copy_count'] = filtered_contents['repo_data_description'].apply(extract_copy_count)

# Group by file ID and take the maximum copy count for unique files (as specified in the query)
unique_files = filtered_contents.loc[filtered_contents.groupby('id')['copy_count'].idxmax()]

# Find the file with the highest copy count
if not unique_files.empty:
    most_copied_file = unique_files.loc[unique_files['copy_count'].idxmax()]
    result_repo_name = most_copied_file['sample_repo_name']
else:
    result_repo_name = "No non-binary Swift file with copy information found."

print('__RESULT__:')
print(json.dumps(result_repo_name))"""

env_args = {'var_function-call-2850923003014532866': 'file_storage/function-call-2850923003014532866.json', 'var_function-call-1766463442254537415': 'file_storage/function-call-1766463442254537415.json', 'var_function-call-713632137538016356': 'file_storage/function-call-713632137538016356.json', 'var_function-call-13432594123923521291': [], 'var_function-call-16997509447462690496': 'file_storage/function-call-16997509447462690496.json', 'var_function-call-10092827166527856325': 'file_storage/function-call-10092827166527856325.json', 'var_function-call-15912791102461805296': 'file_storage/function-call-15912791102461805296.json', 'var_function-call-3073793350228249034': 'file_storage/function-call-3073793350228249034.json', 'var_function-call-6570015369607869120': 'file_storage/function-call-6570015369607869120.json'}

exec(code, env_args)
