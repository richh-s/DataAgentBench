code = """import json
import re

with open(locals()['var_function-call-3271567953918083251'], 'r') as f:
    citations_data = json.load(f)
with open(locals()['var_function-call-17597164597794673073'], 'r') as f:
    paper_docs = json.load(f)

c_titles = set(c['title'] for c in citations_data)
citation_map = {c['title']: int(c['citation_count']) for c in citations_data}

p_titles = set(d['filename'][:-4] for d in paper_docs if d['filename'].endswith('.txt'))
common_titles = list(c_titles.intersection(p_titles))

venue_regex = re.compile(r"CHI\s?'\d{2}|CHI\s?20\d{2}|Conference on Human Factors in Computing Systems", re.IGNORECASE)

chi_papers = []
chi_headers = []
for d in paper_docs:
    if venue_regex.search(d['text'][:1000]):
        chi_papers.append(d['filename'][:-4])
        if len(chi_headers) < 3:
            chi_headers.append(d['text'][:100])

# Intersect CHI papers with Citations
chi_papers_set = set(chi_papers)
papers_with_citations = chi_papers_set.intersection(c_titles)

total_citations = 0
for title in papers_with_citations:
    total_citations += citation_map[title]

debug_info = {
    "total_citations_records": len(citations_data),
    "total_paper_docs": len(paper_docs),
    "common_titles": len(common_titles),
    "chi_papers_found": len(chi_papers),
    "chi_papers_with_citations": len(papers_with_citations),
    "sample_chi_headers": chi_headers,
    "final_sum": total_citations
}

print("__RESULT__:")
print(json.dumps(debug_info))"""

env_args = {'var_function-call-3271567953918083251': 'file_storage/function-call-3271567953918083251.json', 'var_function-call-3271567953918083494': ['paper_docs'], 'var_function-call-17597164597794673073': 'file_storage/function-call-17597164597794673073.json', 'var_function-call-6676021066055813703': 0, 'var_function-call-7180838607779027661': 'Done'}

exec(code, env_args)
