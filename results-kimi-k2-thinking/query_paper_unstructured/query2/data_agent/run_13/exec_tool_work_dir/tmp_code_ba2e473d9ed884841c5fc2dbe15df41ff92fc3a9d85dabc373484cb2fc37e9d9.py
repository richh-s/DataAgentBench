code = """import json
import re

# Read citation data
citation_file_path = locals()['var_functions.query_db:0']
citation_data = []
with open(citation_file_path, 'r') as f:
    citation_data = json.load(f)

# Read paper documents
doc_file_path = locals()['var_functions.query_db:2']
paper_docs = []
with open(doc_file_path, 'r') as f:
    paper_docs = json.load(f)

# Create a mapping of normalized titles to citation counts
citation_map = {}
for cite in citation_data:
    title = cite.get('title', '').strip().lower()
    count = int(cite.get('citation_count', 0))
    citation_map[title] = count

print(f"Total 2018 citations: {len(citation_data)}")
print(f"Total paper documents: {len(paper_docs)}")

# Extract ACM papers and their citation counts using multiple patterns
acm_citations = []
matched_titles = []
acm_paper_count = 0

# Multiple patterns to identify ACM papers
acm_patterns = [
    r'\\bACM\\b',  # Explicit ACM mention
    r'Copyright.*\\bACM\\b',  # ACM copyright
    r'10\\.1145/\\d+',  # ACM DOI pattern
    r'ACM Classification Keywords',  # ACM classification
    r'Permission to make.*ACM',  # ACM permission statement
    r'Association for Computing Machinery',  # Full ACM name
]

# Also check for common ACM venues (but this is less reliable)
acm_venues = ['CHI', 'Ubicomp', 'UbiComp', 'CSCW', 'DIS', 'TEI', 'IUI', 'WWW']

for doc in paper_docs:
    filename = doc.get('filename', '')
    text = doc.get('text', '')
    
    # Extract title from filename
    title = filename.replace('.txt', '') if filename else ''
    normalized_title = title.strip().lower()
    
    # Check if paper is from ACM
    is_acm = False
    
    # Check explicit ACM patterns
    for pattern in acm_patterns:
        if re.search(pattern, text, re.IGNORECASE):
            is_acm = True
            break
    
    # If no explicit ACM mention, check if venue is ACM (less reliable)
    if not is_acm:
        # Look for venue patterns like "CHI '18" or "Proceedings of CHI"
        for venue in acm_venues:
            if re.search(rf'\\b{venue}\\s*\\'\\d{{2}}', text) or \
               re.search(rf'Proceedings of[^\\n]*{venue}', text, re.IGNORECASE):
                is_acm = True
                break
    
    if is_acm:
        acm_paper_count += 1
        # Check if this paper has citation data for 2018
        if normalized_title in citation_map:
            citation_count = citation_map[normalized_title]
            acm_citations.append(citation_count)
            matched_titles.append((title, citation_count))

# Debug information
print(f"\\nTotal ACM papers found: {acm_paper_count}")
print(f"ACM papers with 2018 citations: {len(acm_citations)}")

# Show matched titles
if matched_titles:
    print(f"\\nMatched ACM papers with citations:")
    for title, count in matched_titles:
        print(f"  - {title}: {count} citations")
else:
    print("\\nNo ACM papers matched with 2018 citations")
    # Let's see some examples of what we have
    print("\\nSample ACM papers (no citation match):")
    sample_count = 0
    for doc in paper_docs:
        filename = doc.get('filename', '')
        text = doc.get('text', '')
        title = filename.replace('.txt', '') if filename else ''
        
        is_acm = False
        for pattern in acm_patterns:
            if re.search(pattern, text, re.IGNORECASE):
                is_acm = True
                break
        
        if is_acm:
            normalized_title = title.strip().lower()
            if normalized_title not in citation_map:
                print(f"  - {title} (not in citation data)")
                sample_count += 1
                if sample_count >= 5:
                    break

# Calculate average citation count
if acm_citations:
    avg_citations = sum(acm_citations) / len(acm_citations)
    result = {
        'average_citation_count': round(avg_citations, 2),
        'total_acm_papers_with_citations': len(acm_citations),
        'total_acm_papers_found': acm_paper_count
    }
else:
    result = {
        'average_citation_count': 0,
        'total_acm_papers_with_citations': 0,
        'total_acm_papers_found': acm_paper_count
    }

print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.execute_python:8': {'average_citation_count': 68.5, 'total_acm_papers_with_citations': 2}, 'var_functions.execute_python:10': {'average_citation_count': 68.5, 'total_acm_papers_with_citations': 2}}

exec(code, env_args)
