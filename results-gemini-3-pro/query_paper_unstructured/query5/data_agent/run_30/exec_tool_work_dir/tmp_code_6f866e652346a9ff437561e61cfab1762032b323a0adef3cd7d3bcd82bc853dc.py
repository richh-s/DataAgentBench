code = """import json
import re

# Load citations
with open(locals()['var_function-call-7711183651007727056'], 'r') as f:
    citations_data = json.load(f)

# Load paper docs
with open(locals()['var_function-call-4121090962908109712'], 'r') as f:
    paper_docs_data = json.load(f)

print(f"Total citation records (2020): {len(citations_data)}")
print(f"Total paper docs: {len(paper_docs_data)}")

paper_map = {}
for doc in paper_docs_data:
    if 'filename' in doc:
        title = doc['filename'].replace('.txt', '')
        paper_map[title] = doc['text']

matches = 0
chi_matches = 0
sample_headers = []

for record in citations_data:
    title = record['title']
    if title in paper_map:
        matches += 1
        text = paper_map[title]
        header = text[:500].replace('\n', ' ')
        if re.search(r'\bCHI\b', text[:2000]) or "Conference on Human Factors in Computing Systems" in text[:2000]:
            chi_matches += 1
        else:
            if len(sample_headers) < 5:
                sample_headers.append(header)

print(f"Papers matched by title: {matches}")
print(f"Papers identified as CHI: {chi_matches}")
print("Sample headers of NON-CHI papers:")
for h in sample_headers:
    print(h)
    
print("__RESULT__:")
print(json.dumps("debug done"))"""

env_args = {'var_function-call-7711183651007727056': 'file_storage/function-call-7711183651007727056.json', 'var_function-call-4121090962908109712': 'file_storage/function-call-4121090962908109712.json', 'var_function-call-5326245820750148638': 16}

exec(code, env_args)
