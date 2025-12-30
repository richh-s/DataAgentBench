code = """import json
import re

# Load citations
with open(locals()['var_function-call-13891558846941465066'], 'r') as f:
    citations_data = json.load(f)

# Load papers
with open(locals()['var_function-call-4279784200820574316'], 'r') as f:
    papers_data = json.load(f)

# Create a map of title -> citation_count for 2020
citations_map = {}
for item in citations_data:
    citations_map[item['title']] = item['citation_count']

# Filter papers for CHI
chi_papers = []
chi_titles = []

# Regex for CHI
regex_chi = re.compile(r"CHI\s*['’]?\d{2}|CHI\s+20\d{2}|Conference on Human Factors in Computing Systems", re.IGNORECASE)

for paper in papers_data:
    text = paper.get('text', '')
    header = text[:1000]
    if regex_chi.search(header):
        title = paper.get('filename', '').replace('.txt', '')
        chi_papers.append(paper)
        chi_titles.append(title)

total_citations = 0
found_count = 0
missing_count = 0

for title in chi_titles:
    if title in citations_map:
        total_citations += citations_map[title]
        found_count += 1
    else:
        missing_count += 1

debug_info = {
    "citations_records": len(citations_data),
    "papers_records": len(papers_data),
    "chi_papers_identified": len(chi_papers),
    "matched_citations": found_count,
    "missing_citations": missing_count,
    "total_citations": total_citations,
    "sample_chi_titles": chi_titles[:3],
    "sample_citation_titles": list(citations_map.keys())[:3]
}

print("__RESULT__:")
print(json.dumps(debug_info))"""

env_args = {'var_function-call-3161297584091160815': ['paper_docs'], 'var_function-call-3161297584091160886': ['Citations', 'sqlite_sequence'], 'var_function-call-16261242641906617785': 'file_storage/function-call-16261242641906617785.json', 'var_function-call-4279784200820574316': 'file_storage/function-call-4279784200820574316.json', 'var_function-call-13891558846941465066': 'file_storage/function-call-13891558846941465066.json', 'var_function-call-14966924842371218906': 0}

exec(code, env_args)
