code = """import json
import re

with open(locals()['var_function-call-3179318639355232823']) as f:
    docs = json.load(f)

project_names = ["Broad Beach Road Water Quality Repair", "Point Dume Walkway Repairs"]

results = {}

for doc in docs:
    text = doc['text']
    for name in project_names:
        for m in re.finditer(re.escape(name), text, re.IGNORECASE):
            # Extract segment
            start = m.end()
            # Find next header or reasonable length
            # Simple approach: next 500 chars
            segment = text[start:start+500]
            if "park" in segment.lower():
                results[name] = True
            else:
                if name not in results: results[name] = False

print("__RESULT__:")
print(json.dumps(results))"""

env_args = {'var_function-call-4554034855452536121': ['civic_docs'], 'var_function-call-4554034855452533864': ['Funding'], 'var_function-call-4554034855452535703': 'file_storage/function-call-4554034855452535703.json', 'var_function-call-7560016992368588221': 'file_storage/function-call-7560016992368588221.json', 'var_function-call-3179318639355232823': 'file_storage/function-call-3179318639355232823.json', 'var_function-call-15240581338442732047': 21000, 'var_function-call-15316970010288403584': ['Bluffs Park Shade Structure', 'Broad Beach Road Water Quality Repair', 'Point Dume Walkway Repairs']}

exec(code, env_args)
