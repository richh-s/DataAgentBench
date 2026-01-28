code = """import json
import re

citations_file = locals()['var_function-call-31182004423683262']
papers_file = locals()['var_function-call-15517411522846928457']

with open(citations_file, 'r') as f:
    citations = json.load(f)

with open(papers_file, 'r') as f:
    papers = json.load(f)

print(f"Loaded {len(citations)} citations and {len(papers)} papers.")

print("Sample Citations Titles:")
for c in citations[:5]:
    print(c['title'])

print("\nSample Paper Headers:")
for p in papers[:5]:
    print(f"Filename: {p['filename']}")
    print(f"Header: {p['text'][:200]}") # Print first 200 chars
    print("-" * 20)

# Check for "CHI" in any paper
chi_count = 0
for p in papers:
    if "CHI" in p['text'][:500]:
        chi_count += 1
        if chi_count <= 3:
            print(f"Potential CHI match in: {p['filename']}")
            print(f"Context: {p['text'][:100]}")

print(f"\nTotal papers with 'CHI' in first 500 chars: {chi_count}")
print("__RESULT__:")
print(json.dumps("debug_done"))"""

env_args = {'var_function-call-31182004423683262': 'file_storage/function-call-31182004423683262.json', 'var_function-call-31182004423683057': 'file_storage/function-call-31182004423683057.json', 'var_function-call-15517411522846928457': 'file_storage/function-call-15517411522846928457.json', 'var_function-call-12736721488613794591': 0}

exec(code, env_args)
