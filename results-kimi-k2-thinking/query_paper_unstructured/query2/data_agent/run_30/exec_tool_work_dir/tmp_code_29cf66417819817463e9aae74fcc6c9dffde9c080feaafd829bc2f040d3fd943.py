code = """import json
import re

# Load data
citations_data = locals()['var_functions.query_db:0']
if isinstance(citations_data, str) and citations_data.endswith('.json'):
    with open(citations_data, 'r') as f:
        citations_2018 = json.load(f)
else:
    citations_2018 = citations_data

papers_data = locals()['var_functions.query_db:2']
if isinstance(papers_data, str) and papers_data.endswith('.json'):
    with open(papers_data, 'r') as f:
        paper_docs = json.load(f)
else:
    paper_docs = papers_data

# Improved ACM paper detection
acm_paper_titles = {}
venue_stats = {}

for doc in paper_docs:
    text = doc.get('text', '')
    filename = doc.get('filename', '')
    
    # Extract title from filename
    if filename.endswith('.txt'):
        title = filename[:-4]
    else:
        title = filename
    
    title_key = title.lower().strip()
    
    # Detect ACM publisher with multiple indicators
    is_acm = False
    text_upper = text.upper()
    
    # Direct ACM indicators
    acm_indicators = [
        'ACM COPYRIGHT',
        'PUBLISHED BY ACM',
        'ACM CLASSIFICATION KEYWORDS',
        'ISBN 978-1-4503',
        'DOI.HTTP://DX.DOI.ORG/10.1145',
        'DOI:10.1145',
        'HTTPS://DOI.ORG/10.1145'
    ]
    
    for indicator in acm_indicators:
        if indicator in text_upper:
            is_acm = True
            break
    
    # Check for ACM conference proceedings
    if not is_acm:
        # Look for conference patterns
        conference_patterns = [
            r'PROCEEDINGS OF.*?\d{4}.*?ACM',
            r'ACM.*?PROCEEDINGS',
            r'CONFERENCE ON.*?\d{4}.*?ACM',
            r'ACM.*?CONFERENCE'
        ]
        
        for pattern in conference_patterns:
            if re.search(pattern, text, re.IGNORECASE):
                is_acm = True
                break
    
    # Check for known ACM venues in publication line
    if not is_acm:
        known_acm_venues = ['UBICOMP', 'CHI', 'CSCW', 'DIS', 'UIST', 'ISS', 'TEI', 'IUI', 'WWW']
        # Look for venue+year pattern (common in ACM headers)
        venue_pattern = r'\b(' + '|'.join(known_acm_venues) + r')\b.*?\d{4}'
        if re.search(venue_pattern, text_upper) and ('PROCEEDINGS' in text_upper or 'ACM' in text_upper):
            is_acm = True
    
    if is_acm:
        acm_paper_titles[title_key] = title

print(f"Total papers checked: {len(paper_docs)}")
print(f"ACM papers identified: {len(acm_paper_titles)}")

# Match with citations more effectively
acm_citations = []
unmatched = []

for citation in citations_2018:
    cite_title = citation.get('title', '').strip()
    cite_count = int(citation.get('citation_count', 0))
    
    if not cite_title:
        continue
    
    # Direct match (case-insensitive, whitespace normalized)
    cite_key = ' '.join(cite_title.lower().split())
    
    if cite_key in acm_paper_titles:
        acm_citations.append({
            'title': cite_title,
            'count': cite_count
        })
    else:
        # Try partial matching for potential variations
        for paper_key, original_title in acm_paper_titles.items():
            # Check if they're very similar (one contains the other with minor differences)
            if cite_key in paper_key or paper_key in cite_key:
                # Make sure it's a substantial match (not just a single word)
                cite_words = set(cite_key.split())
                paper_words = set(paper_key.split())
                common_words = cite_words & paper_words
                
                if len(common_words) >= min(len(cite_words), len(paper_words)) * 0.7:
                    acm_citations.append({
                        'title': cite_title,
                        'count': cite_count,
                        'matched_to': original_title
                    })
                    break

# Calculate average
if acm_citations:
    total_citations = sum(c['count'] for c in acm_citations)
    num_papers = len(acm_citations)
    avg_citations = total_citations / num_papers
    
    result = {
        'avg_citation_count': round(avg_citations, 2),
        'num_acm_papers': num_papers,
        'total_citations': total_citations,
        'sample_papers': acm_citations[:10]
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

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.execute_python:14': {'avg_citation_count': 68.5, 'num_acm_papers': 2, 'total_citations': 137}, 'var_functions.execute_python:16': {'avg_citation_count': 68.5, 'num_acm_papers': 2, 'total_citations': 137, 'sample_papers': [{'title': 'A Lived Informatics Model of Personal Informatics', 'count': 50}, {'title': 'ArmSleeve: A Patient Monitoring System to Support Occupational Therapists in Stroke Rehabilitation', 'count': 87}]}}

exec(code, env_args)
