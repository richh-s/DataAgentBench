code = """import json

with open(locals()['var_function-call-1932226808801670089'], 'r') as f:
    papers = json.load(f)

print(f"Total papers: {len(papers)}")

# Check for "physical activity"
pa_count = sum(1 for p in papers if "physical activity" in p['text'].lower())
print(f"Papers with 'physical activity': {pa_count}")

# Check for "2016" in first 1000 chars
year_count = sum(1 for p in papers if "2016" in p['text'][:1000])
print(f"Papers with '2016' in header: {year_count}")

# Print headers of first 3 papers to see format
print("Sample headers:")
for p in papers[:3]:
    print(f"--- {p['filename']} ---")
    print(p['text'][:300].replace('\n', ' '))

print("__RESULT__:")
print(json.dumps("debug_done"))"""

env_args = {'var_function-call-1702073112922347921': 'file_storage/function-call-1702073112922347921.json', 'var_function-call-1932226808801670089': 'file_storage/function-call-1932226808801670089.json', 'var_function-call-962751485773488507': []}

exec(code, env_args)
