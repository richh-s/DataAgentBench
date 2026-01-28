code = """import json
import re

citations_file = locals()['var_function-call-332096647494284469']
papers_file = locals()['var_function-call-9719230712903826217']

with open(citations_file, 'r') as f:
    citations_data = json.load(f)

with open(papers_file, 'r') as f:
    papers_data = json.load(f)

print(f"Total citations: {len(citations_data)}")
print(f"Total papers: {len(papers_data)}")

citation_titles = set(item['title'] for item in citations_data)
paper_titles = set(p['filename'].replace('.txt', '') for p in papers_data)

print(f"Common titles: {len(citation_titles.intersection(paper_titles))}")

# Check Year 2016
papers_2016 = []
for p in papers_data:
    text = p.get('text', '')
    header = text[:2000]
    if '2016' in header:
        papers_2016.append(p['filename'])

print(f"Papers with '2016' in header: {len(papers_2016)}")
if len(papers_2016) > 0:
    print(f"Sample 2016 paper: {papers_2016[0]}")

# Check Physical Activity
papers_pa = []
for p in papers_data:
    text = p.get('text', '').lower()
    if "physical activity" in text:
        papers_pa.append(p['filename'])

print(f"Papers with 'physical activity': {len(papers_pa)}")

# Check Intersection
intersection = set(papers_2016).intersection(set(papers_pa))
print(f"Papers with both: {len(intersection)}")

print("__RESULT__:")
print(json.dumps(list(intersection)))"""

env_args = {'var_function-call-332096647494284469': 'file_storage/function-call-332096647494284469.json', 'var_function-call-332096647494285302': 'file_storage/function-call-332096647494285302.json', 'var_function-call-9719230712903826217': 'file_storage/function-call-9719230712903826217.json', 'var_function-call-9839691519987756055': []}

exec(code, env_args)
