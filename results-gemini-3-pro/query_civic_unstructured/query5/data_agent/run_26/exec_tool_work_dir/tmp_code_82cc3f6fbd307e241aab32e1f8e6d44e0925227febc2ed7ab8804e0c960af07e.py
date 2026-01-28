code = """import json
import re

with open(locals()['var_function-call-5605292304546820245'], 'r') as f:
    docs = json.load(f)
text = docs[0]['text']
norm_text = " ".join(text.split())

with open(locals()['var_function-call-3657045741871633664'], 'r') as f:
    funding_data = json.load(f)

funding_map = {item['Project_Name']: int(item['Amount']) for item in funding_data}

total_funding = 0
found_projects = []

for name, amount in funding_map.items():
    is_disaster = False
    started_2022 = False
    
    # Check Name properties
    if "(FEMA" in name or "(CalOES" in name or "CalJPIA" in name:
        is_disaster = True
    if "2022" in name:
        started_2022 = True
        
    # Search in text
    idx = norm_text.find(" ".join(name.split()))
    
    # Context checks
    if idx != -1:
        context = norm_text[idx:idx+1500]
        
        # Check context for Disaster indicators if not already confirmed
        if not is_disaster:
            if "FEMA" in context or "CalOES" in context or "CalJPIA" in context:
                # Be careful not to match FEMA in the *next* project
                # But context is short enough, usually fine.
                is_disaster = True
            if "Disaster Recovery" in context:
                is_disaster = True
        
        # Check context for Date if not already confirmed
        if not started_2022:
            if re.search(r"Begin Construction[:\s]+[A-Za-z]+\s+2022", context, re.IGNORECASE):
                started_2022 = True
            elif re.search(r"Advertise[:\s]+[A-Za-z]+\s+2022", context, re.IGNORECASE):
                started_2022 = True
            elif re.search(r"Construction was completed[:\s,]+([A-Za-z]+\s+)?2022", context, re.IGNORECASE):
                started_2022 = True
            elif re.search(r"awarded the contract.*2022", context, re.IGNORECASE):
                started_2022 = True

    # If we found it in text, we use the combined info.
    # If not found in text, we rely ONLY on Name properties.
    # If Name says "2022 ... (FEMA)", we count it.
    # If Name says "Project X (FEMA)" but no 2022 in name, and not in text -> We don't know date -> Skip.
    
    if is_disaster and started_2022:
        # One check: If not found in text, and rely on name, is it reliable?
        # Yes, if name has "2022" and "FEMA".
        # If found in text, we trusted context.
        total_funding += amount
        found_projects.append({"name": name, "amount": amount})

print("__RESULT__:")
print(json.dumps({"found_projects": found_projects, "total": total_funding}))"""

env_args = {'var_function-call-5605292304546820245': 'file_storage/function-call-5605292304546820245.json', 'var_function-call-3657045741871633664': 'file_storage/function-call-3657045741871633664.json', 'var_function-call-3095873966328679813': {'projects': [], 'total': 0}, 'var_function-call-4623292609862033463': {'headers': [{'Capital Improvement Projects': 332}, {'Disaster Recovery Projects': 365}], 'found_count': 2, 'examples': ['2022 Morning View Resurfacing & Storm Drain Improvements', 'Bluffs Park Shade Structure']}, 'var_function-call-12935383195900810632': {'found_projects': [{'name': '2022 Morning View Resurfacing & Storm Drain Improvements', 'amount': 38000}, {'name': 'Bluffs Park Shade Structure', 'amount': 21000}, {'name': 'Broad Beach Road Water Quality Repair', 'amount': 93000}, {'name': 'Encinal Canyon Road Repairs', 'amount': 47000}, {'name': 'Malibu Canyon Road Traffic Study', 'amount': 97000}, {'name': 'Malibu Road Slope Repairs', 'amount': 44000}, {'name': 'Marie Canyon Green Streets', 'amount': 50000}, {'name': 'PCH Signal Synchronization System Improvements Project', 'amount': 16000}, {'name': 'Point Dume Walkway Repairs', 'amount': 59000}, {'name': 'Storm Drain Trash Screens', 'amount': 11000}, {'name': 'Storm Drain Trash Screens Phase Two', 'amount': 24000}], 'total': 500000}, 'var_function-call-5490281074798077253': [{'idx': 343, 'type': 'capital', 'text': 'Capital Improvement Projects and Disaster Recovery Projects Status'}, {'idx': 712, 'type': 'capital', 'text': 'Capital Improvement Projects (Design)'}, {'idx': 5624, 'type': 'capital', 'text': 'Capital Improvement Projects (Construction)'}, {'idx': 7116, 'type': 'capital', 'text': 'Capital Improvement Projects (Not Started)'}]}

exec(code, env_args)
