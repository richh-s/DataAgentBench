code = """import json
import re

# Load data
with open(locals()['var_function-call-9219159829113401472'], 'r') as f:
    funding_data = json.load(f)

with open(locals()['var_function-call-15784328976379923357'], 'r') as f:
    civic_docs = json.load(f)

newline_char = chr(10)
full_text = newline_char.join([d.get('text', '') for d in civic_docs])

project_list = funding_data

def is_relevant(txt):
    return re.search(r'emergency|fema', txt, re.IGNORECASE) is not None

results = []

headers = [
    ('Capital Improvement Projects (Design)', 'Design'),
    ('Capital Improvement Projects (Construction)', 'Construction'),
    ('Capital Improvement Projects (Not Started)', 'Not Started')
]

sorted_headers = []
for h_text, status in headers:
    matches = list(re.finditer(re.escape(h_text), full_text, re.IGNORECASE))
    for m in matches:
        sorted_headers.append((m.start(), status))

sorted_headers.sort(key=lambda x: x[0])

text_ranges = []
for i in range(len(sorted_headers)):
    start = sorted_headers[i][0]
    status = sorted_headers[i][1]
    end = sorted_headers[i+1][0] if i+1 < len(sorted_headers) else len(full_text)
    text_ranges.append({'status': status, 'text': full_text[start:end]})

for proj in project_list:
    p_name = proj['Project_Name']
    p_source = proj['Funding_Source']
    p_amount = proj['Amount']
    
    name_relevant = is_relevant(p_name)
    found_status = 'Not Found'
    context_relevant = False
    
    for r in text_ranges:
        idx = r['text'].find(p_name)
        if idx != -1:
            raw_status = r['status']
            chunk = r['text'][idx:idx+2000]
            
            if is_relevant(chunk):
                context_relevant = True
            
            if raw_status == 'Construction':
                if 'completed' in chunk.lower() and 'construction was completed' in chunk.lower():
                    found_status = 'Completed'
                else:
                    found_status = 'Construction'
            else:
                found_status = raw_status
            break
    
    if name_relevant or context_relevant:
        status_out = found_status if found_status != 'Not Found' else 'Unknown'
        results.append({
            'Project_Name': p_name,
            'Funding_Source': p_source,
            'Amount': p_amount,
            'Status': status_out
        })

print('__RESULT__:')
print(json.dumps(results))"""

env_args = {'var_function-call-9219159829113404279': 'file_storage/function-call-9219159829113404279.json', 'var_function-call-9219159829113401472': 'file_storage/function-call-9219159829113401472.json', 'var_function-call-15784328976379923357': 'file_storage/function-call-15784328976379923357.json'}

exec(code, env_args)
