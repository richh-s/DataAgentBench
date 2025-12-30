code = """import json
import re

k1 = 'var_function-call-4764481022315539258'
k2 = 'var_function-call-4764481022315538299'

with open(locals()[k1], 'r') as f:
    funding_data = json.load(f)
with open(locals()[k2], 'r') as f:
    civic_docs = json.load(f)

texts = [d.get('text', '') for d in civic_docs]
full_text = chr(10).join(texts)

def get_base_name(name):
    c = name
    for s in [" (FEMA Project)", " (CalOES Project)", " (FEMA/CalOES Project)", " (CalJPIA Project)"]:
        c = c.replace(s, "")
    return c.strip()

# Headers
h_design = "Capital Improvement Projects (Design)"
h_const = "Capital Improvement Projects (Construction)"
h_not = "Capital Improvement Projects (Not Started)"

indices = []
for h, s in [(h_design, "design"), (h_const, "construction"), (h_not, "not started")]:
    for m in re.finditer(re.escape(h), full_text, re.IGNORECASE):
        indices.append((m.start(), s))
indices.sort(key=lambda x: x[0])

results = []
for rec in funding_data:
    p_name = rec['Project_Name']
    base = get_base_name(p_name)
    
    rel_name = "emergency" in p_name.lower() or "fema" in p_name.lower()
    
    matches = list(re.finditer(re.escape(base), full_text, re.IGNORECASE))
    
    status = "not started"
    rel_context = False
    
    if matches:
        match = matches[0]
        start = match.start()
        end = match.end()
        
        # Header status
        curr = "not started"
        for i, s in indices:
            if i < start:
                curr = s
            else:
                break
        
        # Block
        b_end = end + 1500 # Slightly larger context
        for i, _ in indices:
            if end < i < b_end:
                b_end = i
                break
        
        block = full_text[end:b_end].lower()
        
        # Strict completion check
        if "construction was completed" in block or "project was completed" in block or "notice of completion" in block:
            curr = "completed"
            
        status = curr
        
        if "emergency" in block or "fema" in block:
            rel_context = True
    
    if rel_name or rel_context:
        results.append({
            "Project_Name": p_name,
            "Funding_Source": rec['Funding_Source'],
            "Amount": rec['Amount'],
            "Status": status
        })

print("__RESULT__:")
print(json.dumps(results))"""

