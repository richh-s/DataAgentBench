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

project_history = {}
newline = chr(10)

for doc in docs:
    d_date = get_date(doc)
    text = doc.get("text", "")
    lines = text.split(newline)
    
    for i, line in enumerate(lines):
        if "Updates:" in line or "Project Description:" in line:
            name = ""
            for j in range(i-1, -1, -1):
                s = lines[j].strip()
                if s and "Page" not in s and "Agenda" not in s and "Capital" not in s:
                    name = s
                    break
            
            if name:
                start_string = None
                for k in range(i, min(i+20, len(lines))):
                    sub = lines[k]
                    if k > i and ("Updates:" in sub or "Project Description:" in sub): break
                    if "Begin Construction" in sub or "Start Construction" in sub:
                        start_string = sub
                        break
                
                if name not in project_history:
                    project_history[name] = []
                project_history[name].append( (d_date, start_string) )

names = set()
for name, history in project_history.items():
    history.sort(key=lambda x: x[0], reverse=True)
    
    best_date_line = None
    for d, s in history:
        if s:
            best_date_line = s
            break
    
    if best_date_line:
        if "2022" in best_date_line:
            if "Spring" in best_date_line or "March" in best_date_line or "April" in best_date_line or "May" in best_date_line:
                names.add(name)

df = pd.DataFrame(funds)
res = df[df["Project_Name"].isin(names)]
print("__RESULT__:")
print(json.dumps({
    "count": len(res), 
    "total": res["Amount"].astype(float).sum(),
    "projects": res["Project_Name"].tolist()
}))"""

env_args = {'var_function-call-956811650377216769': 'file_storage/function-call-956811650377216769.json', 'var_function-call-956811650377216698': 'file_storage/function-call-956811650377216698.json', 'var_function-call-13847589957581412543': {'count': 8, 'total': 492000.0}, 'var_function-call-5361508054739911035': {'count': 9, 'total': 508000.0, 'projects': ['Broad Beach Road Water Quality Infrastructure Repairs (CalJPIA Project)', 'Civic Center Water Treatment Facility Phase 2', 'Encinal Canyon Road Drainage Improvements (FEMA/CalOES Project)', 'Latigo Canyon Road Culvert Repairs (FEMA/CalOES Project)', 'Latigo Canyon Road Roadway/Retaining Wall Improvements (FEMA Project)', 'Marie Canyon Green Streets', 'PCH Signal Synchronization System Improvements Project', 'Trancas Canyon Park Planting and Irrigation Repairs (CalJPIA/FEMA Project)', 'Trancas Canyon Park Slope Stabilization Project (CalJPIA Project)']}, 'var_function-call-16467101758424176887': {'count': 3, 'total': 229000.0, 'projects': ['Encinal Canyon Road Drainage Improvements (FEMA/CalOES Project)', 'Latigo Canyon Road Culvert Repairs (FEMA/CalOES Project)', 'Latigo Canyon Road Roadway/Retaining Wall Improvements (FEMA Project)']}}

exec(code, env_args)
