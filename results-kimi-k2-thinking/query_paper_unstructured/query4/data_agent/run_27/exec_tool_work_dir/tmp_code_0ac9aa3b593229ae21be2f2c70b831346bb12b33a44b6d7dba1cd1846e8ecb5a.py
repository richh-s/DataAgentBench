code = """import json
import re

# Access the storage variable - stored as a file path
storage_key = 'var_functions.query_db:2'
file_path = locals()[storage_key]

with open(file_path, 'r') as f:
    papers_data = json.load(f)

# Extract paper information
papers = []
for doc in papers_data:
    filename = doc.get('filename', '')
    text = doc.get('text', '')
    
    # Extract title from filename (remove .txt extension)
    title = filename.replace('.txt', '') if filename else ''
    
    # Extract year - look for 4-digit year patterns (2010-2025)
    year_match = re.search(r'\b(20[12][0-9])\b', text)
    year = int(year_match.group(1)) if year_match else None
    
    # Check if it's in 'physical activity' domain
    # Look for domain indicators in text
    domain_indicators = [
        'physical activity', 'activity tracking', 'fitness', 'exercise', 
        'steps', 'walking', 'running', 'workout'
    ]
    
    text_lower = text.lower()
    is_physical_activity = any(indicator in text_lower for indicator in domain_indicators)
    
    if title and year and is_physical_activity:
        papers.append({
            'title': title,
            'year': year,
            'domain': 'physical activity'
        })

# Filter for papers from 2016
papers_2016 = [p for p in papers if p['year'] == 2016]

result = {
    'total_papers_found': len(papers),
    'papers_2016': papers_2016,
    'count_2016': len(papers_2016)
}

print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.list_db:0': ['paper_docs'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json'}

exec(code, env_args)
