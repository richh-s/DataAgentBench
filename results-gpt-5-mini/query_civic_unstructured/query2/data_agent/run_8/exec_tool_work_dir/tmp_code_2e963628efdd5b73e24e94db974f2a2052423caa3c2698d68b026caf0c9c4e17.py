code = """import json
import pandas as pd
# Load funding records from storage variable
funding_records = var_call_xL1SJpqfnER4jYSyEdua5N2N
# Load civic docs JSON from file path stored in var_call_5T7fSyQFALHSZBFIs4GjWgrD
with open(var_call_5T7fSyQFALHSZBFIs4GjWgrD, 'r') as f:
    civic_docs = json.load(f)

# Prepare funding dataframe
df_f = pd.DataFrame(funding_records)
# Ensure Amount as int
df_f['Amount'] = df_f['Amount'].astype(int)

# Preprocess civic docs texts to lowercase
for doc in civic_docs:
    doc['text_lower'] = doc.get('text','').lower()

# Function to check if project was completed in 2022 based on doc text
def project_completed_in_2022(project_name):
    pn_lower = project_name.lower()
    for doc in civic_docs:
        text = doc['text_lower']
        if pn_lower in text:
            # check for '2022' and completion indications
            if '2022' in text and ("completed" in text or "completion" in text or "notice of completion" in text or "complete construction" in text or "complete construction:" in text):
                return True, doc.get('filename')
            # also check for phrases like 'construction was completed' with year nearby
            # naive check already covered by above
    return False, None

# For each funding project, check civic docs
matched = []
for idx, row in df_f.iterrows():
    pname = row['Project_Name']
    amount = int(row['Amount'])
    completed, filename = project_completed_in_2022(pname)
    if completed:
        matched.append({'Project_Name': pname, 'Amount': amount, 'Filename': filename})

total = sum(m['Amount'] for m in matched)

# Prepare output
output = {'total_funding_completed_in_2022': total, 'matched_projects': matched}

print("__RESULT__:")
print(json.dumps(output))"""

env_args = {'var_call_aGnrt6alQ5qdFjHoMA5CkDwW': ['civic_docs'], 'var_call_lzDPKqyhbS9H6jNWORt7SHDU': ['Funding'], 'var_call_xL1SJpqfnER4jYSyEdua5N2N': [{'Project_Name': 'Bluffs Park Shade Structure', 'Amount': '21000'}, {'Project_Name': 'Bluffs Park Workout Station', 'Amount': '39000'}, {'Project_Name': 'Legacy Park Benches and Arbors Renovation', 'Amount': '41000'}, {'Project_Name': 'Legacy Park Paver Repair Project', 'Amount': '69000'}, {'Project_Name': 'Malibu Bluffs Park Roof Replacement Project', 'Amount': '44000'}, {'Project_Name': 'Malibu Bluffs Park South Walkway', 'Amount': '91000'}, {'Project_Name': 'Malibu Bluffs Park South Walkway Repairs', 'Amount': '81000'}, {'Project_Name': 'Malibu Park Drainage Improvements', 'Amount': '17000'}, {'Project_Name': 'Malibu Park Resurfacing Project', 'Amount': '14000'}, {'Project_Name': 'Malibu Park Storm Drain Repairs', 'Amount': '50000'}, {'Project_Name': 'Permanent Skate Park', 'Amount': '97000'}, {'Project_Name': 'Trancas Canyon Park Planting and Irrigation Repairs', 'Amount': '78000'}, {'Project_Name': 'Trancas Canyon Park Planting and Irrigation Repairs (CalJPIA/FEMA Project)', 'Amount': '44000'}, {'Project_Name': 'Trancas Canyon Park Planting and Irrigation Repairs (FEMA/CalOES Project)', 'Amount': '92000'}, {'Project_Name': 'Trancas Canyon Park Playground', 'Amount': '24000'}, {'Project_Name': 'Trancas Canyon Park Playground Resurfacing', 'Amount': '65000'}, {'Project_Name': 'Trancas Canyon Park Slope Stabilization Project', 'Amount': '68000'}, {'Project_Name': 'Trancas Canyon Park Slope Stabilization Project (CalJPIA Project)', 'Amount': '43000'}, {'Project_Name': 'Trancas Canyon Park Slope Stabilization Project (CalOES Project)', 'Amount': '32000'}, {'Project_Name': 'Trancas Canyon Park Upper and Lower Slopes Repair', 'Amount': '23000'}], 'var_call_5T7fSyQFALHSZBFIs4GjWgrD': 'file_storage/call_5T7fSyQFALHSZBFIs4GjWgrD.json'}

exec(code, env_args)
