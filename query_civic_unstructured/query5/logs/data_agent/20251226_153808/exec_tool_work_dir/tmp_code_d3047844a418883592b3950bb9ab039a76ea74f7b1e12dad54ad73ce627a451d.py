code = """import json

civic_path = var_call_IK3fn2ugEoLmAv5K3pegEKfT
with open(civic_path, 'r', encoding='utf-8') as f:
    civic_docs = json.load(f)

names = [
    'Trancas Canyon Park Planting and Irrigation Repairs',
    'Trancas Canyon Park Slope Stabilization Project'
]

contexts = {}
for name in names:
    contexts[name] = []

for doc in civic_docs:
    text = (doc.get('text') or '').replace('\r\n','\n')
    lines = text.split('\n')
    for idx, ln in enumerate(lines):
        for name in names:
            if name.lower() in ln.lower():
                start = max(0, idx-5)
                end = min(len(lines), idx+30)
                seg = '\n'.join(l.strip() for l in lines[start:end])
                # also find begin construction lines nearby
                if 'Begin Construction' in seg or 'Begin construction' in seg:
                    contexts[name].append({'filename': doc.get('filename'), 'segment': seg})

print('__RESULT__:')
print(json.dumps(contexts))"""

env_args = {'var_call_2KKXqa5RVrT2vjHf1gQGBy65': ['civic_docs'], 'var_call_IK3fn2ugEoLmAv5K3pegEKfT': 'file_storage/call_IK3fn2ugEoLmAv5K3pegEKfT.json', 'var_call_4bAYPsTZoMODzL7tQBATHndp': ['Funding'], 'var_call_t4pMP4lJNGkh6vsjm9xCDWEx': 'file_storage/call_t4pMP4lJNGkh6vsjm9xCDWEx.json', 'var_call_kaXnF2m8GPl1J9oXIje1pDwq': 'ok', 'var_call_ElDAewPKYFmoArgOqYdtWrUA': {'docs': 19, 'funding_rows': 500}, 'var_call_ZdIBJHOcMNOL48rOZtlFzTH7': {'eligible_project_basenames': ['Agenda Item # 4.A.', 'Fire.', 'Trancas Canyon Park Planting and Irrigation Repairs', 'Trancas Canyon Park Slope Stabilization Project', 'Westward Beach Road.', 'at 24712 Malibu Road has been eroded and caused damage to Malibu Road.', 'beginning in April 2022.', 'beginning in Fall 2022.', 'beginning in Spring 2022.', 'bid with bids due November 17.', 'coming weeks.', 'completing the final design.', 'damaged by the Woolsey Fire.', 'drain towards the end of Clover Heights will help eliminate this issue.', 'facilities and roadway embankments that were damaged by the Woolsey Fire.', 'final design and preparing the project for public bidding.', 'guardrails within the project limits.', 'is finalizing the bid documents.', 'of 2022.', 'started and is anticipated to be completed by the Spring of 2022.', 'that was damaged by the Woolsey Fire.', 'timber with non-combustible materials.'], 'funding_records_included': [{'Project_Name': 'Trancas Canyon Park Planting and Irrigation Repairs (CalJPIA/FEMA Project)', 'Amount': 44000}, {'Project_Name': 'Trancas Canyon Park Planting and Irrigation Repairs (FEMA/CalOES Project)', 'Amount': 92000}, {'Project_Name': 'Trancas Canyon Park Slope Stabilization Project (CalJPIA Project)', 'Amount': 43000}, {'Project_Name': 'Trancas Canyon Park Slope Stabilization Project (CalOES Project)', 'Amount': 32000}], 'total_funding': 211000}}

exec(code, env_args)
