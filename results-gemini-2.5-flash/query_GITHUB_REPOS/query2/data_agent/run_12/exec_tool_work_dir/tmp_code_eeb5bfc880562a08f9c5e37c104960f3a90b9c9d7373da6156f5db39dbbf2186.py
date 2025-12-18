code = """import pandas as pd
import json
import re

# Load Swift repository names
swift_repo_names_file = locals()['var_function-call-2998159513762171227']
with open(swift_repo_names_file, 'r') as f:
    swift_repo_names = json.load(f)

# Load all contents data
contents_file = locals()['var_function-call-6600344535602621891']
with open(contents_file, 'r') as f:
    contents_data = json.load(f)

contents_df = pd.DataFrame(contents_data)

# Filter for non-binary files and Swift repositories
non_binary_swift_files = contents_df[
    (contents_df['repo_data_description'].str.contains('non-binary')) &
    (contents_df['sample_repo_name'].isin(swift_repo_names))
].copy()

# Extract copy count
def extract_copies(description):
    match = re.search(r'seen (\d+) times|duplicated (\d+) times|appearing (\d+) times', description)
    if match:
        return int(match.group(1) or match.group(2) or match.group(3))
    return 0

non_binary_swift_files['copies'] = non_binary_swift_files['repo_data_description'].apply(extract_copies)

# Find the file with the most copies, ensuring unique ID
most_copied_file = non_binary_swift_files.sort_values(by='copies', ascending=False).drop_duplicates(subset=['id']).iloc[0]

result_repo_name = most_copied_file['sample_repo_name']

print("__RESULT__:")
print(json.dumps(result_repo_name))"""

env_args = {'var_function-call-7022838797063846419': 'file_storage/function-call-7022838797063846419.json', 'var_function-call-2998159513762171227': 'file_storage/function-call-2998159513762171227.json', 'var_function-call-18205311517710723005': 'file_storage/function-call-18205311517710723005.json', 'var_function-call-6600344535602621891': 'file_storage/function-call-6600344535602621891.json'}

exec(code, env_args)
