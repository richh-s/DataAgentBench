code = """import json
import re

# Load citations
citations_file = locals()['var_function-call-10006919701169471588']
with open(citations_file, 'r') as f:
    citations_data = json.load(f)

# Load papers
papers_file = locals()['var_function-call-6614480246128303859']
with open(papers_file, 'r') as f:
    papers_data = json.load(f)

chi_titles = set()

for paper in papers_data:
    text = paper.get('text', '')
    filename = paper.get('filename', '')
    title = filename.replace('.txt', '')
    
    # Check header for CHI
    # Limit to first 500 chars
    header = text[:500]
    
    # Patterns for CHI
    # 1. CHI 'YY or CHI 20YY
    # 2. Conference on Human Factors in Computing Systems
    # 3. Proceedings of the ... CHI ...
    
    # Regex checks
    is_chi = False
    
    # Check for "CHI" with word boundaries, case sensitive as CHI is an acronym
    # However, sometimes it might be "Chi". But usually CHI.
    if re.search(r'\bCHI\b', header):
        is_chi = True
    elif "Conference on Human Factors in Computing Systems" in header:
        is_chi = True
        
    if is_chi:
        chi_titles.add(title)

# Filter citations
total_citations = 0
matched_papers = 0

for cit in citations_data:
    cit_title = cit['title']
    cit_count = cit['citation_count']
    
    if cit_title in chi_titles:
        total_citations += int(cit_count)
        matched_papers += 1

result = {
    "total_citations": total_citations,
    "chi_paper_count": len(chi_titles),
    "matched_citation_records": matched_papers
}

print("__RESULT__:")
print(json.dumps(result))"""

env_args = {'var_function-call-10006919701169471588': 'file_storage/function-call-10006919701169471588.json', 'var_function-call-10006919701169474509': 'file_storage/function-call-10006919701169474509.json', 'var_function-call-6614480246128303859': 'file_storage/function-call-6614480246128303859.json'}

exec(code, env_args)
