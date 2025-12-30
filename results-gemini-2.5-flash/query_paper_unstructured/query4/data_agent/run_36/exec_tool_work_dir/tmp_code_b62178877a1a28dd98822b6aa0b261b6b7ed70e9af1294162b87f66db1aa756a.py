code = """import pandas as pd
import re
import json

# Load citation data
with open(locals()['var_function-call-1105675117886834803'], 'r') as f:
    citations_data = json.load(f)
citations_df = pd.DataFrame(citations_data)
citations_df['citation_count'] = pd.to_numeric(citations_df['citation_count'])

# Load paper documents
with open(locals()['var_function-call-12491728221895612274'], 'r') as f:
    paper_docs = json.load(f)

# Process paper documents to extract title, year, and domain
papers_info = []
for doc in paper_docs:
    filename = doc['filename']
    title = filename.replace('.txt', '')
    text = doc['text']

    # Check for '2016' as a potential publication year, explicitly using word boundaries to ensure it's a year and not part of another number
    # Search in the first 1000 characters where publication year is likely to appear
    is_published_in_2016 = bool(re.search(r"\b2016\b", text[:1000]))
    
    # Check for 'physical activity' (case-insensitive) in the entire text for domain
    is_physical_activity_domain = 'physical activity' in text.lower()

    if is_published_in_2016 and is_physical_activity_domain:
        papers_info.append({'title': title})

papers_df = pd.DataFrame(papers_info)

# Merge with citations data
# We need to ensure that the citation_year is also considered in the join, though it refers to when citations were received
# The question asks for papers *published* in 2016, so the 'year' from the paper_docs is the primary filter
# The citation_count should be the sum of all citations *for* those papers, regardless of citation_year
merged_df = pd.merge(papers_df, citations_df, on='title', how='inner')

# Calculate total citation count for each paper
result = merged_df.groupby('title')['citation_count'].sum().reset_index()
result.rename(columns={'citation_count': 'total_citation_count'}, inplace=True)

print('__RESULT__:')
print(result.to_json(orient='records'))"""

env_args = {'var_function-call-1105675117886834803': 'file_storage/function-call-1105675117886834803.json', 'var_function-call-12491728221895612274': 'file_storage/function-call-12491728221895612274.json', 'var_function-call-14844828871360626708': [], 'var_function-call-11656898717481283878': [], 'var_function-call-278694898533866311': [], 'var_function-call-568840641661754964': []}

exec(code, env_args)
