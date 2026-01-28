code = """import json
import re

# Load the MongoDB paper documents
with open('var_functions.query_db:2', 'r') as f:
    paper_docs = json.load(f)

# Load the citations data
with open('var_functions.query_db:5', 'r') as f:
    citations = json.load(f)

# Extract paper information
paper_info = []
for doc in paper_docs:
    filename = doc['filename']
    text = doc['text']
    
    # Extract title from filename (remove .txt extension)
    title = filename.replace('.txt', '')
    
    # Extract year from text - look for patterns like '2015' or 'UBICOMP \'15'
    year_match = re.search(r"(?:\b|\')((?:19|20)\d{2})\b", text[:1000])
    year = None
    if year_match:
        year = int(year_match.group(1))
    
    # Try alternative pattern for year (e.g., 'SEPTEMBER 7–11, 2015')
    if not year:
        year_match = re.search(r"(?:JANUARY|FEBRUARY|MARCH|APRIL|MAY|JUNE|JULY|AUGUST|SEPTEMBER|OCTOBER|NOVEMBER|DECEMER)\s+\d+.*?\d{4}", text[:1000])
        if year_match:
            year_str = year_match.group(0)
            year = int(re.search(r"\d{4}", year_str).group(0))
    
    # Extract domain - look for domain keywords in the text
    domain_keywords = ['physical activity', 'fitness', 'exercise', 'activity tracking']
    domain = []
    text_lower = text.lower()
    for keyword in domain_keywords:
        if keyword in text_lower:
            domain.append(keyword)
    
    paper_info.append({
        '_id': doc['_id'],
        'title': title,
        'year': year,
        'domain': domain
    })

# Create a DataFrame for easier processing
import pandas as pd

df_papers = pd.DataFrame(paper_info)
df_citations = pd.DataFrame(citations)

# Convert citation_count to int
df_citations['citation_count'] = df_citations['citation_count'].astype(int)

# Filter papers from 2016
df_papers_2016 = df_papers[df_papers['year'] == 2016]

# Filter papers with physical activity domain
physical_activity_papers = []
for _, paper in df_papers_2016.iterrows():
    if 'physical activity' in paper['domain'] or \
       'fitness' in paper['domain'] or \
       'exercise' in paper['domain'] or \
       'activity tracking' in paper['domain']:
        physical_activity_papers.append(paper)

df_physical_activity = pd.DataFrame(physical_activity_papers)

print(f"Found {len(df_physical_activity)} papers from 2016 in physical activity domain")

# Join with citations to get total citation counts
if not df_physical_activity.empty:
    # Group citations by title and sum
    df_citation_sums = df_citations.groupby('title')['citation_count'].sum().reset()
    df_citation_sums.columns = ['title', 'total_citations']
    
    # Merge with physical activity papers
    result = pd.merge(df_physical_activity, df_citation_sums, on='title', how='left')
    result = result.fillna({'total_citations': 0})
    result['total_citations'] = result['total_citations'].astype(int)
    
    # Select and sort by citations
    final_result = result[['title', 'total_citations']].sort_values('total_citations', ascending=False)
    
    # Convert to list of dicts for JSON output
    output = final_result.to_dict('records')
else:
    output = []

print('__RESULT__:')
print(json.dumps(output, indent=2))"""

env_args = {'var_functions.list_db:0': ['paper_docs'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json'}

exec(code, env_args)
