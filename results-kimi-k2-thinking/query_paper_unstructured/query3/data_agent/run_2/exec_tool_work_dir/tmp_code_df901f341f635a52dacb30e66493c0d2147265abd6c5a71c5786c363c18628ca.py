code = """import json

# Load the results from the previous queries
paper_docs_path = var_functions.query_db:2
citations_data = var_functions.query_db:5

# Read paper docs data
with open(paper_docs_path, 'r') as f:
    paper_docs = json.load(f)

# Read citations data (this is already a Python list from the query)
citations = citations_data

# Extract paper information from the text
import re

papers_info = []

for doc in paper_docs:
    # Get title from filename
    filename = doc.get('filename', '')
    title = filename.replace('.txt', '') if filename else ''
    
    text = doc.get('text', '')
    
    # Extract year - look for patterns like '2017', '2018' in venue info
    # Common patterns: YYYY, YYYY. YYYY, etc.
    year_match = re.search(r'(20[0-2][0-9])', text[:1000])  # Look in first 1000 chars
    year = int(year_match.group(1)) if year_match else None
    
    # Extract venue - look for common HCI venues
    venue_patterns = [
        r'CHI\s*\'?\d{2}',
        r'Ubicomp\s*\'?\d{2}',
        r'UbiComp\s*\'?\d{2}',
        r'CSCW\s*\'?\d{2}',
        r'DIS\s*\'?\d{2}',
        r'PervasiveHealth',
        r'WWW',
        r'IUI',
        r'OzCHI',
        r'TEI',
        r'AH',
        r'UIST',
        r'MobileHCI',
        r'ISS'
    ]
    
    venue = None
    for pattern in venue_patterns:
        match = re.search(pattern, text[:2000], re.IGNORECASE)
        if match:
            venue_match = match.group(0)
            # Clean up venue name
            venue_match = re.sub(r"\'?\d{2}$", "", venue_match)
            venue = venue_match.upper()
            break
    
    # Extract source/publisher
    source_patterns = [
        r'ACM',
        r'IEEE',
        r'PubMed',
        r'Springer',
        r'Elsevier'
    ]
    
    source = None
    for pattern in source_patterns:
        if re.search(pattern, text[:2000]):
            source = pattern
            break
    
    # Extract domain - look for keywords
    domain_patterns = {
        'food': r'\b(food|eating|diet|nutrition|meal)\b',
        'physical activity': r'\b(physical activity|exercise|fitness|workout|step|walking|running)\b',
        'sleep': r'\b(sleep|insomnia|bedtime|circadian)\b',
        'mental': r'\b(mental|stress|anxiety|depression|mood|wellbeing|well-being)\b',
        'finances': r'\b(finance|money|budget|expense|spending|income)\b',
        'productivity': r'\b(productivity|work|task|time management|efficiency|deadline)\b',
        'screen time': r'\b(screen time|digital|phone use|mobile use)\b',
        'social interactions': r'\b(social|interaction|communication|conversation|relationship)\b',
        'location': r'\b(location|place|GPS|geo|spatial)\b',
        'chronic': r'\b(chronic|disease|illness|health condition)\b',
        'diabetes': r'\b(diabetes|blood glucose|sugar)\b',
        'health behavior': r'\b(health behavior|lifestyle|wellness)\b'
    }
    
    domains = []
    text_lower = text.lower()
    for domain_name, pattern in domain_patterns.items():
        if re.search(pattern, text_lower):
            domains.append(domain_name)
    
    # Extract contribution type
    contribution_patterns = {
        'empirical': r'\b(empirical|study|survey|interview|experiment|evaluation|user study|field study|case study)\b',
        'artifact': r'\b(artifact|system|prototype|tool|application|app|design|implementation)\b',
        'theoretical': r'\b(theoretical|theory|model|framework|conceptual|concept)\b',
        'survey': r'\b(survey|literature review|systematic review|meta-analysis)\b',
        'methodological': r'\b(methodological|method|methodology|approach|technique)\b'
    }
    
    contributions = []
    for contrib_name, pattern in contribution_patterns.items():
        if re.search(pattern, text_lower):
            contributions.append(contrib_name)
    
    papers_info.append({
        'title': title,
        'year': year,
        'venue': venue,
        'source': source,
        'domains': domains,
        'contributions': contributions,
        'text': text[:500]  # Store first 500 chars for debugging
    })

# Create a dictionary mapping titles to paper info
papers_dict = {paper['title'].lower(): paper for paper in papers_info}

# Process citations
from collections import defaultdict

# Group citations by title
citations_by_title = defaultdict(list)
for citation in citations:
    cit_title = citation.get('title', '').lower()
    citations_by_title[cit_title].append({
        'citation_count': int(citation.get('citation_count', 0)),
        'citation_year': int(citation.get('citation_year', 0))
    })

# Calculate total citations for each paper
papers_with_citations = []

for title_lower, paper in papers_dict.items():
    # Check if paper is published after 2016 and has 'empirical' contribution
    if paper.get('year') and paper['year'] > 2016:
        if 'empirical' in paper.get('contributions', []):
            # Get total citations
            total_citations = 0
            matching_titles = [t for t in citations_by_title.keys() if t == title_lower]
            
            if matching_titles:
                for match_title in matching_titles:
                    for citation in citations_by_title[match_title]:
                        total_citations += citation['citation_count']
            
            papers_with_citations.append({
                'title': paper['title'],
                'total_citations': total_citations,
                'year': paper['year'],
                'contributions': paper['contributions']
            })

# Sort by total citations descending
papers_with_citations.sort(key=lambda x: x['total_citations'], reverse=True)

# Print results
result = []
for paper in papers_with_citations:
    result.append({
        'title': paper['title'],
        'total_citations': paper['total_citations']
    })

print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.list_db:0': ['paper_docs'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json', 'var_functions.list_db:6': ['Citations', 'sqlite_sequence']}

exec(code, env_args)
