code = """import json
import re

# Load data
citations_data_json = locals()['var_functions.query_db:0']
if isinstance(citations_data_json, str) and citations_data_json.endswith('.json'):
    with open(citations_data_json, 'r') as f:
        citations_2018 = json.load(f)
else:
    citations_2018 = citations_data_json

papers_data_json = locals()['var_functions.query_db:2']
if isinstance(papers_data_json, str) and papers_data_json.endswith('.json'):
    with open(papers_data_json, 'r') as f:
        paper_docs = json.load(f)
else:
    paper_docs = papers_data_json

# Step 1: Extract all paper titles and identify ACM papers more accurately
paper_info = {}
acm_paper_titles = set()

for doc in paper_docs:
    text = doc.get('text', '').upper()
    filename = doc.get('filename', '')
    
    # Extract title from filename
    if filename.endswith('.txt'):
        title = filename[:-4]
    else:
        title = filename
    
    title_key = title.lower().strip()
    paper_info[title_key] = title
    
    # More robust ACM detection
    is_acm = False
    
    # Check for ACM copyright or publication
    if 'ACM' in text or 'ACMDL' in text or 'DOI.ACM.ORG' in text:
        is_acm = True
    
    # Check for ACM conference proceedings
    if not is_acm:
        # Look for ACM-specific patterns
        acm_patterns = [
            r'PROCEEDINGS OF.*ACM',
            r'ACM.*CONFERENCE',
            r'ACM.*SYMPOSIUM',
            r'PUBLISHED BY ACM',
            r'ACM COPYRIGHT'
        ]
        
        for pattern in acm_patterns:
            if re.search(pattern, text, re.IGNORECASE):
                is_acm = True
                break
    
    # Check if it's from a known ACM venue
    if not is_acm:
        known_acm_venues = ['UBICOMP', 'CHI', 'CSCW', 'DIS', 'UIST', 'ISS', 'TEI', 'IUI']
        for venue in known_acm_venues:
            # Check if venue appears near ACM or in publication info
            if venue in text and ('ACM' in text or 'PROCEEDINGS' in text):
                # Additional check: look for year and location pattern (common in ACM papers)
                if re.search(r'\d{4}.*\d{1,2}\s*-\s*\d{1,2}.*[A-Z][A-Z]+', text):
                    is_acm = True
                    break
    
    if is_acm:
        acm_paper_titles.add(title_key)

print(f"Total papers processed: {len(paper_info)}")
print(f"ACM papers identified: {len(acm_paper_titles)}")

# Step 2: Match citations with ACM papers (more flexible matching)
acm_citation_data = []
unmatched_citations = []

for citation in citations_2018:
    cite_title = citation.get('title', '').strip()
    cite_count = int(citation.get('citation_count', 0))
    
    # Try exact match first
    cite_key = cite_title.lower()
    
    if cite_key in acm_paper_titles:
        acm_citation_data.append({
            'title': cite_title,
            'count': cite_count
        })
    else:
        # Try fuzzy matching - check if citation title is similar to any ACM paper title
        best_match = None
        best_score = 0
        
        for paper_key in acm_paper_titles:
            # Simple similarity: check if one is substring of the other
            if cite_key in paper_key or paper_key in cite_key:
                # Calculate overlap ratio
                overlap = len(set(cite_key.split()) & set(paper_key.split()))
                if overlap > best_score:
                    best_score = overlap
                    best_match = paper_key
        
        if best_score >= 3:  # At least 3 words match
            acm_citation_data.append({
                'title': cite_title,
                'count': cite_count,
                'matched_to': paper_info[best_match]
            })
        else:
            unmatched_citations.append(cite_title)

# Calculate average
if acm_citation_data:
    total_citations = sum(item['count'] for item in acm_citation_data)
    num_papers = len(acm_citation_data)
    avg_citations = total_citations / num_papers
    
    result = {
        'avg_citation_count': round(avg_citations, 2),
        'num_acm_papers': num_papers,
        'total_citations': total_citations,
        'sample_papers': acm_citation_data[:5]
    }
else:
    result = {
        'avg_citation_count': 0,
        'num_acm_papers': 0,
        'total_citations': 0,
        'message': 'No ACM papers found in 2018 citation data'
    }

print('__RESULT__:')
print(json.dumps(result, indent=2))"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.execute_python:14': {'avg_citation_count': 68.5, 'num_acm_papers': 2, 'total_citations': 137}}

exec(code, env_args)
