code = """import json
import pandas as pd
import re

# Read the MongoDB data from the file
file_path = var_functions.query_db:2
with open(file_path, 'r') as f:
    mongo_data = json.load(f)

# Let's process the MongoDB data to extract title, year, contribution type
processed_papers = []

for doc in mongo_data:
    filename = doc.get('filename', '')
    text = doc.get('text', '')
    
    # Extract title from filename (remove .txt extension)
    title = filename.replace('.txt', '') if filename else ''
    
    # Try to extract year from the text
    # Look for patterns like '2017', '2018', etc., usually near the beginning
    year = None
    # Search for year patterns in the first part of the text (usually header)
    header_match = re.search(r'(\b20(1[7-9]|[2-9]\d)\b)', text[:500])
    if header_match:
        year = int(header_match.group(1))
    
    # If year not found in header, search in the whole text
    if not year:
        year_match = re.search(r'(\b20(1[7-9]|[2-9]\d)\b)', text)
        if year_match:
            year = int(year_match.group(1))
    
    # Check if it's an empirical contribution
    # Look for clues in the text - "empirical", "study", "survey", "experiment", etc.
    contribution_type = []
    
    # Convert to lowercase for easier searching
    text_lower = text.lower()
    
    # Check for empirical indicators
    if 'empirical' in text_lower or \
       ('study' in text_lower and 'case study' not in text_lower) or \
       'experiment' in text_lower or \
       'user study' in text_lower or \
       'field study' in text_lower:
        contribution_type.append('empirical')
    
    if 'artifact' in text_lower or 'system' in text_lower or 'prototype' in text_lower:
        contribution_type.append('artifact')
    
    if 'theoretical' in text_lower or 'theory' in text_lower or 'model' in text_lower:
        contribution_type.append('theoretical')
    
    if 'survey' in text_lower or 'literature review' in text_lower:
        contribution_type.append('survey')
    
    if contribution_type:
        processed_papers.append({
            'title': title,
            'year': year,
            'contribution': ','.join(contribution_type)
        })

# Create DataFrame for easier filtering
papers_df = pd.DataFrame(processed_papers)

# Count papers by year
if not papers_df.empty:
    year_counts = papers_df['year'].value_counts().sort_index()
    print('__RESULT__:')
    print(json.dumps({
        'total_papers': len(papers_df),
        'year_distribution': year_counts.to_dict(),
        'papers_with_contribution': len(papers_df[papers_df['contribution'].str.contains('empirical')])
    }))
else:
    print('__RESULT__:')
    print(json.dumps({
        'total_papers': 0,
        'message': 'No papers found'
    }))"""

env_args = {'var_functions.list_db:0': ['paper_docs'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json'}

exec(code, env_args)
