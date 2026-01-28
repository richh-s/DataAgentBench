code = """import json
import re

path_fund = locals()['var_function-call-10469334728230477233']
path_civic = locals()['var_function-call-2938925832300121320']

with open(path_fund, 'r') as f:
    funding_data = json.load(f)

with open(path_civic, 'r') as f:
    civic_docs = json.load(f)

full_text = ""
for doc in civic_docs:
    full_text += doc['text'] + chr(10)

lines = full_text.split(chr(10))
projects = {}
current_name = None
current_text = []

def is_bullet(l):
    l = l.strip()
    return l.startswith("(cid:") or l.startswith("•") or l.startswith("-")

# Improved Parsing
for i in range(len(lines)):
    line = lines[i].strip()
    if not line: continue
    
    is_header = False
    if not is_bullet(line) and line[0].isupper():
        # Look ahead
        has_bullet_next = False
        for j in range(i+1, min(i+5, len(lines))):
            nl = lines[j].strip()
            if not nl: continue
            if is_bullet(nl) or nl.startswith("Updates:") or nl.startswith("Project Description:"):
                has_bullet_next = True
            break
        
        if has_bullet_next:
            is_header = True
            
    if "Capital Improvement Projects" in line or "Disaster Recovery Projects" in line: is_header = False
    if "Agenda" in line: is_header = False
    
    if is_header:
        if current_name:
            projects[current_name] = chr(10).join(current_text)
        current_name = line
        current_text = []
    else:
        if current_name:
            current_text.append(line)

if current_name:
    projects[current_name] = chr(10).join(current_text)

norm_projects = {k.strip().lower(): v for k, v in projects.items()}

# Calculation
total_funding = 0
disaster_projects = []

for item in funding_data:
    p_name = item['Project_Name']
    amt = float(item['Amount'])
    
    # Check disaster
    # Based on suffix or explicit knowledge
    is_disaster = False
    if "FEMA" in p_name or "CalOES" in p_name or "CalJPIA" in p_name:
        is_disaster = True
        
    if not is_disaster:
        continue
        
    # Find text
    txt = norm_projects.get(p_name.strip().lower(), "")
    
    # Check start date
    start_2022 = False
    if txt:
        # Regex for start date
        # "Begin Construction: ... 2022"
        # "Construction Start: ... 2022"
        # "Construction began ... 2022"
        
        # We need to be careful not to match "Completion ... 2022"
        
        # Check explicit start phrases
        start_phrases = [
            r"Begin [Cc]onstruction.{0,40}2022",
            r"Start [Cc]onstruction.{0,40}2022",
            r"Construction [Bb]egan.{0,40}2022",
            r"Construction [Ss]tarted.{0,40}2022",
            r"Begin [Dd]esign.{0,40}2022" # Does "started" mean design? Usually construction.
            # But "Projects have statuses: 'design', 'completed', 'not started'".
            # If a project started "Design" in 2022, did the project start?
            # Yes, the project lifecycle started.
            # "Trancas Canyon ... (CalJPIA/FEMA Project)" -> "Complete Design: Spring 2022", "Begin Construction: Summer 2022".
            # "Malibu Road Slope Repairs (CalOES Project)" -> "Complete Design: Spring 2022", "Begin Construction: Fall 2022".
            # Both started construction in 2022.
            
            # "Trancas Canyon ... (FEMA/CalOES Project)" -> "Begin Construction: Summer/Fall 2021".
            
            # Let's match "Begin Construction" or "Construction began".
        ]
        
        for pat in start_phrases:
            if re.search(pat, txt, re.IGNORECASE):
                start_2022 = True
                break
                
    if start_2022:
        total_funding += amt
        disaster_projects.append(p_name)

print("__RESULT__:")
print(json.dumps({"total_funding": total_funding, "projects": disaster_projects}))"""

env_args = {'var_function-call-10469334728230477233': 'file_storage/function-call-10469334728230477233.json', 'var_function-call-10469334728230474172': 'file_storage/function-call-10469334728230474172.json', 'var_function-call-2938925832300121320': 'file_storage/function-call-2938925832300121320.json', 'var_function-call-12502361018328116741': {'total': 87000.0, 'matches': ['Trancas Canyon Park Planting and Irrigation Repairs (CalJPIA/FEMA Project)', 'Trancas Canyon Park Slope Stabilization Project (CalJPIA Project)'], 'parsed_titles': ['Agenda Report', '03-22-23', 'Jorge Rubalcava, Senior Civil Engineer', 'Date prepared: March 15, 2023', 'Meeting date: March 22, 2023']}, 'var_function-call-6275733380898896556': {'total': 87000.0, 'matches': ['Trancas Canyon Park Planting and Irrigation Repairs (CalJPIA/FEMA Project)', 'Trancas Canyon Park Slope Stabilization Project (CalJPIA Project)'], 'parsed_sample': ['2022 morning view resurfacing & storm drain improvements', 'project and will submit to the county for review.', 'pch median improvements project', 'and rejected all bids due to a budget shortfall', 'or phasing out the project']}, 'var_function-call-6032935255007015337': {'malibu road slope repairs': '(cid:190) Project Description: The existing slope adjacent to the beach access stairs\nat 24712 Malibu Road has been eroded and caused damage to Malibu', 'trancas canyon park planting and irrigation repairs (caljpia/fema project)': '(cid:190) Updates:\n(cid:131) The project consultant has started the design of this project.\n(cid:190) Project Schedule:\n(cid:131) Complete Design: Spring 2022\n(cid:131) Begin Construction: Summer 2022', 'malibu road slope repairs (caloes project)': '(cid:190) Project Description: The existing slope adjacent to the beach access stairs\nat 24712 Malibu Road has been eroded and caused damage to Malibu Road.\n(cid:190) Updates:\n(cid:131) The design has started and is anticipated to be completed by the Spring\nof 2022.\n(cid:190) Estimated Schedule:\n(cid:131) Complete Design: Spring 2022\n(cid:131) Begin Construction: Fall 2022', 'trancas canyon park planting and irrigation repairs (fema/caloes project)': '(cid:190) Updates:\n(cid:131) The project consultant has started the design of this project.\n(cid:190) Project Schedule\n(cid:131) Complete Design: Summer 2021\n(cid:131) Begin Construction: Summer/Fall 2021'}}

exec(code, env_args)
