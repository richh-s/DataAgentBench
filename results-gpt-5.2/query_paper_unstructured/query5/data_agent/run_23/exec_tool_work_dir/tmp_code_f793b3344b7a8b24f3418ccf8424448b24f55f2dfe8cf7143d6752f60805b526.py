code = """import json, re, pandas as pd

def load_result(x):
    if isinstance(x, str) and x.endswith('.json'):
        with open(x, 'r', encoding='utf-8') as f:
            return json.load(f)
    return x

cit2020 = load_result(var_call_c8X70NcPSwEBlNBxf1HSl4QO)
docs = load_result(var_call_ppdg6auIbq2cqpU8luUDixQU)

# Build set of CHI paper titles based on text containing 'CHI' conference marker
chi_titles = set()
for d in docs:
    fn = d.get('filename','')
    if not fn.endswith('.txt'):
        continue
    title = fn[:-4]
    text = d.get('text') or ''
    # heuristic: detect CHI venue strings
    if re.search(r'\bCHI\s*[’\']?\d{2}\b', text) or re.search(r'\bCHI\s+\d{4}\b', text) or re.search(r'\bProceedings\s+of\s+the\s+SIGCHI\b', text) or re.search(r'\bSIGCHI\b', text):
        chi_titles.add(title)

# Sum citation counts in 2020 for those titles
rows = []
for r in cit2020:
    t = r.get('title')
    if t in chi_titles:
        try:
            c = int(r.get('citation_count'))
        except Exception:
            c = 0
        rows.append((t,c))

df = pd.DataFrame(rows, columns=['title','citation_count'])

total = int(df['citation_count'].sum()) if len(df) else 0
paper_count = int(df['title'].nunique()) if len(df) else 0

out = {
    "total_citations_2020_for_CHI_papers": total,
    "num_CHI_papers_cited_in_2020": paper_count
}

print('__RESULT__:')
print(json.dumps(out))"""

env_args = {'var_call_c8X70NcPSwEBlNBxf1HSl4QO': 'file_storage/call_c8X70NcPSwEBlNBxf1HSl4QO.json', 'var_call_ppdg6auIbq2cqpU8luUDixQU': 'file_storage/call_ppdg6auIbq2cqpU8luUDixQU.json'}

exec(code, env_args)
