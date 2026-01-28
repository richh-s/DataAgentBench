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

# Function to extract year from paper text
def extract_year(text):
    # Look for conference patterns first
    patterns = [
        r'(CHI|Ubicomp|CSCW|DIS|PervasiveHealth|WWW|IUI|OzCHI|TEI|AH).*?\s+(2016)',
        r'Proceedings.*?\s+(2016)',
        r'Copyright.*?\s+(2016)',
        r'\(C\).*?\s+(2016)',
        r'20(16)',
    ]
    
    for pattern in patterns:
        match = re.search(pattern, text, re.IGNORECASE)
        if match:
            try:
                return int(match.group(2)) if len(match.groups()) >= 2 else int(match.group(1))
            except:
                continue
    return None

# Function to check if paper is about physical activity
def is_physical_activity(text):
    # Check for domain mentions
    domain_patterns = [
        r'physical activity',
        r'exercise',
        r'fitness',
        r'step count',
        r'activity tracking',
        r'sedentary behavior',
        r'active living'
    ]
    
    for pattern in domain_patterns:
        if re.search(pattern, text, re.IGNORECASE):
            return True
    return False

# Extract 2016 physical activity papers
physical_activity_2016 = []

for paper in papers:
    filename = paper['filename']
    text = paper['text']
    
    # Extract title
    title = filename.replace('.txt', '')
    
    # Check if this paper has citation data
    if title not in citation_dict:
        continue
    
    # Extract year
    year = extract_year(text)
    
    # Check if it's from 2016 and about physical activity
    if year == 2016 and is_physical_activity(text):
        physical_activity_2016.append({
            'title': title,
            'total_citations': citation_dict[title]
        })

# Format result
result = json.dumps(physical_activity_2016, indent=2)
print('__RESULT__:')
print(result)"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.execute_python:5': [], 'var_functions.query_db:6': 'file_storage/functions.query_db:6.json', 'var_functions.query_db:8': 'file_storage/functions.query_db:8.json', 'var_functions.execute_python:14': [], 'var_functions.execute_python:12': {'total_papers': 5, 'first_paper_keys': ['_id', 'filename', 'text']}}

exec(code, env_args)
