code = """import json

# Load funding data
with open(locals()['var_function-call-8778761271394130701'], 'r') as f:
    funding_data = json.load(f)

# Load civic docs
with open(locals()['var_function-call-17737362930517738246'], 'r') as f:
    civic_docs = json.load(f)

funded_projects = set()
for record in funding_data:
    try:
        if float(record['Amount']) > 50000:
            funded_projects.add(record['Project_Name'])
    except:
        pass

extracted_projects = set()

for doc in civic_docs:
    text = doc.get('text', '')
    lines = text.split('\n')
    in_section = False
    
    for i, line in enumerate(lines):
        line = line.strip()
        if 'Capital Improvement Projects (Design)' in line:
            in_section = True
            continue
        
        if in_section:
            if 'Capital Improvement Projects (' in line and 'Design' not in line:
                in_section = False
                continue
            
            if not line:
                continue
            
            # Check for common non-project lines
            if line.startswith('Page ') or line.startswith('Agenda Item') or line.lower().startswith('prepared by') or line.lower().startswith('approved by'):
                continue
            
            if line.startswith('(cid:'):
                continue
            
            # Look ahead for bullet points indicating this is a header for a project section
            is_proj = False
            for k in range(i+1, len(lines)):
                nxt = lines[k].strip()
                if not nxt:
                    continue
                if nxt.startswith('(cid:'):
                    is_proj = True
                    break
                else:
                    break
            
            if is_proj:
                extracted_projects.add(line)

final_projects = extracted_projects.intersection(funded_projects)

print('__RESULT__:')
print(json.dumps({
    'count': len(final_projects),
    'projects': list(final_projects),
    'debug_extracted': list(extracted_projects),
    'debug_funded_sample': list(funded_projects)[:5]
}))"""

env_args = {'var_function-call-8778761271394130701': 'file_storage/function-call-8778761271394130701.json', 'var_function-call-8778761271394130352': 'file_storage/function-call-8778761271394130352.json', 'var_function-call-17737362930517738246': 'file_storage/function-call-17737362930517738246.json'}

exec(code, env_args)
