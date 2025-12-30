code = """import json
import re

citations_file = locals()['var_function-call-31182004423683262']
papers_file = locals()['var_function-call-15517411522846928457']

with open(citations_file, 'r') as f:
    citations = json.load(f)

with open(papers_file, 'r') as f:
    papers = json.load(f)

debug_info = []
debug_info.append(f"Loaded {len(citations)} citations and {len(papers)} papers.")

debug_info.append("Sample Citations Titles:")
for c in citations[:3]:
    debug_info.append(c['title'])

debug_info.append("Sample Paper Headers:")
for p in papers[:5]:
    debug_info.append(f"Filename: {p['filename']}")
    debug_info.append(f"Header: {repr(p['text'][:200])}")

chi_count = 0
examples = []
for p in papers:
    # Check looser condition
    if "CHI" in p['text'][:500]:
        chi_count += 1
        if len(examples) < 3:
            examples.append(f"Match: {p['filename']} | Context: {repr(p['text'][:100])}")

debug_info.append(f"Total papers with 'CHI' in first 500 chars: {chi_count}")
debug_info.extend(examples)

print("__RESULT__:")
print(json.dumps(debug_info))"""

env_args = {'var_function-call-31182004423683262': 'file_storage/function-call-31182004423683262.json', 'var_function-call-31182004423683057': 'file_storage/function-call-31182004423683057.json', 'var_function-call-15517411522846928457': 'file_storage/function-call-15517411522846928457.json', 'var_function-call-12736721488613794591': 0, 'var_function-call-15094498137369451799': 'debug_done'}

exec(code, env_args)
