code = """import json, pandas as pd, re

def load_maybe_path(v):
    if isinstance(v, str) and v.endswith('.json'):
        with open(v, 'r', encoding='utf-8') as f:
            return json.load(f)
    return v

cit = load_maybe_path(var_call_J8txm9Nm7LXRKe115bQZgmuM)
docs = load_maybe_path(var_call_gTRoysy304z0d0jMDBpm8Hii)

# titles that are CHI papers based on document header containing CHI
chi_titles = set()
for d in docs:
    fn = d.get('filename','')
    title = fn[:-4] if fn.lower().endswith('.txt') else fn
    text = d.get('text','') or ''
    # match common citation string like "CHI 'YY" or "Proceedings of the SIGCHI" or "CHI 20"
    if re.search(r"\bCHI\b", text) or re.search(r"SIGCHI", text, re.IGNORECASE):
        # try to ensure venue mention, not just in references: check first 2000 chars
        head = text[:2000]
        if re.search(r"\bCHI\b", head) or re.search(r"SIGCHI", head, re.IGNORECASE):
            chi_titles.add(title)

# sum citation counts for 2020 for those titles
# citation_count may be string
chi_total = 0
for r in cit:
    if r.get('title') in chi_titles:
        try:
            chi_total += int(r.get('citation_count') or 0)
        except:
            pass

out = {"total_citation_count_for_CHI_papers_cited_in_2020": chi_total, "num_CHI_papers_matched": len(chi_titles)}
print('__RESULT__:')
print(json.dumps(out))"""

env_args = {'var_call_J8txm9Nm7LXRKe115bQZgmuM': 'file_storage/call_J8txm9Nm7LXRKe115bQZgmuM.json', 'var_call_gTRoysy304z0d0jMDBpm8Hii': 'file_storage/call_gTRoysy304z0d0jMDBpm8Hii.json'}

exec(code, env_args)
