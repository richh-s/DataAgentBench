code = """import json
import re

with open(locals()['var_function-call-3179318639355232823']) as f:
    docs = json.load(f)
with open(locals()['var_function-call-7560016992368588221']) as f:
    funding = json.load(f)

funding_map = {item['Project_Name']: int(item['Amount']) for item in funding}
project_names = list(funding_map.keys())
project_names.sort(key=len, reverse=True)

found_completed = []

for doc in docs:
    text = doc['text']
    matches = []
    for name in project_names:
        for m in re.finditer(re.escape(name), text, re.IGNORECASE):
            matches.append({'start': m.start(), 'end': m.end(), 'name': name})
    matches.sort(key=lambda x: (x['start'], -(x['end'] - x['start'])))
    final_matches = []
    if matches:
        curr = matches[0]
        for next_m in matches[1:]:
            if next_m['start'] >= curr['end']:
                final_matches.append(curr)
                curr = next_m
        final_matches.append(curr)
    
    for i, m in enumerate(final_matches):
        seg_start = m['end']
        seg_end = final_matches[i+1]['start'] if i+1 < len(final_matches) else len(text)
        segment = text[seg_start:seg_end]
        s_lower = segment.lower()
        if re.search(r"construction\s+was\s+completed.{0,100}2022", s_lower):
            found_completed.append(m['name'])

print("__RESULT__:")
print(json.dumps(found_completed))"""

env_args = {'var_function-call-4554034855452536121': ['civic_docs'], 'var_function-call-4554034855452533864': ['Funding'], 'var_function-call-4554034855452535703': 'file_storage/function-call-4554034855452535703.json', 'var_function-call-7560016992368588221': 'file_storage/function-call-7560016992368588221.json', 'var_function-call-3179318639355232823': 'file_storage/function-call-3179318639355232823.json', 'var_function-call-15240581338442732047': 21000}

exec(code, env_args)
