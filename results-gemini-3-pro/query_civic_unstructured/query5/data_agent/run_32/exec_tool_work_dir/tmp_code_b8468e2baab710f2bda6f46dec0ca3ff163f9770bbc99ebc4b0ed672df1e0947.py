code = """import json
import pandas as pd
import re

NEWLINE = chr(10)

path_docs = locals()['var_function-call-10835669272488718990']
path_fund = locals()['var_function-call-10835669272488721645']

with open(path_docs, 'r') as f:
    civic_docs = json.load(f)

with open(path_fund, 'r') as f:
    funding_data = json.load(f)

for r in funding_data:
    r['Amount'] = int(r['Amount'])

df_funding = pd.DataFrame(funding_data)

def get_base_name(name):
    if '(' in name:
        return name.split('(')[0].strip()
    return name.strip()

base_name_groups = {}
for _, row in df_funding.iterrows():
    base = get_base_name(row['Project_Name'])
    if base not in base_name_groups:
        base_name_groups[base] = []
    base_name_groups[base].append(row)

full_text = ""
for doc in civic_docs:
    full_text += doc['text'] + NEWLINE

total_amount = 0
matched_details = []

for base_name, rows in base_name_groups.items():
    # Find all occurrences
    # escape base_name for regex
    pattern = re.escape(base_name)
    
    # We want to check all occurrences until we find a valid start date
    # matching the criteria.
    
    found_for_project = False
    
    for match in re.finditer(pattern, full_text):
        idx = match.start()
        # Context window 600 chars
        context = full_text[idx:idx+600]
        
        # Extract Start
        marker = 'Begin Construction:'
        st = None
        if marker in context:
            after = context.split(marker)[1]
            st = after.split(NEWLINE)[0].strip()
            
        if not st:
            continue
            
        # Check 2022
        if '2022' not in st:
            continue
            
        # Check Disaster
        is_disaster = False
        
        # 1. Suffix in DB
        for row in rows:
            rn = row['Project_Name'].lower()
            if 'fema' in rn or 'caloes' in rn or 'disaster' in rn:
                is_disaster = True
                break
        
        # 2. Keywords in Context (short window)
        if not is_disaster:
            c_lower = context.lower()
            if 'fema' in c_lower or 'caloes' in c_lower or 'disaster' in c_lower:
                is_disaster = True
                
        if is_disaster:
            # Match found!
            group_total = sum(r['Amount'] for r in rows)
            total_amount += group_total
            matched_details.append({'name': base_name, 'amount': group_total, 'start': st})
            found_for_project = True
            break
    
    if not found_for_project:
        # If we didn't find a valid start date in any occurrence, or strictly 2022 was missing
        pass

print('__RESULT__:')
print(json.dumps({'total_amount': total_amount, 'projects': matched_details}))"""

