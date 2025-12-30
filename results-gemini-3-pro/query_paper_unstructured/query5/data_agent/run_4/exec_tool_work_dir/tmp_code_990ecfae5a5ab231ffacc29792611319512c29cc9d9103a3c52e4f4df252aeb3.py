code = """import json
import re

# Load citations
with open(locals()['var_function-call-18234388167969169864'], 'r') as f:
    citations_2020 = json.load(f)

# Load paper docs
with open(locals()['var_function-call-10773655256875707708'], 'r') as f:
    paper_docs = json.load(f)

# Create a dictionary for citations: title -> count
citation_map = {c['title']: c['citation_count'] for c in citations_2020}

total_citations = 0
chi_papers_count = 0

# Debug list
chi_papers_found = []

for doc in paper_docs:
    filename = doc.get('filename', '')
    if not filename.endswith('.txt'):
        continue
    title = filename[:-4]  # remove .txt
    
    text = doc.get('text', '')
    # Check for CHI venue
    # Look in the first 2000 characters for header info
    header_text = text[:2000]
    
    # Regex for CHI as a whole word, or the full conference name
    # CHI is often written as "CHI 'YY" or "CHI 20YY" or just "CHI Conference"
    # Also checking for "Conference on Human Factors in Computing Systems"
    
    is_chi = False
    if re.search(r'\bCHI\b', header_text) or "Conference on Human Factors in Computing Systems" in header_text:
        is_chi = True
    
    if is_chi:
        chi_papers_count += 1
        if title in citation_map:
            count = citation_map[title]
            total_citations += count
            chi_papers_found.append((title, count))

print("__RESULT__:")
print(json.dumps({"total_citations": total_citations, "chi_papers_count": chi_papers_count, "sample_papers": chi_papers_found[:5]}))"""

env_args = {'var_function-call-18234388167969171677': ['paper_docs'], 'var_function-call-18234388167969169864': 'file_storage/function-call-18234388167969169864.json', 'var_function-call-10773655256875707708': 'file_storage/function-call-10773655256875707708.json'}

exec(code, env_args)
