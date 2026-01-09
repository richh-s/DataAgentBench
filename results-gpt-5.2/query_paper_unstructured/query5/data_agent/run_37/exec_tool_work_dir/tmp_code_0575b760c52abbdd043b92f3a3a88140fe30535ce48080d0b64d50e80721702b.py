code = """import json, re

def load_records(maybe_path_or_list):
    if isinstance(maybe_path_or_list, str) and maybe_path_or_list.endswith('.json'):
        with open(maybe_path_or_list, 'r', encoding='utf-8') as f:
            return json.load(f)
    return maybe_path_or_list

cit = load_records(var_call_TRpLmu1z1yAwlBlNZUz41qpT)
docs = load_records(var_call_0xzxrpc7YvsO6yzcV7d1dOG8)

chi_titles = set()
for d in docs:
    fn = d.get('filename','')
    title = fn[:-4] if fn.lower().endswith('.txt') else fn
    text = d.get('text','') or ''
    if re.search(r"\bCHI\b", text) or re.search(r"\bSIGCHI\b", text) or re.search(r"\bCHI\s*'\d{2}\b", text):
        chi_titles.add(title)

# compute
chi_cit_total = 0
chi_papers = 0
for r in cit:
    if r.get('title') in chi_titles:
        chi_papers += 1
        try:
            chi_cit_total += int(r.get('citation_count') or 0)
        except:
            pass

out = {"total_citations_2020_for_CHI_papers": chi_cit_total, "num_CHI_papers_cited_in_2020": chi_papers, "num_docs_detected_as_CHI": len(chi_titles)}
print('__RESULT__:')
print(json.dumps(out))"""

env_args = {'var_call_TRpLmu1z1yAwlBlNZUz41qpT': 'file_storage/call_TRpLmu1z1yAwlBlNZUz41qpT.json', 'var_call_0xzxrpc7YvsO6yzcV7d1dOG8': 'file_storage/call_0xzxrpc7YvsO6yzcV7d1dOG8.json', 'var_call_fir9ov4PUWbvrSB6gVQLqz5q': {'total_citations_2020_for_CHI_papers': 0, 'num_CHI_papers_cited_in_2020': 0}}

exec(code, env_args)
