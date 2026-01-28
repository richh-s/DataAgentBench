code = """import re
import json

# Read the full paper documents result
paper_docs_path = var_functions.query_db:3
with open(paper_docs_path, 'r') as f:
    paper_docs = json.load(f)

# Read the 2020 citations result
citations_2020 = var_functions.query_db:1

# Extract CHI papers from documents with their titles
chi_papers = []
for doc in paper_docs:
    filename = doc.get('filename', '')
    text = doc.get('text', '')
    
    # Extract title from filename
    title = filename.replace('.txt', '') if filename else ''
    
    # Check if this is a CHI paper by looking for CHI venue indicators
    # Look for patterns like "CHI 'YY", "CHI 20YY", "Proceedings of CHI", etc.
    chi_patterns = [
        r"CHI\s+'\d{2}",
        r"CHI\s+20\d{2}",
        r"Proceedings of CHI",
        r"CHI Conference",
        r"ACM.*CHI"
    ]
    
    is_chi = any(re.search(pattern, text) for pattern in chi_patterns)
    
    if is_chi and title:
        chi_papers.append(title)

# Create a set of CHI paper titles for fast lookup
chi_titles_set = set(chi_papers)

# Sum citation counts for CHI papers in 2020
total_citations = 0
matched_papers = []

for citation in citations_2020:
    cit_title = citation.get('title', '')
    cit_count = int(citation.get('citation_count', 0))
    
    # Check if this title matches a CHI paper
    # Use case-insensitive matching and handle slight variations
    for chi_title in chi_titles_set:
        # Check for exact match or very close match
        if cit_title.lower() == chi_title.lower() or \
           chi_title.lower() in cit_title.lower() or \
           cit_title.lower() in chi_title.lower():
            total_citations += cit_count
            matched_papers.append({
                'title': chi_title,
                'citation_count': cit_count,
                'citation_title': cit_title
            })
            break

result = {
    'total_citation_count': total_citations,
    'number_of_chi_papers_cited': len(matched_papers),
    'matched_papers': matched_papers
}

print("__RESULT__:")
print(json.dumps(result, indent=2))"""

env_args = {'var_functions.list_db:0': ['Citations', 'sqlite_sequence'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:3': 'file_storage/functions.query_db:3.json'}

exec(code, env_args)
