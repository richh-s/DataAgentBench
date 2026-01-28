code = """import json
import re

# Read the MongoDB query results
result_file = var_functions.query_db:0
with open(result_file, 'r') as f:
    papers = json.load(f)

# Function to extract year from paper text
def extract_year(text):
    # Look for year patterns
    year_patterns = [
        r'\b2016\b',  # Look for 2016
        r'Proceedings[^\n]*20\d{2}',  # Common in ACM papers  
        r'\b20\d{2}\b'  # Any year in 2000s
    ]
    
    years = []
    for pattern in year_patterns:
        matches = re.findall(pattern, text)
        years.extend(matches)
    
    # Look for 2016 specifically
    for y in years:
        if '2016' in y:
            return 2016
    
    return None

# Function to check if paper is in physical activity domain
def is_physical_activity_domain(text):
    # Look for domain indicators
    domain_indicators = [
        'physical activity',
        'physical activities', 
        'activity tracker',
        'activity trackers',
        'fitness tracker',
        'fitness tracking',
        'exercise',
        'steps per day',
        'step count',
        'sedentary behavior'
    ]
    
    text_lower = text.lower()
    for indicator in domain_indicators:
        if indicator in text_lower:
            return True
    return False

# Extract paper information
papers_2016_physical_activity = []

for paper in papers:
    text = paper.get('text', '')
    filename = paper.get('filename', '')
    
    # Extract title from filename
    title = filename.replace('.txt', '')
    
    # Check if published in 2016
    year = extract_year(text)
    
    # Check if physical activity domain
    is_pa = is_physical_activity_domain(text)
    
    if year == 2016 and is_pa:
        papers_2016_physical_activity.append({
            'title': title,
            '_id': paper['_id']
        })

print("__RESULT__:")
print(json.dumps({'count': len(papers_2016_physical_activity), 'papers': papers_2016_physical_activity}))"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.list_db:2': ['paper_docs']}

exec(code, env_args)
