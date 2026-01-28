code = """import json
import re
import pandas as pd

# Load data
paper_docs_file = locals()['var_functions.query_db:8']
citations_file = locals()['var_functions.query_db:5']

with open(paper_docs_file, 'r') as f:
    paper_docs = json.load(f)

with open(citations_file, 'r') as f:
    citations = json.load(f)

# Step 1: Extract all papers with their publication years
all_papers = []
for doc in paper_docs:
    title = doc['filename'].replace('.txt', '')
    text = doc['text']
    
    # Extract year - try multiple approaches
    year = None
    
    # Look for 4-digit years in the first 3000 chars
    year_matches = re.findall(r"\b(20(?:11|12|13|14|15|16|17|18|19|20|21|22|23|24|25))\b", text[:3000])
    if year_matches:
        year = int(year_matches[0])
    else:
        # Look for conference notation like CHI '16
        conf_match = re.search(r"(?:CHI|UbiComp|CSCW|DIS|PervasiveHealth|IUI|OzCHI|TEI|AH)\s*['\"](\d{2})['\"]", text[:2000])
        if conf_match:
            year = 2000 + int(conf_match.group(1))
    
    # Extract domain information
    text_lower = text.lower()
    domains = []
    
    if 'physical activity' in text_lower or 'fitness' in text_lower or 'exercise' in text_lower:
        domains.append('physical activity')
    if 'sleep' in text_lower:
        domains.append('sleep')
    if 'food' in text_lower or 'diet' in text_lower:
        domains.append('food')
    if 'mental' in text_lower or 'stress' in text_lower:
        domains.append('mental')
    if 'finance' in text_lower or 'money' in text_lower:
        domains.append('finances')
    if 'productivity' in text_lower:
        domains.append('productivity')
    
    all_papers.append({
        'title': title,
        'year': year,
        'domains': domains
    })

df_all = pd.DataFrame(all_papers)

# Show year distribution
print("Papers by year:")
year_counts = df_all['year'].value_counts().sort_index()
print(year_counts)

# Filter for 2016 papers
papers_2016 = df_all[df_all['year'] == 2016]
print(f"\nTotal papers from 2016: {len(papers_2016)}")

# Now filter 2016 papers for physical activity domain
pa_papers_2016 = []
for _, paper in papers_2016.iterrows():
    if 'physical activity' in paper['domains']:
        pa_papers_2016.append({
            'title': paper['title'],
            'year': paper['year']
        })

print(f"Physical activity papers from 2016: {len(pa_papers_2016)}")

# Show which papers these are
for paper in pa_papers_2016:
    print(f"  - {paper['title']}")

# Join with citation data
df_citations = pd.DataFrame(citations)
df_citations['citation_count'] = df_citations['citation_count'].astype(int)
df_citation_sums = df_citations.groupby('title')['citation_count'].sum().reset_index()
df_citation_sums.columns = ['title', 'total_citations']

# Create DataFrame for 2016 PA papers and merge with citations
if pa_papers_2016:
    df_pa_2016 = pd.DataFrame(pa_papers_2016)
    result = pd.merge(df_pa_2016, df_citation_sums, on='title', how='left')
    result = result.fillna({'total_citations': 0})
    result['total_citations'] = result['total_citations'].astype(int)
    output = result[['title', 'total_citations']].to_dict('records')
else:
    output = []

print(f"\nFinal result count: {len(output)}")
result_json = json.dumps(output, indent=2)
print('__RESULT__:')
print(result_json)"""

env_args = {'var_functions.list_db:0': ['paper_docs'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json', 'var_functions.query_db:8': 'file_storage/functions.query_db:8.json', 'var_functions.execute_python:18': [], 'var_functions.execute_python:24': [], 'var_functions.execute_python:30': [], 'var_functions.execute_python:34': []}

exec(code, env_args)
