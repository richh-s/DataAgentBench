code = """import json
import re

# Load paper documents from MongoDB
paper_file = locals()['var_functions.query_db:8']
with open(paper_file, 'r') as f:
    papers = json.load(f)

# Load citation data from SQLite
citation_file = locals()['var_functions.query_db:6']
with open(citation_file, 'r') as f:
    citations = json.load(f)

# Create a dictionary of citations for fast lookup
citation_dict = {item['title']: int(item['total_citations']) for item in citations}

# Function to extract paper information
physical_activity_2016_papers = []

for paper in papers:
    filename = paper['filename']
    text = paper['text']
    
    # Extract title from filename
    title = filename.replace('.txt', '')
    
    # Check if title is in citation_dict (more efficient check first)
    if title not in citation_dict:
        continue
    
    # Extract year - look for 2016 specifically
    year_match = re.search(r'(CHI|Ubicomp|CSCW|DIS|PervasiveHealth|WWW|IUI|OzCHI|TEI|AH|SIGCHI).*?(2016)', text, re.IGNORECASE)
    if not year_match:
        # Also check copyright with 2016
        year_match = re.search(r'\(C\).*?(2016)', text, re.IGNORECASE) or \
                      re.search(r'copyright.*?2016', text, re.IGNORECASE)
    
    year = None
    if year_match:
        try:
            year = int(year_match.group(2)) if len(year_match.groups()) >= 2 else 2016
        except:
            year = 2016 if '2016' in str(year_match.group(0)) else None
    
    # Check if paper is from 2016
    if year != 2016:
        continue
    
    # Check if domain contains 'physical activity'
    # Look for domain patterns in the text
    domain_match = re.search(r'physical activity', text, re.IGNORECASE)
    
    if domain_match:
        physical_activity_2016_papers.append({
            'title': title,
            'year': year,
            'domain': 'physical activity',
            'total_citations': citation_dict[title]
        })

# Format the result
result = json.dumps(physical_activity_2016_papers, indent=2)
print('__RESULT__:')
print(result)"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.execute_python:5': [], 'var_functions.query_db:6': 'file_storage/functions.query_db:6.json', 'var_functions.query_db:8': 'file_storage/functions.query_db:8.json'}

exec(code, env_args)
