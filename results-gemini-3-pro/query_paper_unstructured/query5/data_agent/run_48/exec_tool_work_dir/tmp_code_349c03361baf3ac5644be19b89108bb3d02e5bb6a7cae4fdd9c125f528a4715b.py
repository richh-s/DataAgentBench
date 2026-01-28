code = """import json

# Load citations
with open(locals()['var_function-call-264858034059979045'], 'r') as f:
    citations = json.load(f)

# Load papers
with open(locals()['var_function-call-8351315325764085192'], 'r') as f:
    papers_list = json.load(f)

paper_map = {p['filename']: p['text'] for p in papers_list}

print(f"Total citations: {len(citations)}")
print(f"Total papers fetched: {len(papers_list)}")

# Check matches
matched_count = 0
for cite in citations:
    title = cite['title']
    filename = title + ".txt"
    if filename in paper_map:
        matched_count += 1
    else:
        # Print first mismatch
        if matched_count == 0:
            print(f"Mismatch: '{filename}' not in paper_map")
            # Check if there is a similar filename in paper_map
            # Maybe check first 5 keys
            pass

print(f"Total matched filenames: {matched_count}")
print(f"First 5 keys in paper_map: {list(paper_map.keys())[:5]}")

print("__RESULT__:")
print(json.dumps({"matched": matched_count}))"""

env_args = {'var_function-call-264858034059979045': 'file_storage/function-call-264858034059979045.json', 'var_function-call-16262197769178367218': {'count': 188, 'sample_title': 'Sundroid: Solar Radiation Awareness with Smartphones'}, 'var_function-call-2494524119581093015': 'file_storage/function-call-2494524119581093015.json', 'var_function-call-3380312142503180972': 'file_storage/function-call-3380312142503180972.json', 'var_function-call-8351315325764085192': 'file_storage/function-call-8351315325764085192.json', 'var_function-call-1959921926523090950': {'total_citations': 0, 'num_papers': 0}, 'var_function-call-8389437484024645991': 'Done', 'var_function-call-2898140987180465692': 'Done', 'var_function-call-8612993969594668577': {'total_citations': 114, 'num_papers': 2}, 'var_function-call-4793206800934394654': 'Done'}

exec(code, env_args)
