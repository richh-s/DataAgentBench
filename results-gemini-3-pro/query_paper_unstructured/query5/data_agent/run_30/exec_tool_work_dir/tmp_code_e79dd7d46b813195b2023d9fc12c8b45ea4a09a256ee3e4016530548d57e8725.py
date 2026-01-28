code = """import json

with open(locals()['var_function-call-7711183651007727056'], 'r') as f:
    citations_data = json.load(f)

with open(locals()['var_function-call-4121090962908109712'], 'r') as f:
    paper_docs_data = json.load(f)

paper_map = {d['filename'].replace('.txt', ''): d['text'] for d in paper_docs_data if 'filename' in d}

headers = []
for record in citations_data:
    title = record['title']
    if title in paper_map:
        text = paper_map[title]
        # Get first 100 chars
        snippet = text[:100].replace('\n', ' ')
        headers.append(snippet)
    if len(headers) >= 10:
        break

print("__RESULT__:")
print(json.dumps(headers))"""

env_args = {'var_function-call-7711183651007727056': 'file_storage/function-call-7711183651007727056.json', 'var_function-call-4121090962908109712': 'file_storage/function-call-4121090962908109712.json', 'var_function-call-5326245820750148638': 16, 'var_function-call-17055580434800668848': {'total_citations': 0, 'chi_papers_count': 0, 'matched_titles_preview': []}}

exec(code, env_args)
