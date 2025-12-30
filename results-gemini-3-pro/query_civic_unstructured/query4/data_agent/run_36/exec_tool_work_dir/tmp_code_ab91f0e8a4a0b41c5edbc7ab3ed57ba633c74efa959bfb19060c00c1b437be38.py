code = """import json
import re
import pandas as pd

path_civic = locals()['var_function-call-15751791052793352313']
path_funding = locals()['var_function-call-15751791052793352304']

with open(path_civic, 'r') as f:
    civic_docs = json.load(f)

with open(path_funding, 'r') as f:
    funding_data = json.load(f)

df_funding = pd.DataFrame(funding_data)
df_funding['Amount'] = pd.to_numeric(df_funding['Amount'], errors='coerce').fillna(0)

project_names = df_funding['Project_Name'].unique().tolist()
project_names.sort(key=len, reverse=True)

# Regex for Spring 2022. 
spring_2022_regex = re.compile(r'Spring\s*2022|March\s*2022|April\s*2022|May\s*2022|2022\s*Spring|03/\d{2}/2022|04/\d{2}/2022|05/\d{2}/2022', re.IGNORECASE)

start_keywords = {'begin', 'start', 'advertise', 'commence'}
end_keywords = {'complete', 'finish', 'end', 'conclude', 'finalize'}

def is_start_date(text_segment, date_start_idx):
    search_start = max(0, date_start_idx - 150)
    preceding = text_segment[search_start:date_start_idx].lower()
    
    last_keyword_pos = -1
    last_keyword_type = None
    
    for kw in start_keywords:
        pos = preceding.rfind(kw)
        if pos > last_keyword_pos:
            last_keyword_pos = pos
            last_keyword_type = 'start'
            
    for kw in end_keywords:
        pos = preceding.rfind(kw)
        if pos > last_keyword_pos:
            last_keyword_pos = pos
            last_keyword_type = 'end'
            
    if last_keyword_type == 'start':
        return True
    return False

found_projects = set()

for doc in civic_docs:
    text = doc['text']
    text = text.replace('(cid:190)', '-').replace('(cid:131)', '*')
    
    for proj in project_names:
        matches = list(re.finditer(re.escape(proj), text, re.IGNORECASE))
        for match in matches:
            start_pos = match.end()
            end_pos = start_pos + 1000
            context = text[start_pos:end_pos]
            
            date_matches = list(spring_2022_regex.finditer(context))
            
            for dm in date_matches:
                if is_start_date(context, dm.start()):
                    found_projects.add(proj)
                    break
            
            if proj in found_projects:
                break

matched_df = df_funding[df_funding['Project_Name'].isin(found_projects)]
total_funding = matched_df['Amount'].sum()
count = len(matched_df)

print('__RESULT__:')
print(json.dumps({'count': int(count), 'total_funding': float(total_funding), 'projects': list(matched_df['Project_Name'].unique())}))"""

env_args = {'var_function-call-898378015105959722': 'file_storage/function-call-898378015105959722.json', 'var_function-call-898378015105961733': ['Funding'], 'var_function-call-16470054379603944391': 'file_storage/function-call-16470054379603944391.json', 'var_function-call-16470054379603946372': [{'Funding_ID': '1', 'Project_Name': '2021 Annual Street Maintenance', 'Funding_Source': 'Public-Private Partnership (PPP)', 'Amount': '24000'}, {'Funding_ID': '2', 'Project_Name': '2022 Annual Street Maintenance', 'Funding_Source': 'Government Grant', 'Amount': '45000'}, {'Funding_ID': '3', 'Project_Name': '2022 Morning View Resurfacing & Storm Drain Improvements', 'Funding_Source': 'State Development Grant', 'Amount': '38000'}, {'Funding_ID': '4', 'Project_Name': 'Annual Street Maintenance', 'Funding_Source': 'Corporate Sponsorship', 'Amount': '23000'}, {'Funding_ID': '5', 'Project_Name': 'Birdview Avenue Improvements', 'Funding_Source': 'National Foundation Fund', 'Amount': '79000'}], 'var_function-call-15751791052793352313': 'file_storage/function-call-15751791052793352313.json', 'var_function-call-15751791052793352304': 'file_storage/function-call-15751791052793352304.json'}

exec(code, env_args)
