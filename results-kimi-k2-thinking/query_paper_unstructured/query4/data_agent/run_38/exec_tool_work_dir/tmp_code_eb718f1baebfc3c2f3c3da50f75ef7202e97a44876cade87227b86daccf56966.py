code = """import json
import re
import pandas as pd

# Get file paths
paper_docs_file = locals()['var_functions.query_db:8']

# Read paper documents
with open(paper_docs_file, 'r') as f:
    paper_docs = json.load(f)

# Extract basic info for analysis
all_papers_info = []
for doc in paper_docs:
    filename = doc.get('filename', '')
    text = doc.get('text', '')
    
    if not filename or not text:
        continue
    
    title = filename.replace('.txt', '')
    
    # Extract year more carefully
    year = None
    year_matches = re.findall(r"\b(20\d{2})\b", text[:5000])
    if year_matches:
        valid_years = [int(y) for y in year_matches if 2010 <= int(y) <= 2025]
        if valid_years:
            year = min(valid_years)
    
    # Extract domain indicators
    text_lower = text.lower()
    domains_found = []
    
    # Check various domains
    if 'physical activity' in text_lower or 'fitness' in text_lower or 'exercise' in text_lower:
        domains_found.append('physical activity')
    if 'sleep' in text_lower:
        domains_found.append('sleep')
    if 'food' in text_lower or 'diet' in text_lower:
        domains_found.append('food')
    if 'mental' in text_lower or 'stress' in text_lower:
        domains_found.append('mental')
    if 'finance' in text_lower or 'money' in text_lower:
        domains_found.append('finances')
    
    all_papers_info.append({
        'title': title,
        'year': year,
        'domains': domains_found
    })

# Analyze the data
df_all = pd.DataFrame(all_papers_info)

print("Total papers analyzed:", len(df_all))
print("\nPapers by year:")
print(df_all['year'].value_counts().sort_index())

print("\nPapers from 2016:")
papers_2016 = df_all[df_all['year'] == 2016]
for _, paper in papers_2016.iterrows():
    domains_str = str(paper['domains']) if paper['domains'] else '[]'
    print(f"  - {paper['title'][:80]}... | Domains: {domains_str}")

print("\nAll papers with physical activity domain:")
physical_activity_papers = df_all[df_all['domains'].apply(lambda x: 'physical activity' in x if x else False)]
for _, paper in physical_activity_papers.iterrows():
    print(f"  - {paper['title'][:80]}... | Year: {paper['year']}")

print("\n2016 papers with physical activity domain:")
papers_2016_pa = df_all[
    (df_all['year'] == 2016) & 
    (df_all['domains'].apply(lambda x: 'physical activity' in x if x else False))
]
print("Count:", len(papers_2016_pa))

# Prepare output
output = []
for _, paper in papers_2016_pa.iterrows():
    output.append({
        'title': paper['title'],
        'year': paper['year'],
        'domains': paper['domains']
    })

print('__RESULT__:')
print(json.dumps(output))"""

env_args = {'var_functions.list_db:0': ['paper_docs'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json', 'var_functions.query_db:8': 'file_storage/functions.query_db:8.json', 'var_functions.execute_python:18': []}

exec(code, env_args)
