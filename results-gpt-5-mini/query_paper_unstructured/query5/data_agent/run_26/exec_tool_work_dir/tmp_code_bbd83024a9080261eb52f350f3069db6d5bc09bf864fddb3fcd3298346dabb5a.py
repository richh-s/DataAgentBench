code = """import json
import pandas as pd
with open(var_call_pPDTnlGp6ErQmAFXxr58GiX9, 'r', encoding='utf-8') as f:
    citations = json.load(f)
with open(var_call_Z5jebswmSD6KDdpfws5ksVZ8, 'r', encoding='utf-8') as f:
    papers = json.load(f)

df_cit = pd.DataFrame(citations)
df_cit['citations_2020'] = df_cit['citations_2020'].astype(int)
df_p = pd.DataFrame(papers)
if 'filename' in df_p.columns:
    df_p['title'] = df_p['filename'].str.replace(r"\.txt$", '', regex=True)
else:
    df_p['title'] = None

# simple stats
total_citation_titles = df_cit.shape[0]
total_paper_docs = df_p.shape[0]

# intersection of titles
cit_titles = set(df_cit['title'].tolist())
paper_titles = set(df_p['title'].dropna().tolist())
intersection = list(cit_titles & paper_titles)

# detect CHI by presence of 'CHI' word anywhere in text (case-insensitive)
import re

def contains_chi(text):
    if not isinstance(text, str):
        return False
    return bool(re.search(r"\bCHI\b", text, flags=re.IGNORECASE))

_df = df_p.copy()
_df['contains_chi'] = _df['text'].apply(contains_chi)
chi_papers = _df[_df['contains_chi']==True]
chi_titles = chi_papers['title'].dropna().tolist()

# overlapping titles that are CHI
overlap_chi = list(set(intersection) & set(chi_titles))

output = {
    'total_citation_titles': total_citation_titles,
    'total_paper_documents': total_paper_docs,
    'num_intersection_titles': len(intersection),
    'example_intersection_titles': intersection[:20],
    'num_papers_with_CHI_in_text': int(chi_papers.shape[0]),
    'example_CHI_titles': chi_titles[:20],
    'num_overlap_CHI_and_citations': len(overlap_chi),
    'example_overlap_CHI_titles': overlap_chi[:20]
}
print("__RESULT__:")
print(json.dumps(output))"""

env_args = {'var_call_pPDTnlGp6ErQmAFXxr58GiX9': 'file_storage/call_pPDTnlGp6ErQmAFXxr58GiX9.json', 'var_call_BJUQ9l6I9WyLcYhKHWhEQAHV': ['paper_docs'], 'var_call_Z5jebswmSD6KDdpfws5ksVZ8': 'file_storage/call_Z5jebswmSD6KDdpfws5ksVZ8.json', 'var_call_TSoqVuNb60K4hHJjeLKsomzT': {'total_citations_2020': 0, 'num_papers_cited_in_2020': 0, 'papers': []}}

exec(code, env_args)
