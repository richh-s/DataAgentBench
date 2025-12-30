code = """import json
import re
import pandas as pd

# Load papers
with open(locals()['var_function-call-9482827288994489608'], 'r') as f:
    papers = json.load(f)

# Load citations
with open(locals()['var_function-call-9482827288994490825'], 'r') as f:
    citations_data = json.load(f)
citations_df = pd.DataFrame(citations_data)
citations_df['citation_count'] = pd.to_numeric(citations_df['citation_count'])

# Process papers
results = []
for p in papers:
    text = p.get('text', '')
    filename = p.get('filename', '')
    title = filename.replace('.txt', '')
    
    # Extract Year
    # Look for 2010-2029 in first 2000 chars
    year_match = re.search(r'\b(20[1-2][0-9])\b', text[:2000])
    if year_match:
        year = int(year_match.group(1))
    else:
        # Fallback: Check if title in citations_df and infer year? 
        # No, citation_year is when it was cited.
        year = None
    
    # Extract Contribution (check for 'empirical')
    # Use simple containment
    is_empirical = 'empirical' in text.lower()
    
    if year and year > 2016 and is_empirical:
        results.append({'title': title, 'year': year})

# Filter citations for these titles
result_titles = [r['title'] for r in results]
filtered_citations = citations_df[citations_df['title'].isin(result_titles)]

# Group by title and sum citation_count
final_stats = filtered_citations.groupby('title')['citation_count'].sum().reset_index()

# Convert to list of dicts
output = final_stats.to_dict(orient='records')

print("__RESULT__:")
print(json.dumps(output))"""

env_args = {'var_function-call-16968373354653802012': 'file_storage/function-call-16968373354653802012.json', 'var_function-call-12820784951702258902': ['paper_docs'], 'var_function-call-12820784951702258801': [{'cid': '0', 'name': 'id', 'type': 'INTEGER', 'notnull': '0', 'dflt_value': 'None', 'pk': '1'}, {'cid': '1', 'name': 'title', 'type': 'TEXT', 'notnull': '1', 'dflt_value': 'None', 'pk': '0'}, {'cid': '2', 'name': 'citation_count', 'type': 'INTEGER', 'notnull': '1', 'dflt_value': 'None', 'pk': '0'}, {'cid': '3', 'name': 'citation_year', 'type': 'INTEGER', 'notnull': '1', 'dflt_value': 'None', 'pk': '0'}], 'var_function-call-15186585176547387853': 'file_storage/function-call-15186585176547387853.json', 'var_function-call-9482827288994489608': 'file_storage/function-call-9482827288994489608.json', 'var_function-call-9482827288994490825': 'file_storage/function-call-9482827288994490825.json'}

exec(code, env_args)
