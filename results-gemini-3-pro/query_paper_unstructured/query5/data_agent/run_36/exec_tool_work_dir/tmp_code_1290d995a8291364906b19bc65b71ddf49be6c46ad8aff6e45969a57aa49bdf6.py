code = """import json
import re

# Load citations
citations_path = locals()['var_function-call-12939429308500753230']
with open(citations_path, 'r') as f:
    citations = json.load(f)

# Load papers
papers_path = locals()['var_function-call-16274009200495380828']
with open(papers_path, 'r') as f:
    papers = json.load(f)

chi_titles = set()
debug_info = []

for p in papers:
    text = p.get('text', '')
    # Check the first 1000 characters for venue info
    header = text[:1000]
    
    # Heuristic for CHI
    # Looking for 'CHI' as a distinct word, often followed by year or part of 'CHI Conference'
    # Also checking for the full name.
    # We can be slightly loose but \bCHI\b is good.
    if re.search(r'\bCHI\b', header) or "Conference on Human Factors in Computing Systems" in header:
        title = p.get('filename', '').replace('.txt', '')
        chi_titles.add(title)
        if len(debug_info) < 5:
            debug_info.append(title)

total_citations = 0
matched_papers = 0
for c in citations:
    title = c.get('title')
    count = c.get('citation_count')
    # Handle int/str conversion for count
    try:
        count = int(count)
    except:
        count = 0
        
    if title in chi_titles:
        total_citations += count
        matched_papers += 1

print(f"DEBUG: Found {len(chi_titles)} CHI papers in docs.")
print(f"DEBUG: Matched {matched_papers} CHI papers with citations in 2020.")
print(f"DEBUG: Sample CHI titles: {debug_info}")

print("__RESULT__:")
print(total_citations)"""

env_args = {'var_function-call-16274009200495380828': 'file_storage/function-call-16274009200495380828.json', 'var_function-call-12939429308500753230': 'file_storage/function-call-12939429308500753230.json'}

exec(code, env_args)
