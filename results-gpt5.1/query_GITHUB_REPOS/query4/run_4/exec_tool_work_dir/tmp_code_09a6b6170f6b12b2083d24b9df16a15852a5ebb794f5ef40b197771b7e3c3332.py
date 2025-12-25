code = """import json, re, pandas as pd

# Load commits and languages
commits = pd.DataFrame(var_call_hykaTOJA7RlEzdBhWWG5SCHm)

# languages is in a JSON file path
with open(var_call_DL8vPMZ2Qj6ZttV21YFcZk9P, 'r') as f:
    languages = pd.DataFrame(json.load(f))

# Determine main language from language_description: pick first "Name (NN bytes)" entry
pattern = re.compile(r"([A-Za-z+#.0-9]+) \(\d+ bytes\)")

def extract_main_language(desc):
    if not isinstance(desc, str):
        return None
    m = pattern.search(desc)
    return m.group(1) if m else None

languages['main_language'] = languages['language_description'].apply(extract_main_language)

# Merge commits with languages on repo_name
merged = commits.merge(languages[['repo_name','main_language']], on='repo_name', how='left')

# Filter out Python main language
filtered = merged[merged['main_language'].str.lower() != 'python']

# Order by commit_count desc and take top 5
filtered['commit_count'] = filtered['commit_count'].astype(int)
result_names = filtered.sort_values('commit_count', ascending=False).head(5)['repo_name'].tolist()

out = json.dumps(result_names)
print("__RESULT__:")
print(out)"""

env_args = {'var_call_hykaTOJA7RlEzdBhWWG5SCHm': [{'repo_name': 'torvalds/linux', 'commit_count': '16061'}, {'repo_name': 'apple/swift', 'commit_count': '1051'}, {'repo_name': 'twbs/bootstrap', 'commit_count': '340'}, {'repo_name': 'Microsoft/vscode', 'commit_count': '190'}, {'repo_name': 'facebook/react', 'commit_count': '178'}, {'repo_name': 'tensorflow/tensorflow', 'commit_count': '156'}], 'var_call_DL8vPMZ2Qj6ZttV21YFcZk9P': 'file_storage/call_DL8vPMZ2Qj6ZttV21YFcZk9P.json'}

exec(code, env_args)
