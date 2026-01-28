code = """import json
import re

# Read the full MongoDB results from the file
storage_key = 'var_functions.query_db:2'
mongo_result = locals()[storage_key]

# If it's a file path, read it; otherwise it's the actual data
if isinstance(mongo_result, str) and mongo_result.endswith('.json'):
    with open(mongo_result, 'r', encoding='utf-8') as f:
        all_papers = json.load(f)
else:
    all_papers = mongo_result

print(f"Total papers loaded: {len(all_papers)}")

# Process the papers to extract structured information
paper_data = []

for paper in all_papers:
    filename = paper.get('filename', '')
    text = paper.get('text', '')
    
    # Extract title from filename
    title = filename.replace('.txt', '') if filename else ''
    
    # Extract year from text
    year = None
    # Look for patterns like: CHI '17, UbiComp '15, 2017, etc.
    year_patterns = [
        r"'(\d{2})\b",  # pattern like '17
        r"\b(20\d{2})\b",  # pattern like 2017
    ]
    
    for pattern in year_patterns:
        match = re.search(pattern, text)
        if match:
            year_str = match.group(1)
            if len(year_str) == 2:
                year = 2000 + int(year_str)
            else:
                year = int(year_str)
            break
    
    # Check if paper has empirical contribution
    has_empirical = False
    text_lower = text.lower()
    
    # Check for empirical keywords
    empirical_keywords = ['empirical', 'empirically', 'study', 'evaluation', 'experiment', 'survey', 'interview', 'user study']
    
    # Look in title and abstract/introduction areas
    # Check if it's empirical research
    if 'empirical' in text_lower:
        has_empirical = True
    elif any(keyword in text_lower for keyword in empirical_keywords):
        # Additional check to see if it's describing empirical work
        # Look for phrases that indicate empirical contribution
        empirical_phrases = [
            'we conducted', 'we performed', 'we studied', 'we surveyed',
            'experiment', 'user study', 'field study', 'case study',
            'participants', 'subjects', 'data collection', 'interviewed'
        ]
        if any(phrase in text_lower for phrase in empirical_phrases):
            has_empirical = True
    
    paper_data.append({
        'title': title,
        'year': year,
        'has_empirical': has_empirical,
        'filename': filename
    })

# Filter for papers with empirical contribution after 2016
empirical_papers_after_2016 = [
    paper for paper in paper_data 
    if paper['has_empirical'] and paper['year'] and paper['year'] > 2016
]

print(f"Empirical papers after 2016: {len(empirical_papers_after_2016)}")

# Show sample papers for debugging
for i, paper in enumerate(empirical_papers_after_2016[:3]):
    print(f"{i+1}. {paper['title']} ({paper['year']})")

print('__RESULT__:')
print(json.dumps(empirical_papers_after_2016))"""

env_args = {'var_functions.list_db:0': ['paper_docs'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:4': 'file_storage/functions.query_db:4.json', 'var_functions.execute_python:8': []}

exec(code, env_args)
