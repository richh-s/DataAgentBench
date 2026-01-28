code = """import json
import re

# Load all MongoDB documents
mongo_docs_path = locals()['var_functions.query_db:14']
with open(mongo_docs_path, 'r') as f:
    mongo_docs = json.load(f)

# Load all funding data
funding_path = locals()['var_functions.query_db:2']
with open(funding_path, 'r') as f:
    funding_data = json.load(f)

# Create funding lookup
funding_dict = {}
for item in funding_data:
    pname = item.get('Project_Name', '')
    funding_dict[pname] = {
        'Funding_Source': item.get('Funding_Source', 'Not specified'),
        'Amount': item.get('Amount', 0)
    }

emergency_projects = []

for doc in mongo_docs:
    text = doc['text']
    lines = text.split('\n')
    
    for i, line in enumerate(lines):
        line = line.strip()
        if not line or len(line) < 5:
            continue
        
        skip_keywords = ['Public Works', 'Commission', 'Meeting', 'Agenda', 'Report', 
                        'To:', 'Prepared', 'Approved', 'Date', 'Subject:', 'RECOMMENDED', 
                        'DISCUSSION:', 'Page', 'Item']
        if any(word in line for word in skip_keywords):
            continue
        
        if i + 1 < len(lines):
            next_text = '\n'.join(lines[i+1:i+4])
            
            if 'Updates:' in next_text or 'Project Schedule:' in next_text:
                status = 'Unknown'
                for j in range(i+1, min(i+10, len(lines))):
                    curr = lines[j]
                    if 'Complete' in curr and 'Construction' in curr:
                        status = 'completed'
                        break
                    elif 'Begin Construction' in curr or 'currently under construction' in curr.lower():
                        status = 'in progress'
                        break
                    elif 'Advertise' in curr or 'Project Schedule' in curr:
                        status = 'design'
                        break
                
                combined = (line + ' ' + '\n'.join(lines[max(0,i-2):min(len(lines),i+8)])).lower()
                if 'fema' in combined or 'emergency' in combined or 'siren' in combined or 'warning' in combined:
                    fund_info = funding_dict.get(line, {'Funding_Source': 'Not specified', 'Amount': 0})
                    
                    emergency_projects.append({
                        'Project_Name': line,
                        'Funding_Source': fund_info['Funding_Source'],
                        'Amount': fund_info['Amount'],
                        'Status': status
                    })

for fund in funding_data:
    pname = fund.get('Project_Name', '')
    plower = pname.lower()
    if 'fema' in plower or 'emergency' in plower or 'siren' in plower or 'warning' in plower:
        exists = any(p['Project_Name'] == pname for p in emergency_projects)
        if not exists:
            status = 'Unknown'
            for doc in mongo_docs:
                if pname in doc['text']:
                    if 'currently under construction' in doc['text'].lower():
                        status = 'in progress'
                    elif 'complete construction' in doc['text'].lower():
                        status = 'completed'
                    break
            
            emergency_projects.append({
                'Project_Name': pname,
                'Funding_Source': fund.get('Funding_Source', 'Not specified'),
                'Amount': fund.get('Amount', 0),
                'Status': status
            })

unique_projects = []
seen = set()
for p in emergency_projects:
    if p['Project_Name'] not in seen:
        unique_projects.append(p)
        seen.add(p['Project_Name'])

print('__RESULT__:')
print(json.dumps(unique_projects, indent=2))"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:9': 'file_storage/functions.query_db:9.json', 'var_functions.query_db:14': 'file_storage/functions.query_db:14.json'}

exec(code, env_args)
