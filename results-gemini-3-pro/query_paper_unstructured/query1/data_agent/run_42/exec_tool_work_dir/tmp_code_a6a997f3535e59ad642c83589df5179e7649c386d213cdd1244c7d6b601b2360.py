code = """import json
import re

# Load papers
with open(locals()['var_function-call-1190130121296070935'], 'r') as f:
    papers = json.load(f)

print("__RESULT__:")
debug_info = {}
debug_info["total_papers"] = len(papers)
debug_info["sample_titles"] = [p.get('filename', '') for p in papers[:10]]

# Check if any title contains food
food_titles = [p.get('filename') for p in papers if 'food' in p.get('filename', '').lower()]
debug_info["food_titles_sample"] = food_titles[:10]

# Check keyword extraction on the first paper
text = papers[0]['text']
text_lower = text.lower()
start_match = re.search(r'(author keywords|keywords|index terms)', text_lower)
if start_match:
    start_idx = start_match.end()
    chunk = text_lower[start_idx:start_idx+500]
    debug_info["sample_keyword_chunk"] = chunk
else:
    debug_info["sample_keyword_chunk"] = "Not found"
    debug_info["text_preview"] = text[:500]

print(json.dumps(debug_info))"""

env_args = {'var_function-call-14800347907700836141': 'file_storage/function-call-14800347907700836141.json', 'var_function-call-1190130121296070370': 'file_storage/function-call-1190130121296070370.json', 'var_function-call-1190130121296070935': 'file_storage/function-call-1190130121296070935.json', 'var_function-call-16405168858787139098': {'total_citations': 0, 'food_paper_count': 0, 'matched_citations_records': 0, 'matched_papers_in_citations': 0}}

exec(code, env_args)
