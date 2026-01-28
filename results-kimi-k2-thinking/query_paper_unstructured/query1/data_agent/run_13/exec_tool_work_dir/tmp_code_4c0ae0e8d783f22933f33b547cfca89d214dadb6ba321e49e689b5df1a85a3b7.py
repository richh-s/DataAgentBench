code = """import json
import os

# Load the full citations data from the file
citations_path = locals()['var_functions.query_db:6']
with open(citations_path, 'r') as f:
    citations_data = json.load(f)

# Load the full paper_docs data from the file
paper_docs_path = locals()['var_functions.query_db:8']
with open(paper_docs_path, 'r') as f:
    paper_docs_data = json.load(f)

# Function to extract domain information from paper text
def extract_domains(paper_text):
    text_lower = paper_text.lower()
    domains = []
    
    # Explicit domain markers - look for structured mentions
    # Patterns like "domain: food", "domains: food, sleep", etc.
    
    # List of known domains from the hints
    known_domains = [
        'food', 'physical activity', 'sleep', 'mental', 'finances', 
        'productivity', 'screen time', 'social interactions', 'location',
        'chronic', 'diabetes', 'health behavior', 'health_behavior', 'weight'
    ]
    
    # Look for explicit domain declarations
    lines = paper_text.split('\n')
    for line in lines:
        line_lower = line.lower()
        # Check for domain indicators
        if 'domain' in line_lower:
            for domain in known_domains:
                if domain in line_lower:
                    # Clean up the domain name
                    clean_domain = domain.replace('_', ' ')
                    if clean_domain not in domains:
                        domains.append(clean_domain)
    
    # If no explicit domain found, infer from context
    # Look for mentions in abstract/intro about studying specific domains
    if not domains:
        sections_to_check = []
        # Get parts of the paper that might mention the domain
        lines = paper_text.split('\n')
        for i, line in enumerate(lines[:50]):  # Check first 50 lines (abstract/intro)
            for domain in known_domains:
                # Check if domain is mentioned as a focus area
                if (domain in line.lower() and 
                    any(word in line.lower() for word in ['track', 'study', 'examine', 'investigate', 'explore'])):
                    clean_domain = domain.replace('_', ' ')
                    if clean_domain not in domains:
                        domains.append(clean_domain)
    
    return domains

# Process all papers and extract domain information
papers_with_domains = []
for paper in paper_docs_data:
    filename = paper.get('filename', '')
    text = paper.get('text', '')
    title = filename.replace('.txt', '')
    
    # Extract domains
    domains = extract_domains(text)
    
    papers_with_domains.append({
        'title': title,
        'domains': domains,
        'filename': filename
    })

# Filter papers in the 'food' domain
food_papers = [p for p in papers_with_domains if 'food' in p['domains']]

print('__RESULT__:')
print(json.dumps({
    'total_papers': len(papers_with_domains),
    'papers_with_domains': len([p for p in papers_with_domains if p['domains']]),
    'food_papers': len(food_papers),
    'food_paper_titles': [p['title'] for p in food_papers]
}))"""

env_args = {'var_functions.list_db:0': ['paper_docs'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.list_db:5': ['Citations', 'sqlite_sequence'], 'var_functions.query_db:6': 'file_storage/functions.query_db:6.json', 'var_functions.query_db:8': 'file_storage/functions.query_db:8.json', 'var_functions.execute_python:12': {'total_papers': 5, 'food_papers': 3, 'food_paper_titles': ['A Lived Informatics Model of Personal Informatics', 'A Stage-based Model of Personal Informatics Systems', 'A Wee Bit More Interaction: Designing and Evaluating an Overactive Bladder App']}}

exec(code, env_args)