env_args = {'var_function-call-2829182929966082996': ['civic_docs'], 'var_function-call-2829182929966082987': ['Funding'], 'var_function-call-8308376506612223274': 'file_storage/function-call-8308376506612223274.json', 'var_function-call-8308376506612220475': [{'Funding_ID': '1', 'Project_Name': '2021 Annual Street Maintenance', 'Funding_Source': 'Public-Private Partnership (PPP)', 'Amount': '24000'}, {'Funding_ID': '2', 'Project_Name': '2022 Annual Street Maintenance', 'Funding_Source': 'Government Grant', 'Amount': '45000'}, {'Funding_ID': '3', 'Project_Name': '2022 Morning View Resurfacing & Storm Drain Improvements', 'Funding_Source': 'State Development Grant', 'Amount': '38000'}, {'Funding_ID': '4', 'Project_Name': 'Annual Street Maintenance', 'Funding_Source': 'Corporate Sponsorship', 'Amount': '23000'}, {'Funding_ID': '5', 'Project_Name': 'Birdview Avenue Improvements', 'Funding_Source': 'National Foundation Fund', 'Amount': '79000'}], 'var_function-call-6271954007842849888': 'file_storage/function-call-6271954007842849888.json', 'var_function-call-6271954007842851063': [{'count(*)': '500'}], 'var_function-call-4764481022315539258': 'file_storage/function-call-4764481022315539258.json', 'var_function-call-4764481022315538299': 'file_storage/function-call-4764481022315538299.json', 'var_function-call-8814057602500483012': [{'Project_Name': '2021 Annual Street Maintenance', 'Funding_Source': 'Public-Private Partnership (PPP)', 'Amount': '24000', 'Status': 'not started'}, {'Project_Name': 'Annual Street Maintenance', 'Funding_Source': 'Corporate Sponsorship', 'Amount': '23000', 'Status': 'not started'}, {'Project_Name': 'Birdview Avenue Improvements', 'Funding_Source': 'National Foundation Fund', 'Amount': '79000', 'Status': 'completed'}, {'Project_Name': 'Birdview Avenue Improvements (CalOES Project)', 'Funding_Source': 'International Aid', 'Amount': '85000', 'Status': 'completed'}, {'Project_Name': 'Birdview Avenue Improvements (FEMA/CalOES Project)', 'Funding_Source': 'Research Institution Funding', 'Amount': '14000', 'Status': 'completed'}, {'Project_Name': 'Broad Beach Road Water Quality Infrastructure Repairs', 'Funding_Source': 'International Organization Grant', 'Amount': '87000', 'Status': 'not started'}, {'Project_Name': 'Broad Beach Road Water Quality Infrastructure Repairs (CalJPIA Project)', 'Funding_Source': 'Government Grant', 'Amount': '81000', 'Status': 'not started'}, {'Project_Name': 'Clover Heights Storm Drain', 'Funding_Source': 'Infrastructure Bond', 'Amount': '53000', 'Status': 'completed'}, {'Project_Name': 'Clover Heights Storm Drain (FEMA Project)', 'Funding_Source': 'Local NGO Fund', 'Amount': '21000', 'Status': 'completed'}, {'Project_Name': 'Clover Heights Storm Drainage Improvements', 'Funding_Source': 'Development Bank Loan', 'Amount': '22000', 'Status': 'completed'}, {'Project_Name': 'Corral Canyon Culvert Repairs', 'Funding_Source': 'Federal Assistance', 'Amount': '54000', 'Status': 'completed'}, {'Project_Name': 'Corral Canyon Culvert Repairs (FEMA Project)', 'Funding_Source': 'Municipal Fund', 'Amount': '43000', 'Status': 'completed'}, {'Project_Name': 'Corral Canyon Culvert Repairs (FEMA/CalOES Project)', 'Funding_Source': 'Taxpayer Contribution', 'Amount': '15000', 'Status': 'completed'}, {'Project_Name': 'Corral Canyon Road Bridge Repairs', 'Funding_Source': 'Technology Innovation Fund', 'Amount': '68000', 'Status': 'completed'}, {'Project_Name': 'Corral Canyon Road Bridge Repairs (FEMA Project)', 'Funding_Source': 'Local Business Support', 'Amount': '25000', 'Status': 'completed'}, {'Project_Name': 'Corral Canyon Road Bridge Repairs (FEMA/CalOES Project)', 'Funding_Source': 'Cultural Heritage Grant', 'Amount': '58000', 'Status': 'completed'}, {'Project_Name': 'Encinal Canyon Road Drainage Improvements (FEMA/CalOES Project)', 'Funding_Source': 'Private Sponsor', 'Amount': '94000', 'Status': 'completed'}, {'Project_Name': 'Guardrail Replacement Citywide', 'Funding_Source': 'International Aid', 'Amount': '39000', 'Status': 'not started'}, {'Project_Name': 'Guardrail Replacement Citywide (FEMA Project)', 'Funding_Source': 'Impact Investment Fund', 'Amount': '22000', 'Status': 'not started'}, {'Project_Name': 'Guardrail Replacement Citywide (FEMA/CalOES Project)', 'Funding_Source': 'Development Bank Loan', 'Amount': '45000', 'Status': 'not started'}, {'Project_Name': 'Latigo Canyon Road Culvert Repairs', 'Funding_Source': 'Community Fund', 'Amount': '57000', 'Status': 'not started'}, {'Project_Name': 'Latigo Canyon Road Culvert Repairs (FEMA Project)', 'Funding_Source': 'Federal Assistance', 'Amount': '36000', 'Status': 'not started'}, {'Project_Name': 'Latigo Canyon Road Culvert Repairs (FEMA/CalOES Project)', 'Funding_Source': 'National Foundation Fund', 'Amount': '44000', 'Status': 'not started'}, {'Project_Name': 'Latigo Canyon Road Retaining Wall Repair Project', 'Funding_Source': 'Educational Sponsorship', 'Amount': '97000', 'Status': 'completed'}, {'Project_Name': 'Latigo Canyon Road Roadway/Retaining Wall Improvements', 'Funding_Source': 'Public-Private Partnership (PPP)', 'Amount': '19000', 'Status': 'not started'}, {'Project_Name': 'Latigo Canyon Road Roadway/Retaining Wall Improvements (FEMA Project)', 'Funding_Source': 'Municipal Fund', 'Amount': '91000', 'Status': 'not started'}, {'Project_Name': 'Latigo Canyon Road Roadway/Retaining Wall Improvements (FEMA/CalOES Project)', 'Funding_Source': 'Community Fund', 'Amount': '78000', 'Status': 'not started'}, {'Project_Name': 'Malibu Park Drainage Improvements', 'Funding_Source': 'Crowdfunding', 'Amount': '17000', 'Status': 'completed'}, {'Project_Name': 'Outdoor Warning Sirens (FEMA Project)', 'Funding_Source': 'Environmental Grant', 'Amount': '27000', 'Status': 'completed'}, {'Project_Name': 'Outdoor Warning Sirens (FEMA)', 'Funding_Source': 'State Development Grant', 'Amount': '81000', 'Status': 'not started'}, {'Project_Name': 'Outdoor Warning Sirens - Design (FEMA Project)', 'Funding_Source': 'Local Business Support', 'Amount': '43000', 'Status': 'not started'}, {'Project_Name': 'Outdoor Warningn Sirens - Design (FEMA Project)', 'Funding_Source': 'Technology Innovation Fund', 'Amount': '84000', 'Status': 'not started'}, {'Project_Name': 'Storm Drain Master Plan (FEMA Project)', 'Funding_Source': 'Environmental Grant', 'Amount': '80000', 'Status': 'completed'}, {'Project_Name': 'Trancas Canyon Park Planting and Irrigation Repairs', 'Funding_Source': 'National Foundation Fund', 'Amount': '78000', 'Status': 'not started'}, {'Project_Name': 'Trancas Canyon Park Planting and Irrigation Repairs (CalJPIA/FEMA Project)', 'Funding_Source': 'Infrastructure Bond', 'Amount': '44000', 'Status': 'not started'}, {'Project_Name': 'Trancas Canyon Park Planting and Irrigation Repairs (FEMA/CalOES Project)', 'Funding_Source': 'Infrastructure Bond', 'Amount': '92000', 'Status': 'not started'}, {'Project_Name': 'Trancas Canyon Park Slope Stabilization Project', 'Funding_Source': 'Community Fund', 'Amount': '68000', 'Status': 'not started'}, {'Project_Name': 'Trancas Canyon Park Slope Stabilization Project (CalJPIA Project)', 'Funding_Source': 'Government Grant', 'Amount': '43000', 'Status': 'not started'}, {'Project_Name': 'Trancas Canyon Park Slope Stabilization Project (CalOES Project)', 'Funding_Source': 'International Organization Grant', 'Amount': '32000', 'Status': 'not started'}, {'Project_Name': 'Westward Beach Road Drainage Improvements Project', 'Funding_Source': 'International Organization Grant', 'Amount': '87000', 'Status': 'completed'}, {'Project_Name': 'Westward Beach Road Shoulder Repairs (CalOES Project)', 'Funding_Source': 'Local Business Support', 'Amount': '77000', 'Status': 'not started'}]}

exec(code, env_args)
