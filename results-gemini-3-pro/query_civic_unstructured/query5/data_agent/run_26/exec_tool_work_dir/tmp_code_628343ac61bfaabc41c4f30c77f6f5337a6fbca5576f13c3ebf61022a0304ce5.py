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

# Find locations
found_items = []
for name in project_groups:
    norm_name = " ".join(name.split())
    # Find all occurrences? Just the first one usually.
    # But some might appear in "Updates" of others?
    # We want the Header occurrence. 
    # Usually Project Name is followed by Updates.
    # So we search for "Name Updates" or "Name (cid:190) Updates"
    # In norm_text: "Name (cid:190) Updates"
    
    # Try finding "Name (cid:190) Updates"
    # We don't know exact char for (cid:190) in norm_text so we use regex or partial
    # Try finding name, then check if "Updates" follows soon
    
    idx = norm_text.find(norm_name)
    if idx != -1:
        found_items.append({"name": name, "idx": idx})

found_items.sort(key=lambda x: x['idx'])

total_funding = 0
final_list = []

for i in range(len(found_items)):
    item = found_items[i]
    name = item['name']
    idx = item['idx']
    
    # End index is start of next project or reasonable limit
    if i < len(found_items) - 1:
        end_idx = found_items[i+1]['idx']
    else:
        end_idx = len(norm_text)
    
    # Limit context to max 2000 chars
    if end_idx - idx > 2000:
        end_idx = idx + 2000
        
    context = norm_text[idx:end_idx]
    
    data = project_groups[name]
    
    # Check Disaster in context
    is_disaster = data["is_disaster"]
    if not is_disaster:
        if "FEMA" in context or "CalOES" in context or "CalJPIA" in context:
            is_disaster = True
        # "Disaster Recovery" check?
        # Only if strict context.
        # Check "Disaster Recovery Projects" section?
        # If "Disaster Recovery Projects" appears *before* this project in the sequence of headers...
        # But we are using a list of project names.
        # If "Disaster Recovery Projects" is in the text before this project and AFTER the previous project?
        pass

    # Check Date
    started_2022 = False
    if "2022" in name:
        started_2022 = True
    
    if not started_2022:
        # Check specific patterns
        # "Construction was completed, November 2022"
        # "Construction was completed November 2022"
        # "Begin Construction: ... 2022"
        
        # Regex for "Completed ... 2022"
        if re.search(r"Construction was completed.*?2022", context, re.IGNORECASE):
            started_2022 = True
        elif re.search(r"Begin Construction.*?2022", context, re.IGNORECASE):
            started_2022 = True
        elif re.search(r"Advertise.*?2022", context, re.IGNORECASE):
            started_2022 = True
        elif re.search(r"awarded the contract.*?2022", context, re.IGNORECASE):
            started_2022 = True
            
    if is_disaster and started_2022:
        total_funding += data["total"]
        final_list.append(name)

print("__RESULT__:")
print(json.dumps({"projects": final_list, "total": total_funding}))"""

env_args = {'var_function-call-5605292304546820245': 'file_storage/function-call-5605292304546820245.json', 'var_function-call-3657045741871633664': 'file_storage/function-call-3657045741871633664.json', 'var_function-call-3095873966328679813': {'projects': [], 'total': 0}, 'var_function-call-4623292609862033463': {'headers': [{'Capital Improvement Projects': 332}, {'Disaster Recovery Projects': 365}], 'found_count': 2, 'examples': ['2022 Morning View Resurfacing & Storm Drain Improvements', 'Bluffs Park Shade Structure']}, 'var_function-call-12935383195900810632': {'found_projects': [{'name': '2022 Morning View Resurfacing & Storm Drain Improvements', 'amount': 38000}, {'name': 'Bluffs Park Shade Structure', 'amount': 21000}, {'name': 'Broad Beach Road Water Quality Repair', 'amount': 93000}, {'name': 'Encinal Canyon Road Repairs', 'amount': 47000}, {'name': 'Malibu Canyon Road Traffic Study', 'amount': 97000}, {'name': 'Malibu Road Slope Repairs', 'amount': 44000}, {'name': 'Marie Canyon Green Streets', 'amount': 50000}, {'name': 'PCH Signal Synchronization System Improvements Project', 'amount': 16000}, {'name': 'Point Dume Walkway Repairs', 'amount': 59000}, {'name': 'Storm Drain Trash Screens', 'amount': 11000}, {'name': 'Storm Drain Trash Screens Phase Two', 'amount': 24000}], 'total': 500000}, 'var_function-call-5490281074798077253': [{'idx': 343, 'type': 'capital', 'text': 'Capital Improvement Projects and Disaster Recovery Projects Status'}, {'idx': 712, 'type': 'capital', 'text': 'Capital Improvement Projects (Design)'}, {'idx': 5624, 'type': 'capital', 'text': 'Capital Improvement Projects (Construction)'}, {'idx': 7116, 'type': 'capital', 'text': 'Capital Improvement Projects (Not Started)'}], 'var_function-call-3270848169410763630': {'found_projects': [], 'total': 0}, 'var_function-call-12913647900088782014': {'name': 'Latigo Canyon Road Retaining Wall Repair Project', 'found_idx': 2534, 'context_preview': 'Latigo Canyon Road Retaining Wall Repair Project (cid:190) Updates: (cid:131) Plans and specifications have been completed (cid:131) Awaiting final FEMA/CalOES approval for scope modification (cid:190', 'matches_disaster': True, 'matches_date': False}, 'var_function-call-6399400156716925980': {'projects': [{'name': 'Malibu Road Slope Repairs', 'total': 81000}], 'total_funding': 81000}}

exec(code, env_args)
