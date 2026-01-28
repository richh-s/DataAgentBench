code = """import json
import re
import os

# The result from query_db is stored as a file path
paper_docs_file = var_functions.query_db:2

print(f"Loading paper documents from: {paper_docs_file}")

with open(paper_docs_file, 'r') as f:
    paper_docs = json.load(f)

print(f"Total number of paper documents: {len(paper_docs)}")

# Initialize list to store extracted paper metadata
papers_metadata = []

for doc in paper_docs:
    filename = doc.get('filename', '')
    text = doc.get('text', '')
    
    # Extract title from filename (without .txt extension)
    title_match = re.match(r'^(.*?)\.txt$', filename)
    if title_match:
        title = title_match.group(1)
    else:
        title = ''
    
    # Extract year from text
    year = None
    # Look for 4-digit years first
    year_matches = re.findall(r'\b(20\d{2})\b', text)
    for match in year_matches:
        yr = int(match)
        if 2000 <= yr <= 2025:
            year = yr
            break
    
    # If no 4-digit year, try 2-digit years
    if not year:
        year_matches = re.findall(r"'\b(\d{2})\b", text)
        for match in year_matches:
            yr = int('20' + match)
            if 2000 <= yr <= 2025:
                year = yr
                break
    
    # Extract venue - look for common conference abbreviations
    venue = ''
    venue_patterns = ['UBICOMP', 'CHI', 'CSCW', 'DIS', 'PervasiveHealth', 
                      'WWW', 'IUI', 'OzCHI', 'TEI', 'AH', 'UIST', 'MOBICOM']
    
    for pattern in venue_patterns:
        if re.search(pattern, text, re.IGNORECASE):
            venue = pattern.upper()
            break
    
    # Extract domain
    domain = []
    domain_keywords = {
        'physical activity': ['physical activity', 'fitness', 'exercise', 'steps', 'walking', 'running', 'activity tracking'],
        'food': ['food', 'diet', 'eating', 'nutrition'],
        'sleep': ['sleep', 'sleeping'],
        'mental': ['mental', 'mood', 'stress', 'emotion'],
        'finances': ['finance', 'money', 'expense', 'budget'],
        'location': ['location', 'place', 'gps'],
        'productivity': ['productivity', 'work', 'task'],
        'social': ['social', 'interaction', 'relationship'],
        'screen time': ['screen time', 'phone use', 'digital'],
        'chronic': ['chronic', 'disease', 'health condition'],
        'diabetes': ['diabetes', 'blood sugar'],
        'health_behavior': ['health behavior', 'health_behavior']
    }
    
    text_lower = text.lower()
    for domain_name, keywords in domain_keywords.items():
        if any(keyword in text_lower for keyword in keywords):
            domain.append(domain_name)
    
    # Extract contribution type
    contribution = []
    contribution_keywords = {
        'empirical': ['empirical', 'study', 'survey', 'interview', 'experiment', 'evaluation'],
        'artifact': ['system', 'tool', 'application', 'app', 'prototype', 'design'],
        'theoretical': ['theory', 'model', 'framework', 'concept', 'theoretical'],
        'survey': ['survey', 'review', 'literature'],
        'methodological': ['method', 'methodology', 'approach', 'technique']
    }
    
    # Look in abstract/introduction section
    intro_section = text[:2000].lower()
    for contrib_type, keywords in contribution_keywords.items():
        if any(keyword in intro_section for keyword in keywords):
            contribution.append(contrib_type)
    
    # Extract source/publisher
    source = ''
    if 'ACM' in text:
        source = 'ACM'
    elif 'IEEE' in text:
        source = 'IEEE'
    elif 'PubMed' in text or 'Pubmed' in text:
        source = 'PubMed'
    
    papers_metadata.append({
        'title': title,
        'year': year,
        'venue': venue,
        'source': source,
        'domain': domain,
        'contribution': contribution,
        'filename': filename
    })

# Filter papers from 2016 with 'physical activity' domain
papers_2016_physical_activity = []
for paper in papers_metadata:
    if paper['year'] == 2016 and 'physical activity' in paper['domain']:
        papers_2016_physical_activity.append(paper)

print(f"Number of 2016 papers in physical activity domain: {len(papers_2016_physical_activity)}")

# Display the titles
for paper in papers_2016_physical_activity:
    print(f"Title: {paper['title']}")
    print(f"Year: {paper['year']}")
    print(f"Domain: {paper['domain']}")
    print(f"Venue: {paper['venue']}")
    print("---")

# Prepare result for JSON serialization
result = {
    'papers_2016_physical_activity': papers_2016_physical_activity
}

print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.query_db:0': [{'id': '1', 'title': 'Expense Control: A Gamified, Semi-Automated, Crowd-Based Approach For Receipt Capturing', 'citation_count': '4', 'citation_year': '2017'}, {'id': '2', 'title': 'Expense Control: A Gamified, Semi-Automated, Crowd-Based Approach For Receipt Capturing', 'citation_count': '95', 'citation_year': '2018'}, {'id': '3', 'title': 'Understanding My Data, Myself: Supporting Self-reflection with Ubicomp Technologies', 'citation_count': '32', 'citation_year': '2012'}, {'id': '4', 'title': 'Understanding My Data, Myself: Supporting Self-reflection with Ubicomp Technologies', 'citation_count': '29', 'citation_year': '2013'}, {'id': '5', 'title': 'Understanding My Data, Myself: Supporting Self-reflection with Ubicomp Technologies', 'citation_count': '18', 'citation_year': '2014'}], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json'}

exec(code, env_args)
