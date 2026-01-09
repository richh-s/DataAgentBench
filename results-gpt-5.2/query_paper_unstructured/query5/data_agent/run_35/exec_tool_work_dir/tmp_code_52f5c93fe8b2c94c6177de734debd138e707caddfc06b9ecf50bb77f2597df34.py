code = """import json, re
import pandas as pd

def load_result(x):
    if isinstance(x, str) and x.endswith('.json'):
        with open(x, 'r', encoding='utf-8') as f:
            return json.load(f)
    return x

docs = load_result(var_call_cphjc5O0IOLxmsCEA7Ano7hV)

# Inspect venue markers frequency
patterns = [
    r"\bCHI\b", r"SIGCHI", r"CHI '\d{2}", r"CHI\s*\d{4}", r"Proceedings of the SIGCHI"
]
counts = {p:0 for p in patterns}
examples = {p:[] for p in patterns}
for d in docs:
    title = re.sub(r'\.txt$', '', d.get('filename',''))
    text = d.get('text','') or ''
    for p in patterns:
        if re.search(p, text, flags=re.IGNORECASE):
            counts[p]+=1
            if len(examples[p])<3:
                # capture snippet
                m = re.search(p, text, flags=re.IGNORECASE)
                s = max(0, m.start()-40); e=min(len(text), m.end()+40)
                examples[p].append({'title':title,'snippet':text[s:e].replace('\n',' ')})

print('__RESULT__:')
print(json.dumps({'counts':counts,'examples':examples}))"""

env_args = {'var_call_716txXTTK91v7II6hqFJ85pn': 'file_storage/call_716txXTTK91v7II6hqFJ85pn.json', 'var_call_cphjc5O0IOLxmsCEA7Ano7hV': 'file_storage/call_cphjc5O0IOLxmsCEA7Ano7hV.json', 'var_call_CQxBm5IY6AC5kgbgUYPKZN1p': {'citation_year': 2020, 'num_chi_papers_cited_in_2020': 0, 'total_citations_2020_for_chi_papers': 0}}

exec(code, env_args)
