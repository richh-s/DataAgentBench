code = """import json
import re

with open(locals()['var_function-call-3271567953918083251'], 'r') as f:
    citations_data = json.load(f)
with open(locals()['var_function-call-5688223812059050868'], 'r') as f:
    paper_docs = json.load(f)

citation_map = {c['title']: int(c['citation_count']) for c in citations_data}

# Regex for CHI
regex_str = r"CHI\s?'\d{2}|CHI\s?20\d{2}|Conference on Human Factors in Computing Systems"
venue_regex = re.compile(regex_str, re.IGNORECASE)

chi_citation_sum = 0
chi_papers_found = 0
chi_papers_with_citations = 0
matched_titles = []

for d in paper_docs:
    filename = d.get('filename', '')
    if not filename.endswith('.txt'):
        continue
    title = filename[:-4]
    
    text = d.get('text', '')
    if venue_regex.search(text[:2000]):
        chi_papers_found += 1
        if title in citation_map:
            chi_papers_with_citations += 1
            chi_citation_sum += citation_map[title]
            matched_titles.append({"title": title, "citations": citation_map[title]})

result_obj = {
    "total_docs": len(paper_docs),
    "chi_papers_found": chi_papers_found,
    "chi_papers_with_citations": chi_papers_with_citations,
    "total_citations": chi_citation_sum,
    "matched_samples": matched_titles[:5]
}

print("__RESULT__:")
print(json.dumps(result_obj))"""

env_args = {'var_function-call-3271567953918083251': 'file_storage/function-call-3271567953918083251.json', 'var_function-call-3271567953918083494': ['paper_docs'], 'var_function-call-17597164597794673073': 'file_storage/function-call-17597164597794673073.json', 'var_function-call-6676021066055813703': 0, 'var_function-call-7180838607779027661': 'Done', 'var_function-call-14386505862075830980': {'total_citations_records': 188, 'total_paper_docs': 5, 'common_titles': 4, 'chi_papers_found': 0, 'chi_papers_with_citations': 0, 'sample_chi_headers': [], 'final_sum': 0}, 'var_function-call-5688223812059050868': 'file_storage/function-call-5688223812059050868.json', 'var_function-call-3535785703897433951': 61}

exec(code, env_args)