env_args = {'var_function-call-10835669272488718990': 'file_storage/function-call-10835669272488718990.json', 'var_function-call-10835669272488721645': 'file_storage/function-call-10835669272488721645.json', 'var_function-call-474033538740406040': {'status': 'loaded', 'docs_count': 5, 'funding_count': 500}, 'var_function-call-6347203935522351673': {'total_amount': 1184000, 'projects': [{'name': '2021 Annual Street Maintenance', 'amount': 24000, 'start': 'Spring 2022'}, {'name': 'Annual Street Maintenance', 'amount': 23000, 'start': 'Spring 2022'}, {'name': 'Broad Beach Road Water Quality Infrastructure Repairs', 'amount': 168000, 'start': 'Spring 2022'}, {'name': 'Civic Center Stormwater Diversion Structure', 'amount': 64000, 'start': 'Spring 2022'}, {'name': 'Encinal Canyon Road Drainage Improvements', 'amount': 146000, 'start': 'Fall 2022'}, {'name': 'Latigo Canyon Road Culvert Repairs', 'amount': 137000, 'start': 'April 2022'}, {'name': 'Latigo Canyon Road Roadway/Retaining Wall Improvements', 'amount': 188000, 'start': 'April 2022'}, {'name': 'Trancas Canyon Park Planting and Irrigation Repairs', 'amount': 214000, 'start': 'Spring 2022'}, {'name': 'Trancas Canyon Park Slope Stabilization Project', 'amount': 143000, 'start': 'Spring 2022'}, {'name': 'Westward Beach Road Shoulder Repairs', 'amount': 77000, 'start': 'Fall 2022'}]}, 'var_function-call-2203215841011505581': {'total_amount': 905000, 'projects': [{'name': 'Encinal Canyon Road Drainage Improvements', 'amount': 146000, 'start': 'Fall 2022', 'section': 'Unknown'}, {'name': 'Latigo Canyon Road Culvert Repairs', 'amount': 137000, 'start': 'April 2022', 'section': 'Unknown'}, {'name': 'Latigo Canyon Road Roadway/Retaining Wall Improvements', 'amount': 188000, 'start': 'April 2022', 'section': 'Capital'}, {'name': 'Trancas Canyon Park Planting and Irrigation Repairs', 'amount': 214000, 'start': 'Spring 2022', 'section': 'Unknown'}, {'name': 'Trancas Canyon Park Slope Stabilization Project', 'amount': 143000, 'start': 'Spring 2022', 'section': 'Unknown'}, {'name': 'Westward Beach Road Shoulder Repairs', 'amount': 77000, 'start': 'Fall 2022', 'section': 'Unknown'}]}, 'var_function-call-7890869682996152425': {'total_amount': 2085000, 'projects': [{'name': '2021 Annual Street Maintenance', 'amount': 24000, 'start': 'Spring 2022'}, {'name': 'Annual Street Maintenance', 'amount': 23000, 'start': 'Spring 2022'}, {'name': 'Birdview Avenue Improvements', 'amount': 178000, 'start': 'April 2022'}, {'name': 'Broad Beach Road Water Quality Infrastructure Repairs', 'amount': 168000, 'start': 'Spring 2022'}, {'name': 'City Traffic Signals Backup Power', 'amount': 85000, 'start': 'Spring 2022'}, {'name': 'Civic Center Stormwater Diversion Structure', 'amount': 64000, 'start': 'Spring 2022'}, {'name': 'Civic Center Way Improvements', 'amount': 37000, 'start': 'Spring 2022'}, {'name': 'Corral Canyon Culvert Repairs', 'amount': 112000, 'start': 'April 2022'}, {'name': 'Corral Canyon Road Bridge Repairs', 'amount': 151000, 'start': 'April 2022'}, {'name': 'Encinal Canyon Road Drainage Improvements', 'amount': 146000, 'start': 'Fall 2022'}, {'name': 'Guardrail Replacement Citywide', 'amount': 106000, 'start': 'April 2022'}, {'name': 'Kanan Dume Biofilter', 'amount': 56000, 'start': 'Spring 2022'}, {'name': 'Latigo Canyon Road Culvert Repairs', 'amount': 137000, 'start': 'April 2022'}, {'name': 'Latigo Canyon Road Roadway/Retaining Wall Improvements', 'amount': 188000, 'start': 'April 2022'}, {'name': 'Legacy Park Paver Repair Project', 'amount': 69000, 'start': 'Spring 2022'}, {'name': 'Malibu Park Drainage Improvements', 'amount': 17000, 'start': 'April 2022'}, {'name': 'Trancas Canyon Park Planting and Irrigation Repairs', 'amount': 214000, 'start': 'Spring 2022'}, {'name': 'Trancas Canyon Park Slope Stabilization Project', 'amount': 143000, 'start': 'Spring 2022'}, {'name': 'Trancas Playground Resurfacing', 'amount': 90000, 'start': 'Spring 2022'}, {'name': 'Westward Beach Road Shoulder Repairs', 'amount': 77000, 'start': 'Fall 2022'}]}, 'var_function-call-7833204953145916602': {'total_amount': 0, 'projects': []}, 'var_function-call-12480076851979765714': 'Public Works Commission\nAgenda Report\n\nPublic Works\nCommission Meeting\n03-22-23\nItem\n4.B.\n\nTo:\n\nChair Dittrich and Members of the Public Works Commission\n\nPrepared by:\n\nJorge Rubalcava, Senior Civil Engineer\n\nApproved by:\n\nRob DuBoux, Public Works Director/City Engineer\n\nDate prepared: March 15, 2023\n\nMeeting date: March 22, 2023\n\nSubject:\n\nCapital Improvement Projects and Disaster Recovery Projects Status\nReport\n\nRECOMMENDED ACTION: Receive and file report on the status of the City’s current and\nupcoming Capital Improvement Projects and Disaster Recovery Projects.\n\nDISCUSSION: Staff will provide a status update on the following active projects in the\nFiscal Year 2022-2023 Capital Improvement Program:\n\nCapital Improvement Projects (Design)\n\n2022 Morning View Resurfacing & Storm Drain Improvements\n\n(cid:190) Updates:\n\n(cid:131) Staff is working with the consultant to finalize the design plans for this\n\nproject and will submit to the County for review.\n\n(cid:190) Project Schedule:\n\n(cid:131) Complete Design: Summer 2023\n(cid:131) Advertise: Fall 2023\n(cid:131) Begin Construction: Fall 2023\n\nPCH Median Improvements Project\n\n(cid:190) Updates:\n\n(cid:131) On September 22, 2022, the City received four (4) construction bids\n\nand rejected all bids due to a budget shortfall\n\n(cid:131) City will work with the design consultant to review design alternatives\n\nor phasing out the project\n\n(cid:190) Project Schedule:\n\n(cid:131) Complete Design: Summer 2023\n(cid:131) Advertise: Fall 2023\n\nPage 1 of 6\n\nAgenda Item # 4.B.\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n(cid:131) Begin Construction: Fall 2023\n\nWestward Beach Road Repair Project\n\n(cid:190) Updates:\n\n(cid:131) City working with consultant on the design of the shoulder repairs\n\n(cid:190) Project Schedule:\n\n(cid:131) Complete Design: Summer 2023\n(cid:131) Advertise: Summer 2023\n(cid:131) Begin Construction: Fall 2023\n\nWestward Beach Road Drainage Improvements Project\n\n(cid:190) Updates:\n\n(cid:131) Plans are under review by Fish and Wildlife and City '}

exec(code, env_args)
