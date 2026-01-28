code = """import json
import re

# Load the file with all paper documents using the locals() approach
papers_file = locals()['var_functions.query_db:6']
with open(papers_file, 'r') as f:
    papers = json.load(f)

# Also load citations
citations_file = locals()['var_functions.query_db:8']
with open(citations_file, 'r') as f:
    citations = json.load(f)

# Convert citations to dict for easy lookup
dom = {}
for paper in papers:
    title = paper['filename'].replace('.txt', '')
    
    # Look for domain mentions in the text
    text = paper['text'].lower()
    is_food = 'food' in text
    
    if is_food:
        dom[title] = 'food'

# Now filter citations for food domain papers
food_citations = []
for cit in citations:
    if cit['title'] in dom:
        food_citations.append(cit)

total_citations = sum(int(c['citation_count']) for c in food_citations)

# Let's also list some examples to debug

print('__RESULT__:')
print(json.dumps(f'Found {len(food_citations)} citation records for food papers, total={total_citations}'))"""

env_args = {'var_functions.list_db:0': ['paper_docs'], 'var_functions.query_db:2': [], 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json', 'var_functions.query_db:6': 'file_storage/functions.query_db:6.json', 'var_functions.query_db:8': 'file_storage/functions.query_db:8.json'}

exec(code, env_args)
