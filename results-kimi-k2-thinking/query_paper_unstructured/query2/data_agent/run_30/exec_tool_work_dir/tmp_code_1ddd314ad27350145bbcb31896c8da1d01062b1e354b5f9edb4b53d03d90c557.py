code = """import json
import re

# Access the stored data using proper variable references
citations_data = locals()['var_functions.query_db:20']
papers_data = locals()['var_functions.query_db:2']

# Load the data if they are file paths
if isinstance(citations_data, str) and citations_data.endswith('.json'):
    with open(citations_data, 'r') as f:
        citations_2018 = json.load(f)
else:
    citations_2018 = citations_data

if isinstance(papers_data, str) and papers_data.endswith('.json'):
    with open(papers_data, 'r') as f:
        paper_docs = json.load(f)
else:
    paper_docs = papers_data

print(f"Citations 2018: {len(citations_2018)} records")
print(f"Paper docs: {len(paper_docs)} records")

# Create a dictionary for fast lookup of ACM papers
acm_papers_dict = {}

for doc in paper_docs:
    text = doc.get('text', '')
    filename = doc.get('filename', '')
    
    if filename.endswith('.txt'):
        title = filename[:-4]
    else:
        title = filename
    
    title_normalized = title.lower().strip()
    
    # Check if this is an ACM paper
    text_upper = text.upper()
    is_acm = False
    
    # Multiple indicators for ACM publication
    acm_markers = [
        'ACM COPYRIGHT', 'PUBLISHED BY ACM', 'ACM CLASSIFICATION KEYWORDS',
        'ISBN 978-1-4503', 'DOI.ORG/10.1145', 'DOI:10.1145', 'HTTP://DX.DOI.ORG/10.1145',
        'HTTPS://DOI.ORG/10.1145', 'WWW.ACM.ORG'
    ]
    
    for marker in acm_markers:
        if marker in text_upper:
            is_acm = True
            break
    
    # Check for known ACM conference patterns
    if not is_acm:
        # Look for venue + year + ACM/proceedings pattern
        venues = ['UBICOMP', 'CHI', 'CSCW', 'DIS', 'UIST', 'ISS', 'TEI', 'IUI', 'WWW']
        for venue in venues:
            venue_pattern = rf'\b{venue}\b.*?(?:\d{{4}}|PROCEEDINGS|ACM)'
            if re.search(venue_pattern, text_upper):
                # Verify it's not just a citation
                if 'PROCEEDINGS' in text_upper or venue in text_upper[:1000]:
                    is_acm = True
                    break
    
    if is_acm:
        acm_papers_dict[title_normalized] = title

print(f"ACM papers identified: {len(acm_papers_dict)}")

# Match citations with ACM papers using flexible matching
acm_citation_counts = []
sample_matches = []

for citation in citations_2018:
    cite_title = citation.get('title', '').strip()
    cite_count = int(citation.get('citation_count', 0))
    
    if not cite_title:
        continue
    
    cite_normalized = cite_title.lower()
    
    # Direct match
    if cite_normalized in acm_papers_dict:
        acm_citation_counts.append(cite_count)
        if len(sample_matches) < 5:
            sample_matches.append({
                'citation_title': cite_title,
                'paper_title': acm_papers_dict[cite_normalized],
                'count': cite_count
            })
    else:
        # Try partial/fuzzy matching
        for paper_key, original_title in acm_papers_dict.items():
            # Check similarity
            cite_words = set(cite_normalized.split())
            paper_words = set(paper_key.split())
            
            # Jaccard similarity
            intersection = cite_words & paper_words
            union = cite_words | paper_words
            
            if len(union) > 0 and len(intersection) / len(union) >= 0.8:
                acm_citation_counts.append(cite_count)
                if len(sample_matches) < 5:
                    sample_matches.append({
                        'citation_title': cite_title,
                        'paper_title': original_title,
                        'count': cite_count,
                        'match_type': 'fuzzy'
                    })
                break

# Calculate results
if acm_citation_counts:
    avg_citations = sum(acm_citation_counts) / len(acm_citation_counts)
    result = {
        'avg_citation_count': round(avg_citations, 2),
        'num_acm_papers': len(acm_citation_counts),
        'total_citations': sum(acm_citation_counts),
        'sample_matches': sample_matches
    }
else:
    result = {
        'avg_citation_count': None,
        'num_acm_papers': 0,
        'total_citations': 0,
        'message': 'No ACM papers found'
    }

print('__RESULT__:')
print(json.dumps(result, indent=2))"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.execute_python:14': {'avg_citation_count': 68.5, 'num_acm_papers': 2, 'total_citations': 137}, 'var_functions.execute_python:16': {'avg_citation_count': 68.5, 'num_acm_papers': 2, 'total_citations': 137, 'sample_papers': [{'title': 'A Lived Informatics Model of Personal Informatics', 'count': 50}, {'title': 'ArmSleeve: A Patient Monitoring System to Support Occupational Therapists in Stroke Rehabilitation', 'count': 87}]}, 'var_functions.execute_python:18': {'avg_citation_count': 68.5, 'num_acm_papers': 2, 'total_citations': 137, 'sample_papers': [{'title': 'A Lived Informatics Model of Personal Informatics', 'count': 50}, {'title': 'ArmSleeve: A Patient Monitoring System to Support Occupational Therapists in Stroke Rehabilitation', 'count': 87}]}, 'var_functions.query_db:20': 'file_storage/functions.query_db:20.json', 'var_functions.query_db:22': 'file_storage/functions.query_db:22.json'}

exec(code, env_args)
