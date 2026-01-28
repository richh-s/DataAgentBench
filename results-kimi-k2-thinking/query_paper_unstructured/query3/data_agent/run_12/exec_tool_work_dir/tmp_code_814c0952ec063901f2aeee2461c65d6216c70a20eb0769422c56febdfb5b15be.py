code = """import json
import re

# Read the full MongoDB query result
file_path = var_functions.query_db:2
with open(file_path, 'r') as f:
    papers = json.load(f)

# Extract paper information
paper_info = []
for paper in papers:
    filename = paper.get('filename', '')
    text = paper.get('text', '')
    
    # Extract title from filename (remove .txt extension)
    title = filename.replace('.txt', '') if filename else ''
    
    # Extract year from text - look for patterns like 'YYYY' or conference years
    year_match = re.search(r"(?:\b|')((?:19|20)\d{2})\b", text)
    year = int(year_match.group(1)) if year_match else None
    
    # Extract contribution type - look for keywords in the text
    contribution = []
    text_lower = text.lower()
    
    if 'empirical' in text_lower:
        contribution.append('empirical')
    if 'artifact' in text_lower or 'system' in text_lower or 'tool' in text_lower:
        contribution.append('artifact')
    if 'theoretical' in text_lower or 'theory' in text_lower:
        contribution.append('theoretical')
    if 'survey' in text_lower or 'review' in text_lower:
        contribution.append('survey')
    if 'methodological' in text_lower or 'method' in text_lower:
        contribution.append('methodological')
    
    contribution_str = ','.join(contribution) if contribution else ''
    
    paper_info.append({
        'title': title,
        'year': year,
        'contribution': contribution_str
    })

# Filter papers with empirical contribution and published after 2016
empirical_papers = [p for p in paper_info if p['year'] and p['year'] > 2016 and 'empirical' in p['contribution'].lower()]

print('__RESULT__:')
print(json.dumps(empirical_papers))"""

env_args = {'var_functions.list_db:0': ['paper_docs'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json'}

exec(code, env_args)
