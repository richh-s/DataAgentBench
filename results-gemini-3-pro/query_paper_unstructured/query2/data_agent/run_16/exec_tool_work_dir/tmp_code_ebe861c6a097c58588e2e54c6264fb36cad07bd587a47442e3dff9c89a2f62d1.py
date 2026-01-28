code = """import json
import pandas as pd

citations_path = locals()['var_function-call-15068442808757462000']
with open(citations_path, 'r') as f:
    citations_data = json.load(f)

papers_path = locals()['var_function-call-15068442808757464883']
with open(papers_path, 'r') as f:
    papers_data = json.load(f)

paper_texts = {}
for p in papers_data:
    if 'filename' in p and 'text' in p:
        title = p['filename'].replace('.txt', '')
        paper_texts[title] = p['text']

print("__RESULT__:")
debug_info = {
    "num_citations": len(citations_data),
    "num_papers": len(paper_texts),
    "sample_citation_titles": [x['title'] for x in citations_data[:5]],
    "sample_paper_titles": list(paper_texts.keys())[:5],
    "matching_titles_count": sum(1 for x in citations_data if x['title'] in paper_texts)
}
print(json.dumps(debug_info))"""

env_args = {'var_function-call-15068442808757462000': 'file_storage/function-call-15068442808757462000.json', 'var_function-call-15068442808757464883': 'file_storage/function-call-15068442808757464883.json', 'var_function-call-10205754986180600973': {'average_citation_count': 68.5, 'num_papers': 2}}

exec(code, env_args)
