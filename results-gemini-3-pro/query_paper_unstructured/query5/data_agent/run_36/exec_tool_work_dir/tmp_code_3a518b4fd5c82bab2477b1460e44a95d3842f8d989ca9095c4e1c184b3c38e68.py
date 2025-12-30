code = """import json
import re

# Load citations
citations_path = locals()['var_function-call-12939429308500753230']
with open(citations_path, 'r') as f:
    citations = json.load(f)

# Load papers
papers_path = locals()['var_function-call-11830425974286538439']
with open(papers_path, 'r') as f:
    papers = json.load(f)

chi_titles = set()
for p in papers:
    text = p.get('text', '')
    # Check header (first 500 chars)
    header = text[:500]
    
    # Heuristic: 
    # 1. Look for CHI followed by year (e.g., CHI '15, CHI 2015)
    # 2. Look for "Conference on Human Factors in Computing Systems"
    # 3. Look for "Proceedings of the ... CHI"
    # 4. Just "CHI" in all caps as a distinct word in the header is a strong signal for the venue.
    
    is_chi = False
    if "Conference on Human Factors in Computing Systems" in header:
        is_chi = True
    elif re.search(r'\bCHI\b', header):
        # Additional check: ensure it's not "China" or part of a word (handled by \b)
        # Check if it looks like a venue string? 
        # e.g. "CHI 2015", "CHI '15"
        # If it's just "CHI" in the abstract, it might be a reference.
        # But in the first 500 chars, it's likely the venue or copyright.
        is_chi = True
    
    if is_chi:
        title = p.get('filename', '').replace('.txt', '')
        chi_titles.add(title)

total_citations = 0
for c in citations:
    title = c.get('title')
    count = c.get('citation_count')
    try:
        count = int(count)
    except:
        count = 0
        
    if title in chi_titles:
        total_citations += count

print("__RESULT__:")
print(total_citations)"""

env_args = {'var_function-call-16274009200495380828': 'file_storage/function-call-16274009200495380828.json', 'var_function-call-12939429308500753230': 'file_storage/function-call-12939429308500753230.json', 'var_function-call-13758046956340935094': 0, 'var_function-call-9966761655225880711': [], 'var_function-call-14800163327184198750': ['A Lived Informatics Model of Personal Informatics.txt'], 'var_function-call-11830425974286538439': 'file_storage/function-call-11830425974286538439.json'}

exec(code, env_args)
