code = """import json

citations_path = locals()['var_function-call-14128661174357449322']
papers_path = locals()['var_function-call-2833110841078300927']

with open(papers_path, 'r') as f:
    papers_data = json.load(f)

count_total = len(papers_data)
count_domain = 0
headers = []

for paper in papers_data:
    text = paper.get('text', '')
    if 'physical activity' in text.lower():
        count_domain += 1
        headers.append(text[:200])
        if len(headers) >= 10: # Just take first 10 for inspection
            break

debug_info = {
    "total_papers": count_total,
    "domain_match_count": count_domain,
    "sample_headers": headers
}

print("__RESULT__:")
print(json.dumps(debug_info))"""

env_args = {'var_function-call-2089186070141819768': 'file_storage/function-call-2089186070141819768.json', 'var_function-call-17809202052441850212': 'file_storage/function-call-17809202052441850212.json', 'var_function-call-17961397819046338500': [{'count(*)': '1405'}], 'var_function-call-2833110841078300927': 'file_storage/function-call-2833110841078300927.json', 'var_function-call-14128661174357449322': 'file_storage/function-call-14128661174357449322.json', 'var_function-call-14339253743603628220': []}

exec(code, env_args)
