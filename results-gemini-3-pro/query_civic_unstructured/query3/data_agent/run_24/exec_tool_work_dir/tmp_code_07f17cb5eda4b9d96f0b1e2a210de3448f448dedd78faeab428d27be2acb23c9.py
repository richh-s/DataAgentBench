code = """import json
import re
from datetime import datetime

with open(locals()['var_function-call-2028314322626917702'], 'r') as f:
    funding_data = json.load(f)

with open(locals()['var_function-call-10132172204667131329'], 'r') as f:
    civic_docs = json.load(f)

# Sort docs by date descending
def get_date(filename):
    match = re.search(r'(\d{8})', filename)
    if match:
        return datetime.strptime(match.group(1), '%m%d%Y')
    return datetime.min

civic_docs.sort(key=lambda x: get_date(x['filename']), reverse=True)

extracted = []
seen_projects = set()

for doc in civic_docs:
    lines = doc['text'].splitlines()
    current_status = None
    
    i = 0
    while i < len(lines):
        line = lines[i].strip()
        if not line:
            i += 1
            continue
            
        if "Capital Improvement Projects" in line or "Disaster Recovery Projects" in line:
            if "Design" in line:
                current_status = "design"
            elif "Construction" in line:
                current_status = "construction"
            elif "Not Started" in line:
                current_status = "not started"
            elif "Completed" in line:
                current_status = "completed"
            i += 1
            continue
        
        is_project = False
        j = i + 1
        while j < len(lines) and not lines[j].strip():
            j += 1
        
        if j < len(lines):
            next_start = lines[j].strip()
            if next_start.startswith("Updates:") or next_start.startswith("Project Description:") or next_start.startswith("(cid:"):
                is_project = True
        
        if is_project and current_status:
            p_name = line
            
            # Check if we already have this project (from a newer doc)
            # Use normalized name
            p_name_norm = p_name.lower().strip()
            if p_name_norm in seen_projects:
                # Skip extracting block, just move index
                # But we need to find where this project block ends to update i correctly.
                # So we must parse the block bounds anyway.
                pass
            
            block_lines = []
            k = j
            while k < len(lines):
                l = lines[k].strip()
                if ("Capital Improvement Projects" in l or "Disaster Recovery Projects" in l) and ("(" in l and ")" in l):
                    break
                
                is_new_proj = False
                if l and not l.startswith("Updates:") and not l.startswith("Project Description:") and not l.startswith("(cid:"):
                    m = k + 1
                    while m < len(lines) and not lines[m].strip():
                        m += 1
                    if m < len(lines):
                        ns = lines[m].strip()
                        if ns.startswith("Updates:") or ns.startswith("Project Description:") or ns.startswith("(cid:"):
                            is_new_proj = True
                
                if is_new_proj:
                    break
                
                block_lines.append(l)
                k += 1
            
            block_text = " ".join(block_lines)
            
            if p_name_norm not in seen_projects:
                status = current_status
                if status == "construction":
                    if "completed" in block_text.lower() and ("construction was completed" in block_text.lower() or "notice of completion" in block_text.lower()):
                        status = "completed"
                
                extracted.append({
                    "name": p_name,
                    "text": block_text,
                    "status": status
                })
                seen_projects.add(p_name_norm)
            
            i = k
            continue
            
        i += 1

final_results = []
seen_funding_keys = set()

for p in extracted:
    content = (p['name'] + " " + p['text']).lower()
    if "emergency" in content or "fema" in content:
        p_name_norm = p['name'].lower().replace("(fema project)", "").replace("project", "").strip()
        
        for f in funding_data:
            f_name = f['Project_Name']
            f_name_norm = f_name.lower().replace("(fema project)", "").replace("(caloes project)", "").replace("(fema/caloes project)", "").replace("(fema)", "").replace("project", "").strip()
            
            match = False
            if p_name_norm == f_name_norm:
                match = True
            elif (p_name_norm in f_name_norm and len(p_name_norm) > 10) or (f_name_norm in p_name_norm and len(f_name_norm) > 10):
                match = True
            
            if match:
                item = {
                    "Project_Name": f['Project_Name'],
                    "Funding_Source": f['Funding_Source'],
                    "Amount": f['Amount'],
                    "Status": p['status']
                }
                key = (item['Project_Name'], item['Funding_Source'], str(item['Amount']), item['Status'])
                if key not in seen_funding_keys:
                    seen_funding_keys.add(key)
                    final_results.append(item)

print("__RESULT__:")
print(json.dumps(final_results))"""

