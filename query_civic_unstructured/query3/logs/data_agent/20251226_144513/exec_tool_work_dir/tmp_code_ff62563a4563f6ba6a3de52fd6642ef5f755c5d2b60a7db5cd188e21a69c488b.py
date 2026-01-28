code = """import json
with open(var_call_4APEv3JJcwInnd5pk3hawjPe) as f:
    docs = json.load(f)
funding_records = var_call_wHNjejSFyRL4Tx1OdwZhQFEp
# Extract relevant project names from documents that mention FEMA or emergency warning
project_list = []
doc_texts = [doc['text'] for doc in docs]
# Look for all mentioned projects with emergencies, FEMA, warning, etc., by scanning for likely project name headers and status info
import re
for doc in doc_texts:
    # Search for likely project names and status lines (naively)
    lines = doc.split('\n')
    for i,line in enumerate(lines):
        if ('FEMA' in line or 'emergency' in line or 'Warning' in line or 'sirens' in line or 'disaster' in line or 'Outdoor Warning' in line or 'Backup Power' in line or 'Drainage' in line or 'Latigo Canyon' in line or 'Clover Heights' in line or 'Trancas Canyon' in line or 'Storm Drain' in line or 'Earthquake' in line):
            line_clean = line.strip()
            # Look ahead for a status or type
            status = None
            type_ = None
            topic = None
            for offset in range(1,7):
                if i+offset<len(lines):
                    la = lines[i+offset].lower()
                    if 'status' in la:
                        status = re.sub(r'.*status:?','',la).strip()
                    if 'type' in la:
                        type_ = re.sub(r'.*type:?','',la).strip()
                    if 'topic' in la:
                        topic = re.sub(r'.*topic:?','',la).strip()
            project_list.append({'Project_Name':line_clean,'status':status,'type':type_,'topic':topic})
# Build a lookup for project status/type from unstructured results
proj_status_lookup = {proj['Project_Name']: proj for proj in project_list}
# Join funding record with project status/type
output = []
for fund in funding_records:
    pname = fund['Project_Name']
    match = None
    for key in proj_status_lookup.keys():
        if pname.lower() in key.lower() or key.lower() in pname.lower():
            match = proj_status_lookup[key]
            break
    record = {
        'Project_Name': pname,
        'Funding_Source': fund['Funding_Source'],
        'Amount': fund['Amount'],
        'Status': match['status'] if match else None,
        'Type': match['type'] if match else None,
        'Topic': match['topic'] if match else None
    }
    output.append(record)
result = output
print("__RESULT__:")
print(json.dumps(result))"""

