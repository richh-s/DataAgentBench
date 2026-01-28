code = """import json
import re
import pandas as pd

civic_docs_path = locals()['var_function-call-774567713491960706']
with open(civic_docs_path, 'r') as f:
    civic_docs = json.load(f)

funding_path = locals()['var_function-call-774567713491960115']
with open(funding_path, 'r') as f:
    funding_data = json.load(f)

def parse_civic_doc(text):
    text = text.replace('\r', '')
    
    sections_map = {
        'Capital Improvement Projects (Design)': 'Design',
        'Capital Improvement Projects (Construction)': 'Construction',
        'Capital Improvement Projects (Not Started)': 'Not Started',
        'Capital Improvement Projects (Completed)': 'Completed',
        'Disaster Recovery Projects': 'Disaster'
    }
    
    found_sections = []
    for header, status in sections_map.items():
        pattern = re.escape(header)
        for match in re.finditer(pattern, text, re.IGNORECASE):
            found_sections.append({'status': status, 'start': match.start(), 'header': match.group()})
    
    found_sections.sort(key=lambda x: x['start'])
    
    parsed_projects = []
    
    rx = r'\n([^\n]+)\n+\(cid:190\)'
    
    for i in range(len(found_sections)):
        section = found_sections[i]
        start_idx = section['start'] + len(section['header'])
        end_idx = found_sections[i+1]['start'] if i+1 < len(found_sections) else len(text)
        
        section_text = text[start_idx:end_idx]
        
        project_matches = list(re.finditer(rx, section_text))
        
        for j in range(len(project_matches)):
            p_start = project_matches[j].start(1)
            p_end = project_matches[j+1].start(0) if j+1 < len(project_matches) else len(section_text)
            
            p_title = project_matches[j].group(1).strip()
            p_content = section_text[project_matches[j].end():p_end]
            
            parsed_projects.append({
                'Project_Name': p_title,
                'Status': section['status'],
                'Content': p_content
            })
            
    return parsed_projects

all_projects = []
for doc in civic_docs:
    all_projects.extend(parse_civic_doc(doc['text']))

df_projects = pd.DataFrame(all_projects)
df_funding = pd.DataFrame(funding_data)

relevant_projects = pd.DataFrame()
if not df_projects.empty:
    def is_rel(row):
        s = (row['Project_Name'] + ' ' + row['Content']).lower()
        return 'emergency' in s or 'fema' in s
    relevant_projects = df_projects[df_projects.apply(is_rel, axis=1)]

results = []
processed_ids = set()

for idx, proj in relevant_projects.iterrows():
    p_name = proj['Project_Name']
    matches = df_funding[df_funding['Project_Name'] == p_name]
    if matches.empty:
        matches = df_funding[df_funding['Project_Name'].str.contains(re.escape(p_name), case=False, na=False)]
    
    if not matches.empty:
        for _, fund in matches.iterrows():
            results.append({
                'Project_Name': fund['Project_Name'],
                'Funding_Source': fund['Funding_Source'],
                'Amount': fund['Amount'],
                'Status': proj['Status']
            })
            processed_ids.add(fund['Funding_ID'])

rel_fund = df_funding[df_funding['Project_Name'].str.contains('emergency|fema', case=False, regex=True)]
for idx, fund in rel_fund.iterrows():
    if fund['Funding_ID'] not in processed_ids:
        f_name = fund['Project_Name']
        status = 'Unknown'
        if not df_projects.empty:
             match = df_projects[df_projects['Project_Name'].apply(lambda x: x in f_name)]
             if not match.empty:
                 status = match.iloc[0]['Status']
        
        results.append({
            'Project_Name': f_name,
            'Funding_Source': fund['Funding_Source'],
            'Amount': fund['Amount'],
            'Status': status
        })
        processed_ids.add(fund['Funding_ID'])

print('__RESULT__:')
print(pd.DataFrame(results).drop_duplicates().to_json(orient='records'))"""

env_args = {'var_function-call-774567713491960115': 'file_storage/function-call-774567713491960115.json', 'var_function-call-774567713491960706': 'file_storage/function-call-774567713491960706.json'}

exec(code, env_args)
