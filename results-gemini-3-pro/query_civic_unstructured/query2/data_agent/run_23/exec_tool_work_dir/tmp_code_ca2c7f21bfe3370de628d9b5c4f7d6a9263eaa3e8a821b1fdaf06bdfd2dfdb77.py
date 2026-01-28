code = """import json
import re

# Load data
with open(locals()['var_function-call-17402731764388360423'], 'r') as f:
    civic_docs = json.load(f)

with open(locals()['var_function-call-17402731764388360612'], 'r') as f:
    funding_data = json.load(f)

funding_dict = {}
for row in funding_data:
    p_name = row['Project_Name'].strip()
    # Normalize spaces
    p_name = " ".join(p_name.split())
    if p_name not in funding_dict:
        funding_dict[p_name] = 0
    funding_dict[p_name] += row['Amount']

# Keywords
topics_kw = ["park", "road", "fema", "fire", "emergency", "drainage", "storm", "highway", "bridge", "playground", "water", "guardrail"]

extracted_projects = []

for doc in civic_docs:
    text = doc['text']
    lines = [l.strip() for l in text.split('\n') if l.strip()]
    
    i = 0
    while i < len(lines):
        line = lines[i]
        
        # Identify Potential Project Name
        # Heuristic: Followed by "Updates" or "Project Description" or "Project Schedule" within next few lines
        # And implies it's a header.
        
        is_header = True
        # Exclude common headers
        if "Agenda" in line or "Page" in line or line.startswith('('):
            is_header = False
        if "Capital Improvement Projects" in line:
            is_header = False
            
        is_project = False
        if is_header:
            # Look ahead
            for k in range(1, 6):
                if i + k < len(lines):
                    next_l = lines[i+k]
                    if any(x in next_l for x in ["Updates:", "Project Description:", "Project Schedule:", "Estimated Schedule:"]):
                        is_project = True
                        break
        
        if is_project:
            p_name = line
            p_name_clean = " ".join(p_name.split())
            
            # Extract block
            block_lines = []
            j = i + 1
            while j < len(lines):
                nl = lines[j]
                # Check if nl is start of next project
                # reusing the heuristic: is it a header followed by indicators?
                is_next_proj = False
                if not ("Agenda" in nl or "Page" in nl or nl.startswith('(') or "Capital Improvement Projects" in nl):
                     for m in range(1, 6):
                        if j + m < len(lines):
                            nnl = lines[j+m]
                            if any(x in nnl for x in ["Updates:", "Project Description:", "Project Schedule:", "Estimated Schedule:"]):
                                is_next_proj = True
                                break
                
                if is_next_proj:
                    break
                
                block_lines.append(nl)
                j += 1
            
            block_text = " ".join(block_lines)
            
            # Check conditions
            # 1. Park related
            is_park = "park" in p_name_clean.lower() or "park" in block_text.lower()
            
            # 2. Completed
            is_completed = "completed" in block_text.lower()
            
            # 3. Date 2022
            is_2022 = False
            if is_completed:
                # Look for completion date
                # We want "completed ... 2022"
                # Let's split into sentences or phrases by bullets
                # The text uses (cid:190) and (cid:131) as bullets, but they are characters.
                # Regex to find "completed" and "2022" in close proximity.
                # Or simply: if "completed" and "2022" appear in the same sentence/line segment.
                
                # Let's check segments separated by newlines or periods
                segments = re.split(r'[.|:]', block_text) # Split by period or colon
                for seg in segments:
                    if "completed" in seg.lower() and "2022" in seg:
                        is_2022 = True
                        break
            
            if is_park and is_completed and is_2022:
                extracted_projects.append(p_name_clean)
            
            i = j # Advance outer loop
        else:
            i += 1

# Match with funding
total_amount = 0
matches = []

for p_name in extracted_projects:
    # Try exact match
    if p_name in funding_dict:
        total_amount += funding_dict[p_name]
        matches.append({"name": p_name, "amount": funding_dict[p_name]})
    else:
        # Debug: check for near matches?
        # Maybe suffix issues?
        pass

print("__RESULT__:")
print(json.dumps({"matches": matches, "total_funding": total_amount}))"""

env_args = {'var_function-call-17402731764388360423': 'file_storage/function-call-17402731764388360423.json', 'var_function-call-17402731764388360612': 'file_storage/function-call-17402731764388360612.json'}

exec(code, env_args)
