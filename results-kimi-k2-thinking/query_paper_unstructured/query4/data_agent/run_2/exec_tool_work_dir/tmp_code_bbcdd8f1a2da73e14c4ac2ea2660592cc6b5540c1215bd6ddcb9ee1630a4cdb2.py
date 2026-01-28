code = """import json
import pandas as pd

# Read the file from storage
file_path = locals()['var_functions.query_db:2']
papers_data = []
with open(file_path, 'r', encoding='utf-8') as f:
    papers_data = json.load(f)

# Create DataFrame and inspect structure
df_papers = pd.DataFrame(papers_data)

# Extract title from filename (remove .txt extension)
df_papers['title'] = df_papers['filename'].str.replace('.txt$', '', regex=True)

# Function to extract year from text
import re

def extract_year(text):
    # Look for publication years in various formats
    year_patterns = [
        r'(\d{4})\s+(?:CHI|Proceedings|Conference|Symposium|Workshop)',
        r'(\d{4})\s+(?:Ubicomp|CSCW|DIS|PervasiveHealth|WWW|IUI|OzCHI|TEI|AH)',
        r'(?:CHI|Ubicomp|CSCW) (\d{4})',
        r'\b(201[4-9])\b'  # Match years 2014-2019
    ]
    
    for pattern in year_patterns:
        matches = re.findall(pattern, text)
        if matches:
            return int(matches[0])
    return None

# Extract years
df_papers['year'] = df_papers['text'].apply(extract_year)

# Filter for 2016 papers
df_2016 = df_papers[df_papers['year'] == 2016]

# Check if domains are mentioned in text for physical activity
physical_activity_keywords = ['physical activity', 'exercise', 'fitness', 'activity tracking', 'step count', 'walking', 'running', 'sports']

def is_physical_activity_paper(text):
    text_lower = text.lower()
    for keyword in physical_activity_keywords:
        if keyword in text_lower:
            return True
    return False

# Filter for physical activity domain
df_2016_pa = df_2016[df_2016['text'].apply(is_physical_activity_paper)]

# Get titles for citation matching
print('__RESULT__:')
print(json.dumps({
    'num_2016_pa_papers': len(df_2016_pa),
    'titles': df_2016_pa['title'].tolist(),
    'all_2016_titles': df_2016['title'].tolist()
}))"""

env_args = {'var_functions.list_db:0': ['paper_docs'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json'}

exec(code, env_args)
