code = """import json
import re

with open(locals()['var_function-call-3271567953918083251'], 'r') as f:
    citations_data = json.load(f)
with open(locals()['var_function-call-5688223812059050868'], 'r') as f:
    paper_docs = json.load(f)

c_titles = set(c['title'] for c in citations_data)
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
    # Check first 2000 chars
    header = text[:2000]
    
    if venue_regex.search(header):
        chi_papers_found += 1
        if title in citation_map:
            chi_papers_with_citations += 1
            chi_citation_sum += citation_map[title]
            matched_titles.append(title)

print("DEBUG: Total papers:", len(paper_docs))
print("DEBUG: CHI papers found:", chi_papers_found)
print("DEBUG: CHI papers with citations:", chi_papers_with_citations)
print("DEBUG: Total CHI Citations:", chi_citation_sum)
if matched_titles:
    print("DEBUG: Sample matched titles:", matched_titles[:3])

print("__RESULT__:")
print(json.dumps(chi_citation_sum))"""

env_args = {'var_function-call-3271567953918083251': 'file_storage/function-call-3271567953918083251.json', 'var_function-call-3271567953918083494': ['paper_docs'], 'var_function-call-17597164597794673073': 'file_storage/function-call-17597164597794673073.json', 'var_function-call-6676021066055813703': 0, 'var_function-call-7180838607779027661': 'Done', 'var_function-call-14386505862075830980': {'total_citations_records': 188, 'total_paper_docs': 5, 'common_titles': 4, 'chi_papers_found': 0, 'chi_papers_with_citations': 0, 'sample_chi_headers': [], 'final_sum': 0}, 'var_function-call-5688223812059050868': 'file_storage/function-call-5688223812059050868.json'}

exec(code, env_args)
