code = """import json, re
import pandas as pd

def load_records(maybe_path_or_list):
    if isinstance(maybe_path_or_list, str) and maybe_path_or_list.endswith('.json'):
        with open(maybe_path_or_list, 'r', encoding='utf-8') as f:
            return json.load(f)
    return maybe_path_or_list

cit = load_records(var_call_TRpLmu1z1yAwlBlNZUz41qpT)
docs = load_records(var_call_0xzxrpc7YvsO6yzcV7d1dOG8)

# Build set of CHI titles from docs by simple venue detection.
chi_titles = set()
for d in docs:
    fn = d.get('filename','')
    title = fn[:-4] if fn.lower().endswith('.txt') else fn
    text = d.get('text','') or ''
    if re.search(r'\bCHI\b', text) or re.search(r"\bCHI\s*'\d{2}\b", text) or re.search(r'\bSIGCHI\b', text):
        # avoid false positives by requiring CHI proceedings cue
        if re.search(r'\bCHI\b', text) and re.search(r'\bACM\b', text):
            chi_titles.add(title)
        elif re.search(r'\bProceedings\b', text, flags=re.I) and re.search(r'\bCHI\b', text):
            chi_titles.add(title)
        elif re.search(r'\bSIGCHI\b', text):
            chi_titles.add(title)

# Filter citations for CHI titles and sum counts across CHI papers
# citation_count may be string
chi_cit_total = 0
for r in cit:
    if r.get('title') in chi_titles:
        try:
            chi_cit_total += int(r.get('citation_count') or 0)
        except:
            chi_cit_total += 0

out = {"total_citations_2020_for_CHI_papers": chi_cit_total, "num_CHI_papers_cited_in_2020": sum(1 for r in cit if r.get('title') in chi_titles)}
print('__RESULT__:')
print(json.dumps(out))"""

env_args = {'var_call_TRpLmu1z1yAwlBlNZUz41qpT': 'file_storage/call_TRpLmu1z1yAwlBlNZUz41qpT.json', 'var_call_0xzxrpc7YvsO6yzcV7d1dOG8': 'file_storage/call_0xzxrpc7YvsO6yzcV7d1dOG8.json'}

exec(code, env_args)
