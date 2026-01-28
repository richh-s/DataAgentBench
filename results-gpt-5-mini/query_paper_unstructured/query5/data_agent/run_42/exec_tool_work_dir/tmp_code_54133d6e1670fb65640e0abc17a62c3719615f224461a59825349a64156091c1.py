code = """import json
import re
import pandas as pd

with open(var_call_wUhxLxFcVguqIU7X1OUE1nAP, 'r', encoding='utf-8') as f:
    citations = json.load(f)
with open(var_call_bLpC6T6gFnPJTLEqwOqSEsjz, 'r', encoding='utf-8') as f:
    paper_docs = json.load(f)

# DataFrames
c_df = pd.DataFrame(citations)
p_df = pd.DataFrame(paper_docs)

# Normalize titles
c_df['title'] = c_df['title'].str.strip()
p_df['title'] = p_df['filename'].str.replace(r"\.txt$", '', regex=True).str.strip()

# How many citation titles match any paper_doc title?
merged_all = pd.merge(c_df, p_df[['title']], on='title', how='inner')
num_matches_all = len(merged_all)

# For each matched paper in paper_docs, check if its text contains 'CHI' (case-insensitive)
def contains_chi(text):
    if not isinstance(text, str):
        return False
    return bool(re.search(r"\bCHI\b", text, flags=re.IGNORECASE) or re.search(r"SIGCHI", text, flags=re.IGNORECASE) or re.search(r"Conference on Human Factors in Computing Systems", text, flags=re.IGNORECASE))

# Build mapping title -> text for matched titles
title_to_text = {p['filename'].replace('.txt',''): p.get('text','') for p in paper_docs}

matched_records = []
for idx, row in c_df.iterrows():
    title = row['title']
    if title in title_to_text:
        text = title_to_text[title]
        is_chi = contains_chi(text)
        matched_records.append({'title': title, 'citation_count': int(row['citation_count']), 'is_chi': is_chi})

# Filter only is_chi True
chi_matches = [r for r in matched_records if r['is_chi']]

total_citations_chi = sum(r['citation_count'] for r in chi_matches)

result = {
    'num_citation_titles_total': len(c_df),
    'num_paper_docs_total': len(p_df),
    'num_titles_matching_paper_docs': num_matches_all,
    'num_chi_matches': len(chi_matches),
    'total_citations_2020_for_CHI_papers': total_citations_chi,
    'chi_papers': chi_matches[:100]  # include up to first 100
}

print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_call_wUhxLxFcVguqIU7X1OUE1nAP': 'file_storage/call_wUhxLxFcVguqIU7X1OUE1nAP.json', 'var_call_bLpC6T6gFnPJTLEqwOqSEsjz': 'file_storage/call_bLpC6T6gFnPJTLEqwOqSEsjz.json', 'var_call_xsN1Yb2XH5Jp63LSxzRuw6xn': {'total_citations_2020_for_CHI_papers': 0, 'num_papers_counted': 0, 'papers': []}}

exec(code, env_args)
