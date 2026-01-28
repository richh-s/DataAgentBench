code = """import json, re

def load_tool_result(x):
    if isinstance(x, str) and x.endswith('.json'):
        with open(x, 'r', encoding='utf-8') as f:
            return json.load(f)
    return x

docs = load_tool_result(var_call_TDnMk5TxCu8yMFjaBkwMw1Gt)

# search for common venue markers
markers = ['CHI', 'SIGCHI', 'Proceedings of the', 'Conference on Human Factors', 'CHI\'']
counts={}
for m in markers:
    pat = re.compile(m, flags=re.IGNORECASE)
    counts[m]=sum(1 for d in docs if pat.search(d.get('text') or ''))

# also find top 20 venue tokens like UBICOMP, CSCW, DIS in headers: first 200 chars
venue_tokens=['UBICOMP','CSCW','CHI','DIS','IUI','WWW','TEI','OzCHI','AH','PervasiveHealth']
head_counts={}
for t in venue_tokens:
    pat=re.compile(r"\b"+re.escape(t)+r"\b", flags=re.IGNORECASE)
    head_counts[t]=sum(1 for d in docs if pat.search((d.get('text') or '')[:500]))

print('__RESULT__:')
print(json.dumps({"marker_counts": counts, "head_counts": head_counts}))"""

env_args = {'var_call_9X83BuiCEEyXT0BZpBCna1M4': 'file_storage/call_9X83BuiCEEyXT0BZpBCna1M4.json', 'var_call_TDnMk5TxCu8yMFjaBkwMw1Gt': 'file_storage/call_TDnMk5TxCu8yMFjaBkwMw1Gt.json', 'var_call_egAvhU1ylTDfdvxAYA2Oo6Ls': {'total_citation_count_2020_for_CHI_papers': 0, 'num_chi_papers_with_2020_citations': 0}, 'var_call_g8d2v5XBvpSsIzTEcs9vcv3G': {'num_docs': 99, 'num_with_CHI_token_in_first50': 0, 'sample': []}}

exec(code, env_args)
