code = """import json
import pandas as pd
import re

# Read the MongoDB data from the file
storage_key = 'var_functions.query_db:2'
file_path = locals()[storage_key]

with open(file_path, 'r') as f:
    mongo_data = json.load(f)

# Process the MongoDB data to extract title, year, contribution type
processed_empirical_papers = []

for doc in mongo_data:
    filename = doc.get('filename', '')
    text = doc.get('text', '')
    
    # Extract title from filename (remove .txt extension)
    title = filename.replace('.txt', '') if filename else ''
    
    # Try to extract year from the text
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
    text_lower = text.lower()
    is_empirical = False
    
    # Check for empirical indicators
    if ('empirical' in text_lower or 
        ('study' in text_lower and 'case study' not in text_lower) or
        'experiment' in text_lower or 
        'user study' in text_lower or 
        'field study' in text_lower):
        is_empirical = True
    
    # Only add empirical papers published after 2016
    if is_empirical and year and year > 2016:
        processed_empirical_papers.append({
            'title': title,
            'year': year
        })

# Create DataFrame with empirical papers
empirical_papers_df = pd.DataFrame(processed_empirical_papers)

# Get titles of these empirical papers
empirical_titles = empirical_papers_df['title'].tolist()

print('__RESULT__:')
print(json.dumps({
    'empirical_papers_count': len(empirical_papers_df),
    'empirical_paper_titles': empirical_titles[:10]  # Top 10 as sample
}))"""

env_args = {'var_functions.list_db:0': ['paper_docs'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json'}

exec(code, env_args)
