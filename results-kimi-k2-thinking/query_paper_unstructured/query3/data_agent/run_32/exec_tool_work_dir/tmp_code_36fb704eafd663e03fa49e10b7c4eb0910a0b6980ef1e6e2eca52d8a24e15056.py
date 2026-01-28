code = """import json
import re

# Load MongoDB data from the file
storage_key = 'var_functions.query_db:12'
mongo_result = locals()[storage_key]

# Read the file if it's a path, otherwise use the data directly
if isinstance(mongo_result, str) and mongo_result.endswith('.json'):
    with open(mongo_result, 'r', encoding='utf-8') as f:
        all_papers = json.load(f)
else:
    all_papers = mongo_result

print(f"Total papers loaded: {len(all_papers)}")

# Extract structured information from each paper
papers_with_metadata = []

for paper in all_papers:
    filename = paper.get('filename', '')
    text = paper.get('text', '')
    
    # Extract title from filename
    title = filename.replace('.txt', '') if filename else ''
    
    # Extract year from text using multiple patterns
    year = None
    
    # Pattern 1: Look for venue notation like CHI '17, UbiComp '15, etc.
    venue_pattern = r"[A-Z][a-zA-Z]*\s+'(\d{2})\b"
    match = re.search(venue_pattern, text)
    if match:
        year = 2000 + int(match.group(1))
    else:
        # Pattern 2: Look for full year like 2017, 2018
        full_year_pattern = r"\b(20[1-9]\d)\b"
        match = re.search(full_year_pattern, text)
        if match:
            year = int(match.group(1))
    
    # Check if paper has empirical contribution
    # Look for keywords that indicate empirical research
    text_lower = text.lower()
    has_empirical = False
    
    # Direct mention of empirical
    if 'empirical' in text_lower:
        has_empirical = True
    else:
        # Look for research methodology indicators
        empirical_indicators = [
            'we conducted', 'we performed', 'we studied', 'we surveyed',
            'experiment', 'user study', 'field study', 'case study',
            'participants', 'subjects', 'data collection', 'interviewed',
            'qualitative study', 'quantitative study', 'mixed methods',
            'survey of', 'interviews with', 'evaluation of'
        ]
        
        # Check abstract/intro area (first 2000 characters)
        intro_text = text_lower[:2000]
        indicator_count = sum(1 for indicator in empirical_indicators if indicator in intro_text)
        
        # If multiple indicators found, likely empirical
        if indicator_count >= 2:
            has_empirical = True
    
    papers_with_metadata.append({
        'title': title,
        'year': year,
        'has_empirical': has_empirical,
        'text_sample': text[:200]  # For debugging
    })

# Filter for empirical papers after 2016
empirical_papers_after_2016 = [
    paper for paper in papers_with_metadata 
    if paper['has_empirical'] and paper['year'] and paper['year'] > 2016
]

print(f"Empirical papers after 2016: {len(empirical_papers_after_2016)}")

# Show some examples
for i, paper in enumerate(empirical_papers_after_2016[:5]):
    print(f"{i+1}. {paper['title']} ({paper['year']})")

print('__RESULT__:')
print(json.dumps(empirical_papers_after_2016))"""

env_args = {'var_functions.list_db:0': ['paper_docs'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:4': 'file_storage/functions.query_db:4.json', 'var_functions.execute_python:8': [], 'var_functions.execute_python:10': [], 'var_functions.query_db:12': 'file_storage/functions.query_db:12.json'}

exec(code, env_args)
