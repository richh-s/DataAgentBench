code = """import pandas as pd
import re
import json

# Load citation data
with open(locals()['var_function-call-14304633044885485792'], 'r') as f:
    citations_data = json.load(f)['results']

# Load paper documents data
with open(locals()['var_function-call-10800172074614865330'], 'r') as f:
    paper_docs_data = json.load(f)['results']

citations_df = pd.DataFrame(citations_data)
citations_df['citation_count'] = pd.to_numeric(citations_df['citation_count'])

food_domain_papers = set()
for doc in paper_docs_data:
    text = doc['text']
    filename = doc['filename']
    title = filename.replace('.txt', '')

    # Search for domain information in the text
    # The regex looks for "domain:" followed by any characters (non-greedy) until "contribution:" or end of string
    match = re.search(r'domain:\s*([^\n]+)', text, re.IGNORECASE)
    if match:
        domains_str = match.group(1)
        if 'food' in domains_str.lower():
            food_domain_papers.add(title)
    
    # Also check if 'food' is mentioned directly in the text as a domain example in context.
    # This is a fallback/additional check, as sometimes domains might be listed without a clear "domain: " prefix,
    # but the problem description implies a structured 'domain:' field.
    # Example from preview: "tracking location [24,30], finances [20], food [11], weight [19,25]"
    # This would be caught by a more general text search.
    if 'food' in text.lower() and ('domain' in text.lower() or 'tracking' in text.lower()):
        food_domain_papers.add(title)


total_citation_count = citations_df[citations_df['title'].isin(food_domain_papers)]['citation_count'].sum()

print('__RESULT__:')
print(json.dumps(total_citation_count))"""

env_args = {'var_function-call-14304633044885485792': 'file_storage/function-call-14304633044885485792.json', 'var_function-call-17520914025772869307': [], 'var_function-call-10800172074614865330': 'file_storage/function-call-10800172074614865330.json'}

exec(code, env_args)
