code = """import json
import re

# Read the full paper documents results
paper_docs_file = var_functions.query_db:2
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
    
    # Extract year from text - look for patterns like YEAR, 2016 or '2016
    # Common patterns: YEAR 2016, '16, 2016
    year = None
    year_patterns = [
        r'\b(20\d{2})\b',  # 4-digit year starting with 20
        r"'\b(\d{2})\b"  # 2-digit year with apostrophe
    ]
    
    for pattern in year_patterns:
        matches = re.findall(pattern, text)
        if matches:
            for match in matches:
                # Convert to 4-digit year
                if len(match) == 4:
                    yr = int(match)
                elif len(match) == 2:
                    yr = int('20' + match)
                
                # Reasonable publication years (2000-2025)
                if 2000 <= yr <= 2025:
                    year = yr
                    break
            if year:
                break
    
    # Extract venue - look for common conference abbreviations
    venue = ''
    venue_patterns = [
        r'UBICOMP', r'CHI', r'CSCW', r'DIS', r'PervasiveHealth', 
        r'WWW', r'IUI', r'OzCHI', r'TEI', r'AH', r'UIST', r'MOBICOM'
    ]
    
    for pattern in venue_patterns:
        if re.search(pattern, text, re.IGNORECASE):
            venue = pattern.upper()
            break
    
    # Extract domain - look for 'physical activity' or related terms
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
    
    abstract_pattern = r'ABSTRACT\s*([^\\n]*?)(?=(?:INTRODUCTION|BACKGROUND|1\\s+INTRODUCTION|$))'
    abstract_match = re.search(abstract_pattern, text, re.IGNORECASE | re.DOTALL)
    abstract_text = abstract_match.group(1) if abstract_match else text[:1000]
    
    abstract_lower = abstract_text.lower()
    for contrib_type, keywords in contribution_keywords.items():
        if any(keyword in abstract_lower for keyword in keywords):
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
papers_2016 = []
for paper in papers_metadata:
    if paper['year'] == 2016 and 'physical activity' in paper['domain']:
        papers_2016.append(paper)

print(f"\nNumber of 2016 papers in physical activity domain: {len(papers_2016)}")
print("\nTitles:")
for paper in papers_2016:
    print(f"- {paper['title']}")

# Save results for next step
result = {
    'papers_metadata': papers_metadata,
    'papers_2016': papers_2016
}

print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.query_db:0': [{'id': '1', 'title': 'Expense Control: A Gamified, Semi-Automated, Crowd-Based Approach For Receipt Capturing', 'citation_count': '4', 'citation_year': '2017'}, {'id': '2', 'title': 'Expense Control: A Gamified, Semi-Automated, Crowd-Based Approach For Receipt Capturing', 'citation_count': '95', 'citation_year': '2018'}, {'id': '3', 'title': 'Understanding My Data, Myself: Supporting Self-reflection with Ubicomp Technologies', 'citation_count': '32', 'citation_year': '2012'}, {'id': '4', 'title': 'Understanding My Data, Myself: Supporting Self-reflection with Ubicomp Technologies', 'citation_count': '29', 'citation_year': '2013'}, {'id': '5', 'title': 'Understanding My Data, Myself: Supporting Self-reflection with Ubicomp Technologies', 'citation_count': '18', 'citation_year': '2014'}], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json'}

exec(code, env_args)
