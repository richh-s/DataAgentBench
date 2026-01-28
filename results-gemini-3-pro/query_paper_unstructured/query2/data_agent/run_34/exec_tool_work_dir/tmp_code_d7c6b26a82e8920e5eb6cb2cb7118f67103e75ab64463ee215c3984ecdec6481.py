code = """import json
import re

# Load citations
with open(locals()['var_function-call-12716425983166983767']) as f:
    citations_list = json.load(f)

# Map title -> citation_count
# Verify if there are duplicate titles for 2018 (should not be, but good to handle)
citations_map = {}
for item in citations_list:
    citations_map[item['title']] = item['citation_count']

# Load papers
with open(locals()['var_function-call-14376232811721009151']) as f:
    papers = json.load(f)

acm_citation_counts = []
debug_sources = []

for p in papers:
    title = p['filename'].replace('.txt', '')
    if title in citations_map:
        text = p.get('text', '')
        # Check for ACM in the first 5000 characters to avoid references
        head_text = text[:5000]
        
        # Check for ACM
        # Use regex to find whole word ACM, or part of copyright string
        if "ACM" in head_text:
             acm_citation_counts.append(citations_map[title])
        
avg_citations = 0
if len(acm_citation_counts) > 0:
    avg_citations = sum(acm_citation_counts) / len(acm_citation_counts)

print("__RESULT__:")
print(json.dumps(avg_citations))"""

env_args = {'var_function-call-12716425983166983767': 'file_storage/function-call-12716425983166983767.json', 'var_function-call-14376232811721009151': 'file_storage/function-call-14376232811721009151.json'}

exec(code, env_args)
