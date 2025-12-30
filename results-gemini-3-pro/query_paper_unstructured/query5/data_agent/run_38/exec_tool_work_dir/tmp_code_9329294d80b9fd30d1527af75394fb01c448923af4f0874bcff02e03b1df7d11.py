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

debug_info = {
    "citations_count": len(citations_titles),
    "papers_count": len(paper_titles),
    "intersection_all": len(paper_titles.intersection(citations_titles)),
    "chi_count": len(chi_titles),
    "intersection_chi": len(chi_titles.intersection(citations_titles)),
    "sample_citations": list(citations_titles)[:3],
    "sample_papers": list(paper_titles)[:3],
    "sample_chi": list(chi_titles)[:3]
}

print("__RESULT__:")
print(json.dumps(debug_info))"""

env_args = {'var_function-call-937877723818181910': 'file_storage/function-call-937877723818181910.json', 'var_function-call-937877723818184371': 'file_storage/function-call-937877723818184371.json', 'var_function-call-5956507868376137751': 'file_storage/function-call-5956507868376137751.json', 'var_function-call-4834077622578291638': 'file_storage/function-call-4834077622578291638.json', 'var_function-call-13589113433172976096': 16, 'var_function-call-17003770300273918978': 'debug'}

exec(code, env_args)
