code = """import json
import re

citations_path = locals()['var_function-call-12939429308500753230']
with open(citations_path, 'r') as f:
    citations = json.load(f)

papers_path = locals()['var_function-call-11830425974286538439']
with open(papers_path, 'r') as f:
    papers = json.load(f)

print(f"DEBUG: Total papers: {len(papers)}")
print(f"DEBUG: Total citations records: {len(citations)}")

# Check for CHI in all text of first 10 papers
for i, p in enumerate(papers[:10]):
    text = p.get('text', '')
    title = p.get('filename', '')
    if "CHI" in text:
        print(f"DEBUG: Paper {i} '{title}' has CHI in text. Index: {text.find('CHI')}")
        print(f"DEBUG: Snippet: {text[text.find('CHI'):text.find('CHI')+50]}")
    else:
        print(f"DEBUG: Paper {i} '{title}' does NOT have CHI in text.")

# Check titles overlap
paper_titles = set(p.get('filename', '').replace('.txt', '') for p in papers)
citation_titles = set(c.get('title') for c in citations)

overlap = paper_titles.intersection(citation_titles)
print(f"DEBUG: Overlap count: {len(overlap)}")
print(f"DEBUG: Sample overlap: {list(overlap)[:5]}")

print("__RESULT__:")
print(json.dumps({"status": "debug complete"}))"""

env_args = {'var_function-call-16274009200495380828': 'file_storage/function-call-16274009200495380828.json', 'var_function-call-12939429308500753230': 'file_storage/function-call-12939429308500753230.json', 'var_function-call-13758046956340935094': 0, 'var_function-call-9966761655225880711': [], 'var_function-call-14800163327184198750': ['A Lived Informatics Model of Personal Informatics.txt'], 'var_function-call-11830425974286538439': 'file_storage/function-call-11830425974286538439.json', 'var_function-call-2236700066034859830': 0}

exec(code, env_args)
