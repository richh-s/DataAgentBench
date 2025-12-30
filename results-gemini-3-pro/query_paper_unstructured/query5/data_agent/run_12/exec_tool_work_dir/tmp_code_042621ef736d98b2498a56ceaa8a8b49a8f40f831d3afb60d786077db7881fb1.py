code = """import json

papers_file = locals()['var_function-call-6614480246128303859']
with open(papers_file, 'r') as f:
    papers_data = json.load(f)

citations_file = locals()['var_function-call-10006919701169471588']
with open(citations_file, 'r') as f:
    citations_data = json.load(f)

print("__RESULT__:")
debug_info = {
    "paper_headers": [{ "filename": p['filename'], "header": p['text'][:200] } for p in papers_data[:10]],
    "citation_titles": [c['title'] for c in citations_data[:5]]
}
print(json.dumps(debug_info))"""

env_args = {'var_function-call-10006919701169471588': 'file_storage/function-call-10006919701169471588.json', 'var_function-call-10006919701169474509': 'file_storage/function-call-10006919701169474509.json', 'var_function-call-6614480246128303859': 'file_storage/function-call-6614480246128303859.json', 'var_function-call-327744894284243669': {'total_citations': 0, 'chi_paper_count': 0, 'matched_citation_records': 0}}

exec(code, env_args)
