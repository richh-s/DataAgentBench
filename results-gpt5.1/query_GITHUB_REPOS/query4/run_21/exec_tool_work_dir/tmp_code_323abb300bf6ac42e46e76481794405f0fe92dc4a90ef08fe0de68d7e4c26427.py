code = """import json, re, pandas as pd

# Load full languages table
path = var_call_wmAYh5PqEGXezR0HUTRV8Nnd
with open(path, 'r') as f:
    languages = json.load(f)

# Build dataframe
lang_df = pd.DataFrame(languages)

# Function to extract main language as the one with max bytes
pattern = re.compile(r"([A-Za-z+#]+) \((\d+) bytes\)")

def get_main_language(desc):
    if not isinstance(desc, str):
        return None
    matches = pattern.findall(desc)
    if not matches:
        return None
    # matches is list of (language, bytes)
    lang, _ = max(((l, int(b)) for l, b in matches), key=lambda x: x[1])
    return lang

lang_df['main_language'] = lang_df['language_description'].apply(get_main_language)

# Filter out main_language == 'Python'
non_python = lang_df[lang_df['main_language'] != 'Python'][['repo_name', 'main_language']]

result = non_python.to_dict(orient='records')

print("__RESULT__:")
print(json.dumps(result))"""

env_args = {'var_call_Cu1B7pb1tEfru9lfPoCrITwp': [{'repo_name': 'torvalds/linux', 'commit_count': '16061'}, {'repo_name': 'apple/swift', 'commit_count': '1051'}, {'repo_name': 'twbs/bootstrap', 'commit_count': '340'}, {'repo_name': 'Microsoft/vscode', 'commit_count': '190'}, {'repo_name': 'facebook/react', 'commit_count': '178'}, {'repo_name': 'tensorflow/tensorflow', 'commit_count': '156'}], 'var_call_iHxTyeiUeQeID2U4JhcjQYnf': ['languages', 'repos', 'licenses'], 'var_call_wmAYh5PqEGXezR0HUTRV8Nnd': 'file_storage/call_wmAYh5PqEGXezR0HUTRV8Nnd.json'}

exec(code, env_args)
