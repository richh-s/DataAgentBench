code = """import json
import pandas as pd

# Load data
with open(locals()['var_function-call-96073466168105581'], 'r') as f:
    civic_docs = json.load(f)

funding_records = locals()['var_function-call-96073466168105534']
if isinstance(funding_records, str) and funding_records.endswith('.json'):
     with open(funding_records, 'r') as f:
        funding_records = json.load(f)

funding_df = pd.DataFrame(funding_records)
funding_df['Amount'] = pd.to_numeric(funding_df['Amount'])

valid_names = set(funding_df['Project_Name'].unique())

started_projects = set()

for doc in civic_docs:
    text = doc['text']
    lines = text.splitlines()
    current_project = None
    
    for line in lines:
        line_clean = line.strip()
        if not line_clean:
            continue
            
        if line_clean in valid_names:
            current_project = line_clean
        
        if current_project:
            if "Spring 2022" in line_clean:
                if "Begin" in line_clean or "Start" in line_clean or "commence" in line_clean.lower():
                    started_projects.add(current_project)

matched_funding = funding_df[funding_df['Project_Name'].isin(started_projects)]
total_funding = int(matched_funding['Amount'].sum()) # Convert to python int
count = len(started_projects)

print("__RESULT__:")
print(json.dumps({
    "project_count": count,
    "total_funding": total_funding,
    "projects": list(started_projects)
}, indent=2))"""

env_args = {'var_function-call-9243709298217568361': ['civic_docs'], 'var_function-call-9243709298217569292': ['Funding'], 'var_function-call-1240620947166126016': 'file_storage/function-call-1240620947166126016.json', 'var_function-call-1240620947166124723': [{'Funding_ID': '1', 'Project_Name': '2021 Annual Street Maintenance', 'Funding_Source': 'Public-Private Partnership (PPP)', 'Amount': '24000'}, {'Funding_ID': '2', 'Project_Name': '2022 Annual Street Maintenance', 'Funding_Source': 'Government Grant', 'Amount': '45000'}, {'Funding_ID': '3', 'Project_Name': '2022 Morning View Resurfacing & Storm Drain Improvements', 'Funding_Source': 'State Development Grant', 'Amount': '38000'}, {'Funding_ID': '4', 'Project_Name': 'Annual Street Maintenance', 'Funding_Source': 'Corporate Sponsorship', 'Amount': '23000'}, {'Funding_ID': '5', 'Project_Name': 'Birdview Avenue Improvements', 'Funding_Source': 'National Foundation Fund', 'Amount': '79000'}], 'var_function-call-96073466168105581': 'file_storage/function-call-96073466168105581.json', 'var_function-call-96073466168105534': 'file_storage/function-call-96073466168105534.json', 'var_function-call-14693348802718225967': [{'project': 'Marie Canyon Green Streets', 'line': '(cid:131) Begin Construction: Spring 2022'}, {'project': 'PCH Signal Synchronization System Improvements Project', 'line': '(cid:131) Complete Final Design: Spring 2022'}, {'project': 'Westward Beach Road Improvements Project', 'line': '(cid:131) Complete Design: Spring 2022'}, {'project': 'shade structures at Malibu Bluffs Park.', 'line': '(cid:131) Complete Design: Spring 2022'}, {'project': 'shade structures at Malibu Bluffs Park.', 'line': '(cid:131) Begin Construction: Spring 2022'}, {'project': 'amenities such as trash cans, benches, tables, and restrooms.', 'line': 'Commission will then review the project in Spring 2022 before final'}, {'project': 'amenities such as trash cans, benches, tables, and restrooms.', 'line': '(cid:131) Complete Design: Spring 2022'}, {'project': 'turn lane at the intersection of PCH and Trancas Canyon Road.', 'line': '(cid:131) Begin Design: Spring 2022'}, {'project': 'Broad Beach Road Water Quality Infrastructure Repairs (CalJPIA Project)', 'line': '(cid:131) Begin Construction: Spring 2022'}, {'project': 'Trancas Canyon Park Planting and Irrigation Repairs (CalJPIA/FEMA Project)', 'line': '(cid:131) Complete Design: Spring 2022'}, {'project': 'Trancas Canyon Park Planting and Irrigation Repairs (CalJPIA/FEMA Project)', 'line': '(cid:131) Begin Construction: Spring 2022'}, {'project': 'Trancas Canyon Park Slope Stabilization Project (CalJPIA Project)', 'line': '(cid:131) Complete Design: Spring 2022'}, {'project': 'Trancas Canyon Park Slope Stabilization Project (CalJPIA Project)', 'line': '(cid:131) Begin Construction: Spring 2022'}, {'project': 'within the City.', 'line': '(cid:131) Completion Date: Spring 2022'}, {'project': 'facilities and roadway embankments that were damaged by the Woolsey Fire.', 'line': '(cid:131) The project design will commence during the Spring 2022.'}, {'project': 'at 24712 Malibu Road has been eroded and caused damage to Malibu Road.', 'line': '(cid:131) Complete Design: Spring 2022'}, {'project': 'Clover Heights Storm Drain (FEMA Project)', 'line': '(cid:131) Complete Design: Spring 2022'}, {'project': 'Latigo Canyon Road Culvert Repairs (FEMA/CalOES Project)', 'line': '(cid:131) Begin Construction: Spring 2022'}, {'project': 'Encinal Canyon Road Drainage Improvements (FEMA/CalOES Project)', 'line': '(cid:131) Begin Construction: Spring 2022'}, {'project': 'Clover Heights Storm Drain (FEMA Project)', 'line': '(cid:131) Complete Design: Spring 2022'}]}

exec(code, env_args)
