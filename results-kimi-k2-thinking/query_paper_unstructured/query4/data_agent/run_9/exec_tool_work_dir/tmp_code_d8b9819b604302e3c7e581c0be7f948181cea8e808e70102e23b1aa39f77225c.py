code = """import json
import re

# Read the query result from file
result_path = var_functions.query_db:18
with open(result_path, 'r') as f:
    papers_physical_activity = json.load(f)

print(f"Total papers mentioning 'physical activity': {len(papers_physical_activity)}")

# Function to extract year from paper text
def extract_year(text):
    # Look for patterns like "2016", "CHI 2016", "UbiComp 2016", etc.
    year_patterns = [
        r'\b(2016)\b',
        r'CHI\s*\b(2016)\b',
        r'UbiComp\s*\b(2016)\b',
        r'CSCW\s*\b(2016)\b',
        r'DIS\s*\b(2016)\b',
        r'PervasiveHealth\s*\b(2016)\b',
        r'WWW\s*\b(2016)\b',
        r'IUI\s*\b(2016)\b',
        r'OzCHI\s*\b(2016)\b',
        r'TEI\s*\b(2016)\b',
        r'AH\s*\b(2016)\b'
    ]
    
    text_upper = text.upper()
    for pattern in year_patterns:
        match = re.search(pattern, text_upper)
        if match:
            return int(match.group(1))
    return None

# Filter papers from 2016 in physical activity domain
papers_2016_physical_activity = []

for paper in papers_physical_activity:
    filename = paper.get('filename', '')
    title = filename.replace('.txt', '') if filename else 'Unknown'
    text = paper.get('text', '')
    
    # Extract year
    year = extract_year(text)
    
    # Check if it's from 2016
    if year == 2016:
        # Check if it's in physical activity domain (count occurrences)
        physical_activity_count = len(re.findall(r'physical activity', text, re.IGNORECASE))
        
        papers_2016_physical_activity.append({
            'title': title,
            'filename': filename,
            'year': year,
            'physical_activity_mentions': physical_activity_count
        })

print(f"\nFound {len(papers_2016_physical_activity)} papers from 2016 in physical activity domain:")
for paper in papers_2016_physical_activity:
    print(f"  - {paper['title']} (mentions: {paper['physical_activity_mentions']})")

# Export the filtered papers
print('__RESULT__:')
print(json.dumps(papers_2016_physical_activity))"""

env_args = {'var_functions.list_db:0': ['paper_docs'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:6': [], 'var_functions.query_db:8': 'file_storage/functions.query_db:8.json', 'var_functions.list_db:14': ['Citations', 'sqlite_sequence'], 'var_functions.query_db:16': 'file_storage/functions.query_db:16.json', 'var_functions.query_db:18': 'file_storage/functions.query_db:18.json'}

exec(code, env_args)
