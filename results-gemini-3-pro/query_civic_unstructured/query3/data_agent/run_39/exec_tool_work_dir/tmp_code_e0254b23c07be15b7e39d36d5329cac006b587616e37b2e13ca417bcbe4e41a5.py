code = """import json

with open(locals()['var_function-call-16869852261944468410'], 'r') as f:
    civic_docs = json.load(f)

with open(locals()['var_function-call-2108232826166806416'], 'r') as f:
    funding_data = json.load(f)

projects = []
newline = chr(10)
keywords = ['emergency', 'fema']

for doc in civic_docs:
    text = doc['text']
    lines = text.split(newline)
    
    current_status = None
    i = 0
    while i < len(lines):
        line = lines[i].strip()
        
        if 'Capital Improvement Projects (Design)' in line:
            current_status = 'design'
        elif 'Capital Improvement Projects (Construction)' in line:
            current_status = 'construction'
        elif 'Capital Improvement Projects (Not Started)' in line:
            current_status = 'not_started'
        
        # Check project start
        is_proj = False
        # Look ahead
        for off in range(1, 4):
            if i + off < len(lines):
                l = lines[i+off].strip()
                if 'Updates:' in l or 'Project Description:' in l:
                    is_proj = True
                    break
        
        if is_proj and current_status and line:
            p_name = line
            p_lines = []
            j = i
            while j < len(lines):
                if 'Capital Improvement Projects (' in lines[j]:
                    break
                
                # Check next project
                is_next = False
                if j > i:
                    for off in range(1, 4):
                        if j + off < len(lines):
                            l = lines[j+off].strip()
                            if ('Updates:' in l or 'Project Description:' in l) and lines[j].strip():
                                is_next = True
                                break
                if is_next:
                    break
                p_lines.append(lines[j])
                j += 1
            
            p_text = newline.join(p_lines)
            p_text_lower = p_text.lower()
            
            final_status = current_status
            if current_status == 'construction':
                if 'completed' in p_text_lower and 'under construction' not in p_text_lower:
                     final_status = 'completed'
                elif 'notice of completion' in p_text_lower:
                     final_status = 'completed'
            
            projects.append({
                'Project_Name': p_name,
                'text': p_text,
                'status': final_status
            })
            
            i = j
            continue
            
        i += 1

final_results = []
for p in projects:
    name = p['Project_Name']
    txt = p['text'].lower()
    nm_lower = name.lower()
    
    rel = False
    if 'emergency' in nm_lower or 'fema' in nm_lower: rel = True
    if 'emergency' in txt or 'fema' in txt: rel = True
    
    fund = []
    has_fema_fund = False
    
    for f in funding_data:
        fn = f['Project_Name']
        fnl = fn.lower()
        match = False
        if nm_lower in fnl or fnl in nm_lower:
            match = True
        
        if match:
            fund.append(f)
            if 'fema' in fnl or 'emergency' in fnl:
                has_fema_fund = True
    
    if rel or has_fema_fund:
        if not fund:
            final_results.append({
                'Project_Name': name,
                'Funding_Source': None,
                'Amount': None,
                'Status': p['status']
            })
        else:
            for fd in fund:
                final_results.append({
                    'Project_Name': fd['Project_Name'],
                    'Funding_Source': fd['Funding_Source'],
                    'Amount': fd['Amount'],
                    'Status': p['status']
                })

print('__RESULT__:')
print(json.dumps(final_results, indent=2))"""

env_args = {'var_function-call-4927192058268625758': ['civic_docs'], 'var_function-call-4927192058268625809': ['Funding'], 'var_function-call-2108232826166805977': 'file_storage/function-call-2108232826166805977.json', 'var_function-call-2108232826166806416': 'file_storage/function-call-2108232826166806416.json', 'var_function-call-16869852261944468410': 'file_storage/function-call-16869852261944468410.json'}

exec(code, env_args)
