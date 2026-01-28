code = """import json

# Load paper docs
with open(locals()['var_function-call-7398565704940874410'], 'r') as f:
    paper_docs = json.load(f)

# Load citations
with open(locals()['var_function-call-14596373756638571722'], 'r') as f:
    citations_data = json.load(f)

citation_titles = set(c['title'] for c in citations_data)

print(f"Total docs: {len(paper_docs)}")
print(f"Total citations records: {len(citations_data)}")

# Check for "physical activity"
pa_count = sum(1 for d in paper_docs if 'physical activity' in d['text'].lower())
print(f"Docs with 'physical activity': {pa_count}")

# Check for "2016" in header
y2016_count = sum(1 for d in paper_docs if '2016' in d['text'][:1000])
print(f"Docs with '2016' in header: {y2016_count}")

# Check for match of both
match_count = sum(1 for d in paper_docs if 'physical activity' in d['text'].lower() and '2016' in d['text'][:1000])
print(f"Docs matching both: {match_count}")

# Check title matching
sample_doc = paper_docs[0]
sample_title = sample_doc['filename'].replace('.txt', '')
print(f"Sample Title from Doc: '{sample_title}'")
print(f"Is Sample Title in Citations? {sample_title in citation_titles}")

# Print a few titles from matching docs to see if they exist in citations
matching_docs = [d for d in paper_docs if 'physical activity' in d['text'].lower() and '2016' in d['text'][:1000]]
if matching_docs:
    print("Sample matching doc titles:")
    for d in matching_docs[:3]:
        t = d['filename'].replace('.txt', '')
        print(f"'{t}' (In citations: {t in citation_titles})")

print("__RESULT__:")
print("DEBUG_DONE")"""

env_args = {'var_function-call-5420876219690003843': 'file_storage/function-call-5420876219690003843.json', 'var_function-call-14495357574425764744': 'file_storage/function-call-14495357574425764744.json', 'var_function-call-7398565704940874410': 'file_storage/function-call-7398565704940874410.json', 'var_function-call-14596373756638571722': 'file_storage/function-call-14596373756638571722.json', 'var_function-call-10948899133377792843': []}

exec(code, env_args)
