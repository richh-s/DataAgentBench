code = """import json
import re

with open(locals()['var_function-call-5605292304546820245'], 'r') as f:
    docs = json.load(f)
text = docs[0]['text']
norm_text = " ".join(text.split())

with open(locals()['var_function-call-3657045741871633664'], 'r') as f:
    funding_data = json.load(f)

project_groups = {}
for item in funding_data:
    raw_name = item['Project_Name']
    amount = int(item['Amount'])
    clean_name = re.sub(r'\s*\((FEMA|CalOES|CalJPIA).*?\)', '', raw_name, flags=re.IGNORECASE).strip()
    
    if clean_name not in project_groups:
        project_groups[clean_name] = {"total": 0, "is_disaster": False, "raw_names": []}
    
    project_groups[clean_name]["total"] += amount
    project_groups[clean_name]["raw_names"].append(raw_name)
    if re.search(r'\((FEMA|CalOES|CalJPIA)', raw_name, re.IGNORECASE):
        project_groups[clean_name]["is_disaster"] = True

# Debug Broad Beach
target = "Broad Beach Road Water Quality Repair"
data = project_groups.get(target)
print("__RESULT__:")
if data:
    norm_name = " ".join(target.split())
    matches = [m.start() for m in re.finditer(re.escape(norm_name), norm_text)]
    context = norm_text[matches[0]:matches[0]+500]
    
    # Check date regex
    started = False
    if re.search(r"Construction was completed.*?2022", context, re.IGNORECASE):
        started = True
        
    print(json.dumps({
        "name": target,
        "data": data, # check is_disaster
        "started": started,
        "context": context[:100]
    }))
else:
    print(json.dumps({"error": "Target not found in groups", "keys": list(project_groups.keys())[:5]}))"""

env_args = {'var_function-call-5605292304546820245': 'file_storage/function-call-5605292304546820245.json', 'var_function-call-3657045741871633664': 'file_storage/function-call-3657045741871633664.json', 'var_function-call-3095873966328679813': {'projects': [], 'total': 0}, 'var_function-call-4623292609862033463': {'headers': [{'Capital Improvement Projects': 332}, {'Disaster Recovery Projects': 365}], 'found_count': 2, 'examples': ['2022 Morning View Resurfacing & Storm Drain Improvements', 'Bluffs Park Shade Structure']}, 'var_function-call-12935383195900810632': {'found_projects': [{'name': '2022 Morning View Resurfacing & Storm Drain Improvements', 'amount': 38000}, {'name': 'Bluffs Park Shade Structure', 'amount': 21000}, {'name': 'Broad Beach Road Water Quality Repair', 'amount': 93000}, {'name': 'Encinal Canyon Road Repairs', 'amount': 47000}, {'name': 'Malibu Canyon Road Traffic Study', 'amount': 97000}, {'name': 'Malibu Road Slope Repairs', 'amount': 44000}, {'name': 'Marie Canyon Green Streets', 'amount': 50000}, {'name': 'PCH Signal Synchronization System Improvements Project', 'amount': 16000}, {'name': 'Point Dume Walkway Repairs', 'amount': 59000}, {'name': 'Storm Drain Trash Screens', 'amount': 11000}, {'name': 'Storm Drain Trash Screens Phase Two', 'amount': 24000}], 'total': 500000}, 'var_function-call-5490281074798077253': [{'idx': 343, 'type': 'capital', 'text': 'Capital Improvement Projects and Disaster Recovery Projects Status'}, {'idx': 712, 'type': 'capital', 'text': 'Capital Improvement Projects (Design)'}, {'idx': 5624, 'type': 'capital', 'text': 'Capital Improvement Projects (Construction)'}, {'idx': 7116, 'type': 'capital', 'text': 'Capital Improvement Projects (Not Started)'}], 'var_function-call-3270848169410763630': {'found_projects': [], 'total': 0}, 'var_function-call-12913647900088782014': {'name': 'Latigo Canyon Road Retaining Wall Repair Project', 'found_idx': 2534, 'context_preview': 'Latigo Canyon Road Retaining Wall Repair Project (cid:190) Updates: (cid:131) Plans and specifications have been completed (cid:131) Awaiting final FEMA/CalOES approval for scope modification (cid:190', 'matches_disaster': True, 'matches_date': False}, 'var_function-call-6399400156716925980': {'projects': [{'name': 'Malibu Road Slope Repairs', 'total': 81000}], 'total_funding': 81000}, 'var_function-call-8165053220729173082': {'projects': [], 'total': 0}, 'var_function-call-9838480401155406048': {'projects': [{'name': 'Malibu Road Slope Repairs', 'total': 81000}], 'total': 81000}, 'var_function-call-1945164751821335729': {'matches': [6632], 'context': 'Broad Beach Road Water Quality Repair (cid:190) Updates: (cid:131) Construction was completed, November 2022 (cid:131) Notice of completion filed January 2023 Point Dume Walkway Repairs (cid:190) Updates: (cid:131) Construction was completed, November 2022 (cid:131) Notice of completion filed January 2023 Capital Improvement Projects (Not Started) PCH Median Improvements at Paradise Cove and Zuma Beach (cid:190) Project Description: This project was identified in the 2015 PCH Safety Study and in'}}

exec(code, env_args)
