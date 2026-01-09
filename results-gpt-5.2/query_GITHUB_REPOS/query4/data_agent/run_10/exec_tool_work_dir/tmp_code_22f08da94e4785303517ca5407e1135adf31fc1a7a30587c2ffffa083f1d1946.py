code = """import json, re
import pandas as pd

commits = pd.DataFrame(var_call_glil3uPuQDx4PcONf4DVzRvB)
commits['commit_count'] = commits['commit_count'].astype(int)
repo_set = set(commits['repo_name'].tolist())

# stream-load languages and keep only needed repos
path = var_call_yfd8HOAIKDaESlvQM3l3Da2S
with open(path, 'r', encoding='utf-8') as f:
    langs_data = json.load(f)

pattern = re.compile(r'([A-Za-z0-9+#\.\- ]+)\s*\((\d[\d,]*)\s*bytes\)')

def main_lang(desc):
    if not isinstance(desc, str):
        return None
    matches = pattern.findall(desc)
    if not matches:
        return None
    best_lang, best_bytes = None, -1
    for lang, b in matches:
        b = int(b.replace(',', ''))
        lang = lang.strip().rstrip(':')
        if b > best_bytes:
            best_lang, best_bytes = lang, b
    return best_lang

lang_map = {}
for rec in langs_data:
    rn = rec.get('repo_name')
    if rn in repo_set:
        lang_map[rn] = main_lang(rec.get('language_description'))

commits['main_language'] = commits['repo_name'].map(lang_map)
filtered = commits[(commits['main_language'].notna()) & (commits['main_language'].str.lower() != 'python')]

top5 = filtered.sort_values(['commit_count','repo_name'], ascending=[False, True]).head(5)
answer_list = top5['repo_name'].tolist()

print('__RESULT__:')
print(json.dumps(answer_list))"""

env_args = {'var_call_glil3uPuQDx4PcONf4DVzRvB': [{'repo_name': 'torvalds/linux', 'commit_count': '16061'}, {'repo_name': 'apple/swift', 'commit_count': '1051'}, {'repo_name': 'twbs/bootstrap', 'commit_count': '340'}, {'repo_name': 'Microsoft/vscode', 'commit_count': '190'}, {'repo_name': 'facebook/react', 'commit_count': '178'}, {'repo_name': 'tensorflow/tensorflow', 'commit_count': '156'}], 'var_call_yfd8HOAIKDaESlvQM3l3Da2S': 'file_storage/call_yfd8HOAIKDaESlvQM3l3Da2S.json'}

exec(code, env_args)
