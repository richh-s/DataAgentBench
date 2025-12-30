code = """import json
import pandas as pd

res = locals()['var_function-call-903221830060996598']
if isinstance(res, str):
    res = json.loads(res)

path_funding = locals()['var_function-call-15751791052793352304']
with open(path_funding, 'r') as f:
    funding_data = json.load(f)
df_funding = pd.DataFrame(funding_data)
df_funding['Amount'] = pd.to_numeric(df_funding['Amount'], errors='coerce').fillna(0)

invalid_names = {'Discussion', 'Recommended Action', 'Subject', 'Item', 'To', 'From', 'Agenda Report', 'Public Works Commission'}

projects = res['projects']
valid_projects = [p for p in projects if p not in invalid_names]

matched_df = df_funding[df_funding['Project_Name'].isin(valid_projects)]
total_funding = matched_df['Amount'].sum()
count = len(matched_df)

print('__RESULT__:')
print(json.dumps({'count': int(count), 'total_funding': float(total_funding), 'projects': list(matched_df['Project_Name'].unique())}))"""

env_args = {'var_function-call-898378015105959722': 'file_storage/function-call-898378015105959722.json', 'var_function-call-898378015105961733': ['Funding'], 'var_function-call-16470054379603944391': 'file_storage/function-call-16470054379603944391.json', 'var_function-call-16470054379603946372': [{'Funding_ID': '1', 'Project_Name': '2021 Annual Street Maintenance', 'Funding_Source': 'Public-Private Partnership (PPP)', 'Amount': '24000'}, {'Funding_ID': '2', 'Project_Name': '2022 Annual Street Maintenance', 'Funding_Source': 'Government Grant', 'Amount': '45000'}, {'Funding_ID': '3', 'Project_Name': '2022 Morning View Resurfacing & Storm Drain Improvements', 'Funding_Source': 'State Development Grant', 'Amount': '38000'}, {'Funding_ID': '4', 'Project_Name': 'Annual Street Maintenance', 'Funding_Source': 'Corporate Sponsorship', 'Amount': '23000'}, {'Funding_ID': '5', 'Project_Name': 'Birdview Avenue Improvements', 'Funding_Source': 'National Foundation Fund', 'Amount': '79000'}], 'var_function-call-15751791052793352313': 'file_storage/function-call-15751791052793352313.json', 'var_function-call-15751791052793352304': 'file_storage/function-call-15751791052793352304.json', 'var_function-call-903221830060996598': {'count': 25, 'total_funding': 1316000.0, 'projects': ['2021 Annual Street Maintenance', 'Annual Street Maintenance', 'Bluffs Park Shade Structure', 'Broad Beach Road Water Quality Infrastructure Repairs', 'Broad Beach Road Water Quality Infrastructure Repairs (CalJPIA Project)', 'Civic Center Water Treatment Facility Phase 2', 'Clover Heights Storm Drain', 'Clover Heights Storm Drain (FEMA Project)', 'Discussion', 'Encinal Canyon Road Drainage Improvements', 'Encinal Canyon Road Drainage Improvements (CalOES Project)', 'Encinal Canyon Road Drainage Improvements (FEMA/CalOES Project)', 'Latigo Canyon Road Culvert Repairs', 'Latigo Canyon Road Culvert Repairs (FEMA Project)', 'Latigo Canyon Road Culvert Repairs (FEMA/CalOES Project)', 'Latigo Canyon Road Roadway/Retaining Wall Improvements', 'Latigo Canyon Road Roadway/Retaining Wall Improvements (FEMA Project)', 'Marie Canyon Green Streets', 'PCH at Trancas Canyon Road Right Turn Lane', 'Recommended Action', 'Trancas Canyon Park Planting and Irrigation Repairs', 'Trancas Canyon Park Planting and Irrigation Repairs (CalJPIA/FEMA Project)', 'Trancas Canyon Park Slope Stabilization Project', 'Trancas Canyon Park Slope Stabilization Project (CalJPIA Project)', 'Westward Beach Road Improvements Project']}}

exec(code, env_args)
