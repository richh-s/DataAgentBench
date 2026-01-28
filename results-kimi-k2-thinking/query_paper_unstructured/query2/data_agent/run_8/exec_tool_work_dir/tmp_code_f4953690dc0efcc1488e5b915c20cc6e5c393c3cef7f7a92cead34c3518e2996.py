code = """import json
import re

# Load the citations data for 2018
citations_2018_path = 'var_functions.query_db:0'
with open(citations_2018_path, 'r') as f:
    citations_2018 = json.load(f)

# Load the paper_docs data
paper_docs_path = 'var_functions.query_db:2'
with open(paper_docs_path, 'r') as f:
    paper_docs = json.load(f)

print(f"Total citations in 2018: {len(citations_2018)}")
print(f"Total paper documents: {len(paper_docs)}")

# Extract ACM papers from paper_docs
acm_papers = []
for doc in paper_docs:
    text = doc.get('text', '')
    filename = doc.get('filename', '')
    
    # Extract title from filename
    title = filename.replace('.txt', '')
    
    # Check if ACM is mentioned in the text (common indicators)
    # Look for ACM references in the text
    acm_indicators = [
        'ACM ',
        'ACM,', 
        'Association for Computing Machinery',
        'Permission to make digital or hard copies',
        'http://dx.doi.org/10.1145/',
        'ISBN: 978-1-4503-',
        '978-1-4503-',
        'UBICOMP',
        'CHI ',
        'CSCW ',
        'DIS ',
        'TEI ',
        'IUI ',
        'PervasiveHealth',
        'WWW ',
        'OzCHI',
        'AH '
    ]
    
    acm_venue_indicators = [
        'UBICOMP',
        'CHI', 
        'CSCW',
        'DIS',
        'TEI',
        'IUI',
        'PervasiveHealth',
        'WWW'
    ]
    
    # Check for explicit ACM mentions
    has_acm_explicit = 'ACM' in text or 'Association for Computing Machinery' in text
    
    # Check for ACM venues and publication patterns
    has_acm_venue = any(venue in text for venue in acm_venue_indicators)
    has_acm_pattern = any(pattern in text for pattern in acm_indicators)
    
    # Consider it ACM if it has explicit ACM mention OR ACM venue with publication patterns
    if has_acm_explicit or (has_acm_venue and has_acm_pattern):
        acm_papers.append({
            'title': title,
            'filename': filename,
            'text_preview': text[:1000]  # Just for debugging
        })

print(f"Identified ACM papers: {len(acm_papers)}")

# Create a mapping of titles to citation counts
citation_map = {item['title']: int(item['citation_count']) for item in citations_2018}

# Match ACM papers with citations
matched_papers = []
for paper in acm_papers:
    paper_title = paper['title']
    if paper_title in citation_map:
        matched_papers.append({
            'title': paper_title,
            'citation_count': citation_map[paper_title]
        })

print(f"Matched ACM papers with 2018 citations: {len(matched_papers)}")

if matched_papers:
    total_citations = sum(p['citation_count'] for p in matched_papers)
    avg_citations = total_citations / len(matched_papers)
    print(f"Average citation count: {avg_citations:.2f}")
    print(f"Total citations: {total_citations}")
    
    # Show some examples
    print("\nSample matched papers:")
    for i, p in enumerate(matched_papers[:5]):
        print(f"  {i+1}. {p['title']}: {p['citation_count']} citations")
else:
    print("No matches found. Let's check title matching...")
    
    # Debug: check if titles are formatted differently
    sample_citation_titles = list(citation_map.keys())[:5]
    sample_doc_titles = [p['title'] for p in acm_papers[:5]]
    
    print("Sample citation titles:", sample_citation_titles)
    print("Sample doc titles:", sample_doc_titles)"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json'}

exec(code, env_args)
