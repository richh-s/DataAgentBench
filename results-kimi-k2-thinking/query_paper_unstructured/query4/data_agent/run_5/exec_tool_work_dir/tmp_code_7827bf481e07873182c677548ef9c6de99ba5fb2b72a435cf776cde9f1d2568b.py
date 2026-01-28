code = """import json
import re

# Load full citations data
citations_path = locals()['var_functions.query_db:12']
with open(citations_path, 'r') as f:
    citations = json.load(f)

# Load full paper documents
paper_docs_path = locals()['var_functions.query_db:4']
with open(paper_docs_path, 'r') as f:
    paper_docs = json.load(f)

# Extract paper information
papers = []
for doc in paper_docs:
    filename = doc.get('filename', '')
    text = doc.get('text', '')
    
    # Extract title from filename
    title = filename.replace('.txt', '') if filename else ''
    
    # Extract year from the text
    year = None
    year_patterns = [
        r'\b(20\d{2})\b',  # 4-digit year starting with 20
        r"CHI\s+(\d{4})",
        r"UbiComp\s+'(\d{2})",
        r"CSCW\s+(\d{4})",
        r"DIS\s+(\d{4})",
        r"PervasiveHealth\s+(\d{4})",
        r"WWW\s+(\d{4})",
        r"IUI\s+(\d{4})",
        r"OzCHI\s+(\d{4})",
        r"TEI\s+(\d{4})",
        r"AH\s+(\d{4})"
    ]
    
    for pattern in year_patterns:
        match = re.search(pattern, text)
        if match:
            if "UbiComp" in pattern and match.group(1):
                year = int("20" + match.group(1))
            elif match.group(1):
                year = int(match.group(1))
            if year and 2000 <= year <= 2025:
                break
    
    # Extract domain information
    domain = []
    text_lower = text.lower()
    
    # Look for physical activity domain
    if re.search(r'physical activity|fitness|exercise|activity tracking', text_lower):
        domain.append('physical activity')
    
    # Look for other domains  
    if re.search(r'food|diet|nutrition|eating', text_lower):
        domain.append('food')
    if re.search(r'sleep', text_lower):
        domain.append('sleep')
    if re.search(r'mental health|depression|anxiety|stress', text_lower):
        domain.append('mental')
    if re.search(r'finance|money|expense|budget', text_lower):
        domain.append('finances')
    if re.search(r'location|place|gps|where', text_lower):
        domain.append('location')
    if re.search(r'productivity|work|task', text_lower):
        domain.append('productivity')
    if re.search(r'screen|phone|device|technology', text_lower):
        domain.append('screen time')
    if re.search(r'social|interaction|people|friend', text_lower):
        domain.append('social interactions')
    if re.search(r'diabetes|health|medical|disease', text_lower):
        domain.append('diabetes')
        domain.append('health behavior')
    
    papers.append({
        'title': title,
        'year': year,
        'domain': domain,
        'filename': filename
    })

# Aggregate citations by title
citation_totals = {}
for citation in citations:
    title = citation.get('title', '')
    count = int(citation.get('citation_count', 0))
    citation_totals[title] = citation_totals.get(title, 0) + count

# Find papers from 2016 in physical activity domain
results = []
for paper in papers:
    if paper['year'] == 2016 and 'physical activity' in paper['domain']:
        total_citations = citation_totals.get(paper['title'], 0)
        results.append({
            'title': paper['title'],
            'total_citation_count': total_citations
        })

print('__RESULT__:')
print(json.dumps(results))"""

env_args = {'var_functions.query_db:0': [{'id': '1', 'title': 'Expense Control: A Gamified, Semi-Automated, Crowd-Based Approach For Receipt Capturing', 'citation_count': '4', 'citation_year': '2017'}, {'id': '2', 'title': 'Expense Control: A Gamified, Semi-Automated, Crowd-Based Approach For Receipt Capturing', 'citation_count': '95', 'citation_year': '2018'}, {'id': '3', 'title': 'Understanding My Data, Myself: Supporting Self-reflection with Ubicomp Technologies', 'citation_count': '32', 'citation_year': '2012'}, {'id': '4', 'title': 'Understanding My Data, Myself: Supporting Self-reflection with Ubicomp Technologies', 'citation_count': '29', 'citation_year': '2013'}, {'id': '5', 'title': 'Understanding My Data, Myself: Supporting Self-reflection with Ubicomp Technologies', 'citation_count': '18', 'citation_year': '2014'}, {'id': '6', 'title': 'Understanding My Data, Myself: Supporting Self-reflection with Ubicomp Technologies', 'citation_count': '95', 'citation_year': '2015'}, {'id': '7', 'title': 'Understanding My Data, Myself: Supporting Self-reflection with Ubicomp Technologies', 'citation_count': '14', 'citation_year': '2016'}, {'id': '8', 'title': 'Sundroid: Solar Radiation Awareness with Smartphones', 'citation_count': '12', 'citation_year': '2012'}, {'id': '9', 'title': 'Sundroid: Solar Radiation Awareness with Smartphones', 'citation_count': '76', 'citation_year': '2013'}, {'id': '10', 'title': 'Sundroid: Solar Radiation Awareness with Smartphones', 'citation_count': '55', 'citation_year': '2014'}], 'var_functions.query_db:1': 'file_storage/functions.query_db:1.json', 'var_functions.query_db:4': 'file_storage/functions.query_db:4.json', 'var_functions.execute_python:8': 'file_storage/functions.execute_python:8.json', 'var_functions.execute_python:10': 'file_storage/functions.execute_python:10.json', 'var_functions.query_db:12': 'file_storage/functions.query_db:12.json'}

exec(code, env_args)
