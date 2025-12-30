code = """import json
import pandas as pd
import re
from datetime import datetime

# Load data
funding_path = locals()['var_function-call-7306303962980445652']
with open(funding_path, 'r') as f:
    funding_data = json.load(f)
funding_df = pd.DataFrame(funding_data)

docs_path = locals()['var_function-call-7306303962980444991']
with open(docs_path, 'r') as f:
    civic_docs = json.load(f)

def get_doc_date(filename):
    # Search for MMDDYYYY
    match = re.search(r'(\d{8})', filename)
    if match:
        try:
            return datetime.strptime(match.group(1), '%m%d%Y')
        except ValueError:
            return datetime.min
    return datetime.min

def is_spring_2022(date_str):
    if not date_str: return False
    date_str = date_str.lower()
    if 'spring' in date_str and '2022' in date_str: return True
    if '2022' in date_str:
        if 'march' in date_str or 'april' in date_str or 'may' in date_str: return True
        if '03/2022' in date_str or '04/2022' in date_str or '05/2022' in date_str: return True
        if '2022-03' in date_str or '2022-04' in date_str or '2022-05' in date_str: return True
    return False

project_names = funding_df['Project_Name'].unique()
project_dates = {p: [] for p in project_names}

for doc in civic_docs:
    doc_date = get_doc_date(doc.get('filename', ''))
    text = doc['text']
    
    # Identify project chunks
    found_projects = []
    for pname in project_names:
        for m in re.finditer(re.escape(pname), text, re.IGNORECASE):
            found_projects.append((m.start(), pname))
            
    found_projects.sort(key=lambda x: x[0])
    
    for i in range(len(found_projects)):
        start_idx, pname = found_projects[i]
        end_idx = found_projects[i+1][0] if i < len(found_projects) - 1 else len(text)
        chunk = text[start_idx:end_idx]
        
        # Regex for start date
        pat = r'(?:Begin Construction|Start Construction|Construction Start|Construction Begins|Estimated Start)[\s:]*(.*)'
        match = re.search(pat, chunk, re.IGNORECASE)
        if match:
            date_str = match.group(1).strip()
            # Store (date, date_str)
            project_dates[pname].append((doc_date, date_str))

# Analyze projects
final_matches = []
for pname, entries in project_dates.items():
    if not entries:
        continue
    # Sort by doc_date desc
    entries.sort(key=lambda x: x[0], reverse=True)
    latest_date_str = entries[0][1]
    
    if is_spring_2022(latest_date_str):
        final_matches.append(pname)

count = len(final_matches)
total_funding = funding_df[funding_df['Project_Name'].isin(final_matches)]['Amount'].astype(float).sum()

result = {
    "count": count,
    "total_funding": total_funding,
    "projects": final_matches
}

print("__RESULT__:")
print(json.dumps(result))"""

env_args = {'var_function-call-13605293396723611551': 'file_storage/function-call-13605293396723611551.json', 'var_function-call-13605293396723609998': [{'Funding_ID': '1', 'Project_Name': '2021 Annual Street Maintenance', 'Funding_Source': 'Public-Private Partnership (PPP)', 'Amount': '24000'}, {'Funding_ID': '2', 'Project_Name': '2022 Annual Street Maintenance', 'Funding_Source': 'Government Grant', 'Amount': '45000'}, {'Funding_ID': '3', 'Project_Name': '2022 Morning View Resurfacing & Storm Drain Improvements', 'Funding_Source': 'State Development Grant', 'Amount': '38000'}, {'Funding_ID': '4', 'Project_Name': 'Annual Street Maintenance', 'Funding_Source': 'Corporate Sponsorship', 'Amount': '23000'}, {'Funding_ID': '5', 'Project_Name': 'Birdview Avenue Improvements', 'Funding_Source': 'National Foundation Fund', 'Amount': '79000'}], 'var_function-call-7306303962980445652': 'file_storage/function-call-7306303962980445652.json', 'var_function-call-7306303962980444991': 'file_storage/function-call-7306303962980444991.json', 'var_function-call-16927142306798057421': {'count': 12, 'total_funding': 621000.0, 'projects': ['Latigo Canyon Road Roadway/Retaining Wall Improvements (FEMA Project)', 'Trancas Canyon Park Planting and Irrigation Repairs (CalJPIA/FEMA Project)', 'Encinal Canyon Road Drainage Improvements (FEMA/CalOES Project)', 'PCH Median Improvements Project', 'PCH Signal Synchronization System Improvements Project', 'Latigo Canyon Road Culvert Repairs (FEMA Project)', 'Trancas Canyon Park Slope Stabilization Project (CalJPIA Project)', 'Latigo Canyon Road Culvert Repairs (FEMA/CalOES Project)', 'Broad Beach Road Water Quality Infrastructure Repairs (CalJPIA Project)', 'Marie Canyon Green Streets', 'Civic Center Water Treatment Facility Phase 2', 'Bluffs Park Shade Structure']}}

exec(code, env_args)
