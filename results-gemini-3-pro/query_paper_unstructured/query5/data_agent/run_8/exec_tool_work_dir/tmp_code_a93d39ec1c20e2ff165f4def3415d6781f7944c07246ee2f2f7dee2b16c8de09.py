code = """import json
import re

# Load citations
with open(locals()['var_function-call-4961661729464848456'], 'r') as f:
    citations = json.load(f)

# Create a lookup for citation counts by title
citation_map = {c['title']: int(c['citation_count']) for c in citations}
cited_titles = set(citation_map.keys())

# Load papers
with open(locals()['var_function-call-14263536467630025147'], 'r') as f:
    papers = json.load(f)

print(f"Loaded {len(papers)} papers.")

total_citations = 0
matched_papers = 0
chi_papers_count = 0

for paper in papers:
    # Extract title from filename
    filename = paper.get('filename', '')
    if filename.endswith('.txt'):
        title = filename[:-4]
    else:
        title = filename
    
    # Check if this paper was cited in 2020 (i.e., is in our citation map)
    if title in citation_map:
        matched_papers += 1
        text = paper.get('text', '')
        
        # Check for CHI venue
        # Heuristics: Look for "CHI" as a whole word, or the full name.
        # Often appears as "CHI 'XX" or "CHI 20XX"
        if re.search(r'\bCHI\b', text) or "Conference on Human Factors in Computing Systems" in text:
            chi_papers_count += 1
            total_citations += citation_map[title]

print(f"Papers matching citation list: {matched_papers}")
print(f"Papers identified as CHI: {chi_papers_count}")
print(f"Total citations: {total_citations}")

print("__RESULT__:")
print(json.dumps(total_citations))"""

env_args = {'var_function-call-4961661729464848456': 'file_storage/function-call-4961661729464848456.json', 'var_function-call-4306319526809017372': 188, 'var_function-call-9160616424066584020': 'file_storage/function-call-9160616424066584020.json', 'var_function-call-16237189493323066997': 5, 'var_function-call-14263536467630025147': 'file_storage/function-call-14263536467630025147.json'}

exec(code, env_args)
