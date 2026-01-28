code = """import json
import re

# Load citations
with open(locals()['var_function-call-4961661729464848456'], 'r') as f:
    citations = json.load(f)

citation_map = {c['title']: int(c['citation_count']) for c in citations}

# Load papers
with open(locals()['var_function-call-14263536467630025147'], 'r') as f:
    papers = json.load(f)

total_citations = 0
chi_papers = []

for paper in papers:
    filename = paper.get('filename', '')
    if filename.endswith('.txt'):
        title = filename[:-4]
    else:
        title = filename
    
    if title in citation_map:
        text = paper.get('text', '')
        # Check header (first 2000 chars) for CHI
        header = text[:2000]
        # Regex for CHI as a word, or full conference name
        # Case sensitive "CHI" to avoid "Chi"
        if re.search(r'\bCHI\b', header) or "Conference on Human Factors in Computing Systems" in header:
            chi_papers.append(title)
            total_citations += citation_map[title]

print(f"Identified {len(chi_papers)} CHI papers.")
print(f"Titles: {chi_papers}")
print(f"Total citations: {total_citations}")

print("__RESULT__:")
print(json.dumps(total_citations))"""

env_args = {'var_function-call-4961661729464848456': 'file_storage/function-call-4961661729464848456.json', 'var_function-call-4306319526809017372': 188, 'var_function-call-9160616424066584020': 'file_storage/function-call-9160616424066584020.json', 'var_function-call-16237189493323066997': 5, 'var_function-call-14263536467630025147': 'file_storage/function-call-14263536467630025147.json', 'var_function-call-95742628409748684': 1551}

exec(code, env_args)
