code = """import json, pandas as pd

def load(v):
    if isinstance(v, str):
        with open(v,'r',encoding='utf-8') as f:
            return json.load(f)
    return v

fund = load(var_call_VytrNwJGLmcecp3MVoz7WkP3)
started = var_call_2VqvNreVbGVJ7DkmAzegQ8D9['started_2022_disaster_projects']

fdf = pd.DataFrame(fund)
fdf['Total_Amount'] = fdf['Total_Amount'].astype(int)

sdf = pd.DataFrame({'Project_Name': started})
merged = sdf.merge(fdf, on='Project_Name', how='left')
merged['Total_Amount'] = merged['Total_Amount'].fillna(0).astype(int)

result = {
    'projects': merged.to_dict(orient='records'),
    'total_funding': int(merged['Total_Amount'].sum()),
    'missing_projects': merged.loc[merged['Total_Amount']==0,'Project_Name'].tolist()
}
print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_call_kG8ZQWCW2AVY2ZXpQKanylNW': ['Funding'], 'var_call_jVGLGQgarGHvy0J91PYPUfMo': ['civic_docs'], 'var_call_jDyoHOwxFQnWh3YXVXOOXXe1': 'file_storage/call_jDyoHOwxFQnWh3YXVXOOXXe1.json', 'var_call_wdpKCzaziu8R6N0HjcFJdX7l': 'file_storage/call_wdpKCzaziu8R6N0HjcFJdX7l.json', 'var_call_ebmDP9U7vETKwz1Nt2kBhfZv': {'started_2022_disaster_projects': [], 'count': 0}, 'var_call_z7Mf6VF2TPmhf1Kchq3B0YPc': 'file_storage/call_z7Mf6VF2TPmhf1Kchq3B0YPc.json', 'var_call_8NeVT5nkAvKK0lvLybafZDhM': {'started_2022_disaster_projects': ['Summer 2022.', 'Trancas Canyon Park Planting and Irrigation Repairs (CalJPIA/FEMA Project)', 'Trancas Canyon Park Slope Stabilization Project (CalJPIA Project)', 'at 24712 Malibu Road has been eroded and caused damage to Malibu Road.', 'beginning in April 2022.', 'beginning in Fall 2022.', 'beginning in Spring 2022.', 'bid with bids due November 17.', 'coming weeks.', 'completing the final design.', 'final design and preparing the project for public bidding.', 'guardrails within the project limits.', 'is finalizing the bid documents.', 'of 2022.', 'started and is anticipated to be completed by the Spring of 2022.', 'timber with non-combustible materials.'], 'count': 16}, 'var_call_2VqvNreVbGVJ7DkmAzegQ8D9': {'started_2022_disaster_projects': ['Broad Beach Road Water Quality Infrastructure Repairs (CalJPIA Project)', 'Encinal Canyon Road Drainage Improvements (CalOES Project)', 'Latigo Canyon Road Culvert Repairs (FEMA Project)', 'Latigo Canyon Road Roadway/Retaining Wall Improvements (FEMA Project)', 'Malibu Road Slope Repairs (CalOES Project)', 'Trancas Canyon Park Planting and Irrigation Repairs (CalJPIA/FEMA Project)', 'Trancas Canyon Park Slope Stabilization Project (CalJPIA Project)', 'Westward Beach Road Shoulder Repairs (CalOES Project)'], 'count': 8}, 'var_call_VytrNwJGLmcecp3MVoz7WkP3': 'file_storage/call_VytrNwJGLmcecp3MVoz7WkP3.json'}

exec(code, env_args)
