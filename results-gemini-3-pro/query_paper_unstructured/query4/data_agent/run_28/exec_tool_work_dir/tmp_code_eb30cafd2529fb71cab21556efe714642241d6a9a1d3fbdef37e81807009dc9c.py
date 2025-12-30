code = """import json

# Load paper docs
with open(locals()['var_function-call-7398565704940874410'], 'r') as f:
    paper_docs = json.load(f)

# Load citations
with open(locals()['var_function-call-14596373756638571722'], 'r') as f:
    citations_data = json.load(f)

citation_titles = set(c['title'] for c in citations_data)

stats = {}
stats["total_docs"] = len(paper_docs)
stats["total_citations"] = len(citations_data)

# Check for "physical activity"
stats["pa_count"] = sum(1 for d in paper_docs if 'physical activity' in d['text'].lower())

# Check for "2016" in header
stats["y2016_count"] = sum(1 for d in paper_docs if '2016' in d['text'][:1000])

# Check for match of both
matching_docs = [d for d in paper_docs if 'physical activity' in d['text'].lower() and '2016' in d['text'][:1000]]
stats["match_count"] = len(matching_docs)

# Check title matching
sample_doc = paper_docs[0]
sample_title = sample_doc['filename'].replace('.txt', '')
stats["sample_title"] = sample_title
stats["sample_in_citations"] = sample_title in citation_titles

# Sample matching titles
matching_titles_info = []
for d in matching_docs[:5]:
    t = d['filename'].replace('.txt', '')
    matching_titles_info.append({"title": t, "in_citations": t in citation_titles})
stats["matching_samples"] = matching_titles_info

print("__RESULT__:")
print(json.dumps(stats))"""

env_args = {'var_function-call-5420876219690003843': 'file_storage/function-call-5420876219690003843.json', 'var_function-call-14495357574425764744': 'file_storage/function-call-14495357574425764744.json', 'var_function-call-7398565704940874410': 'file_storage/function-call-7398565704940874410.json', 'var_function-call-14596373756638571722': 'file_storage/function-call-14596373756638571722.json', 'var_function-call-10948899133377792843': []}

exec(code, env_args)
