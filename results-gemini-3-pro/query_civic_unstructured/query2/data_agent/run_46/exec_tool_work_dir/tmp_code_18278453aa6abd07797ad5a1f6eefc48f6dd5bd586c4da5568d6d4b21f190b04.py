code = """import json
import re

# Load funding data
with open(locals()['var_function-call-14713834321312381364'], 'r') as f:
    funding_data = json.load(f)

# Load civic docs
with open(locals()['var_function-call-14713834321312381855'], 'r') as f:
    civic_docs = json.load(f)

# Combine all text from civic docs
full_text = " ".join([doc.get('text', '') for doc in civic_docs])

# Helper to identify park projects by name
def is_park_project(name):
    keywords = ['park', 'playground', 'recreation', 'open space', 'skate']
    return any(k in name.lower() for k in keywords)

matched_projects = []
total_funding = 0

for project in funding_data:
    p_name = project['Project_Name']
    p_amount = project['Amount']
    
    if not is_park_project(p_name):
        continue
        
    # Search in text for project name
    # We use finditer to handle multiple occurrences
    starts = [m.start() for m in re.finditer(re.escape(p_name), full_text)]
    
    completed_2022 = False
    
    for start in starts:
        # Get chunk
        chunk = full_text[start:start+1000]
        chunk_lower = chunk.lower()
        
        # Check conditions
        # "Construction was completed" AND "2022"
        # "Construction completed" AND "2022"
        # "Project completed" AND "2022"
        
        if "completed" in chunk_lower and "2022" in chunk_lower:
            # Check proximity and context
            # We want to avoid "Design completed in 2022" if the project itself isn't done.
            # But typically "Construction was completed" is the phrasing for finished projects.
            
            if "construction was completed" in chunk_lower:
                # Check if 2022 follows
                idx = chunk_lower.find("construction was completed")
                snippet = chunk_lower[idx:idx+100]
                if "2022" in snippet:
                    completed_2022 = True
                    break
            
            # Fallback: just "completed" and "2022" but not "design"
            # This is risky, let's stick to strong signals first.
            # The preview showed: "Construction was completed, November 2022"
            
            if "construction completed" in chunk_lower:
                 idx = chunk_lower.find("construction completed")
                 snippet = chunk_lower[idx:idx+100]
                 if "2022" in snippet:
                     completed_2022 = True
                     break
            
            # What if "Notice of completion filed January 2023" and "completed November 2022"
            if "completed" in chunk_lower and "november 2022" in chunk_lower:
                # Likely match
                 completed_2022 = True
                 break

    if completed_2022:
        matched_projects.append(project)
        total_funding += int(p_amount)

print("__RESULT__:")
print(json.dumps({"matched_projects": [p['Project_Name'] for p in matched_projects], "total_funding": total_funding}))"""

env_args = {'var_function-call-14713834321312381364': 'file_storage/function-call-14713834321312381364.json', 'var_function-call-14713834321312381855': 'file_storage/function-call-14713834321312381855.json'}

exec(code, env_args)
