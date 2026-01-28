code = """import json
import re

with open(locals()['var_function-call-8351315325764085192'], 'r') as f:
    papers_list = json.load(f)

count = 0
for p in papers_list:
    text = p['text'][:1000]
    if "CHI" in text:
        print(f"Match in {p['filename']}:")
        # Print the context around CHI
        match = re.search(r".{0,50}CHI.{0,50}", text)
        if match:
            print(match.group(0))
        count += 1
        if count > 5:
            break

print(f"Total containing 'CHI': {count} (stopped at 6)")

print("__RESULT__:")
print(json.dumps("Done"))"""

env_args = {'var_function-call-264858034059979045': 'file_storage/function-call-264858034059979045.json', 'var_function-call-16262197769178367218': {'count': 188, 'sample_title': 'Sundroid: Solar Radiation Awareness with Smartphones'}, 'var_function-call-2494524119581093015': 'file_storage/function-call-2494524119581093015.json', 'var_function-call-3380312142503180972': 'file_storage/function-call-3380312142503180972.json', 'var_function-call-8351315325764085192': 'file_storage/function-call-8351315325764085192.json', 'var_function-call-1959921926523090950': {'total_citations': 0, 'num_papers': 0}, 'var_function-call-8389437484024645991': 'Done'}

exec(code, env_args)
