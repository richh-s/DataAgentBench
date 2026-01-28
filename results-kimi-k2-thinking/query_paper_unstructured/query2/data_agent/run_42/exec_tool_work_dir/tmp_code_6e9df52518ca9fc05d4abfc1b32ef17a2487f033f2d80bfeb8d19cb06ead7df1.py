code = """import json
import pandas as pd
import re
from collections import defaultdict

# Load the citations data for 2018
citations_key = 'var_functions.query_db:0'
citations_file = locals()[citations_key]
with open(citations_file, 'r') as f:
    citations_data = json.load(f)

# Load the paper documents data
papers_key = 'var_functions.query_db:2'
papers_file = locals()[papers_key]
with open(papers_file, 'r') as f:
    papers_data = json.load(f)

print(f"Loaded {len(citations_data)} citation records for 2018")
print(f"Loaded {len(papers_data)} paper documents")

# Preview the data structure
print("\nFirst citation record:")
print(citations_data[0])

# Extract paper information
def extract_paper_info(text, filename):
    paper_info = {
        'title': filename.replace('.txt', ''),
        'year': None,
        'venue': None,
        'source': None,
        'domain': None,
        'contribution': None
    }
    
    # Convert text to lowercase for easier matching
    text_lower = text.lower()
    
    # Extract year - look for patterns like YYYY or 'YY
    year_match = re.search(r"(19|20)\d{2}", text[:1000])
    if year_match:
        paper_info['year'] = year_match.group(0)
    
    # Look for venue patterns
    venues = ['chi', 'ubicomp', 'cscw', 'dis', 'pervasivehealth', 'www', 'iui', 'ozchi', 'tei', 'ah']
    for venue in venues:
        if venue in text_lower:
            paper_info['venue'] = venue.upper()
            break
    
    # Look for source/publisher
    if 'acm' in text_lower:
        paper_info['source'] = 'ACM'
    elif 'ieee' in text_lower:
        paper_info['source'] = 'IEEE'
    elif 'pubmed' in text_lower:
        paper_info['source'] = 'PubMed'
    
    # Look for domains
    domains = ['food', 'physical activity', 'sleep', 'mental', 'finances', 'productivity', 
               'screen time', 'social interactions', 'location', 'chronic', 'diabetes', 'health_behavior']
    paper_info['domain'] = []
    for domain in domains:
        if domain.replace(' ', '') in text_lower.replace(' ', '').replace('_', ''):
            paper_info['domain'].append(domain)
    
    # Look for contribution types
    contributions = ['empirical', 'artifact', 'theoretical', 'survey', 'methodological']
    paper_info['contribution'] = []
    for contrib in contributions:
        if contrib in text_lower:
            paper_info['contribution'].append(contrib)
    
    return paper_info

# Extract information from all papers
papers_info = []
for paper in papers_data[:10]:  # Process first 10 for testing
    info = extract_paper_info(paper['text'], paper['filename'])
    papers_info.append(info)

print("\nExtracted paper info sample:")
for info in papers_info[:3]:
    print(info)

# Create a mapping from title to paper info
paper_map = {info['title'].lower(): info for info in papers_info}

# Check ACM papers
acm_citations = []
for citation in citations_data:
    title_lower = citation['title'].lower()
    if title_lower in paper_map:
        paper_info = paper_map[title_lower]
        if paper_info['source'] == 'ACM':
            acm_citations.append({
                'title': citation['title'],
                'citation_count': int(citation['citation_count']),
                'source': paper_info['source']
            })

print(f"\nFound {len(acm_citations)} ACM papers with citations in 2018")
if acm_citations:
    print("\nSample ACM citations:")
    for item in acm_citations[:5]:
        print(item)"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json'}

exec(code, env_args)
