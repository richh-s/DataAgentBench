code = """import json, re

def load_tool_result(x):
    if isinstance(x, str) and x.endswith('.json'):
        with open(x, 'r', encoding='utf-8') as f:
            return json.load(f)
    return x

docs = load_tool_result(var_call_TDnMk5TxCu8yMFjaBkwMw1Gt)

# venue extraction: take first line containing pattern like "XXXX 'YY" or "XXXX 'YYYY" within first 2000 chars
venues=[]
for d in docs:
    txt=(d.get('text') or '')[:3000]
    m=re.search(r"\b([A-Z][A-Z0-9]+)\s*['’`]?\d{2}\b", txt)
    if m:
        venues.append(m.group(1))

from collections import Counter
c=Counter(venues)
print('__RESULT__:')
print(json.dumps({"num_with_venue_pattern": len(venues), "top": c.most_common(15)}))"""

env_args = {'var_call_9X83BuiCEEyXT0BZpBCna1M4': 'file_storage/call_9X83BuiCEEyXT0BZpBCna1M4.json', 'var_call_TDnMk5TxCu8yMFjaBkwMw1Gt': 'file_storage/call_TDnMk5TxCu8yMFjaBkwMw1Gt.json', 'var_call_egAvhU1ylTDfdvxAYA2Oo6Ls': {'total_citation_count_2020_for_CHI_papers': 0, 'num_chi_papers_with_2020_citations': 0}, 'var_call_g8d2v5XBvpSsIzTEcs9vcv3G': {'num_docs': 99, 'num_with_CHI_token_in_first50': 0, 'sample': []}, 'var_call_psJPuKe7nzwBVzyyv38Y8QAv': {'marker_counts': {'CHI': 99, 'SIGCHI': 54, 'Proceedings of the': 55, 'Conference on Human Factors': 53}, 'head_counts': {'UBICOMP': 0, 'CSCW': 0, 'CHI': 0, 'DIS': 0, 'IUI': 0, 'WWW': 0, 'TEI': 0, 'OzCHI': 0, 'AH': 0, 'PervasiveHealth': 0}}}

exec(code, env_args)
