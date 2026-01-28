code = """import json
import re

# Load the MongoDB results
mongo_results = locals()['var_functions.query_db:2']

# If mongo_results is a string (file path), load it
if isinstance(mongo_results, str):
    with open(mongo_results, 'r') as f:
        mongo_results = json.load(f)

# Load the citation data
citation_results = locals()['var_functions.query_db:6']
if isinstance(citation_results, str):
    with open(citation_results, 'r') as f:
        citation_results = json.load(f)

# Convert citation results to a dictionary for easy lookup
citation_dict = {}
for item in citation_results:
    title = item.get('title', '')
    citations = int(item.get('total_citations', 0))
    citation_dict[title] = citations

# Process MongoDB documents to extract papers in 'physical activity' domain from 2016
physical_activity_papers_2016 = []

for doc in mongo_results:
    text = doc.get('text', '')
    filename = doc.get('filename', '')
    
    # Extract title from filename
    title = filename.replace('.txt', '') if filename else ''
    
    # Skip if no title
    if not title:
        continue
    
    # Check if paper is in physical activity domain (case-insensitive)
    if 'physical activity' not in text.lower():
        continue
    
    # Extract year - look for 2016 specifically
    year = None
    
    # Pattern 1: Look for venue year patterns like 'CHI 2016' or 'UbiComp 2016'
    venue_pattern = r'(CHI|UbiComp|CSCW|DIS|PervasiveHealth|WWW|IUI|OzCHI|TEI|AH|Ubicomp)[\s\'"]*2016'
    if re.search(venue_pattern, text, re.IGNORECASE):
        year = 2016
    
    # Pattern 2: Look for copyright year patterns
    if not year:
        copyright_pattern = r'Copyright[^\n]*2016'
        if re.search(copyright_pattern, text):
            year = 2016
    
    # Pattern 3: Look for explicit year mentions in context
    if not year:
        # Check if 2016 appears frequently in the text
        year_2016_count = len(re.findall(r'\b2016\b', text))
        year_2015_count = len(re.findall(r'\b2015\b', text))
        year_2017_count = len(re.findall(r'\b2017\b', text))
        
        # If 2016 is mentioned most frequently, assume it's 2016
        if year_2016_count > year_2015_count and year_2016_count > year_2017_count:
            year = 2016
    
    # Check if it's specifically 2016
    if year == 2016:
        # Get citation count if available
        total_citations = citation_dict.get(title, 0)
        
        physical_activity_papers_2016.append({
            'title': title,
            'year': year,
            'total_citations': total_citations
        })

# Sort by citations descending
physical_activity_papers_2016.sort(key=lambda x: x['total_citations'], reverse=True)

# Format output as a list of dictionaries for easier processing
result_data = physical_activity_papers_2016

print('__RESULT__:')
print(json.dumps(result_data))"""

env_args = {'var_functions.list_db:0': ['paper_docs'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.list_db:5': ['Citations', 'sqlite_sequence'], 'var_functions.query_db:6': 'file_storage/functions.query_db:6.json'}

exec(code, env_args)
