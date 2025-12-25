code = """import json, re, pandas as pd

# languages large result file path
languages_data = var_call_dkVzufWYhIVe4yckBHki7FtO

# load full languages table
with open(languages_data, 'r') as f:
    languages = json.load(f)

langs_df = pd.DataFrame(languages)

# heuristic to extract main language: the first language mentioned before first '(' or comma is usually main
# but descriptions are like "The codebase includes: Ruby (22,438 bytes), Shell ..." or "The codebase includes: Shell (...), Ruby ..."

def extract_main_language(desc: str):
    if not isinstance(desc, str):
        return None
    # find all patterns Language (number bytes)
    matches = re.findall(r'([A-Za-z+#]+) \((?:[0-9,]+) bytes\)', desc)
    if matches:
        # assume first occurrence corresponds to largest (as text states ordering by size)
        return matches[0]
    # fallback: take first capitalized word after colon
    m = re.search(r':\s*([A-Za-z+#]+)', desc)
    return m.group(1) if m else None

langs_df['main_language'] = langs_df['language_description'].apply(extract_main_language)

# commits data
commits_df = pd.DataFrame(var_call_ukuSIa7x1OlKMHrS29bJB3O1)
commits_df['commit_count'] = commits_df['commit_count'].astype(int)

# join on repo_name to get language
merged = commits_df.merge(langs_df[['repo_name','main_language']], on='repo_name', how='left')

# filter out Python main language
filtered = merged[merged['main_language'].str.lower() != 'python']

# sort by commit_count desc and take top 5
result = filtered.sort_values('commit_count', ascending=False).head(5)['repo_name'].tolist()

out = json.dumps(result)
print("__RESULT__:")
print(out)"""

env_args = {'var_call_dkVzufWYhIVe4yckBHki7FtO': 'file_storage/call_dkVzufWYhIVe4yckBHki7FtO.json', 'var_call_ukuSIa7x1OlKMHrS29bJB3O1': [{'repo_name': 'torvalds/linux', 'commit_count': '16061'}, {'repo_name': 'apple/swift', 'commit_count': '1051'}, {'repo_name': 'twbs/bootstrap', 'commit_count': '340'}, {'repo_name': 'Microsoft/vscode', 'commit_count': '190'}, {'repo_name': 'facebook/react', 'commit_count': '178'}, {'repo_name': 'tensorflow/tensorflow', 'commit_count': '156'}]}

exec(code, env_args)
