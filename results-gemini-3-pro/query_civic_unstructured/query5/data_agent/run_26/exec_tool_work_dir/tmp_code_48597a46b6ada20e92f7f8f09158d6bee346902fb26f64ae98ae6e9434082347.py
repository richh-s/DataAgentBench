code = """import json
import re

with open(locals()['var_function-call-5605292304546820245'], 'r') as f:
    docs = json.load(f)
text = docs[0]['text']
norm_text = " ".join(text.split())

with open(locals()['var_function-call-3657045741871633664'], 'r') as f:
    funding_data = json.load(f)
funding_map = {item['Project_Name']: int(item['Amount']) for item in funding_data}

target = "Latigo Canyon Road Retaining Wall Repair Project"
norm_target = " ".join(target.split())

idx = norm_text.find(norm_target)
context = ""
matches_date = False
matches_disaster = False

if idx != -1:
    context = norm_text[idx:idx+1000]
    if "FEMA" in context or "CalOES" in context:
        matches_disaster = True
    
    if re.search(r"Advertise[:\s]+[A-Za-z]+\s+2022", context, re.IGNORECASE):
        matches_date = True
        
print("__RESULT__:")
print(json.dumps({
    "name": target,
    "found_idx": idx,
    "context_preview": context[:200],
    "matches_disaster": matches_disaster,
    "matches_date": matches_date
}))"""

env_args = {'var_function-call-5605292304546820245': 'file_storage/function-call-5605292304546820245.json', 'var_function-call-3657045741871633664': 'file_storage/function-call-3657045741871633664.json', 'var_function-call-3095873966328679813': {'projects': [], 'total': 0}, 'var_function-call-4623292609862033463': {'headers': [{'Capital Improvement Projects': 332}, {'Disaster Recovery Projects': 365}], 'found_count': 2, 'examples': ['2022 Morning View Resurfacing & Storm Drain Improvements', 'Bluffs Park Shade Structure']}, 'var_function-call-12935383195900810632': {'found_projects': [{'name': '2022 Morning View Resurfacing & Storm Drain Improvements', 'amount': 38000}, {'name': 'Bluffs Park Shade Structure', 'amount': 21000}, {'name': 'Broad Beach Road Water Quality Repair', 'amount': 93000}, {'name': 'Encinal Canyon Road Repairs', 'amount': 47000}, {'name': 'Malibu Canyon Road Traffic Study', 'amount': 97000}, {'name': 'Malibu Road Slope Repairs', 'amount': 44000}, {'name': 'Marie Canyon Green Streets', 'amount': 50000}, {'name': 'PCH Signal Synchronization System Improvements Project', 'amount': 16000}, {'name': 'Point Dume Walkway Repairs', 'amount': 59000}, {'name': 'Storm Drain Trash Screens', 'amount': 11000}, {'name': 'Storm Drain Trash Screens Phase Two', 'amount': 24000}], 'total': 500000}, 'var_function-call-5490281074798077253': [{'idx': 343, 'type': 'capital', 'text': 'Capital Improvement Projects and Disaster Recovery Projects Status'}, {'idx': 712, 'type': 'capital', 'text': 'Capital Improvement Projects (Design)'}, {'idx': 5624, 'type': 'capital', 'text': 'Capital Improvement Projects (Construction)'}, {'idx': 7116, 'type': 'capital', 'text': 'Capital Improvement Projects (Not Started)'}], 'var_function-call-3270848169410763630': {'found_projects': [], 'total': 0}}

exec(code, env_args)
