code = """import json, re
import pandas as pd

def load_maybe_path(v):
    if isinstance(v, str) and v.endswith('.json'):
        with open(v, 'r', encoding='utf-8') as f:
            return json.load(f)
    return v

cit = load_maybe_path(var_call_ZXHJTPjYXcYVQ0XFA8b2WUjK)
docs = load_maybe_path(var_call_Re9iJDoyLfirehlI5pWAa2Gj)

chi_titles = set()
chi_pat = re.compile(r"\bCHI\b")
for d in docs:
    fn = d.get('filename','')
    title = fn[:-4] if fn.lower().endswith('.txt') else fn
    text = d.get('text','') or ''
    if chi_pat.search(text):
        chi_titles.add(title)

# sum citations in 2020 for CHI presented papers
# citation_count may come as string

total = 0
for r in cit:
    if r.get('title') in chi_titles:
        try:
            total += int(r.get('citation_count') or 0)
        except Exception:
            pass

out = {"total_citations_2020_for_CHI_papers": total, "num_CHI_papers_matched": len(set([r.get('title') for r in cit if r.get('title') in chi_titles]))}
print('__RESULT__:')
print(json.dumps(out))"""

env_args = {'var_call_ZXHJTPjYXcYVQ0XFA8b2WUjK': 'file_storage/call_ZXHJTPjYXcYVQ0XFA8b2WUjK.json', 'var_call_Re9iJDoyLfirehlI5pWAa2Gj': 'file_storage/call_Re9iJDoyLfirehlI5pWAa2Gj.json'}

exec(code, env_args)
