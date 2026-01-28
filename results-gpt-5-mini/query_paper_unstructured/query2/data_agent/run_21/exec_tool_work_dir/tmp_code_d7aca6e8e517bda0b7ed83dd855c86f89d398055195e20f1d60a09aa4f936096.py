code = """import json, re
with open(var_call_KPR0QfG3IgVsiP9AnZrxJYky, 'r', encoding='utf-8') as f:
    papers = json.load(f)
with open(var_call_0IhcTd0dtQfLFy75CHzl4H5f, 'r', encoding='utf-8') as f:
    citations = json.load(f)

# build mapping and also collect ACM-detected titles
def normalize(s):
    return re.sub(r"\s+", " ", s).strip()

title_to_source = {}
acm_titles = []
for p in papers:
    filename = p.get('filename', '')
    title = filename[:-4] if filename.lower().endswith('.txt') else filename
    text = p.get('text', '') or ''
    src = 'Unknown'
    if re.search(r'\bACM\b', text, re.IGNORECASE):
        src = 'ACM'
    elif re.search(r'\bIEEE\b', text, re.IGNORECASE):
        src = 'IEEE'
    elif re.search(r'PubMed', text, re.IGNORECASE) or re.search(r'Pub Med', text, re.IGNORECASE):
        src = 'PubMed'
    title_norm = normalize(title)
    title_to_source[title_norm] = src
    if src == 'ACM':
        acm_titles.append(title_norm)

# Now check how many citation titles match these
citation_titles = [normalize(c.get('title','')) for c in citations]

matches = [t for t in citation_titles if t in title_to_source]
matched_acm = [t for t in matches if title_to_source.get(t)=='ACM']

sample_acm = acm_titles[:10]
sample_matched_acm = matched_acm[:10]

res = {
    'num_papers_total': len(papers),
    'num_acm_detected_in_papers': len(acm_titles),
    'num_citation_records': len(citations),
    'num_titles_matching_between_dbs': len(matches),
    'num_matched_acm_titles': len(matched_acm),
    'sample_acm_titles': sample_acm,
    'sample_matched_acm_titles': sample_matched_acm
}

print('__RESULT__:')
print(json.dumps(res))"""

env_args = {'var_call_ACVHbXhs6Dqf6k8Z8Zu1aBoy': ['paper_docs'], 'var_call_0IhcTd0dtQfLFy75CHzl4H5f': 'file_storage/call_0IhcTd0dtQfLFy75CHzl4H5f.json', 'var_call_KPR0QfG3IgVsiP9AnZrxJYky': 'file_storage/call_KPR0QfG3IgVsiP9AnZrxJYky.json', 'var_call_3mdlsZh8ZAdDyxaZT5lf0ny5': {'average_citation_count': None, 'paper_count': 0}}

exec(code, env_args)
