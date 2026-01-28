code = """import json
import pandas as pd
import re

# Load data from storage files
with open(var_call_4EFqrNYfrs8yFpChOBcDWvsl, 'r', encoding='utf-8') as f:
    data_citations = json.load(f)
with open(var_call_2yhsNBZQnu2ffxQCZqh7e4hH, 'r', encoding='utf-8') as f:
    data_papers = json.load(f)

# DataFrames
cit = pd.DataFrame(data_citations)
papers = pd.DataFrame(data_papers)

# Normalize citation_count
cit['citation_count'] = pd.to_numeric(cit['citation_count'], errors='coerce').fillna(0).astype(int)

# Extract title from filename
papers['title'] = papers['filename'].str.replace(r"\.txt$", '', regex=True)

# Build dict title -> text
title_to_text = dict(zip(papers['title'], papers['text'].fillna('')))

# Intersection of titles
titles_in_both = set(cit['title']).intersection(set(papers['title']))

# Patterns indicating CHI
patterns = [r"\bCHI\b", r"SIGCHI", r"Proceedings of the SIGCHI", r"Proceedings.*CHI", r"ACM CHI", r"Human Factors in Computing Systems", r"CHI\s*'", r"CHI\s*20\d{2}", r"CHI:\"]

chi_titles = []
for t in sorted(titles_in_both):
    text = title_to_text.get(t, '')
    found = False
    for pat in patterns:
        if re.search(pat, text, flags=re.IGNORECASE|re.DOTALL):
            found = True
            break
    if found:
        chi_titles.append(t)

# For any titles not matched by patterns, also check filename for 'CHI' or 'chi' or conference year patterns
for t in sorted(titles_in_both):
    if t in chi_titles:
        continue
    fn = None
    # find filename
    # reverse mapping
    try:
        fn = papers.loc[papers['title']==t, 'filename'].iloc[0]
    except Exception:
        fn = ''
    if fn and re.search(r"\bCHI\b", fn, flags=re.IGNORECASE):
        chi_titles.append(t)

# As a fallback, check if the paper text contains typical CHI ACM copyright lines like 'ACM' and year and 'CHI'
# (already covered), else check venue lines near top (first 500 chars) for 'CHI' variants
for t in sorted(titles_in_both):
    if t in chi_titles:
        continue
    text = title_to_text.get(t, '')
    header = text[:800]
    if re.search(r"CHI|SIGCHI|Human Factors in Computing Systems|CHI'|ACM SIGCHI|Proceedings", header, flags=re.IGNORECASE):
        chi_titles.append(t)

chi_titles = sorted(set(chi_titles))

# Now sum citation counts for these titles from cit dataframe
chi_cit_df = cit[cit['title'].isin(chi_titles)].copy()

total_citations = int(chi_cit_df['citation_count'].sum())

# Prepare detailed list of titles and counts
titles_counts = chi_cit_df[['title', 'citation_count']].sort_values(by='citation_count', ascending=False).to_dict(orient='records')

result = {
    'total_citations_for_CHI_papers_in_2020': total_citations,
    'num_chi_papers_cited_in_2020': len(titles_counts),
    'papers': titles_counts
}

print("__RESULT__:")
print(json.dumps(result))"""

env_args = {'var_call_4EFqrNYfrs8yFpChOBcDWvsl': 'file_storage/call_4EFqrNYfrs8yFpChOBcDWvsl.json', 'var_call_JJ4mKnI7jt2F0rjjoG3g96oU': ['paper_docs'], 'var_call_2yhsNBZQnu2ffxQCZqh7e4hH': 'file_storage/call_2yhsNBZQnu2ffxQCZqh7e4hH.json', 'var_call_CyA4TwHOpP9WArQOHRRwUJJa': {'total_citations': 0, 'num_papers': 0}, 'var_call_Otdj0nrxCx3VsmIzY64kQNPc': 'file_storage/call_Otdj0nrxCx3VsmIzY64kQNPc.json'}

exec(code, env_args)
