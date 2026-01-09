code = """import json, re
import pandas as pd

def load_tool_result(x):
    if isinstance(x, str) and x.endswith('.json'):
        with open(x, 'r', encoding='utf-8') as f:
            return json.load(f)
    return x

docs = load_tool_result(var_call_TDnMk5TxCu8yMFjaBkwMw1Gt)

sample=[]
for d in docs[:50]:
    txt=(d.get('text') or '')
    if re.search(r"\bCHI\b", txt, flags=re.IGNORECASE):
        sample.append({"filename": d.get('filename'), "chi_snip": re.findall(r".{0,40}CHI.{0,40}", txt, flags=re.IGNORECASE)[:2]})

print('__RESULT__:')
print(json.dumps({"num_docs": len(docs), "num_with_CHI_token_in_first50": len(sample), "sample": sample[:5]}))"""

env_args = {'var_call_9X83BuiCEEyXT0BZpBCna1M4': 'file_storage/call_9X83BuiCEEyXT0BZpBCna1M4.json', 'var_call_TDnMk5TxCu8yMFjaBkwMw1Gt': 'file_storage/call_TDnMk5TxCu8yMFjaBkwMw1Gt.json', 'var_call_egAvhU1ylTDfdvxAYA2Oo6Ls': {'total_citation_count_2020_for_CHI_papers': 0, 'num_chi_papers_with_2020_citations': 0}}

exec(code, env_args)