env_args = {'var_call_4APEv3JJcwInnd5pk3hawjPe': 'file_storage/call_4APEv3JJcwInnd5pk3hawjPe.json', 'var_call_wHNjejSFyRL4Tx1OdwZhQFEp': [{'Funding_ID': '3', 'Project_Name': '2022 Morning View Resurfacing & Storm Drain Improvements', 'Funding_Source': 'State Development Grant', 'Amount': '38000'}, {'Funding_ID': '7', 'Project_Name': 'Birdview Avenue Improvements (FEMA/CalOES Project)', 'Funding_Source': 'Research Institution Funding', 'Amount': '14000'}, {'Funding_ID': '15', 'Project_Name': 'City Traffic Signals Backup Power', 'Funding_Source': 'Social Impact Investment', 'Amount': '85000'}, {'Funding_ID': '21', 'Project_Name': 'Clover Heights Storm Drain', 'Funding_Source': 'Infrastructure Bond', 'Amount': '53000'}, {'Funding_ID': '22', 'Project_Name': 'Clover Heights Storm Drain (FEMA Project)', 'Funding_Source': 'Local NGO Fund', 'Amount': '21000'}, {'Funding_ID': '23', 'Project_Name': 'Clover Heights Storm Drainage Improvements', 'Funding_Source': 'Development Bank Loan', 'Amount': '22000'}, {'Funding_ID': '25', 'Project_Name': 'Corral Canyon Culvert Repairs (FEMA Project)', 'Funding_Source': 'Municipal Fund', 'Amount': '43000'}, {'Funding_ID': '26', 'Project_Name': 'Corral Canyon Culvert Repairs (FEMA/CalOES Project)', 'Funding_Source': 'Taxpayer Contribution', 'Amount': '15000'}, {'Funding_ID': '28', 'Project_Name': 'Corral Canyon Road Bridge Repairs (FEMA Project)', 'Funding_Source': 'Local Business Support', 'Amount': '25000'}, {'Funding_ID': '29', 'Project_Name': 'Corral Canyon Road Bridge Repairs (FEMA/CalOES Project)', 'Funding_Source': 'Cultural Heritage Grant', 'Amount': '58000'}, {'Funding_ID': '32', 'Project_Name': 'Encinal Canyon 60-inch Storm Drain Repairs', 'Funding_Source': 'Municipal Fund', 'Amount': '56000'}, {'Funding_ID': '33', 'Project_Name': 'Encinal Canyon Road Drainage Improvements', 'Funding_Source': 'Non-profit Organization Grant', 'Amount': '34000'}, {'Funding_ID': '34', 'Project_Name': 'Encinal Canyon Road Drainage Improvements (CalOES Project)', 'Funding_Source': 'Educational Sponsorship', 'Amount': '18000'}, {'Funding_ID': '35', 'Project_Name': 'Encinal Canyon Road Drainage Improvements (FEMA/CalOES Project)', 'Funding_Source': 'Private Sponsor', 'Amount': '94000'}, {'Funding_ID': '38', 'Project_Name': 'Guardrail Replacement Citywide (FEMA Project)', 'Funding_Source': 'Impact Investment Fund', 'Amount': '22000'}, {'Funding_ID': '39', 'Project_Name': 'Guardrail Replacement Citywide (FEMA/CalOES Project)', 'Funding_Source': 'Development Bank Loan', 'Amount': '45000'}, {'Funding_ID': '42', 'Project_Name': 'Latigo Canyon Road Culvert Repairs', 'Funding_Source': 'Community Fund', 'Amount': '57000'}, {'Funding_ID': '43', 'Project_Name': 'Latigo Canyon Road Culvert Repairs (FEMA Project)', 'Funding_Source': 'Federal Assistance', 'Amount': '36000'}, {'Funding_ID': '44', 'Project_Name': 'Latigo Canyon Road Culvert Repairs (FEMA/CalOES Project)', 'Funding_Source': 'National Foundation Fund', 'Amount': '44000'}, {'Funding_ID': '45', 'Project_Name': 'Latigo Canyon Road Retaining Wall Repair Project', 'Funding_Source': 'Educational Sponsorship', 'Amount': '97000'}, {'Funding_ID': '46', 'Project_Name': 'Latigo Canyon Road Roadway/Retaining Wall Improvements', 'Funding_Source': 'Public-Private Partnership (PPP)', 'Amount': '19000'}, {'Funding_ID': '47', 'Project_Name': 'Latigo Canyon Road Roadway/Retaining Wall Improvements (FEMA Project)', 'Funding_Source': 'Municipal Fund', 'Amount': '91000'}, {'Funding_ID': '48', 'Project_Name': 'Latigo Canyon Road Roadway/Retaining Wall Improvements (FEMA/CalOES Project)', 'Funding_Source': 'Community Fund', 'Amount': '78000'}, {'Funding_ID': '55', 'Project_Name': 'Malibu Park Drainage Improvements', 'Funding_Source': 'Crowdfunding', 'Amount': '17000'}, {'Funding_ID': '57', 'Project_Name': 'Malibu Park Storm Drain Repairs', 'Funding_Source': 'Taxpayer Contribution', 'Amount': '50000'}, {'Funding_ID': '64', 'Project_Name': 'Outdoor Warning Signs', 'Funding_Source': 'Urban Renewal Fund', 'Amount': '92000'}, {'Funding_ID': '65', 'Project_Name': 'Outdoor Warning Sirens', 'Funding_Source': 'Social Impact Investment', 'Amount': '28000'}, {'Funding_ID': '66', 'Project_Name': 'Outdoor Warning Sirens (FEMA Project)', 'Funding_Source': 'Environmental Grant', 'Amount': '27000'}, {'Funding_ID': '67', 'Project_Name': 'Outdoor Warning Sirens (FEMA)', 'Funding_Source': 'State Development Grant', 'Amount': '81000'}, {'Funding_ID': '68', 'Project_Name': 'Outdoor Warning Sirens - Design (FEMA Project)', 'Funding_Source': 'Local Business Support', 'Amount': '43000'}, {'Funding_ID': '69', 'Project_Name': 'Outdoor Warningn Sirens - Design (FEMA Project)', 'Funding_Source': 'Technology Innovation Fund', 'Amount': '84000'}, {'Funding_ID': '73', 'Project_Name': 'PCH Overhead Warning Signs', 'Funding_Source': 'International Organization Grant', 'Amount': '73000'}, {'Funding_ID': '76', 'Project_Name': 'PCH at Trancas Canyon Road Right Turn Lane', 'Funding_Source': 'Corporate Sponsorship', 'Amount': '90000'}, {'Funding_ID': '81', 'Project_Name': 'Storm Drain Master Plan', 'Funding_Source': 'Social Impact Investment', 'Amount': '77000'}, {'Funding_ID': '82', 'Project_Name': 'Storm Drain Master Plan (FEMA Project)', 'Funding_Source': 'Environmental Grant', 'Amount': '80000'}, {'Funding_ID': '83', 'Project_Name': 'Storm Drain Trash Screens', 'Funding_Source': 'Impact Investment Fund', 'Amount': '11000'}, {'Funding_ID': '84', 'Project_Name': 'Storm Drain Trash Screens Phase Two', 'Funding_Source': 'National Foundation Fund', 'Amount': '24000'}, {'Funding_ID': '85', 'Project_Name': 'Trancas Canyon Park Planting and Irrigation Repairs', 'Funding_Source': 'National Foundation Fund', 'Amount': '78000'}, {'Funding_ID': '86', 'Project_Name': 'Trancas Canyon Park Planting and Irrigation Repairs (CalJPIA/FEMA Project)', 'Funding_Source': 'Infrastructure Bond', 'Amount': '44000'}, {'Funding_ID': '87', 'Project_Name': 'Trancas Canyon Park Planting and Irrigation Repairs (FEMA/CalOES Project)', 'Funding_Source': 'Infrastructure Bond', 'Amount': '92000'}, {'Funding_ID': '88', 'Project_Name': 'Trancas Canyon Park Playground', 'Funding_Source': 'Crowdfunding', 'Amount': '24000'}, {'Funding_ID': '89', 'Project_Name': 'Trancas Canyon Park Playground Resurfacing', 'Funding_Source': 'Philanthropic Donation', 'Amount': '65000'}, {'Funding_ID': '90', 'Project_Name': 'Trancas Canyon Park Slope Stabilization Project', 'Funding_Source': 'Community Fund', 'Amount': '68000'}, {'Funding_ID': '91', 'Project_Name': 'Trancas Canyon Park Slope Stabilization Project (CalJPIA Project)', 'Funding_Source': 'Government Grant', 'Amount': '43000'}, {'Funding_ID': '92', 'Project_Name': 'Trancas Canyon Park Slope Stabilization Project (CalOES Project)', 'Funding_Source': 'International Organization Grant', 'Amount': '32000'}, {'Funding_ID': '93', 'Project_Name': 'Trancas Canyon Park Upper and Lower Slopes Repair', 'Funding_Source': 'International Organization Grant', 'Amount': '23000'}, {'Funding_ID': '96', 'Project_Name': 'Westward Beach Road Drainage Improvements Project', 'Funding_Source': 'International Organization Grant', 'Amount': '87000'}]}

exec(code, env_args)
