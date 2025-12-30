code = """import json
import re

# Load citations
citations_file = locals()['var_function-call-937877723818181910']
with open(citations_file, 'r') as f:
    citations_data = json.load(f)

citations_titles = set()
for entry in citations_data:
    citations_titles.add(entry['title'])

# Load papers
papers_file = locals()['var_function-call-4834077622578291638']
with open(papers_file, 'r') as f:
    papers_data = json.load(f)

paper_titles = set()
chi_titles = set()

# Regex for CHI
chi_patterns = [
    r"CHI\s+'\d{2}",
    r"CHI\s+20\d{2}",
    r"CHI\s+Conference",
    r"Conference on Human Factors in Computing Systems"
]
compiled_patterns = [re.compile(p, re.IGNORECASE) for p in chi_patterns]

for paper in papers_data:
    filename = paper.get('filename', '')
    title = filename.replace('.txt', '')
    paper_titles.add(title)
    
    text = paper.get('text', '')
    header = text[:2000]
    is_chi = False
    for p in compiled_patterns:
        if p.search(header):
            is_chi = True
            break
    if is_chi:
        chi_titles.add(title)

print(f"Total citations loaded: {len(citations_titles)}")
print(f"Total papers loaded: {len(paper_titles)}")
print(f"Intersection of papers and citations: {len(paper_titles.intersection(citations_titles))}")
print(f"Identified CHI papers: {len(chi_titles)}")
print(f"Intersection of CHI papers and citations: {len(chi_titles.intersection(citations_titles))}")

print("Sample Citation Titles:", list(citations_titles)[:3])
print("Sample Paper Titles:", list(paper_titles)[:3])
if len(chi_titles) > 0:
    print("Sample CHI Titles:", list(chi_titles)[:3])

print("__RESULT__:")
print(json.dumps("debug"))"""

env_args = {'var_function-call-937877723818181910': 'file_storage/function-call-937877723818181910.json', 'var_function-call-937877723818184371': 'file_storage/function-call-937877723818184371.json', 'var_function-call-5956507868376137751': 'file_storage/function-call-5956507868376137751.json', 'var_function-call-4834077622578291638': 'file_storage/function-call-4834077622578291638.json', 'var_function-call-13589113433172976096': 16}

exec(code, env_args)
