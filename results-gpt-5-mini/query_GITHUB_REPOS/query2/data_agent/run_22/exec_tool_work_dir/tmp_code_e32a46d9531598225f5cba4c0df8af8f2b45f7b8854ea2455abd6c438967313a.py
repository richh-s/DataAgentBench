code = """import json, re, pandas as pd

# Load the large query results from storage variables
# var_call_rQb3Uv0hbBO0UmHpG43ottzi and var_call_1EgL7SZuF5yfM8OehHYpMviu are provided by the tool results
contents_src = var_call_rQb3Uv0hbBO0UmHpG43ottzi
languages_src = var_call_1EgL7SZuF5yfM8OehHYpMviu

def load_src(src):
    if isinstance(src, str) and src.endswith('.json'):
        with open(src, 'r', encoding='utf-8') as f:
            return json.load(f)
    else:
        return src

contents = load_src(contents_src)
languages = load_src(languages_src)

# Create DataFrames
df_contents = pd.DataFrame(contents)
df_lang = pd.DataFrame(languages)

# Keep only non-binary Swift files: ensure repo_data_description mentions non-binary and path ends with .swift
mask_nonbinary = df_contents['repo_data_description'].str.lower().str.contains('non-binary')
mask_swift = df_contents['sample_path'].str.lower().str.endswith('.swift')
df = df_contents[mask_nonbinary & mask_swift].copy()

# Extract copy counts from repo_data_description
def extract_copies(text):
    if not isinstance(text, str):
        return None
    m = re.search(r"(\d+)\s+(?:times|time)", text)
    if m:
        return int(m.group(1))
    # fallback: look for 'copied (\d+)'
    m2 = re.search(r"copied\s+(\d+)", text)
    if m2:
        return int(m2.group(1))
    return None

df['copies'] = df['repo_data_description'].apply(extract_copies)

# Drop rows without a parsed copies
df = df[df['copies'].notnull()].copy()

# Ensure unique by id: take max copies per id and keep associated rows
agg = df.groupby('id', as_index=False).agg({'copies':'max'})
max_copies = agg['copies'].max()

# IDs with max copies
max_ids = agg[agg['copies']==max_copies]['id'].tolist()

# Find all sample_repo_name for these ids
rows_max = df[df['id'].isin(max_ids)]
repo_names_for_max = sorted(rows_max['sample_repo_name'].dropna().unique().tolist())

# Create set of Swift repos from languages query results
swift_repos = set(df_lang['repo_name'].dropna().tolist())

# Find intersection: repos among repo_names_for_max that are Swift
swift_candidates = [r for r in repo_names_for_max if r in swift_repos]

# If none found, also consider checking exact owner/repo lowercase match
if not swift_candidates:
    swift_repos_lower = {r.lower(): r for r in swift_repos}
    for r in repo_names_for_max:
        if r.lower() in swift_repos_lower:
            swift_candidates.append(swift_repos_lower[r.lower()])

# Choose the first candidate sorted
result_repo = swift_candidates[0] if swift_candidates else None

output = {
    'max_copies': int(max_copies) if pd.notnull(max_copies) else None,
    'file_ids_with_max_copies': max_ids,
    'sample_repos_for_these_files': repo_names_for_max,
    'swift_repos_containing_file': swift_candidates,
    'selected_repository': result_repo
}

import json
print("__RESULT__:")
print(json.dumps(output))"""

env_args = {'var_call_rQb3Uv0hbBO0UmHpG43ottzi': 'file_storage/call_rQb3Uv0hbBO0UmHpG43ottzi.json', 'var_call_1EgL7SZuF5yfM8OehHYpMviu': 'file_storage/call_1EgL7SZuF5yfM8OehHYpMviu.json'}

exec(code, env_args)
