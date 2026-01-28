code = """import json
import re

with open(locals()['var_function-call-16563647665074861239'], 'r') as f:
    civic_docs = json.load(f)

with open(locals()['var_function-call-13407039906520759084'], 'r') as f:
    funding_data = json.load(f)

funding_map = {item['Project_Name'].strip(): int(item['Amount']) for item in funding_data}

projects = []
ignore_lines = [
    "Capital Improvement Projects (Design)",
    "Capital Improvement Projects (Construction)",
    "Capital Improvement Projects (Not Started)",
    "Disaster Recovery Projects",
    "Public Works Commission",
    "Agenda Report",
    "Subject:",
    "Date prepared:", 
    "Meeting date:", 
    "To:", "From:", "Prepared by:", "Approved by:",
    "RECOMMENDED ACTION:", "DISCUSSION:", "Page ", "Agenda Item"
]

for doc in civic_docs:
    text = doc['text']
    # Removing special chars, careful with escaping
    # Just replace them if they exist as literals
    text = text.replace('(cid:190)', '')
    text = text.replace('(cid:131)', '')

    chunks = text.split("Updates:")
    
    for i in range(1, len(chunks)):
        prev_chunk = chunks[i-1]
        lines = [l.strip() for l in prev_chunk.split('\n') if l.strip()]
        
        project_name = None
        for line in reversed(lines):
            is_ignore = False
            for ign in ignore_lines:
                if ign in line:
                    is_ignore = True
                    break
            if not is_ignore:
                project_name = line
                break
        
        if not project_name:
            continue
            
        details = chunks[i]
        
        # Regex with double escaped backslashes for JSON transport
        st = None
        # Pattern: Begin Construction: <text>
        # Use simple string logic if regex fails repeatedly?
        # Let's try matching "Begin Construction:"
        if "Begin Construction:" in details:
            part = details.split("Begin Construction:")[1]
            # Take first line or up to newline
            st_line = part.split('\n')[0].strip()
            st = st_line
        
        p_type = "capital"
        disaster_kws = ["FEMA", "CalOES", "CalJPIA", "Woolsey", "Disaster", "Fire"]
        
        if any(kw.lower() in project_name.lower() for kw in disaster_kws):
            p_type = "disaster"
        elif any(kw.lower() in details.lower() for kw in disaster_kws):
            p_type = "disaster"
            
        projects.append({
            "name": project_name,
            "type": p_type,
            "st": st
        })

total_funding = 0
matched_projects = []

for p in projects:
    if p['type'] == 'disaster':
        if p['st'] and '2022' in p['st']:
            amt = funding_map.get(p['name'])
            if amt is not None:
                total_funding += amt
                matched_projects.append({'name': p['name'], 'amount': amt, 'st': p['st']})

print("__RESULT__:")
print(json.dumps({"total_funding": total_funding, "matched_projects": matched_projects}))"""

env_args = {'var_function-call-16563647665074861239': 'file_storage/function-call-16563647665074861239.json', 'var_function-call-13407039906520759084': 'file_storage/function-call-13407039906520759084.json'}

exec(code, env_args)
