code = """import json, re, pandas as pd

def load_records(x):
    if isinstance(x, str):
        with open(x, 'r', encoding='utf-8') as f:
            return json.load(f)
    return x

commits = pd.DataFrame(load_records(var_call_rLmXhlgziCmcV35G3QLjCkP2))
langs = pd.DataFrame(load_records(var_call_JVMoUfcOw7xJgQOHMIGi8h9l))

commits['commit_count'] = commits['commit_count'].astype(int)

# parse main language from language_description by taking language with max bytes
pat = re.compile(r"([A-Za-z0-9_+.#-]+) \((\d[\d,]*) bytes\)")

def main_lang(desc):
    if not isinstance(desc, str):
        return None
    matches = pat.findall(desc)
    if not matches:
        return None
    best_lang, best_bytes = None, -1
    for lang, b in matches:
        nb = int(b.replace(',', ''))
        if nb > best_bytes:
            best_lang, best_bytes = lang, nb
    return best_lang

langs['main_language'] = langs['language_description'].map(main_lang)

df = commits.merge(langs[['repo_name','main_language']], on='repo_name', how='left')
# filter main language not python (case-insensitive). If unknown, exclude.
df = df[df['main_language'].notna()]
df = df[df['main_language'].str.lower() != 'python']

top5 = df.sort_values(['commit_count','repo_name'], ascending=[False, True]).head(5)
answer = top5['repo_name'].tolist()

print('__RESULT__:')
print(json.dumps(answer))"""

env_args = {'var_call_rLmXhlgziCmcV35G3QLjCkP2': [{'repo_name': 'torvalds/linux', 'commit_count': '16061'}, {'repo_name': 'apple/swift', 'commit_count': '1051'}, {'repo_name': 'twbs/bootstrap', 'commit_count': '340'}, {'repo_name': 'Microsoft/vscode', 'commit_count': '190'}, {'repo_name': 'facebook/react', 'commit_count': '178'}, {'repo_name': 'tensorflow/tensorflow', 'commit_count': '156'}], 'var_call_JVMoUfcOw7xJgQOHMIGi8h9l': 'file_storage/call_JVMoUfcOw7xJgQOHMIGi8h9l.json'}

exec(code, env_args)
