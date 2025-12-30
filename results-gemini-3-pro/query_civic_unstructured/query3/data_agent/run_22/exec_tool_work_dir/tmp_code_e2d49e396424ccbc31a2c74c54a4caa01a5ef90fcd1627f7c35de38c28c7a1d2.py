code = """import json
import pandas as pd

with open(locals()['var_function-call-4228173855339130551'], 'r') as f:
    civic_docs = json.load(f)

with open(locals()['var_function-call-4228173855339128632'], 'r') as f:
    funding_data = json.load(f)

funding_df = pd.DataFrame(funding_data)
funding_df['Project_Name'] = funding_df['Project_Name'].str.strip()

extracted_projects = []

for doc in civic_docs:
    text = doc['text']
    lines = text.split('\n')
    sections = []
    
    # Identify sections
    for i, line in enumerate(lines):
        line = line.strip()
        # Check for headers
        if ('Capital Improvement Projects (' in line or 'Disaster Recovery Projects (' in line) and line.endswith(')'):
            start_paren = line.rfind('(')
            end_paren = line.rfind(')')
            if start_paren != -1 and end_paren != -1:
                status = line[start_paren+1:end_paren].lower()
                sections.append({'status': status, 'start_line': i})
    
    # Process sections
    for idx, section in enumerate(sections):
        status = section['status']
        start = section['start_line'] + 1
        end = sections[idx+1]['start_line'] if idx + 1 < len(sections) else len(lines)
        
        section_lines = lines[start:end]
        section_text = '\n'.join(section_lines)
        
        # Split by marker
        cid_marker = '(cid:190)'
        token = '||SPLIT||'
        section_text_clean = section_text.replace(cid_marker, token)
        parts = section_text_clean.split(token)
        
        # parts[0] end -> Name 1
        # parts[1] start -> Body 1 ... end -> Name 2
        
        if len(parts) < 2:
            continue
            
        for p_idx in range(1, len(parts)):
            # Name from prev part
            prev_part = parts[p_idx-1]
            prev_lines = [l.strip() for l in prev_part.split('\n') if l.strip()]
            if not prev_lines:
                continue
            p_name = prev_lines[-1]
            
            # Body from current part
            curr_part = parts[p_idx]
            curr_lines = [l.strip() for l in curr_part.split('\n') if l.strip()]
            
            if p_idx < len(parts) - 1:
                # Remove last line (next name)
                if curr_lines:
                    body_lines = curr_lines[:-1]
                else:
                    body_lines = []
            else:
                body_lines = curr_lines
            
            p_text = ' '.join(body_lines)
            
            # Status check
            final_status = status
            if 'Construction was completed' in p_text:
                final_status = 'completed'
            
            # Keywords
            combined = (p_name + ' ' + p_text).lower()
            if 'emergency' in combined or 'fema' in combined:
                extracted_projects.append({
                    'Project_Name': p_name,
                    'status': final_status
                })

# Join
extracted_df = pd.DataFrame(extracted_projects)
if not extracted_df.empty:
    extracted_df['Project_Name'] = extracted_df['Project_Name'].str.strip()
    merged = pd.merge(extracted_df, funding_df, on='Project_Name', how='inner')
    result = merged[['Project_Name', 'Funding_Source', 'Amount', 'status']].to_dict(orient='records')
else:
    result = []

print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_function-call-9734910196601830303': 'file_storage/function-call-9734910196601830303.json', 'var_function-call-9734910196601828350': [{'Funding_ID': '1', 'Project_Name': '2021 Annual Street Maintenance', 'Funding_Source': 'Public-Private Partnership (PPP)', 'Amount': '24000'}, {'Funding_ID': '2', 'Project_Name': '2022 Annual Street Maintenance', 'Funding_Source': 'Government Grant', 'Amount': '45000'}, {'Funding_ID': '3', 'Project_Name': '2022 Morning View Resurfacing & Storm Drain Improvements', 'Funding_Source': 'State Development Grant', 'Amount': '38000'}, {'Funding_ID': '4', 'Project_Name': 'Annual Street Maintenance', 'Funding_Source': 'Corporate Sponsorship', 'Amount': '23000'}, {'Funding_ID': '5', 'Project_Name': 'Birdview Avenue Improvements', 'Funding_Source': 'National Foundation Fund', 'Amount': '79000'}], 'var_function-call-4228173855339130551': 'file_storage/function-call-4228173855339130551.json', 'var_function-call-4228173855339128632': 'file_storage/function-call-4228173855339128632.json'}

exec(code, env_args)
