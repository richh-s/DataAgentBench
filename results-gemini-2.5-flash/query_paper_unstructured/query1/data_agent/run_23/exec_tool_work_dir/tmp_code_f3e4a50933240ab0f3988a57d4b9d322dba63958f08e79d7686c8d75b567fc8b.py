code = """import pandas as pd
import json
import re

# Load citation data
with open(locals()['var_function-call-17816044128111581166'], 'r') as f:
    citation_data = json.load(f)
citations_df = pd.DataFrame(citation_data)
citations_df['citation_count'] = pd.to_numeric(citations_df['citation_count'])

# Load paper documents
with open(locals()['var_function-call-622875477707212501'], 'r') as f:
    paper_docs_data = json.load(f)

# Extract domain and title from paper documents
paper_info = []
for doc in paper_docs_data:
    filename = doc['filename']
    title = filename.replace('.txt', '')
    text = doc['text']

    # Extract domain using regex (case-insensitive for 'domain: food')
    domain_match = re.search(r"domain:\s*([^\n]+)", text, re.IGNORECASE)
    domain = domain_match.group(1).strip() if domain_match else ""

    paper_info.append({'title': title, 'domain': domain})

paper_info_df = pd.DataFrame(paper_info)

# Filter for papers in the 'food' domain
food_papers_df = paper_info_df[paper_info_df['domain'].str.contains('food', case=False, na=False)]

# Merge with citation data
merged_df = pd.merge(food_papers_df, citations_df, on='title', how='inner')

# Calculate total citation count for food domain papers
total_citation_count = merged_df['citation_count'].sum()

print('__RESULT__:')
print(json.dumps(total_citation_count))"""

env_args = {'var_function-call-17816044128111581166': 'file_storage/function-call-17816044128111581166.json', 'var_function-call-622875477707212501': 'file_storage/function-call-622875477707212501.json'}

exec(code, env_args)
