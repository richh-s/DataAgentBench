code = """import json
import re

# Load the data from the previous query
file_path = locals()['var_functions.query_db:5']

with open(file_path, 'r') as f:
    papers_data = json.load(f)

print(f"Total papers retrieved: {len(papers_data)}")

# Function to extract year from text
year_pattern = re.compile(r'\b2016\b')

# Function to check if paper is in physical activity domain
pa_pattern = re.compile(r'physical activity', re.IGNORECASE)

# Process papers
papers_2016_pa = []

for paper in papers_data:
    text = paper.get('text', '')
    filename = paper.get('filename', '')
    
    # Check if text contains 2016 and physical activity
    has_2016 = bool(year_pattern.search(text))
    has_pa = bool(pa_pattern.search(text))
    
    if has_2016 and has_pa:
        # Extract title from filename (remove .txt)
        title = filename.replace('.txt', '') if filename else ''
        
        papers_2016_pa.append({
            'title': title,
            'filename': filename
        })

print(f"Papers from 2016 in physical activity domain: {len(papers_2016_pa)}")
print("Paper titles:")
for p in papers_2016_pa:
    print(f"- {p['title']}")

# Output the list for next steps
result = papers_2016_pa
print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.list_db:0': ['paper_docs'], 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json', 'var_functions.list_db:6': ['Citations', 'sqlite_sequence']}

exec(code, env_args)
