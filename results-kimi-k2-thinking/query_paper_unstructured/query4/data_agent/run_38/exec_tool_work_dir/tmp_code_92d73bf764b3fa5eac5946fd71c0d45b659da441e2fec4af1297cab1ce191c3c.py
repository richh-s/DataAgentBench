code = """import json
import re
import pandas as pd

# Access the stored file paths
paper_docs_file = locals()['var_functions.query_db:8']

# Read paper documents
with open(paper_docs_file, 'r') as f:
    paper_docs = json.load(f)

print(f"Processing {len(paper_docs)} papers...")

# Extract years first
years_info = []
for doc in paper_docs:
    filename = doc.get('filename', '')
    text = doc.get('text', '')
    
    if not filename or not text:
        continue
    
    # Extract title
    title = filename.replace('.txt', '')
    
    # Extract year from text
    year = None
    
    # Pattern 1: Look for 4-digit years
    year_matches = re.findall(r"\b(20\d{2})\b", text[:5000])
    if year_matches:
        valid_years = [int(y) for y in year_matches if 2010 <= int(y) <= 2025]
        if valid_years:
            year = min(valid_years)
    
    # Pattern 2: Look for conference notation
    if not year:
        conf_matches = re.findall(r"[\'\"](\d{2})[\'\"]", text[:2000])
        for match in conf_matches:
            year_int = 2000 + int(match)
            if 2010 <= year_int <= 2025:
                year = year_int
                break
    
    years_info.append({'title': title, 'year': year})

df_years = pd.DataFrame(years_info)
print("Papers by year:")
print(df_years['year'].value_counts().sort_index())

# Find physical activity papers across all years
pa_papers = []
for doc in paper_docs:
    filename = doc.get('filename', '')
    text = doc.get('text', '')
    
    if not filename or not text:
        continue
    
    title = filename.replace('.txt', '')
    text_lower = text.lower()
    
    # More comprehensive physical activity keywords
    pa_keywords = ['physical activity', 'fitness', 'exercise', 'activity tracker', 
                   'step count', 'walking', 'running', 'activity tracking']
    has_pa = any(keyword in text_lower for keyword in pa_keywords)
    
    if has_pa:
        # Get year for this paper
        year_matches = re.findall(r"\b(20\d{2})\b", text[:5000])
        year = None
        if year_matches:
            valid_years = [int(y) for y in year_matches if 2010 <= int(y) <= 2025]
            if valid_years:
                year = min(valid_years)
        
        pa_papers.append({'title': title, 'year': year, 'domain': 'physical activity'})

df_pa = pd.DataFrame(pa_papers)
print(f"\nPhysical activity papers: {len(df_pa)}")
print("Year distribution:")
print(df_pa['year'].value_counts().sort_index())

# Filter for 2016 specifically
pa_2016 = df_pa[df_pa['year'] == 2016]
print(f"\nPhysical activity papers from 2016: {len(pa_2016)}")

# Now get citation counts
citations_file = locals()['var_functions.query_db:5']
with open(citations_file, 'r') as f:
    citations = json.load(f)

df_citations = pd.DataFrame(citations)
df_citations['citation_count'] = df_citations['citation_count'].astype(int)
df_citation_sums = df_citations.groupby('title')['citation_count'].sum().reset_index()
df_citation_sums.columns = ['title', 'total_citations']

# Merge with 2016 PA papers
if not pa_2016.empty:
    result = pd.merge(pa_2016, df_citation_sums, on='title', how='left')
    result = result.fillna({'total_citations': 0})
    result['total_citations'] = result['total_citations'].astype(int)
    result = result[['title', 'total_citations']].sort_values('total_citations', ascending=False)
    output = result.to_dict('records')
else:
    output = []

print("Final output:", output)
print('__RESULT__:')
print(json.dumps(output))"""

env_args = {'var_functions.list_db:0': ['paper_docs'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json', 'var_functions.query_db:8': 'file_storage/functions.query_db:8.json', 'var_functions.execute_python:18': [], 'var_functions.execute_python:24': []}

exec(code, env_args)
