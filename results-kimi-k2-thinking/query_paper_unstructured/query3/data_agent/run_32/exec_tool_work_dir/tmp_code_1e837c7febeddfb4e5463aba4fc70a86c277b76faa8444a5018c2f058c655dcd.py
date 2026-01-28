code = """import json
import re

# Read the full MongoDB results from the file
storage_key = 'var_functions.query_db:2'
if isinstance(locals()[storage_key], str) and locals()[storage_key].endswith('.json'):
    # It's a file path
    with open(locals()[storage_key], 'r') as f:
        all_papers = json.load(f)
else:
    # It's already loaded
    all_papers = locals()[storage_key]

print(f"Total papers retrieved: {len(all_papers)}")

# Function to extract paper information from the text
paper_info = []

for paper in all_papers:
    filename = paper['filename']
    text = paper['text']
    
    # Extract title from filename (remove .txt extension)
    title = filename.replace('.txt', '')
    
    # Extract year from text - look for patterns like "20XX" or "'XX" near venue information
    year = None
    # Try patterns like: CHI '17, UbiComp '15, etc.
    year_match = re.search(r"'(\d{2})\b", text)
    if year_match:
        year_str = year_match.group(1)
        # Convert to full year (assuming 2000s)
        year = 2000 + int(year_str)
    else:
        # Try full year pattern like 2017, 2018, etc.
        year_match = re.search(r"\b(20\d{2})\b", text)
        if year_match:
            year = int(year_match.group(1))
    
    # Extract contribution - look for patterns that indicate contribution type
    contribution = []
    text_lower = text.lower()
    
    # Check for empirical contribution (the main focus)
    if 'empirical' in text_lower:
        contribution.append('empirical')
    if 'empirically' in text_lower:
        contribution.append('empirical')
    
    paper_info.append({
        'title': title,
        'year': year,
        'contribution': contribution,
        'filename': filename
    })

# Filter papers with 'empirical' contribution and published after 2016
empirical_papers_after_2016 = [
    paper for paper in paper_info 
    if 'empirical' in paper['contribution'] and paper['year'] and paper['year'] > 2016
]

print(f"Papers with empirical contribution after 2016: {len(empirical_papers_after_2016)}")

# Show examples for debugging
for i, paper in enumerate(empirical_papers_after_2016[:5]):
    print(f"{i+1}. {paper['title']} - Year: {paper['year']}")

print('__RESULT__:')
print(json.dumps(empirical_papers_after_2016))"""

env_args = {'var_functions.list_db:0': ['paper_docs'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:4': 'file_storage/functions.query_db:4.json'}

exec(code, env_args)
