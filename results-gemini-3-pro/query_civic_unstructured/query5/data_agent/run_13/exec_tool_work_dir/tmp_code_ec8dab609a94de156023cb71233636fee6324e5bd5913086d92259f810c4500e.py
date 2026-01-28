code = """import json
import re

# Access file paths
path_docs = locals()['var_function-call-3874891945524290296']
path_funding = locals()['var_function-call-15854994629238298351']

# Load files
with open(path_docs, 'r') as f:
    docs = json.load(f)

with open(path_funding, 'r') as f:
    funding = json.load(f)

funding_map = {item['Project_Name']: int(item['Amount']) for item in funding}
project_names = list(funding_map.keys())

disaster_suffixes = ["(FEMA Project)", "(CalJPIA Project)", "(CalOES Project)", "(FEMA)", "(CalOES)", "(CalJPIA)", "Disaster Recovery"]
disaster_keywords = ["FEMA", "CalOES", "CalJPIA", "Woolsey", "Fire", "Disaster", "Emergency"]

start_phrases = ["begin construction", "construction start", "start date", "work began", "construction began"]

matches = {}

for proj in project_names:
    is_disaster = False
    started_2022 = False
    
    # Check suffix
    for s in disaster_suffixes:
        if s.lower() in proj.lower():
            is_disaster = True
            break
            
    for doc in docs:
        text = doc['text']
        if proj in text:
            start_idx = 0
            while True:
                idx = text.find(proj, start_idx)
                if idx == -1:
                    break
                
                snippet = text[idx:idx+2000]
                
                if not is_disaster:
                    for kw in disaster_keywords:
                        if kw.lower() in snippet.lower():
                            is_disaster = True
                            break
                
                lines = snippet.splitlines()
                for line in lines:
                    line_lower = line.lower()
                    for phrase in start_phrases:
                        if phrase in line_lower:
                            if "2022" in line:
                                started_2022 = True
                
                if is_disaster and started_2022:
                    break
                
                start_idx = idx + 1
        
        if is_disaster and started_2022:
            break

    if is_disaster and started_2022:
        matches[proj] = funding_map[proj]

total_amount = sum(matches.values())
print("__RESULT__:")
print(json.dumps({"total_funding": total_amount, "projects": list(matches.keys())}))"""

env_args = {'var_function-call-3965553099974352021': ['civic_docs'], 'var_function-call-4642291863643268056': 'file_storage/function-call-4642291863643268056.json', 'var_function-call-15854994629238298351': 'file_storage/function-call-15854994629238298351.json', 'var_function-call-3874891945524290296': 'file_storage/function-call-3874891945524290296.json'}

exec(code, env_args)
