code = """import json
import pandas as pd
import re

# Load paper documents
paper_docs_var = locals().get('var_functions.query_db:14', [])
print("Paper docs variable type:", type(paper_docs_var))

# Load citations data
citations_var = locals().get('var_functions.query_db:15', [])
print("Citations variable type:", type(citations_var))

# If they are strings (file paths), load them
if isinstance(paper_docs_var, str):
    with open(paper_docs_var, 'r') as f:
        paper_docs = json.load(f)
else:
    paper_docs = paper_docs_var

if isinstance(citations_var, str):
    with open(citations_var, 'r') as f:
        citations = json.load(f)
else:
    citations = citations_var

print("Paper docs count:", len(paper_docs))
print("Citations count:", len(citations))

# Process paper docs to extract info
paper_info = []
for doc in paper_docs[:100]:  # Process first 100 to see structure
    text = doc.get('text', '')
    filename = doc.get('filename', '')
    
    # Extract title from filename
    title = filename.replace('.txt', '') if filename else ''
    
    # Extract year - look for patterns like '2016', 'CHI 16', etc.
    year = None
    year_patterns = [
        r'CHI\s*[''"`]?\s*(\d{2})\b',
        r'Ubicomp\s*[''"`]?\s*(\d{2})\b', 
        r'CSCW\s*[''"`]?\s*(\d{2})\b',
        r'(\d{4})\s*[-–]\s*\d{4}',
        r'(20\d{2})\b'
    ]
    
    for pattern in year_patterns:
        match = re.search(pattern, text)
        if match:
            yr = match.group(1)
            if len(yr) == 2:
                year = int('20' + yr)
            elif len(yr) == 4:
                year = int(yr)
            if year and 2010 <= year <= 2020:
                break
    
    # Extract domain - look for physical activity
    domain = []
    domain_keywords = {
        'physical activity': ['physical activity', 'fitness', 'exercise', 'steps', 'walking',
                            'running', 'workout', 'activit'],
        'sleep': ['sleep', 'insomnia'],
        'food': ['food', 'eating', 'diet', 'nutrition'],
        'mental': ['mental', 'stress', 'anxiety', 'depression'],
        'chronic': ['chronic', 'diabetes', 'health'],
        'productivity': ['productivity', 'work'],
        'finances': ['finance', 'money', 'expense']
    }
    
    lower_text = text.lower()
    for domain_name, keywords in domain_keywords.items():
        if any(keyword in lower_text for keyword in keywords):
            domain.append(domain_name)
    
    if title and year:
        paper_info.append({
            'title': title,
            'year': year,
            'domains': domain
        })

print("Processed", len(paper_info), "papers")
if paper_info:
    print("Sample:", paper_info[0])

# Filter papers from 2016 in physical activity domain
papers_2016_activity = [p for p in paper_info if p['year'] == 2016 and 'physical activity' in p['domains']]
print("\n2016 physical activity papers:", len(papers_2016_activity))
if papers_2016_activity:
    for p in papers_2016_activity:
        print(p['title'])

# Convert citations to DataFrame
df_citations = pd.DataFrame(citations)
print("\nCitations DataFrame shape:", df_citations.shape)
print("Columns:", df_citations.columns.tolist())"""

env_args = {'var_functions.list_db:0': ['paper_docs'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:3': 'file_storage/functions.query_db:3.json', 'var_functions.query_db:6': 'file_storage/functions.query_db:6.json', 'var_functions.query_db:7': 'file_storage/functions.query_db:7.json', 'var_functions.query_db:14': 'file_storage/functions.query_db:14.json', 'var_functions.query_db:15': 'file_storage/functions.query_db:15.json'}

exec(code, env_args)
