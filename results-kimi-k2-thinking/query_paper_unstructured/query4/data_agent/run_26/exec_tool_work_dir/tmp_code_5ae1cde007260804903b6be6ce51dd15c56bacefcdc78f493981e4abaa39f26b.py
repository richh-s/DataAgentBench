code = """import json
import re

# Read the physical activity papers from the query result
with open('var_functions.query_db:5.json', 'r') as f:
    papers = json.load(f)

# Function to parse paper info
def parse_paper_info(paper):
    text = paper['text']
    filename = paper['filename']
    
    # Extract title from filename
    title = filename.replace('.txt', '')
    
    # Try to extract year from the text
    year = None
    # Look for patterns like "CHI 2016" or similar
    patterns = ['CHI', 'CSCW', 'DIS', 'TEI', 'IUI', 'WWW']
    for pattern in patterns:
        match = re.search(pattern + r"\s*'?.?\s*(\d{4})", text, re.IGNORECASE)
        if match and 2010 <= int(match.group(1)) <= 2025:
            year = int(match.group(1))
            break
    
    # Check if physical activity is mentioned in the paper
    domain = 'physical activity' if re.search(r'physical activity', text, re.IGNORECASE) else None
    
    return {
        'title': title,
        'year': year,
        'filename': filename,
        'domain': domain
    }

# Parse all papers
parsed_papers = []
for paper in papers:
    parsed = parse_paper_info(paper)
    if parsed['domain'] and parsed['year'] == 2016:
        parsed_papers.append(parsed)

result_json = json.dumps(parsed_papers)
print('__RESULT__:')
print(result_json)"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.list_db:2': ['Citations', 'sqlite_sequence'], 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json'}

exec(code, env_args)
