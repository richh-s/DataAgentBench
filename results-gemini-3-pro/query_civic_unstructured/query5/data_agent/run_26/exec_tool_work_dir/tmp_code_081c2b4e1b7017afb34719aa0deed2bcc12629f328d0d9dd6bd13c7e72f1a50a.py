code = """import json
import re

with open(locals()['var_function-call-5605292304546820245'], 'r') as f:
    docs = json.load(f)
text = docs[0]['text']
norm_text = " ".join(text.split())

with open(locals()['var_function-call-3657045741871633664'], 'r') as f:
    funding_data = json.load(f)

# Group funding
project_groups = {}
for item in funding_data:
    raw_name = item['Project_Name']
    amount = int(item['Amount'])
    clean_name = re.sub(r'\s*\((FEMA|CalOES|CalJPIA).*?\)', '', raw_name, flags=re.IGNORECASE).strip()
    
    if clean_name not in project_groups:
        project_groups[clean_name] = {"total": 0, "is_disaster": False}
    
    project_groups[clean_name]["total"] += amount
    if re.search(r'\((FEMA|CalOES|CalJPIA)', raw_name, re.IGNORECASE):
        project_groups[clean_name]["is_disaster"] = True

total_funding = 0
found_projects = []

for name, data in project_groups.items():
    norm_name = " ".join(name.split())
    # Regex find all occurrences
    # escape name
    pattern = re.escape(norm_name)
    matches = [m.start() for m in re.finditer(pattern, norm_text)]
    
    is_valid_project = False
    
    for idx in matches:
        # Check context
        context = norm_text[idx:idx+1500]
        
        # Check if this occurrence is the "Main" entry (has Updates or Schedule)
        # Look for "Updates" or "Schedule" or "Description" nearby
        if "Updates" in context[:200] or "Project Schedule" in context[:500] or "Project Description" in context[:500]:
             # This is likely the main entry
             
             # Check Disaster
             local_is_disaster = data["is_disaster"]
             if not local_is_disaster:
                 if "FEMA" in context or "CalOES" in context or "CalJPIA" in context:
                     local_is_disaster = True
            
             # Check Date
             started_2022 = False
             if "2022" in name:
                 started_2022 = True
             
             if not started_2022:
                 if re.search(r"Construction was completed.*?2022", context, re.IGNORECASE):
                     started_2022 = True
                 elif re.search(r"Begin Construction.*?2022", context, re.IGNORECASE):
                     started_2022 = True
                 elif re.search(r"Advertise.*?2022", context, re.IGNORECASE):
                     started_2022 = True
                 elif re.search(r"awarded the contract.*?2022", context, re.IGNORECASE):
                     started_2022 = True
            
             if local_is_disaster and started_2022:
                 is_valid_project = True
                 break # Found valid entry
    
    if is_valid_project:
        total_funding += data["total"]
        found_projects.append({"name": name, "total": data["total"]})

print("__RESULT__:")
print(json.dumps({"projects": found_projects, "total": total_funding}))"""

env_args = {'var_function-call-5605292304546820245': 'file_storage/function-call-5605292304546820245.json', 'var_function-call-3657045741871633664': 'file_storage/function-call-3657045741871633664.json', 'var_function-call-3095873966328679813': {'projects': [], 'total': 0}, 'var_function-call-4623292609862033463': {'headers': [{'Capital Improvement Projects': 332}, {'Disaster Recovery Projects': 365}], 'found_count': 2, 'examples': ['2022 Morning View Resurfacing & Storm Drain Improvements', 'Bluffs Park Shade Structure']}, 'var_function-call-12935383195900810632': {'found_projects': [{'name': '2022 Morning View Resurfacing & Storm Drain Improvements', 'amount': 38000}, {'name': 'Bluffs Park Shade Structure', 'amount': 21000}, {'name': 'Broad Beach Road Water Quality Repair', 'amount': 93000}, {'name': 'Encinal Canyon Road Repairs', 'amount': 47000}, {'name': 'Malibu Canyon Road Traffic Study', 'amount': 97000}, {'name': 'Malibu Road Slope Repairs', 'amount': 44000}, {'name': 'Marie Canyon Green Streets', 'amount': 50000}, {'name': 'PCH Signal Synchronization System Improvements Project', 'amount': 16000}, {'name': 'Point Dume Walkway Repairs', 'amount': 59000}, {'name': 'Storm Drain Trash Screens', 'amount': 11000}, {'name': 'Storm Drain Trash Screens Phase Two', 'amount': 24000}], 'total': 500000}, 'var_function-call-5490281074798077253': [{'idx': 343, 'type': 'capital', 'text': 'Capital Improvement Projects and Disaster Recovery Projects Status'}, {'idx': 712, 'type': 'capital', 'text': 'Capital Improvement Projects (Design)'}, {'idx': 5624, 'type': 'capital', 'text': 'Capital Improvement Projects (Construction)'}, {'idx': 7116, 'type': 'capital', 'text': 'Capital Improvement Projects (Not Started)'}], 'var_function-call-3270848169410763630': {'found_projects': [], 'total': 0}, 'var_function-call-12913647900088782014': {'name': 'Latigo Canyon Road Retaining Wall Repair Project', 'found_idx': 2534, 'context_preview': 'Latigo Canyon Road Retaining Wall Repair Project (cid:190) Updates: (cid:131) Plans and specifications have been completed (cid:131) Awaiting final FEMA/CalOES approval for scope modification (cid:190', 'matches_disaster': True, 'matches_date': False}, 'var_function-call-6399400156716925980': {'projects': [{'name': 'Malibu Road Slope Repairs', 'total': 81000}], 'total_funding': 81000}, 'var_function-call-8165053220729173082': {'projects': [], 'total': 0}}

exec(code, env_args)
