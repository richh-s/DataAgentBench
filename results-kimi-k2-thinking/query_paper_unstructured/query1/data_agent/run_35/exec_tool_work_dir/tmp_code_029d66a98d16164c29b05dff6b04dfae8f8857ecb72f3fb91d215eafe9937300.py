code = """import json
import pandas as pd

# Load citations data
citations_path = locals()['var_functions.query_db:2']
with open(citations_path, 'r') as f:
    citations_data = json.load(f)

# Convert to DataFrame for easier processing
citations_df = pd.DataFrame(citations_data)

# Load paper docs data
paper_docs_path = locals()['var_functions.query_db:5']
with open(paper_docs_path, 'r') as f:
    paper_docs_data = json.load(f)

# Extract paper information from documents
import re

paper_info = []
for doc in paper_docs_data:
    title = doc['filename'].replace('.txt', '')
    text = doc['text']
    
    # Extract year
    year = None
    year_patterns = [
        r'UBICOMP\s*\'?(\d{2})',
        r'CHI\s*\'?(\d{2})',
        r'CSCW\s*\'?(\d{2})',
        r'DIS\s*\'?(\d{2})',
        r'(\d{4})\s*,\s*[^\d]*(?:Conference|Proceedings)',
        r'(?:Proceedings|Conference).*?(\d{4})',
        r'(\d{4})\s*[-–]\s*\d{4}\s*',
    ]
    
    for pattern in year_patterns:
        match = re.search(pattern, text, re.IGNORECASE)
        if match:
            year_str = match.group(1)
            if len(year_str) == 2:
                year = int('20' + year_str) if int(year_str) < 50 else int('19' + year_str)
            elif len(year_str) == 4:
                year = int(year_str)
            if year and 2000 <= year <= 2030:
                break
    
    # Extract venue
    venue = None
    venue_patterns = {
        'CHI': r'CHI\s*[\'"]?(?:\d{2}|\d{4})',
        'Ubicomp': r'Ubi(?:Comp|comp)',
        'CSCW': r'CSCW',
        'DIS': r'DIS',
        'PervasiveHealth': r'PervasiveHealth',
        'WWW': r'WWW',
        'IUI': r'IUI',
        'OzCHI': r'OzCHI',
        'TEI': r'TEI',
        'AH': r'AH\b',
    }
    
    for vname, pattern in venue_patterns.items():
        if re.search(pattern, text):
            venue = vname
            break
    
    # Extract source
    source = None
    if 'ACM' in text:
        source = 'ACM'
    elif 'IEEE' in text:
        source = 'IEEE'
    elif 'PubMed' in text:
        source = 'PubMed'
    
    # Extract domains
    domains = []
    domain_keywords = {
        'food': ['food', 'eating', 'diet', 'nutrition', 'meal', 'calorie'],
        'physical activity': ['physical activity', 'exercise', 'fitness', 'workout', 'sports', 'steps', 'walking', 'running'],
        'sleep': ['sleep', 'insomnia', 'bedtime', 'circadian'],
        'mental': ['mental', 'psychology', 'depression', 'anxiety', 'stress', 'mood', 'cognitive'],
        'finances': ['finances', 'financial', 'money', 'expense', 'budget', 'payment'],
        'productivity': ['productivity', 'work', 'task', 'efficiency', 'performance'],
        'screen time': ['screen time', 'digital', 'technology use', 'smartphone', 'computer'],
        'social interactions': ['social', 'interaction', 'communication', 'relationship'],
        'location': ['location', 'place', 'gps', 'geographic'],
        'chronic': ['chronic', 'disease', 'illness', 'health condition'],
        'diabetes': ['diabetes', 'blood sugar', 'glucose'],
        'health_behavior': ['health behavior', 'wellness', 'preventive health', 'lifestyle'],
    }
    
    text_lower = text.lower()
    for domain, keywords in domain_keywords.items():
        if any(keyword in text_lower for keyword in keywords):
            domains.append(domain)
    
    # Extract contribution type
    contribution = []
    contribution_keywords = {
        'empirical': ['empirical', 'study', 'survey', 'experiment', 'user study', 'interview', 'field study'],
        'artifact': ['system', 'application', 'app', 'tool', 'prototype', 'design', 'implementation'],
        'theoretical': ['theoretical', 'model', 'framework', 'conceptual', 'theory'],
        'survey': ['survey', 'review', 'literature review', 'state of the art'],
        'methodological': ['methodology', 'method', 'approach', 'technique'],
    }
    
    for cont_type, keywords in contribution_keywords.items():
        if any(keyword in text_lower for keyword in keywords):
            contribution.append(cont_type)
    
    paper_info.append({
        'title': title,
        'year': year,
        'venue': venue,
        'source': source,
        'domains': domains,
        'contribution': contribution
    })

# Create DataFrame for paper info
paper_df = pd.DataFrame(paper_info)

# Debug: show some info
print(f"Total papers: {len(paper_df)}")
print(f"Papers with domains: {paper_df[paper_df['domains'].apply(lambda x: len(x) > 0)].shape[0]}")

# Filter papers in 'food' domain
food_papers = paper_df[paper_df['domains'].apply(lambda x: 'food' in x)]
print(f"Food domain papers: {len(food_papers)}")

if len(food_papers) > 0:
    print("\nSample food papers:")
    print(food_papers[['title', 'year']].head())
else:
    print("\nNo food papers found. Checking domain values...")
    all_domains = set()
    for dlist in paper_df['domains']:
        all_domains.update(dlist)
    print(f"All domains found: {sorted(all_domains)}")

# For debugging, show papers with food-related keywords in text
print("\nChecking papers with 'food' in text...")
food_text_papers = []
for doc in paper_docs_data:
    text = doc['text'].lower()
    if 'food' in text or 'eating' in text or 'diet' in text:
        food_text_papers.append(doc['filename'].replace('.txt', ''))

print(f"Papers with food keywords in text: {len(food_text_papers)}")
print(food_text_papers[:10])"""

