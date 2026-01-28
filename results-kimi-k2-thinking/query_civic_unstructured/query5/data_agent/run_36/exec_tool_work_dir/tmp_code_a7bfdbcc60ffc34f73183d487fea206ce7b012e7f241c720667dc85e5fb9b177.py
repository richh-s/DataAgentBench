code = """import json

# Load data
f = open(locals()['var_functions.query_db:6'])
funding = json.load(f)
f.close()

c = open(locals()['var_functions.query_db:30'])
docs = json.load(c)
c.close()

# Build funding lookup
d = {}
for item in funding:
    d[item['Project_Name']] = int(item['Amount'])

# Find projects
projects = []
total = 0

for doc in docs:
    text = doc.get('text', '')
    lines = text.split('\n')
    
    for line in lines:
        line = line.strip()
        if len(line) < 5:
            continue
        
        # Skip common lines
        if 'Page' in line or 'Agenda' in line or 'Prepared' in line or 'Date' in line:
            continue
        
        if '2022' in line and not line.startswith('(') and not line.startswith('•'):
            low = line.lower()
            if 'fema' in low or 'caloes' in low or 'caljpia' in low or 'fire' in low:
                amt = 0
                if line in d:
                    amt = d[line]
                else:
                    base = line.split('(FEMA')[0].strip()
                    if base in d:
                        amt = d[base]
                
                if amt > 0:
                    projects.append({'name': line, 'amount': amt})
                    total += amt

print('__RESULT__:')
print(json.dumps({'count': len(projects), 'total': total, 'projects': projects}))"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:6': 'file_storage/functions.query_db:6.json', 'var_functions.execute_python:10': {'total_records': 500, 'sample_records': [{'Funding_ID': '1', 'Project_Name': '2021 Annual Street Maintenance', 'Funding_Source': 'Public-Private Partnership (PPP)', 'Amount': '24000'}, {'Funding_ID': '2', 'Project_Name': '2022 Annual Street Maintenance', 'Funding_Source': 'Government Grant', 'Amount': '45000'}, {'Funding_ID': '3', 'Project_Name': '2022 Morning View Resurfacing & Storm Drain Improvements', 'Funding_Source': 'State Development Grant', 'Amount': '38000'}]}, 'var_functions.execute_python:12': {'civic_docs_count': 5, 'first_doc_preview': 'Public Works Commission\nAgenda Report\n\nPublic Works\nCommission Meeting\n03-22-23\nItem\n4.B.\n\nTo:\n\nChair Dittrich and Members of the Public Works Commission\n\nPrepared by:\n\nJorge Rubalcava, Senior Civil Engineer\n\nApproved by:\n\nRob DuBoux, Public Works Director/City Engineer\n\nDate prepared: March 15, 2023\n\nMeeting date: March 22, 2023\n\nSubject:\n\nCapital Improvement Projects and Disaster Recovery Projects Status\nReport\n\nRECOMMENDED ACTION: Receive and file report on the status of the City’s current an'}, 'var_functions.execute_python:22': {'total_funding_records': 500, 'total_funding_amount': 28094000, 'disaster_projects_count': 27, 'disaster_projects': [['Birdview Avenue Improvements (CalOES Project)', 85000], ['Birdview Avenue Improvements (FEMA/CalOES Project)', 14000], ['Broad Beach Road Water Quality Infrastructure Repairs (CalJPIA Project)', 81000], ['Clover Heights Storm Drain (FEMA Project)', 21000], ['Corral Canyon Culvert Repairs (FEMA Project)', 43000], ['Corral Canyon Culvert Repairs (FEMA/CalOES Project)', 15000], ['Corral Canyon Road Bridge Repairs (FEMA Project)', 25000], ['Corral Canyon Road Bridge Repairs (FEMA/CalOES Project)', 58000], ['Encinal Canyon Road Drainage Improvements (CalOES Project)', 18000], ['Encinal Canyon Road Drainage Improvements (FEMA/CalOES Project)', 94000], ['Guardrail Replacement Citywide (FEMA Project)', 22000], ['Guardrail Replacement Citywide (FEMA/CalOES Project)', 45000], ['Latigo Canyon Road Culvert Repairs (FEMA Project)', 36000], ['Latigo Canyon Road Culvert Repairs (FEMA/CalOES Project)', 44000], ['Latigo Canyon Road Roadway/Retaining Wall Improvements (FEMA Project)', 91000], ['Latigo Canyon Road Roadway/Retaining Wall Improvements (FEMA/CalOES Project)', 78000], ['Malibu Road Slope Repairs (CalOES Project)', 37000], ['Outdoor Warning Sirens (FEMA Project)', 27000], ['Outdoor Warning Sirens (FEMA)', 81000], ['Outdoor Warning Sirens - Design (FEMA Project)', 43000]]}, 'var_functions.query_db:30': 'file_storage/functions.query_db:30.json'}

exec(code, env_args)
