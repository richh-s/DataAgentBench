code = """import json
import pandas as pd
import re

# Load Swift repository names
with open(locals()['var_function-call-5026490014690946050'], 'r') as f:
    swift_repos_data = json.load(f)
swift_repo_names = [repo['repo_name'] for repo in swift_repos_data['results']]

# Load non-binary file contents (pre-filtered by the previous step's query)
with open(locals()['var_function-call-7490348254204994015'], 'r') as f:
    non_binary_contents_data = json.load(f)

# Convert to DataFrame
df_contents = pd.DataFrame(non_binary_contents_data)

# Further filter out binary files by ensuring 'Binary' is NOT in repo_data_description
df_contents = df_contents[~df_contents['repo_data_description'].str.contains('Binary', na=False)]

# Filter for files belonging to Swift repositories
df_swift_contents = df_contents[df_contents['sample_repo_name'].isin(swift_repo_names)]

# Extract copy count from repo_data_description
def extract_copies(description):
    match = re.search(r'seen (\d+) times', description)
    if match:
        return int(match.group(1))
    return 0

df_swift_contents['copies'] = df_swift_contents['repo_data_description'].apply(extract_copies)

# Ensure each file is uniquely determined by its ID and find the one with the most copies
# Group by ID and take the row with the maximum copies. If there are ties in copies for the same ID across different repos,
# then either of them is fine, but the problem specifies "each file is uniquely determined by its ID",
# implying we should consider `id` as the unique identifier for a file, regardless of `sample_repo_name`
# for finding "the file". Once "the file" is found, we can get its repo name.

# To handle cases where the same file (same id) might appear in multiple repos with different copy counts
# (due to the "sample_repo_name" perhaps meaning a specific instance of the file in a repo, not the global count)
# I should first aggregate copies by id, then take the max.
# However, the problem states "Identify the repository ... that contains the most frequently copied non-binary Swift file"
# This suggests that "most frequently copied" is related to the file's individual count in a repository sample.

# Let's consider `id` as the unique file identifier. If a file with the same `id` appears in multiple `sample_repo_name`,
# we treat them as different instances regarding their copy counts in the context of their specific `sample_repo_name`.
# So we need to find the `(id, sample_repo_name)` combination that has the highest `copies`.

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
