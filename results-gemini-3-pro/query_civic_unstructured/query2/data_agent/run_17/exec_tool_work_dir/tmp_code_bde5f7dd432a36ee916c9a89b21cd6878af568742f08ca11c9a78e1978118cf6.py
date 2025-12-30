code = """import json
import re

with open(locals()['var_function-call-10057184920144794313'], 'r') as f:
    funding_data = json.load(f)

with open(locals()['var_function-call-10057184920144796126'], 'r') as f:
    civic_docs = json.load(f)

park_status = []

construction_completed_re = re.compile(r'(construction\s+was\s+completed|complete\s+construction)[:\s]+.*?(\d{4})', re.IGNORECASE | re.DOTALL)

for project in funding_data:
    p_name = project['Project_Name']
    tokens = re.split(r'[^a-zA-Z0-9]', p_name.lower())
    if "park" in tokens or "playground" in tokens:
        # It's a park project
        status_found = "Not Found in Docs"
        completion_date = "N/A"
        
        for doc in civic_docs:
            text = doc['text']
            idx = text.find(p_name)
            if idx != -1:
                context = text[idx:idx+500]
                
                # Check for completion date
                match = construction_completed_re.search(context)
                if match:
                    status_found = "Completed"
                    completion_date = match.group(2) # Group 2 is the year
                    # Also grab the whole match to see month
                    full_match = match.group(0)
                else:
                    # Check if it mentions "Completed" without date in context?
                    if "completed" in context.lower():
                        status_found = "Mentioned Completed"
                    else:
                        status_found = "Found, no completion detected"
                
                park_status.append({
                    "name": p_name,
                    "status": status_found,
                    "date_match": completion_date if status_found == "Completed" else None,
                    "context_preview": context[:200].replace("\n", " ")
                })
                break # Just check first doc occurrence for now

print("__RESULT__:")
print(json.dumps(park_status))"""

env_args = {'var_function-call-10057184920144794313': 'file_storage/function-call-10057184920144794313.json', 'var_function-call-10057184920144796126': 'file_storage/function-call-10057184920144796126.json', 'var_function-call-16463367332335965304': {'total_funding': 0, 'projects': [], 'debug': []}, 'var_function-call-12562812388912151187': {'found': True, 'context': 'Bluffs Park Shade Structure\n\n(cid:190) Updates: Construction was completed November 2022. Notice of completion\n\nfiled January 2023\n\nPage 4 of 6\n\nAgenda Item # 4.B.\n\n\n\n\n\n\n\n\n\n\n\nMarie Canyon Green Streets\n(cid:190) Updates:\n\n(cid:131) Construction was completed, January 2023\n(cid:131) Scheduled for Council acceptance on April 24, 2023\n\nBroad Beach Road Water Quality Repair\n\n(cid:190) Updates:\n\n(cid:131) Construction was completed, November 2022\n(cid:131) Notice of completion filed January 2023\n\nPoi'}, 'var_function-call-4420774818653847510': {'total_funding': 0, 'projects': [], 'logs': ['Checking Bluffs Park Shade Structure, is_park=False', 'Found completion in doc: Construction was completed November 2022', 'Failed to qualify. Found in docs: True, Completed 2022: True']}, 'var_function-call-15478542269899668790': {'name': 'Bluffs Park Shade Structure', 'match': 'None', 'bool': False}, 'var_function-call-5050739371739425431': {'total_funding': 21000, 'projects': [['Bluffs Park Shade Structure', 21000]]}}

exec(code, env_args)
