code = """import json
import pandas as pd

funding_path = locals()['var_function-call-15165357656390883116']
docs_path = locals()['var_function-call-13981208063081827307']

with open(funding_path, 'r') as f:
    funding_records = json.load(f)
df_funding = pd.DataFrame(funding_records)

with open(docs_path, 'r') as f:
    docs = json.load(f)

projects = []
status_map = {
    "Capital Improvement Projects (Design)": "design",
    "Capital Improvement Projects (Construction)": "construction",
    "Capital Improvement Projects (Not Started)": "not started"
}

for doc in docs:
    text = doc['text']
    sections = []
    for header, status_code in status_map.items():
        idx = text.find(header)
        if idx != -1:
            sections.append({'start': idx, 'status': status_code, 'header_len': len(header)})
    
    sections.sort(key=lambda x: x['start'])
    
    for i in range(len(sections)):
        current_section = sections[i]
        start_pos = current_section['start'] + current_section['header_len']
        status = current_section['status']
        end_pos = sections[i+1]['start'] if i + 1 < len(sections) else len(text)
        section_text = text[start_pos:end_pos]
        
        normalized_text = section_text.replace("(cid:190) Project Description:", "(cid:190) Updates:")
        parts = normalized_text.split("(cid:190) Updates:")
        
        current_name = None
        lines0 = [l.strip() for l in parts[0].split('\\n') if l.strip()]
        if lines0:
            current_name = lines0[-1]
        
        for k in range(1, len(parts)):
            body_part = parts[k]
            next_name = None
            content_text = body_part
            
            if k < len(parts) - 1:
                lines = [l.strip() for l in body_part.split('\\n') if l.strip()]
                if lines:
                    next_name = lines[-1]
                    idx_name = body_part.rfind(next_name)
                    if idx_name != -1:
                        content_text = body_part[:idx_name]
            
            if current_name:
                final_status = status
                if status == 'construction':
                    if 'Construction was completed' in content_text or 'Notice of completion filed' in content_text:
                        final_status = 'completed'
                
                combined = (current_name + " " + content_text).lower()
                is_relevant = 'emergency' in combined or 'fema' in combined
                
                projects.append({
                    "Project_Name": current_name,
                    "Status": final_status,
                    "Is_Relevant_Text": is_relevant
                })
            
            current_name = next_name

df_projects = pd.DataFrame(projects)
df_funding['norm_name'] = df_funding['Project_Name'].str.lower().str.strip()
df_projects['norm_name'] = df_projects['Project_Name'].str.lower().str.strip()

mapping = {}
funding_names = df_funding['norm_name'].unique()
project_names = df_projects['norm_name'].unique()

for p in project_names:
    if not isinstance(p, str): continue
    match = None
    if p in funding_names:
        match = p
    else:
        for f in funding_names:
            if p in f or f in p:
                if len(p) > 10 and len(f) > 10:
                    match = f
                    break
    mapping[p] = match

df_projects['matched_funding_name'] = df_projects['norm_name'].map(mapping)
merged = pd.merge(df_projects, df_funding, left_on='matched_funding_name', right_on='norm_name', how='inner', suffixes=('_extracted', '_funding'))

# Use Project_Name_funding for the check
merged['Is_Relevant_Funding'] = merged['Project_Name_funding'].str.lower().str.contains('emergency|fema')
merged['Is_Relevant'] = merged['Is_Relevant_Text'] | merged['Is_Relevant_Funding']

final_results = merged[merged['Is_Relevant']].copy()
final_results['Project_Name'] = final_results['Project_Name_funding']

out_cols = ['Project_Name', 'Funding_Source', 'Amount', 'Status']
print("__RESULT__:")
print(final_results[out_cols].to_json(orient='records'))"""

env_args = {'var_function-call-4192215151994041760': 'file_storage/function-call-4192215151994041760.json', 'var_function-call-15165357656390883116': 'file_storage/function-call-15165357656390883116.json', 'var_function-call-13981208063081827307': 'file_storage/function-call-13981208063081827307.json'}

exec(code, env_args)
