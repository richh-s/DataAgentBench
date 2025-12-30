code = """import json
import pandas as pd
import re
from datetime import datetime

p_c = locals()['var_function-call-956811650377216769']
p_f = locals()['var_function-call-956811650377216698']

with open(p_c, 'r') as f: docs = json.load(f)
with open(p_f, 'r') as f: funds = json.load(f)

def get_date(doc):
    fname = doc.get("filename", "")
    m = re.search(r'(\d{8})', fname)
    if m:
        dstr = m.group(1)
        try:
            return datetime.strptime(dstr, "%m%d%Y")
        except:
            pass
    return datetime.min

docs.sort(key=get_date, reverse=True)

names = set()
processed_projects = set()
newline = chr(10)

for doc in docs:
    text = doc.get("text", "")
    lines = text.split(newline)
    
    doc_projects = {}
    
    for i, line in enumerate(lines):
        if "Updates:" in line or "Project Description:" in line:
            name = ""
            for j in range(i-1, -1, -1):
                s = lines[j].strip()
                if s and "Page" not in s and "Agenda" not in s and "Capital" not in s:
                    name = s
                    break
            
            if name:
                start_date_line = ""
                for k in range(i, min(i+20, len(lines))):
                    sub = lines[k]
                    if k > i and ("Updates:" in sub or "Project Description:" in sub): break
                    if "Begin Construction" in sub or "Start Construction" in sub:
                        start_date_line = sub
                        break
                
                if name not in doc_projects:
                    doc_projects[name] = start_date_line

    for name, date_line in doc_projects.items():
        if name in processed_projects:
            continue
        
        processed_projects.add(name)
        
        if date_line:
            # Check for Spring 2022
            # date_line example: "(cid:131) Begin Construction: Fall 2023"
            if "2022" in date_line:
                if "Spring" in date_line or "March" in date_line or "April" in date_line or "May" in date_line:
                    names.add(name)

df = pd.DataFrame(funds)
res = df[df["Project_Name"].isin(names)]
print("__RESULT__:")
print(json.dumps({
    "count": len(res), 
    "total": res["Amount"].astype(float).sum(),
    "projects": res["Project_Name"].tolist()
}))"""

env_args = {'var_function-call-956811650377216769': 'file_storage/function-call-956811650377216769.json', 'var_function-call-956811650377216698': 'file_storage/function-call-956811650377216698.json', 'var_function-call-13847589957581412543': {'count': 8, 'total': 492000.0}, 'var_function-call-5361508054739911035': {'count': 9, 'total': 508000.0, 'projects': ['Broad Beach Road Water Quality Infrastructure Repairs (CalJPIA Project)', 'Civic Center Water Treatment Facility Phase 2', 'Encinal Canyon Road Drainage Improvements (FEMA/CalOES Project)', 'Latigo Canyon Road Culvert Repairs (FEMA/CalOES Project)', 'Latigo Canyon Road Roadway/Retaining Wall Improvements (FEMA Project)', 'Marie Canyon Green Streets', 'PCH Signal Synchronization System Improvements Project', 'Trancas Canyon Park Planting and Irrigation Repairs (CalJPIA/FEMA Project)', 'Trancas Canyon Park Slope Stabilization Project (CalJPIA Project)']}}

exec(code, env_args)
