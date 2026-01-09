code = """import json, re
import pandas as pd

def load_records(v):
    if isinstance(v, str) and v.endswith('.json'):
        with open(v, 'r', encoding='utf-8') as f:
            return json.load(f)
    return v

nonpy = load_records(var_call_WHd7JS4qQL1LbZwRPOzLoPYI)
readmes = load_records(var_call_Hf76dFy8i2EsbFWDM0wEBSNc)

nonpy_set = set(r['repo_name'] for r in nonpy)

# Filter README.md rows to repos in nonpy set
rows = [r for r in readmes if r.get('repo_name') in nonpy_set]

total = len(rows)

# Heuristic for copyright info
pat = re.compile(r"(?:copyright\s*(?:\(c\))?\s*\d{2,4}|©\s*\d{2,4}|\bcopyright\b|all rights reserved)", re.IGNORECASE)
with_cp = sum(1 for r in rows if isinstance(r.get('content'), str) and pat.search(r['content'] or ''))

prop = (with_cp / total) if total else None

out = {
    'non_python_repos_with_readme_md_count': total,
    'with_copyright_in_readme_md_count': with_cp,
    'proportion': prop
}
print('__RESULT__:')
print(json.dumps(out))"""

env_args = {'var_call_WHd7JS4qQL1LbZwRPOzLoPYI': 'file_storage/call_WHd7JS4qQL1LbZwRPOzLoPYI.json', 'var_call_Hf76dFy8i2EsbFWDM0wEBSNc': 'file_storage/call_Hf76dFy8i2EsbFWDM0wEBSNc.json'}

exec(code, env_args)
