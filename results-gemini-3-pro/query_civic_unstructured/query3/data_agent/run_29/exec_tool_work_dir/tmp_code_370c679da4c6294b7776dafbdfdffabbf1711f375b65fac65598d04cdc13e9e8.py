code = """import json
import re

# Load Funding Data
with open(locals()['var_function-call-14523358791805029933'], 'r') as f:
    funding_data = json.load(f)

funding_map = {item['Project_Name']: item for item in funding_data}
funding_keys = list(funding_map.keys())

# Load Civic Docs
with open(locals()['var_function-call-18295450404769870360'], 'r') as f:
    civic_docs = json.load(f)

extracted_projects = []

for doc in civic_docs:
    text = doc['text']
    lines = text.split('\n')
    
    current_status_context = 'Unknown'
    
    i = 0
    while i < len(lines):
        line = lines[i].strip()
        
        # Check for Headers
        if 'Capital Improvement Projects (' in line:
            # Extract status inside parens
            parts = line.split('(')
            if len(parts) > 1:
                st = parts[1].split(')')[0]
                current_status_context = st.lower()
            i += 1
            continue
            
        if not line:
            i += 1
            continue
            
        # Look ahead for marker
        j = i + 1
        found_marker = False
        while j < len(lines):
            next_line = lines[j].strip()
            if not next_line:
                j += 1
                continue
            if 'Updates:' in next_line or 'Project Description:' in next_line:
                found_marker = True
                break
            else:
                break
        
        if found_marker:
            p_name = line
            # Collect description
            p_description = []
            k = j
            while k < len(lines):
                l_text = lines[k].strip()
                if 'Capital Improvement Projects (' in l_text:
                    break
                
                # Look ahead for next project
                m = k + 1
                is_next_project = False
                while m < len(lines):
                    m_line = lines[m].strip()
                    if not m_line:
                        m += 1
                        continue
                    if 'Updates:' in m_line or 'Project Description:' in m_line:
                        is_next_project = True
                    break
                
                if is_next_project:
                    break
                
                p_description.append(l_text)
                k += 1
            
            full_desc = ' '.join(p_description)
            
            # Determine Status
            status = current_status_context
            desc_lower = full_desc.lower()
            if 'completed' in desc_lower and 'construction' in desc_lower:
                status = 'completed'
            elif 'not started' in desc_lower:
                status = 'not started'
            
            extracted_projects.append({
                'Project_Name': p_name,
                'Status': status,
                'Description': full_desc,
                'Filename': doc['filename']
            })
            i = k
        else:
            i += 1

final_results = []

for p in extracted_projects:
    name = p['Project_Name']
    desc = p['Description']
    
    # Check relevance
    is_relevant = False
    if 'emergency' in name.lower() or 'fema' in name.lower():
        is_relevant = True
    if 'emergency' in desc.lower() or 'fema' in desc.lower():
        is_relevant = True
        
    if is_relevant:
        # Match Funding
        funding = funding_map.get(name)
        if not funding:
            for k in funding_keys:
                if k.startswith(name):
                    funding = funding_map[k]
                    break
        
        funding_source = funding['Funding_Source'] if funding else None
        amount = funding['Amount'] if funding else None
        st = p['Status'].lower()
        
        final_results.append({
            'Project_Name': name,
            'Funding_Source': funding_source,
            'Amount': amount,
            'Status': st
        })

print('__RESULT__:')
print(json.dumps(final_results))"""

env_args = {'var_function-call-9697041815942477768': 'file_storage/function-call-9697041815942477768.json', 'var_function-call-292566524849709372': [{'Funding_ID': '1', 'Project_Name': '2021 Annual Street Maintenance', 'Funding_Source': 'Public-Private Partnership (PPP)', 'Amount': '24000'}, {'Funding_ID': '2', 'Project_Name': '2022 Annual Street Maintenance', 'Funding_Source': 'Government Grant', 'Amount': '45000'}, {'Funding_ID': '3', 'Project_Name': '2022 Morning View Resurfacing & Storm Drain Improvements', 'Funding_Source': 'State Development Grant', 'Amount': '38000'}, {'Funding_ID': '4', 'Project_Name': 'Annual Street Maintenance', 'Funding_Source': 'Corporate Sponsorship', 'Amount': '23000'}, {'Funding_ID': '5', 'Project_Name': 'Birdview Avenue Improvements', 'Funding_Source': 'National Foundation Fund', 'Amount': '79000'}], 'var_function-call-18295450404769870360': 'file_storage/function-call-18295450404769870360.json', 'var_function-call-14523358791805029933': 'file_storage/function-call-14523358791805029933.json'}

exec(code, env_args)