env_args = {'var_functions.query_db:0': [{'id': '1', 'title': 'Expense Control: A Gamified, Semi-Automated, Crowd-Based Approach For Receipt Capturing', 'citation_count': '4', 'citation_year': '2017'}, {'id': '2', 'title': 'Expense Control: A Gamified, Semi-Automated, Crowd-Based Approach For Receipt Capturing', 'citation_count': '95', 'citation_year': '2018'}, {'id': '3', 'title': 'Understanding My Data, Myself: Supporting Self-reflection with Ubicomp Technologies', 'citation_count': '32', 'citation_year': '2012'}, {'id': '4', 'title': 'Understanding My Data, Myself: Supporting Self-reflection with Ubicomp Technologies', 'citation_count': '29', 'citation_year': '2013'}, {'id': '5', 'title': 'Understanding My Data, Myself: Supporting Self-reflection with Ubicomp Technologies', 'citation_count': '18', 'citation_year': '2014'}, {'id': '6', 'title': 'Understanding My Data, Myself: Supporting Self-reflection with Ubicomp Technologies', 'citation_count': '95', 'citation_year': '2015'}, {'id': '7', 'title': 'Understanding My Data, Myself: Supporting Self-reflection with Ubicomp Technologies', 'citation_count': '14', 'citation_year': '2016'}, {'id': '8', 'title': 'Sundroid: Solar Radiation Awareness with Smartphones', 'citation_count': '12', 'citation_year': '2012'}, {'id': '9', 'title': 'Sundroid: Solar Radiation Awareness with Smartphones', 'citation_count': '76', 'citation_year': '2013'}, {'id': '10', 'title': 'Sundroid: Solar Radiation Awareness with Smartphones', 'citation_count': '55', 'citation_year': '2014'}], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json'}

exec(code, env_args)
