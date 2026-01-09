code = """import json, pandas as pd, re

# Load citations 2020
cit_path = var_call_EKtGZXxv277yQXqhyqnzYrmB
with open(cit_path, 'r', encoding='utf-8') as f:
    cit_records = json.load(f)

# Load paper docs
docs_path = var_call_k9rUOUEo0omsrgNndTbOdtXK
with open(docs_path, 'r', encoding='utf-8') as f:
    doc_records = json.load(f)

# Build title set for CHI papers by detecting venue in text
chi_titles = set()
for d in doc_records:
    fn = d.get('filename','')
    if not fn.endswith('.txt'):
        continue
    title = fn[:-4]
    text = (d.get('text') or '')
    # detect CHI as venue: look for patterns like "CHI 'YY" or "CHI 20" or "Proceedings of the SIGCHI"
    t = text.upper()
    if (re.search(r"\bCHI\s*'\d{2}\b", t) or re.search(r"\bCHI\s+\d{4}\b", t) or ('SIGCHI' in t and 'CHI' in t)):
        chi_titles.add(title)

# Join with citations (citation_count may be str)
rows = []
for r in cit_records:
    title = r.get('title')
    if title in chi_titles:
        try:
            cc = int(r.get('citation_count') or 0)
        except:
            cc = 0
        rows.append({'title': title, 'citation_count_2020': cc})

# Summarize total and include per-paper list (all papers presented at CHI and cited in 2020)
df = pd.DataFrame(rows)
if df.empty:
    out = {'total_citations_2020_for_CHI_papers': 0, 'paper_count': 0, 'per_paper': []}
else:
    df = df.sort_values(['citation_count_2020','title'], ascending=[False, True])
    out = {
        'total_citations_2020_for_CHI_papers': int(df['citation_count_2020'].sum()),
        'paper_count': int(df.shape[0]),
        'per_paper': df.to_dict(orient='records')
    }

print('__RESULT__:')
print(json.dumps(out, ensure_ascii=False))"""

env_args = {'var_call_EKtGZXxv277yQXqhyqnzYrmB': 'file_storage/call_EKtGZXxv277yQXqhyqnzYrmB.json', 'var_call_k9rUOUEo0omsrgNndTbOdtXK': 'file_storage/call_k9rUOUEo0omsrgNndTbOdtXK.json'}

exec(code, env_args)
