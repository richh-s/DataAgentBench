code = """import json
import re

def load_var(v):
    # If v is a string, it may be a file path to a JSON file produced by earlier calls
    if isinstance(v, str):
        try:
            with open(v, 'r', encoding='utf-8') as f:
                return json.load(f)
        except Exception:
            try:
                return json.loads(v)
            except Exception:
                return v
    return v

# Load previous tool results available as variables
meta = load_var(var_call_8REea6hiZc1DVbCn8oYkdMS0)
contents = load_var(var_call_4w9mY46BKkPJMCPgxCMw03SG)

# Build set of non-Python repository names
non_python_repos = set()
for rec in meta:
    name = rec.get('repo_name')
    if name:
        non_python_repos.add(name)

# Filter README.md files from contents belonging to non-Python repos
readme_entries = []
for rec in contents:
    repo = rec.get('sample_repo_name') or rec.get('sample_repo') or rec.get('repo_name')
    path = rec.get('sample_path') or rec.get('path') or ''
    if not repo or repo not in non_python_repos:
        continue
    if not isinstance(path, str):
        continue
    lp = path.lower()
    if lp.endswith('readme.md') or (lp.endswith('.md') and 'readme' in lp):
        readme_entries.append(rec)

# Pattern to detect copyright-like text
pattern = re.compile(r'©|\bcopyright\b|all rights reserved', re.I)

total = 0
matches = 0
for rec in readme_entries:
    total += 1
    content = rec.get('content') or ''
    if not isinstance(content, str):
        content = str(content)
    if pattern.search(content):
        matches += 1

proportion = None
if total > 0:
    proportion = matches / total

result = {
    'total_readme_md_files_in_non_python_repos': total,
    'readme_md_with_copyright': matches,
    'proportion': proportion
}

print("__RESULT__:")
print(json.dumps(result))"""

env_args = {'var_call_8REea6hiZc1DVbCn8oYkdMS0': 'file_storage/call_8REea6hiZc1DVbCn8oYkdMS0.json', 'var_call_4w9mY46BKkPJMCPgxCMw03SG': 'file_storage/call_4w9mY46BKkPJMCPgxCMw03SG.json'}

exec(code, env_args)
