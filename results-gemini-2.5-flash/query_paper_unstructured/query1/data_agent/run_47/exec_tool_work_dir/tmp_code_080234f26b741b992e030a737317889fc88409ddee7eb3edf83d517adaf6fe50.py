code = """import pandas as pd
import re
import json

# Load citation data
with open(locals()['var_function-call-14304633044885485792'], 'r') as f:
    citations_data = json.load(f)

# Load paper documents data
with open(locals()['var_function-call-10800172074614865330'], 'r') as f:
    paper_docs_data = json.load(f)

citations_df = pd.DataFrame(citations_data)
citations_df['citation_count'] = pd.to_numeric(citations_df['citation_count'])

food_domain_papers = set()
for doc in paper_docs_data:
    text = doc['text'].lower()
    filename = doc['filename']
    title = filename.replace('.txt', '')

    # Check for 'food' related keywords in the text. This is a heuristic approach
    # since a clear 'domain: food' might not always be present.
    # The problem description mentions: "Common domains include: 'food'", 
    # and "When matching domains or contributions, use substring/contains matching since values may be part of a list."
    if 'food' in text and ('domain' in text or 'tracking' in text or 'topic' in text or 'study' in text or 'research' in text):
        food_domain_papers.add(title)

total_citation_count = citations_df[citations_df['title'].isin(food_domain_papers)]['citation_count'].sum()

print('__RESULT__:')
print(json.dumps(int(total_citation_count)))"""

env_args = {'var_function-call-14304633044885485792': 'file_storage/function-call-14304633044885485792.json', 'var_function-call-17520914025772869307': [], 'var_function-call-10800172074614865330': 'file_storage/function-call-10800172074614865330.json'}

exec(code, env_args)
