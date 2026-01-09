code = """import json, re

def load_records(x):
    if isinstance(x, str) and x.endswith('.json'):
        with open(x, 'r', encoding='utf-8') as f:
            return json.load(f)
    return x

docs = load_records(var_call_pvTCjSMWywozLbTWbJxMrYkz)

# Count venue markers occurrences in first 2000 chars
patterns = {
    'CHI': r"\bCHI\b",
    'UbiComp': r"\bUBICOMP\b",
    'CSCW': r"\bCSCW\b",
    'DIS': r"\bDIS\b",
    'OzCHI': r"\bOzCHI\b",
    'TEI': r"\bTEI\b",
    'PervasiveHealth': r"\bPervasiveHealth\b",
}
counts={k:0 for k in patterns}
examples={k:None for k in patterns}
for d in docs:
    text=(d.get('text') or '')[:2000]
    for k,pat in patterns.items():
        if re.search(pat, text, flags=re.IGNORECASE):
            counts[k]+=1
            if examples[k] is None:
                examples[k]=d.get('filename')

out={'counts':counts,'examples':examples,'num_docs':len(docs)}
print('__RESULT__:')
print(json.dumps(out))"""

env_args = {'var_call_BcWhDTVY3BnFEfednxP48zAS': 'file_storage/call_BcWhDTVY3BnFEfednxP48zAS.json', 'var_call_pvTCjSMWywozLbTWbJxMrYkz': 'file_storage/call_pvTCjSMWywozLbTWbJxMrYkz.json', 'var_call_bASQvEW0WB1P5KWNnl7YQG56': {'total_citations_2020_for_CHI_papers': 0, 'num_chi_papers_cited_in_2020': 0}}

exec(code, env_args)
