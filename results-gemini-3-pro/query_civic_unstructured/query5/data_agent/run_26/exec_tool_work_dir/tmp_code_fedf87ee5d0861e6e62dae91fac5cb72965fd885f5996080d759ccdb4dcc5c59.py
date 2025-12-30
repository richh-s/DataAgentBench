code = """import json
import re

with open(locals()['var_function-call-5605292304546820245'], 'r') as f:
    docs = json.load(f)
text = docs[0]['text']
norm_text = " ".join(text.split())

with open(locals()['var_function-call-3657045741871633664'], 'r') as f:
    funding_data = json.load(f)

# Group funding by Clean Name
project_groups = {}

for item in funding_data:
    raw_name = item['Project_Name']
    amount = int(item['Amount'])
    
    # Clean name: remove (FEMA...), (CalOES...), (CalJPIA...)
    # pattern: space + ( + one of keywords + ... + )
    clean_name = re.sub(r'\s*\((FEMA|CalOES|CalJPIA).*?\)', '', raw_name, flags=re.IGNORECASE)
    clean_name = clean_name.strip()
    
    if clean_name not in project_groups:
        project_groups[clean_name] = {"total": 0, "is_disaster": False, "raw_names": []}
    
    project_groups[clean_name]["total"] += amount
    project_groups[clean_name]["raw_names"].append(raw_name)
    
    # Check if this record implies disaster
    if re.search(r'\((FEMA|CalOES|CalJPIA)', raw_name, re.IGNORECASE):
        project_groups[clean_name]["is_disaster"] = True

total_funding = 0
found_details = []

for name, data in project_groups.items():
    # Search name in text
    norm_name = " ".join(name.split())
    # Use simpler find
    idx = norm_text.find(norm_name)
    
    if idx != -1:
        context = norm_text[idx:idx+1500]
        
        # Check context for disaster
        if not data["is_disaster"]:
            if "FEMA" in context or "CalOES" in context or "CalJPIA" in context:
                data["is_disaster"] = True
            if "Disaster Recovery" in context:
                 # Check strictness
                 data["is_disaster"] = True

        # Check Start Date 2022
        started_2022 = False
        if "2022" in name:
            started_2022 = True
            
        if not started_2022:
             if re.search(r"Begin Construction[:\s]+[A-Za-z]+\s+2022", context, re.IGNORECASE):
                 started_2022 = True
             elif re.search(r"Advertise[:\s]+[A-Za-z]+\s+2022", context, re.IGNORECASE):
                 started_2022 = True
             elif re.search(r"Construction was completed[:\s,]+([A-Za-z]+\s+)?2022", context, re.IGNORECASE):
                 started_2022 = True
             elif re.search(r"awarded the contract.*2022", context, re.IGNORECASE):
                 started_2022 = True
        
        if data["is_disaster"] and started_2022:
            total_funding += data["total"]
            found_details.append({"name": name, "total": data["total"]})

print("__RESULT__:")
print(json.dumps({"projects": found_details, "total_funding": total_funding}))"""

env_args = {'var_function-call-5605292304546820245': 'file_storage/function-call-5605292304546820245.json', 'var_function-call-3657045741871633664': 'file_storage/function-call-3657045741871633664.json', 'var_function-call-3095873966328679813': {'projects': [], 'total': 0}, 'var_function-call-4623292609862033463': {'headers': [{'Capital Improvement Projects': 332}, {'Disaster Recovery Projects': 365}], 'found_count': 2, 'examples': ['2022 Morning View Resurfacing & Storm Drain Improvements', 'Bluffs Park Shade Structure']}, 'var_function-call-12935383195900810632': {'found_projects': [{'name': '2022 Morning View Resurfacing & Storm Drain Improvements', 'amount': 38000}, {'name': 'Bluffs Park Shade Structure', 'amount': 21000}, {'name': 'Broad Beach Road Water Quality Repair', 'amount': 93000}, {'name': 'Encinal Canyon Road Repairs', 'amount': 47000}, {'name': 'Malibu Canyon Road Traffic Study', 'amount': 97000}, {'name': 'Malibu Road Slope Repairs', 'amount': 44000}, {'name': 'Marie Canyon Green Streets', 'amount': 50000}, {'name': 'PCH Signal Synchronization System Improvements Project', 'amount': 16000}, {'name': 'Point Dume Walkway Repairs', 'amount': 59000}, {'name': 'Storm Drain Trash Screens', 'amount': 11000}, {'name': 'Storm Drain Trash Screens Phase Two', 'amount': 24000}], 'total': 500000}, 'var_function-call-5490281074798077253': [{'idx': 343, 'type': 'capital', 'text': 'Capital Improvement Projects and Disaster Recovery Projects Status'}, {'idx': 712, 'type': 'capital', 'text': 'Capital Improvement Projects (Design)'}, {'idx': 5624, 'type': 'capital', 'text': 'Capital Improvement Projects (Construction)'}, {'idx': 7116, 'type': 'capital', 'text': 'Capital Improvement Projects (Not Started)'}], 'var_function-call-3270848169410763630': {'found_projects': [], 'total': 0}, 'var_function-call-12913647900088782014': {'name': 'Latigo Canyon Road Retaining Wall Repair Project', 'found_idx': 2534, 'context_preview': 'Latigo Canyon Road Retaining Wall Repair Project (cid:190) Updates: (cid:131) Plans and specifications have been completed (cid:131) Awaiting final FEMA/CalOES approval for scope modification (cid:190', 'matches_disaster': True, 'matches_date': False}}

exec(code, env_args)
