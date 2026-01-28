code = """import json
import re

# Load the full datasets
citations_path = locals()['var_functions.query_db:6']
paper_docs_path = locals()['var_functions.query_db:8']

with open(citations_path, 'r') as f:
    citations_data = json.load(f)

with open(paper_docs_path, 'r') as f:
    paper_docs_data = json.load(f)

# Function to extract domains from paper text
def extract_domains(paper_text, paper_title):
    text_lower = paper_text.lower()
    title_lower = paper_title.lower()
    
    domains = []
    
    # List of known domains
    known_domains = [
        'food', 'physical activity', 'sleep', 'mental', 'finances', 
        'productivity', 'screen time', 'social interactions', 'location',
        'chronic', 'diabetes', 'health behavior', 'weight'
    ]
    
    # Check if food is explicitly mentioned in abstract/intro
    lines = paper_text.split('\n')
    abstract_section = []
    intro_section = []
    in_abstract = False
    in_intro = False
    
    for i, line in enumerate(lines[:100]):  # Check first 100 lines
        line_lower = line.strip().lower()
        
        # Detect section headers
        if 'abstract' in line_lower and len(line_lower) < 20:
            in_abstract = True
            continue
        if 'introduction' in line_lower and len(line_lower) < 20:
            in_abstract = False
            in_intro = True
            continue
        if 'keywords' in line_lower or 'categories' in line_lower:
            in_abstract = False
            in_intro = False
            continue
            
        if in_abstract or in_intro:
            for domain in known_domains:
                if domain in line_lower:
                    clean_domain = domain.replace('_', ' ')
                    if clean_domain not in domains:
                        domains.append(clean_domain)
    
    # Also check the title
    for domain in known_domains:
        if domain in title_lower:
            clean_domain = domain.replace('_', ' ')
            if clean_domain not in domains:
                domains.append(clean_domain)
    
    # For the Lived Informatics paper specifically, check if it mentions food tracking
    if 'lived informatics' in title_lower:
        # Look for specific mentions about food in the full text
        if 'food[' in text_lower or 'food ' in text_lower:
            if 'food' not in domains:
                domains.append('food')
    
    return domains

# Process all papers
papers_info = []
for paper in paper_docs_data:
    filename = paper.get('filename', '')
    text = paper.get('text', '')
    title = filename.replace('.txt', '')
    
    domains = extract_domains(text, title)
    
    papers_info.append({
        'title': title,
        'domains': domains,
        'filename': filename
    })

# Filter food papers
food_papers = [p for p in papers_info if 'food' in p['domains']]

# Get citations for food papers
food_paper_titles = [p['title'] for p in food_papers]

food_citations = []
for citation in citations_data:
    cit_title = citation.get('title', '')
    if cit_title in food_paper_titles:
        food_citations.append({
            'title': cit_title,
            'citation_count': int(citation.get('citation_count', 0)),
            'citation_year': citation.get('citation_year')
        })

# Calculate total citations
total_citations = sum([c['citation_count'] for c in food_citations])

# Group by paper for debugging
paper_citation_totals = {}
for citation in food_citations:
    title = citation['title']
    if title not in paper_citation_totals:
        paper_citation_totals[title] = 0
    paper_citation_totals[title] += citation['citation_count']

print('__RESULT__:')
print(json.dumps({
    'food_papers_count': len(food_papers),
    'food_paper_titles': food_paper_titles,
    'total_citation_records': len(food_citations),
    'total_citation_count': total_citations,
    'citations_by_paper': paper_citation_totals
}, indent=2))"""

env_args = {'var_functions.list_db:0': ['paper_docs'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.list_db:5': ['Citations', 'sqlite_sequence'], 'var_functions.query_db:6': 'file_storage/functions.query_db:6.json', 'var_functions.query_db:8': 'file_storage/functions.query_db:8.json', 'var_functions.execute_python:12': {'total_papers': 5, 'food_papers': 3, 'food_paper_titles': ['A Lived Informatics Model of Personal Informatics', 'A Stage-based Model of Personal Informatics Systems', 'A Wee Bit More Interaction: Designing and Evaluating an Overactive Bladder App']}, 'var_functions.execute_python:16': {'total_papers': 5, 'first_paper_keys': ['_id', 'filename', 'text']}}

exec(code, env_args)
