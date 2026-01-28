code = """import json
import re

# Read the MongoDB results file
with open('/tmp/tmpa8i6hpt8.json', 'r') as f:
    papers_data = json.load(f)

print(f"Total papers found: {len(papers_data)}")

# Extract paper information
papers_2016 = []

for paper in papers_data:
    # Extract title from filename
    filename = paper['filename']
    title = filename.replace('.txt', '')
    
    # Look for 2016 in the text
    text = paper['text']
    has_2016 = False
    
    # Search for 2016 specifically
    if re.search(r'\b2016\b', text):
        has_2016 = True
    else:
        # Check for venue patterns with 16
        venue_patterns = re.findall(r'[A-Z]+\s*16', text)
        if venue_patterns:
            # Look for common venues
            common_venues = ['CHI', 'Ubicomp', 'CSCW', 'DIS', 'PervasiveHealth', 'WWW', 'IUI', 'OzCHI', 'TEI', 'AH']
            for pattern in venue_patterns:
                for venue in common_venues:
                    if venue in pattern:
                        has_2016 = True
                        break
    
    if has_2016:
        papers_2016.append({
            'title': title
        })

print(f"Papers from 2016: {len(papers_2016)}")

# Show sample papers from 2016
if papers_2016:
    print("\nSample 2016 papers:")
    for p in papers_2016[:10]:
        print(f"  - {p['title']}")
else:
    print("No 2016 papers found with 'physical activity'")

# Prepare result for next step
result = {
    'papers_2016': papers_2016,
    'count': len(papers_2016)
}

print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.execute_python:9': {'status': 'debugging'}}

exec(code, env_args)
