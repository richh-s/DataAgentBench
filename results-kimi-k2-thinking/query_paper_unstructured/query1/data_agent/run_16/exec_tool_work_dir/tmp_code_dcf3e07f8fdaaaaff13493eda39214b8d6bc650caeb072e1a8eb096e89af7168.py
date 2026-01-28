code = """import json
import re

# Load the data
paper_docs_path = locals()['var_functions.query_db:6']
citations_path = locals()['var_functions.query_db:12']

# Read paper documents
with open(paper_docs_path, 'r') as f:
    paper_docs = json.load(f)

# Read citation data
with open(citations_path, 'r') as f:
    citations = json.load(f)

# Initialize storage for paper information
paper_info = []

# Regular expressions for extractions
domain_pattern = re.compile(r'(?i)\b(food|physical activity|sleep|mental|finances|productivity|screen time|social interactions|location|chronic|diabetes|health behavior)\b')
year_pattern = re.compile(r'\b(200[0-9]|201[0-9]|202[0-9])\b')
venue_pattern = re.compile(r'\b(CHI|Ubicomp|CSCW|DIS|PervasiveHealth|WWW|IUI|OzCHI|TEI|AH|UbiComp)\b')

# Extract paper information
for doc in paper_docs:
    title = doc['filename'].replace('.txt', '')
    text = doc['text']
    
    # Extract year
    year_match = year_pattern.search(text)
    year = int(year_match.group(0)) if year_match else None
    
    # Extract domains
    domains = list(set(domain_pattern.findall(text.lower())))
    domain = ','.join(domains) if domains else ''
    
    # Extract venue
    venue_match = venue_pattern.search(text)
    venue = venue_match.group(0) if venue_match else ''
    
    paper_info.append({
        'title': title,
        'domain': domain,
        'year': year,
        'venue': venue,
        'filename': doc['filename']
    })

print("Total papers:", len(paper_info))
print("Sample extraction:", paper_info[0])
print("Papers with 'food' domain:", len([p for p in paper_info if 'food' in p['domain'].lower()]))

# Store for later use
result = {
    'paper_info': paper_info,
    'citations': citations
}

print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.query_db:0': [{'id': '1', 'title': 'Expense Control: A Gamified, Semi-Automated, Crowd-Based Approach For Receipt Capturing', 'citation_count': '4', 'citation_year': '2017'}, {'id': '2', 'title': 'Expense Control: A Gamified, Semi-Automated, Crowd-Based Approach For Receipt Capturing', 'citation_count': '95', 'citation_year': '2018'}, {'id': '3', 'title': 'Understanding My Data, Myself: Supporting Self-reflection with Ubicomp Technologies', 'citation_count': '32', 'citation_year': '2012'}, {'id': '4', 'title': 'Understanding My Data, Myself: Supporting Self-reflection with Ubicomp Technologies', 'citation_count': '29', 'citation_year': '2013'}, {'id': '5', 'title': 'Understanding My Data, Myself: Supporting Self-reflection with Ubicomp Technologies', 'citation_count': '18', 'citation_year': '2014'}], 'var_functions.list_db:2': ['paper_docs'], 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json', 'var_functions.query_db:6': 'file_storage/functions.query_db:6.json', 'var_functions.query_db:12': 'file_storage/functions.query_db:12.json'}

exec(code, env_args)
