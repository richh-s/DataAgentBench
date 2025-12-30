code = """import json
import re

# Load Mongo Data
with open(locals()['var_function-call-16563647665074861239'], 'r') as f:
    civic_docs = json.load(f)

# Load Funding Data
with open(locals()['var_function-call-13407039906520759084'], 'r') as f:
    funding_data = json.load(f)

funding_map = {item['Project_Name']: int(item['Amount']) for item in funding_data}

projects = []
# Headers/Lines to ignore when identifying project name
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
    # Normalize unicode bullets
    text = text.replace(u'\u00be', '')
    text = text.replace('(cid:190)', '')
    text = text.replace(u'\u0083', '') # Another bullet seen in preview (cid:131)
    text = text.replace('(cid:131)', '')

    # Split by "Updates:"
    chunks = text.split("Updates:")
    
    # Process chunks
    # chunks[0] is intro. chunks[1] is details of Proj1 + Proj2 Name at end.
    # Wait, splitting by "Updates:" leaves the Project Name at the end of the PREVIOUS chunk.
    # And the details in the CURRENT chunk.
    
    for i in range(1, len(chunks)):
        # 1. Identify Project Name from the end of chunks[i-1]
        prev_chunk = chunks[i-1]
        lines = [l.strip() for l in prev_chunk.split('\n') if l.strip()]
        
        project_name = None
        # Walk backwards finding the first line that isn't a header/ignore line
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
            
        # 2. Extract Info from current chunk (chunks[i])
        # The current chunk contains the updates, schedule etc. for this project
        # AND the name of the NEXT project at the very end (which we ignore here, handled in next iteration)
        
        details = chunks[i]
        
        # We need to limit 'details' to avoid reading into the next project's name?
        # Actually, since we split by "Updates:", the next project name is at the end of 'details'.
        # The 'details' text will look like:
        # "Staff is working... \n Project Schedule: \n Begin Construction: Fall 2023 \n \n Next Project Name"
        # So searching for "Begin Construction" within 'details' works fine.
        
        # Extract Start Date
        st = None
        st_match = re.search(r'Begin Construction:\s*([A-Za-z0-9\s]+)', details, re.IGNORECASE)
        if st_match:
            st = st_match.group(1).strip()
            
        # Extract Type
        p_type = "capital"
        disaster_kws = ["FEMA", "CalOES", "CalJPIA", "Woolsey", "Disaster", "Fire"]
        
        # Check Name
        if any(kw.lower() in project_name.lower() for kw in disaster_kws):
            p_type = "disaster"
        # Check Details (Topic keywords)
        # But be careful not to match "Disaster" in the header if it leaked?
        # Or checking if keywords appear in the 'Updates' text.
        elif any(kw.lower() in details.lower() for kw in disaster_kws):
            p_type = "disaster"
            
        projects.append({
            "name": project_name,
            "type": p_type,
            "st": st
        })

# Filter and Sum
total_funding = 0
matched_projects = []

for p in projects:
    if p['type'] == 'disaster':
        if p['st'] and '2022' in p['st']:
            # Check if name exists in funding
            # Exact match? Or contains?
            # Start with exact match
            amt = funding_map.get(p['name'])
            if amt is not None:
                total_funding += amt
                matched_projects.append({'name': p['name'], 'amount': amt, 'st': p['st']})
            else:
                # Try stripping extra spaces or substring matching?
                # Maybe the extracted name has punctuation differences.
                pass

print("__RESULT__:")
print(json.dumps({"total_funding": total_funding, "matched_projects": matched_projects}))"""

env_args = {'var_function-call-16563647665074861239': 'file_storage/function-call-16563647665074861239.json', 'var_function-call-13407039906520759084': 'file_storage/function-call-13407039906520759084.json'}

exec(code, env_args)
