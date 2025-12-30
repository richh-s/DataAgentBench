code = """import json

funding_path = locals()['var_function-call-8835626806368298115']
docs_path = locals()['var_function-call-9685015997201823152']

with open(funding_path, 'r') as f:
    funding_records = json.load(f)

with open(docs_path, 'r') as f:
    docs = json.load(f)

full_text = " ".join([d['text'] for d in docs])

total_funding = 0
results = []

for row in funding_records:
    name = row['Project_Name']
    
    # 1. Determine if Disaster Project
    is_disaster = False
    
    # Suffix Check
    suffixes = ["(FEMA", "(CalOES", "(CalJPIA", "(Woolsey"]
    if any(s in name for s in suffixes):
        is_disaster = True
    
    # Base Name for text search
    if "(" in name:
        base_name = name.split("(")[0].strip()
    else:
        base_name = name
        
    # Find in text
    # We look for the base_name.
    # We grab a snippet after it.
    idx = full_text.find(base_name)
    
    snippet = ""
    if idx != -1:
        snippet = full_text[idx:idx+2000] # Grab 2000 chars
    
    # Text-based Type Check (if not already found via suffix)
    # Check if snippet implies disaster
    # E.g. "Disaster Recovery Projects" header above it? 
    # Or keywords "FEMA", "CalOES" in the snippet?
    if not is_disaster and snippet:
        if "FEMA" in snippet or "CalOES" in snippet or "Disaster" in snippet:
             # Be careful, "Disaster" might be in the header "Disaster Recovery Projects"
             # matching "Disaster" keyword might be too broad if it appears in general text.
             # But "FEMA" and "CalOES" are specific.
             if "FEMA" in snippet or "CalOES" in snippet:
                 is_disaster = True
    
    if not is_disaster:
        continue

    # 2. Check Start Date == 2022
    # Look for "Begin Construction: ... 2022" in snippet
    started_2022 = False
    
    if snippet:
        # Simple string search for patterns
        # "Begin Construction: [Month] 2022"
        # "Begin Construction: 2022"
        # "Advertise: ... 2022"? No, advertised is not started.
        # "Start: ... 2022"
        
        # We can look for the "Begin Construction" label and check the immediate following text.
        bc_index = snippet.find("Begin Construction:")
        if bc_index != -1:
            bc_text = snippet[bc_index:bc_index+50] # "Begin Construction: Fall 2022"
            if "2022" in bc_text:
                started_2022 = True
        
        # What if it says "Construction was completed November 2022"?
        # Does that mean it started in 2022? 
        # "Bluffs Park Shade Structure" -> "Construction was completed November 2022."
        # If it was a small project, maybe.
        # But if we stick to "Begin Construction", we are safer.
        # However, looking at the data:
        # "Bluffs Park Shade Structure" (Amount 21000) - Completed Nov 2022. Likely started 2022.
        # "Broad Beach Road..." - Completed Nov 2022.
        # "Point Dume Walkway..." - Completed Nov 2022.
        # These are "Capital" projects in the text example.
        
        # Let's see if any "Disaster" project started in 2022.
        
        # Also check for "Updates: Construction was completed... 2022" 
        # If the project is "Disaster" type, maybe we count it.
        # But strictly "started in 2022".
        
        # Let's include "Begin Construction" checks first.

    if started_2022:
        total_funding += int(row['Amount'])
        results.append(name)

print("__RESULT__:")
print(json.dumps(total_funding))"""

env_args = {'var_function-call-6821876032245033894': ['Funding'], 'var_function-call-8835626806368298115': 'file_storage/function-call-8835626806368298115.json', 'var_function-call-9685015997201823152': 'file_storage/function-call-9685015997201823152.json'}

exec(code, env_args)
