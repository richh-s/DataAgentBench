code = """import json
import re

# Load citations
with open(locals()['var_function-call-9485982252767693581'], 'r') as f:
    citations = json.load(f)

# Load papers
# The previous query returned all papers (or a large subset)
with open(locals()['var_function-call-18114231173969465501'], 'r') as f:
    papers = json.load(f)

# Create lookup for citations
# key: title, value: citation_count
citation_map = {c['title']: c['citation_count'] for c in citations}

total_citations = 0
matched_papers = []

for paper in papers:
    filename = paper.get('filename', '')
    if filename.endswith('.txt'):
        title = filename[:-4]
    else:
        title = filename
    
    # Check if this paper is in our citation list (cited in 2020)
    if title in citation_map:
        text = paper.get('text', '')
        # Check for CHI in the first 2000 chars
        # We look for CHI as a whole word, case sensitive
        # Also, venue might be in the header.
        header = text[:2000]
        if re.search(r'\bCHI\b', header):
            count = citation_map[title]
            # Ensure count is int
            try:
                count = int(count)
            except:
                count = 0
            total_citations += count
            matched_papers.append(title)

print(f"Matched {len(matched_papers)} papers.")
print("__RESULT__:")
print(total_citations)"""

env_args = {'var_function-call-9485982252767693581': 'file_storage/function-call-9485982252767693581.json', 'var_function-call-9485982252767692568': 'file_storage/function-call-9485982252767692568.json', 'var_function-call-2245160326568444986': 188, 'var_function-call-11048170535639833603': 'file_storage/function-call-11048170535639833603.json', 'var_function-call-18114231173969465501': 'file_storage/function-call-18114231173969465501.json'}

exec(code, env_args)
