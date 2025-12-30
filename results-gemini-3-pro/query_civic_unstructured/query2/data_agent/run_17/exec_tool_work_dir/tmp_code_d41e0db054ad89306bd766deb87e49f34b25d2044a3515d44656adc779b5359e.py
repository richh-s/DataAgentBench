code = """import json
import re

with open(locals()['var_function-call-10057184920144794313'], 'r') as f:
    funding_data = json.load(f)

with open(locals()['var_function-call-10057184920144796126'], 'r') as f:
    civic_docs = json.load(f)

qualifying_projects = set()
debug_logs = []

# Regex
construction_completed_re = re.compile(r'(construction\s+was\s+completed|complete\s+construction).*?2022', re.IGNORECASE | re.DOTALL)

for project in funding_data:
    p_name = project['Project_Name']
    
    # Check park
    is_park = False
    if re.search(r'\bpark\b|\bplayground\b', p_name, re.IGNORECASE):
        is_park = True
    
    if p_name == "Bluffs Park Shade Structure":
        debug_logs.append(f"Checking {p_name}, is_park={is_park}")

    found_in_docs = False
    completed_in_2022 = False
    
    for doc in civic_docs:
        text = doc['text']
        idx = text.find(p_name)
        if idx != -1:
            found_in_docs = True
            # Context
            context = text[idx:idx+1000]
            
            match = construction_completed_re.search(context)
            if match:
                completed_in_2022 = True
                if p_name == "Bluffs Park Shade Structure":
                    debug_logs.append(f"Found completion in doc: {match.group(0)}")
                break # Found completion, move to next project
    
    if is_park and completed_in_2022:
        qualifying_projects.add((p_name, int(project['Amount'])))
    elif p_name == "Bluffs Park Shade Structure":
         debug_logs.append(f"Failed to qualify. Found in docs: {found_in_docs}, Completed 2022: {completed_in_2022}")

total_funding = sum(amount for _, amount in qualifying_projects)

print("__RESULT__:")
print(json.dumps({"total_funding": total_funding, "projects": list(qualifying_projects), "logs": debug_logs}))"""

env_args = {'var_function-call-10057184920144794313': 'file_storage/function-call-10057184920144794313.json', 'var_function-call-10057184920144796126': 'file_storage/function-call-10057184920144796126.json', 'var_function-call-16463367332335965304': {'total_funding': 0, 'projects': [], 'debug': []}, 'var_function-call-12562812388912151187': {'found': True, 'context': 'Bluffs Park Shade Structure\n\n(cid:190) Updates: Construction was completed November 2022. Notice of completion\n\nfiled January 2023\n\nPage 4 of 6\n\nAgenda Item # 4.B.\n\n\n\n\n\n\n\n\n\n\n\nMarie Canyon Green Streets\n(cid:190) Updates:\n\n(cid:131) Construction was completed, January 2023\n(cid:131) Scheduled for Council acceptance on April 24, 2023\n\nBroad Beach Road Water Quality Repair\n\n(cid:190) Updates:\n\n(cid:131) Construction was completed, November 2022\n(cid:131) Notice of completion filed January 2023\n\nPoi'}}

exec(code, env_args)