env_args = {'var_function-call-2105256659697284702': ['civic_docs'], 'var_function-call-2105256659697283933': ['Funding'], 'var_function-call-2028314322626917702': 'file_storage/function-call-2028314322626917702.json', 'var_function-call-2028314322626917971': 'file_storage/function-call-2028314322626917971.json', 'var_function-call-4575957102787257553': [{'_id': '694eef5c4ec675b6b5f5a285', 'filename': 'malibucity_agenda_03222023-2060.txt'}, {'_id': '694eef5c4ec675b6b5f5a286', 'filename': 'malibucity_agenda__01262022-1835.txt'}, {'_id': '694eef5c4ec675b6b5f5a287', 'filename': 'malibucity_agenda__01272021-1626.txt'}, {'_id': '694eef5c4ec675b6b5f5a288', 'filename': 'malibucity_agenda__03022021-1648.txt'}, {'_id': '694eef5c4ec675b6b5f5a289', 'filename': 'malibucity_agenda__03232022-1869.txt'}], 'var_function-call-10132172204667131329': 'file_storage/function-call-10132172204667131329.json', 'var_function-call-1555749136325638796': [{'Project_Name': 'Latigo Canyon Road Retaining Wall Repair Project', 'Funding_Source': 'Educational Sponsorship', 'Amount': '97000', 'Status': 'design'}, {'Project_Name': 'Latigo Canyon Road Roadway/Retaining Wall Improvements', 'Funding_Source': 'Public-Private Partnership (PPP)', 'Amount': '19000', 'Status': 'completed'}, {'Project_Name': 'Latigo Canyon Road Roadway/Retaining Wall Improvements (FEMA Project)', 'Funding_Source': 'Municipal Fund', 'Amount': '91000', 'Status': 'completed'}, {'Project_Name': 'Latigo Canyon Road Roadway/Retaining Wall Improvements (FEMA/CalOES Project)', 'Funding_Source': 'Community Fund', 'Amount': '78000', 'Status': 'completed'}, {'Project_Name': 'Trancas Canyon Park Planting and Irrigation Repairs', 'Funding_Source': 'National Foundation Fund', 'Amount': '78000', 'Status': 'completed'}, {'Project_Name': 'Trancas Canyon Park Planting and Irrigation Repairs (CalJPIA/FEMA Project)', 'Funding_Source': 'Infrastructure Bond', 'Amount': '44000', 'Status': 'completed'}, {'Project_Name': 'Trancas Canyon Park Planting and Irrigation Repairs (FEMA/CalOES Project)', 'Funding_Source': 'Infrastructure Bond', 'Amount': '92000', 'Status': 'completed'}, {'Project_Name': 'Trancas Canyon Park Slope Stabilization Project', 'Funding_Source': 'Community Fund', 'Amount': '68000', 'Status': 'completed'}, {'Project_Name': 'Trancas Canyon Park Slope Stabilization Project (CalJPIA Project)', 'Funding_Source': 'Government Grant', 'Amount': '43000', 'Status': 'completed'}, {'Project_Name': 'Trancas Canyon Park Slope Stabilization Project (CalOES Project)', 'Funding_Source': 'International Organization Grant', 'Amount': '32000', 'Status': 'completed'}, {'Project_Name': 'Guardrail Replacement Citywide', 'Funding_Source': 'International Aid', 'Amount': '39000', 'Status': 'completed'}, {'Project_Name': 'Guardrail Replacement Citywide (FEMA Project)', 'Funding_Source': 'Impact Investment Fund', 'Amount': '22000', 'Status': 'completed'}, {'Project_Name': 'Guardrail Replacement Citywide (FEMA/CalOES Project)', 'Funding_Source': 'Development Bank Loan', 'Amount': '45000', 'Status': 'completed'}, {'Project_Name': 'Corral Canyon Road Bridge Repairs', 'Funding_Source': 'Technology Innovation Fund', 'Amount': '68000', 'Status': 'completed'}, {'Project_Name': 'Corral Canyon Road Bridge Repairs (FEMA Project)', 'Funding_Source': 'Local Business Support', 'Amount': '25000', 'Status': 'completed'}, {'Project_Name': 'Corral Canyon Road Bridge Repairs (FEMA/CalOES Project)', 'Funding_Source': 'Cultural Heritage Grant', 'Amount': '58000', 'Status': 'completed'}, {'Project_Name': 'Corral Canyon Culvert Repairs', 'Funding_Source': 'Federal Assistance', 'Amount': '54000', 'Status': 'completed'}, {'Project_Name': 'Corral Canyon Culvert Repairs (FEMA Project)', 'Funding_Source': 'Municipal Fund', 'Amount': '43000', 'Status': 'completed'}, {'Project_Name': 'Corral Canyon Culvert Repairs (FEMA/CalOES Project)', 'Funding_Source': 'Taxpayer Contribution', 'Amount': '15000', 'Status': 'completed'}, {'Project_Name': 'Clover Heights Storm Drain', 'Funding_Source': 'Infrastructure Bond', 'Amount': '53000', 'Status': 'completed'}, {'Project_Name': 'Clover Heights Storm Drain (FEMA Project)', 'Funding_Source': 'Local NGO Fund', 'Amount': '21000', 'Status': 'completed'}, {'Project_Name': 'Clover Heights Storm Drainage Improvements', 'Funding_Source': 'Development Bank Loan', 'Amount': '22000', 'Status': 'completed'}, {'Project_Name': 'Latigo Canyon Road Culvert Repairs', 'Funding_Source': 'Community Fund', 'Amount': '57000', 'Status': 'completed'}, {'Project_Name': 'Latigo Canyon Road Culvert Repairs (FEMA Project)', 'Funding_Source': 'Federal Assistance', 'Amount': '36000', 'Status': 'completed'}, {'Project_Name': 'Latigo Canyon Road Culvert Repairs (FEMA/CalOES Project)', 'Funding_Source': 'National Foundation Fund', 'Amount': '44000', 'Status': 'completed'}, {'Project_Name': 'Outdoor Warningn Sirens - Design (FEMA Project)', 'Funding_Source': 'Technology Innovation Fund', 'Amount': '84000', 'Status': 'completed'}, {'Project_Name': 'Broad Beach Road Water Quality Infrastructure Repairs', 'Funding_Source': 'International Organization Grant', 'Amount': '87000', 'Status': 'not started'}, {'Project_Name': 'Broad Beach Road Water Quality Infrastructure Repairs (CalJPIA Project)', 'Funding_Source': 'Government Grant', 'Amount': '81000', 'Status': 'not started'}, {'Project_Name': 'Trancas Canyon Park Planting and Irrigation Repairs', 'Funding_Source': 'National Foundation Fund', 'Amount': '78000', 'Status': 'not started'}, {'Project_Name': 'Trancas Canyon Park Planting and Irrigation Repairs (FEMA/CalOES Project)', 'Funding_Source': 'Infrastructure Bond', 'Amount': '92000', 'Status': 'not started'}, {'Project_Name': 'Birdview Avenue Improvements', 'Funding_Source': 'National Foundation Fund', 'Amount': '79000', 'Status': 'not started'}, {'Project_Name': 'Birdview Avenue Improvements (CalOES Project)', 'Funding_Source': 'International Aid', 'Amount': '85000', 'Status': 'not started'}, {'Project_Name': 'Birdview Avenue Improvements (FEMA/CalOES Project)', 'Funding_Source': 'Research Institution Funding', 'Amount': '14000', 'Status': 'not started'}, {'Project_Name': 'Guardrail Replacement Citywide', 'Funding_Source': 'International Aid', 'Amount': '39000', 'Status': 'not started'}, {'Project_Name': 'Guardrail Replacement Citywide (FEMA Project)', 'Funding_Source': 'Impact Investment Fund', 'Amount': '22000', 'Status': 'not started'}, {'Project_Name': 'Guardrail Replacement Citywide (FEMA/CalOES Project)', 'Funding_Source': 'Development Bank Loan', 'Amount': '45000', 'Status': 'not started'}, {'Project_Name': 'Corral Canyon Road Bridge Repairs', 'Funding_Source': 'Technology Innovation Fund', 'Amount': '68000', 'Status': 'not started'}, {'Project_Name': 'Corral Canyon Road Bridge Repairs (FEMA Project)', 'Funding_Source': 'Local Business Support', 'Amount': '25000', 'Status': 'not started'}, {'Project_Name': 'Corral Canyon Road Bridge Repairs (FEMA/CalOES Project)', 'Funding_Source': 'Cultural Heritage Grant', 'Amount': '58000', 'Status': 'not started'}, {'Project_Name': 'Corral Canyon Culvert Repairs', 'Funding_Source': 'Federal Assistance', 'Amount': '54000', 'Status': 'not started'}, {'Project_Name': 'Corral Canyon Culvert Repairs (FEMA Project)', 'Funding_Source': 'Municipal Fund', 'Amount': '43000', 'Status': 'not started'}, {'Project_Name': 'Corral Canyon Culvert Repairs (FEMA/CalOES Project)', 'Funding_Source': 'Taxpayer Contribution', 'Amount': '15000', 'Status': 'not started'}, {'Project_Name': 'Clover Heights Storm Drain', 'Funding_Source': 'Infrastructure Bond', 'Amount': '53000', 'Status': 'not started'}, {'Project_Name': 'Clover Heights Storm Drain (FEMA Project)', 'Funding_Source': 'Local NGO Fund', 'Amount': '21000', 'Status': 'not started'}, {'Project_Name': 'Clover Heights Storm Drainage Improvements', 'Funding_Source': 'Development Bank Loan', 'Amount': '22000', 'Status': 'not started'}, {'Project_Name': 'Latigo Canyon Road Culvert Repairs', 'Funding_Source': 'Community Fund', 'Amount': '57000', 'Status': 'not started'}, {'Project_Name': 'Latigo Canyon Road Culvert Repairs (FEMA Project)', 'Funding_Source': 'Federal Assistance', 'Amount': '36000', 'Status': 'not started'}, {'Project_Name': 'Latigo Canyon Road Culvert Repairs (FEMA/CalOES Project)', 'Funding_Source': 'National Foundation Fund', 'Amount': '44000', 'Status': 'not started'}, {'Project_Name': 'Encinal Canyon Road Drainage Improvements', 'Funding_Source': 'Non-profit Organization Grant', 'Amount': '34000', 'Status': 'not started'}, {'Project_Name': 'Encinal Canyon Road Drainage Improvements (CalOES Project)', 'Funding_Source': 'Educational Sponsorship', 'Amount': '18000', 'Status': 'not started'}, {'Project_Name': 'Encinal Canyon Road Drainage Improvements (FEMA/CalOES Project)', 'Funding_Source': 'Private Sponsor', 'Amount': '94000', 'Status': 'not started'}, {'Project_Name': 'Outdoor Warning Sirens', 'Funding_Source': 'Social Impact Investment', 'Amount': '28000', 'Status': 'not started'}, {'Project_Name': 'Outdoor Warning Sirens (FEMA Project)', 'Funding_Source': 'Environmental Grant', 'Amount': '27000', 'Status': 'not started'}, {'Project_Name': 'Outdoor Warning Sirens (FEMA)', 'Funding_Source': 'State Development Grant', 'Amount': '81000', 'Status': 'not started'}, {'Project_Name': 'Latigo Canyon Road Roadway/Retaining Wall Improvements', 'Funding_Source': 'Public-Private Partnership (PPP)', 'Amount': '19000', 'Status': 'not started'}, {'Project_Name': 'Latigo Canyon Road Roadway/Retaining Wall Improvements (FEMA Project)', 'Funding_Source': 'Municipal Fund', 'Amount': '91000', 'Status': 'not started'}, {'Project_Name': 'Latigo Canyon Road Roadway/Retaining Wall Improvements (FEMA/CalOES Project)', 'Funding_Source': 'Community Fund', 'Amount': '78000', 'Status': 'not started'}, {'Project_Name': 'Outdoor Warning Sirens - Design (FEMA Project)', 'Funding_Source': 'Local Business Support', 'Amount': '43000', 'Status': 'not started'}, {'Project_Name': 'Storm Drain Master Plan', 'Funding_Source': 'Social Impact Investment', 'Amount': '77000', 'Status': 'not started'}, {'Project_Name': 'Storm Drain Master Plan (FEMA Project)', 'Funding_Source': 'Environmental Grant', 'Amount': '80000', 'Status': 'not started'}, {'Project_Name': 'Storm Drain Master Plan', 'Funding_Source': 'Social Impact Investment', 'Amount': '77000', 'Status': 'completed'}, {'Project_Name': 'Storm Drain Master Plan (FEMA Project)', 'Funding_Source': 'Environmental Grant', 'Amount': '80000', 'Status': 'completed'}]}

exec(code, env_args)
