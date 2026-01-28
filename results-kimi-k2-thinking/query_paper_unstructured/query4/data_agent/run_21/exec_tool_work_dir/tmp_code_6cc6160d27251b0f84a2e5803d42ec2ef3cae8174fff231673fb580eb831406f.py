code = """import json
import re

# Read the full result from the MongoDB query
file_path = var_functions.query_db:4
with open(file_path, 'r') as f:
    papers = json.load(f)

print(f"Found {len(papers)} papers with 'physical activity' in text")

# Extract metadata (title, year, domain) from papers
paper_metadata = []

for paper in papers:
    text = paper.get('text', '')
    filename = paper.get('filename', '')
    
    # Extract title from filename (without .txt)
    title = filename.replace('.txt', '') if filename else ''
    
    # Extract year - look for patterns like 2016, 2015, etc.
    # Common patterns: year in header, copyright, or references
    year_match = re.search(r'(20\d{2})', text)
    year = int(year_match.group(1)) if year_match else None
    
    # Check if domain contains "physical activity"
    # Since domain may be in text, let's search for the pattern
    domain_match = re.search(r'physical activity', text, re.IGNORECASE)
    
    if domain_match and year == 2016:
        paper_metadata.append({
            'title': title,
            'year': year,
            'filename': filename
        })

print(f"Papers from 2016 in physical activity domain: {len(paper_metadata)}")
for p in paper_metadata:
    print(f"  - {p['title']}")

print("__RESULT__:")
print(json.dumps(paper_metadata))"""

env_args = {'var_functions.list_db:0': ['paper_docs'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:4': 'file_storage/functions.query_db:4.json'}

exec(code, env_args)
