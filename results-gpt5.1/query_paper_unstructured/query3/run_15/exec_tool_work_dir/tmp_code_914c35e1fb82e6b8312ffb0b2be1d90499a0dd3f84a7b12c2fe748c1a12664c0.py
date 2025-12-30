code = """import re, json, pandas as pd, os, textwrap

# Load full results for papers and citations
with open(var_call_c7tUt2A91ZGDU2PwVp6CSgZj, 'r') as f:
    papers = json.load(f)
with open(var_call_EVLnousZR6IkuWPvHEZqiFG2, 'r') as f:
    citations = json.load(f)

# Helper to extract year from text
year_pattern = re.compile(r'\b(20[0-9]{2}|19[0-9]{2})\b')

def extract_year(text):
    years = [int(y) for y in year_pattern.findall(text)]
    if not years:
        return None
    # Heuristic: publication year likely between 2000 and 2025 and appears near venue line; just take min >= 2000
    cand = [y for y in years if 2000 <= y <= 2025]
    return min(cand) if cand else None

# Build dataframe of papers with filename (title), contribution flag, and year
rows = []
for p in papers:
    text = p.get('text', '') or ''
    # crude contribution detection: look for 'contribution' section mentioning empirical
    contrib_match = re.search(r'contribution[s]?[^\n]*', text, re.IGNORECASE)
    has_empirical = False
    if contrib_match:
        seg = contrib_match.group(0)
        if re.search(r'empirical', seg, re.IGNORECASE):
            has_empirical = True
    # also fallback: anywhere 'empirical study' or 'empirical evaluation'
    if not has_empirical and re.search(r'empirical', text, re.IGNORECASE):
        has_empirical = True
    year = extract_year(text)
    title = (p.get('filename') or '').replace('.txt','')
    rows.append({'title': title, 'year': year, 'has_empirical': has_empirical})

paper_df = pd.DataFrame(rows)

# Filter empirical and year > 2016
paper_emp = paper_df[(paper_df['has_empirical']) & (paper_df['year'].notna()) & (paper_df['year'] > 2016)]

cit_df = pd.DataFrame(citations)
cit_df['total_citations'] = cit_df['total_citations'].astype(int)

merged = pd.merge(paper_emp, cit_df, on='title', how='inner')

result = merged[['title', 'total_citations']].drop_duplicates().sort_values('title').to_dict(orient='records')

out = json.dumps(result)
print("__RESULT__:")
print(out)"""

env_args = {'var_call_c7tUt2A91ZGDU2PwVp6CSgZj': 'file_storage/call_c7tUt2A91ZGDU2PwVp6CSgZj.json', 'var_call_EVLnousZR6IkuWPvHEZqiFG2': 'file_storage/call_EVLnousZR6IkuWPvHEZqiFG2.json'}

exec(code, env_args)
