code = """import json
import re

path_funding = locals()["var_function-call-6833374196738575429"]
path_docs = locals()["var_function-call-2571732605933953840"]

with open(path_funding, "r") as f:
    funding_data = json.load(f)
with open(path_docs, "r") as f:
    civic_docs = json.load(f)

projects = []
marker_updates = "Updates:"
marker_schedule = "Project Schedule:"

for doc in civic_docs:
    lines = doc["text"].splitlines()
    for i in range(len(lines)):
        line = lines[i].strip()
        if marker_updates in line or marker_schedule in line:
             name = None
             for k in range(i-1, -1, -1):
                 p = lines[k].strip()
                 if p:
                     if "Agenda" not in p and "Projects" not in p and "Report" not in p:
                         name = p
                     break
             
             if name:
                 chunk = " ".join([l.strip() for l in lines[i:i+50]])
                 m = re.search("Begin Construction:?\\s*([A-Za-z0-9, ]+)", chunk)
                 if m:
                     date = m.group(1).strip()
                     projects.append((name, date))

spring_2022_projects = set()
for p in projects:
    name, date = p
    d = date.lower()
    is_spring = False
    if "spring 2022" in d or "spring, 2022" in d:
        is_spring = True
    elif "2022" in d:
        if "march" in d or "april" in d or "may" in d:
            is_spring = True
    
    if is_spring:
        spring_2022_projects.add(name)

# Aggregate funding
f_map = {}
for r in funding_data:
    name = re.sub("\\s+", " ", r["Project_Name"]).strip().lower()
    amt = int(r["Amount"])
    if name in f_map:
        f_map[name] += amt
    else:
        f_map[name] = amt

f_keys = list(f_map.keys())

total = 0
found_list = []
processed = set()

for name in spring_2022_projects:
    if name in processed:
        continue
    processed.add(name)
    clean = re.sub("\\s+", " ", name).strip().lower()
    
    matched = False
    if clean in f_map:
        total += f_map[clean]
        found_list.append(name)
    else:
        for k in f_keys:
            if k in clean or clean in k:
                total += f_map[k]
                found_list.append(name)
                matched = True
                break

print("__RESULT__:")
print(json.dumps({"count": len(found_list), "total_funding": total, "projects": found_list}))"""

env_args = {'var_function-call-3413924578737441379': ['civic_docs'], 'var_function-call-3413924578737439684': ['Funding'], 'var_function-call-6833374196738575429': 'file_storage/function-call-6833374196738575429.json', 'var_function-call-6833374196738572946': 'file_storage/function-call-6833374196738572946.json', 'var_function-call-2571732605933953840': 'file_storage/function-call-2571732605933953840.json', 'var_function-call-15650630818313751010': {'docs_count': 5, 'funding_count': 500}, 'var_function-call-14631719410272625992': {'filenames': ['malibucity_agenda_03222023-2060.txt', 'malibucity_agenda__01262022-1835.txt', 'malibucity_agenda__01272021-1626.txt', 'malibucity_agenda__03022021-1648.txt', 'malibucity_agenda__03232022-1869.txt'], 'hits': [{'filename': 'malibucity_agenda__01262022-1835.txt', 'snippet': 'Found Spring 2022'}, {'filename': 'malibucity_agenda__01262022-1835.txt', 'snippet': 'Found Month 2022'}, {'filename': 'malibucity_agenda__01272021-1626.txt', 'snippet': 'Found Spring 2022'}, {'filename': 'malibucity_agenda__01272021-1626.txt', 'snippet': 'Found Month 2022'}, {'filename': 'malibucity_agenda__03022021-1648.txt', 'snippet': 'Found Spring 2022'}, {'filename': 'malibucity_agenda__03022021-1648.txt', 'snippet': 'Found Month 2022'}, {'filename': 'malibucity_agenda__03232022-1869.txt', 'snippet': 'Found Spring 2022'}, {'filename': 'malibucity_agenda__03232022-1869.txt', 'snippet': 'Found Month 2022'}]}, 'var_function-call-1942969761525720729': {'count': 9, 'total_funding': 459000, 'projects': ['Trancas Canyon Park Planting and Irrigation Repairs (CalJPIA/FEMA Project)', 'Civic Center Water Treatment Facility Phase 2', 'Trancas Canyon Park Slope Stabilization Project (CalJPIA Project)', 'Civic Center Stormwater Diversion Structure', '2021 Annual Street Maintenance', 'Latigo Canyon Road Roadway/Retaining Wall Improvements (FEMA Project)', 'Broad Beach Road Water Quality Infrastructure Repairs (CalJPIA Project)', 'Malibu Park Drainage Improvements', 'Marie Canyon Green Streets']}}

exec(code, env_args)
