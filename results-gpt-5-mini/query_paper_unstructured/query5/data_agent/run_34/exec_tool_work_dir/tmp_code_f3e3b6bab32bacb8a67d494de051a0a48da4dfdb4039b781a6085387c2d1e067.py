code = """import json, re
with open(var_call_2bAjaySMuMe33fCE9m2xfmXn, 'r', encoding='utf-8') as f:
    citations_data = json.load(f)
with open(var_call_wAsr13mFxq2D2MUGPbhJu8fy, 'r', encoding='utf-8') as f:
    papers = json.load(f)

paper_titles = {p['filename'][:-4]: p for p in papers if p.get('filename','').endswith('.txt')}
citation_titles = [c['title'] for c in citations_data]

num_citation_titles = len(citation_titles)
num_paper_docs = len(papers)

# intersection
matched_titles = [t for t in citation_titles if t in paper_titles]
num_matched = len(matched_titles)

# count matched papers that mention CHI in their text
chi_re = re.compile(r"\bCHI\b", re.IGNORECASE)
matched_with_chi = []
for t in matched_titles:
    text = paper_titles[t].get('text','')
    if chi_re.search(text):
        matched_with_chi.append(t)

output = {
    'num_citation_records_2020': num_citation_titles,
    'num_paper_documents': num_paper_docs,
    'num_titles_in_both': num_matched,
    'num_matched_with_CHI_in_text': len(matched_with_chi),
    'sample_matched_titles': matched_titles[:20],
    'sample_matched_with_CHI': matched_with_chi[:20]
}

print("__RESULT__:")
print(json.dumps(output))"""

env_args = {'var_call_eeoUlpIf6RV1DGs1dvCSwE5Y': ['paper_docs'], 'var_call_Q5cWEdrlC2DtUePUiKYJHMQa': ['Citations', 'sqlite_sequence'], 'var_call_2bAjaySMuMe33fCE9m2xfmXn': 'file_storage/call_2bAjaySMuMe33fCE9m2xfmXn.json', 'var_call_wAsr13mFxq2D2MUGPbhJu8fy': 'file_storage/call_wAsr13mFxq2D2MUGPbhJu8fy.json', 'var_call_sfCknWDbePWzx0Z5KXKFc2G8': {'num_papers': 0, 'total_citations_2020': 0, 'papers': []}}

exec(code, env_args)
