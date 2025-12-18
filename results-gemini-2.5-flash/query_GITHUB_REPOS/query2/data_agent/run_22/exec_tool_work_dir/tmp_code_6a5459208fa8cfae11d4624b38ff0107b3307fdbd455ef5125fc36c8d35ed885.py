code = """import json
import pandas as pd
import re

# Load Swift repository names
with open(locals()['var_function-call-12615506705198542954'], 'r') as f:
    swift_repos = json.load(f)

# Load all file contents data
with open(locals()['var_function-call-2167082898009311104'], 'r') as f:
    all_contents = json.load(f)

df_contents = pd.DataFrame(all_contents)

# Filter for non-binary and Swift files
df_swift_files = df_contents[
    (~df_contents['repo_data_description'].str.contains('binary')) &
    (df_contents['sample_path'].str.endswith('.swift')) &
    (df_contents['sample_repo_name'].isin(swift_repos))
].copy()

# Extract the number of copies
# The 'repo_data_description' contains 'seen X times' or 'duplicated X times' or 'appearing X times'.
def extract_copies(description):
    match = re.search(r'(?:seen|duplicated|appearing)\s(\d+)\stimes', description)
    return int(match.group(1)) if match else 1 # Default to 1 if no count is found

df_swift_files['copies'] = df_swift_files['repo_data_description'].apply(extract_copies)

# Group by 'id' and 'sample_repo_name' to get unique files and their total copies
# (Each file is uniquely determined by its ID, but can appear in multiple repos with different copy counts in description).
# Here we want to find the file ID with the most copies *across all its occurrences in Swift repos*.
# The problem statement says "each file is uniquely determined by its ID". So we should sum copies per ID first.
df_file_copies = df_swift_files.groupby(['id', 'sample_repo_name'])['copies'].sum().reset_index()

# Find the file ID with the maximum total copies
most_copied_file = df_file_copies.loc[df_file_copies['copies'].idxmax()]

# Get the repository name for the most copied file ID
repo_with_most_copied_file = most_copied_file['sample_repo_name']

print("__RESULT__:")
print(json.dumps(repo_with_most_copied_file))"""

env_args = {'var_function-call-347823077341566621': 'file_storage/function-call-347823077341566621.json', 'var_function-call-8080805660567023187': [], 'var_function-call-12615506705198542954': 'file_storage/function-call-12615506705198542954.json', 'var_function-call-17964744684272180105': 'file_storage/function-call-17964744684272180105.json', 'var_function-call-2167082898009311104': 'file_storage/function-call-2167082898009311104.json'}

exec(code, env_args)
