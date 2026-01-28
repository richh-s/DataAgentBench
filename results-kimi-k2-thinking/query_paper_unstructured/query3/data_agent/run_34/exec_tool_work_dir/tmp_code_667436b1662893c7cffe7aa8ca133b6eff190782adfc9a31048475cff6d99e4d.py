code = """import json
import pandas as pd
import re

# Read the MongoDB data from the file
storage_key = 'var_functions.query_db:2'
file_path = locals()[storage_key]

with open(file_path, 'r') as f:
    mongo_data = json.load(f)

# Initialize list for empirical papers after 2016
empirical_papers = []

# Process each document
for doc in mongo_data:
    # Extract title from filename (remove .txt extension)
    filename = doc.get('filename', '')
    if not filename:
        continue
        
    title = filename.replace('.txt', '')
    
    # Get text content
    text = doc.get('text', '')
    if not text:
        continue
    
    # Try to extract year from the text - look for patterns like 2017, 2018, etc.
    year = None
    # Search in first 1000 characters (usually contains header with year)
    year_matches = re.findall(r'\b20(1[7-9]|[2-9]\d)\b', text[:1000])
    if year_matches:
        year = int('20' + year_matches[0])
    
    # Skip if no year found or year <= 2016
    if not year or year <= 2016:
        continue
    
    # Check if empirical contribution based on content
    text_lower = text.lower()
    
    # Look for empirical research indicators
    empirical_indicators = [
        'empirical',
        'study',
        'experiment',
        'user study',
        'field study',
        'evaluation',
        'participants',
        'survey',
        'interview',
        'data collected',
        'quantitative',
        'qualitative'
    ]
    
    # Count empirical indicators (excluding false positives)
    indicator_count = 0
    for indicator in empirical_indicators:
        if indicator in text_lower:
            # Avoid false positives
            if indicator == 'study' and 'case study' in text_lower:
                continue
            indicator_count += 1
    
    # If we have multiple empirical indicators, count as empirical
    if indicator_count >= 2:
        empirical_papers.append({
            'title': title,
            'year': year
        })

# Count empirical papers by year
if empirical_papers:
    ep_df = pd.DataFrame(empirical_papers)
    year_counts = ep_df['year'].value_counts().sort_index()
    
    print('__RESULT__:')
    print(json.dumps({
        'total_empirical_papers_after_2016': len(empirical_papers),
        'year_distribution': year_counts.to_dict(),
        'sample_papers': empirical_papers[:10]
    }))
else:
    print('__RESULT__:')
    print(json.dumps({
        'message': 'No empirical papers found after 2016',
        'empirical_papers': []
    }))"""

env_args = {'var_functions.list_db:0': ['paper_docs'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json'}

exec(code, env_args)
