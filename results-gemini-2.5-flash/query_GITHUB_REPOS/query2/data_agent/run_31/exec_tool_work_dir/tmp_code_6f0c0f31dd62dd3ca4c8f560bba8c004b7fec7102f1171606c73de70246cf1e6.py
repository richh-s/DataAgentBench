code = """import json
import pandas as pd
import re

# Load Swift repository names - corrected access
with open(locals()['var_function-call-5026490014690946050'], 'r') as f:
    swift_repos_data_raw = json.load(f)
swift_repo_names = [repo['repo_name'] for repo in swift_repos_data_raw]

# Load non-binary file contents (pre-filtered by the previous step's query) - corrected access
with open(locals()['var_function-call-7490348254204994015'], 'r') as f:
    non_binary_contents_data_raw = json.load(f)

# Convert to DataFrame
df_contents = pd.DataFrame(non_binary_contents_data_raw)

# Filter for files belonging to Swift repositories
df_swift_contents = df_contents[df_contents['sample_repo_name'].isin(swift_repo_names)]

# Extract copy count from repo_data_description
def extract_copies(description):
    match = re.search(r'seen (\\d+) times', description)
    if match:
        return int(match.group(1))
    return 0

df_swift_contents['copies'] = df_swift_contents['repo_data_description'].apply(extract_copies)

# Find the row with the maximum 'copies'
if not df_swift_contents.empty:
    most_copied_file = df_swift_contents.loc[df_swift_contents['copies'].idxmax()]
    result_repo_name = most_copied_file['sample_repo_name']
else:
    result_repo_name = "No Swift non-binary files found."

print("__RESULT__:")
print(json.dumps(result_repo_name))"""

env_args = {'var_function-call-5026490014690946050': 'file_storage/function-call-5026490014690946050.json', 'var_function-call-7490348254204994015': 'file_storage/function-call-7490348254204994015.json'}

exec(code, env_args)
