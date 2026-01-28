code = """import json
import re

# Load data
with open(locals()['var_function-call-10057184920144794313'], 'r') as f:
    funding_data = json.load(f)

with open(locals()['var_function-call-10057184920144796126'], 'r') as f:
    civic_docs = json.load(f)

# Combine all text for easier searching (or process per doc to maintain context)
# Processing per doc is safer to avoid cross-project pollution, but projects are distinct.
# However, the structure is repetitive.
# Let's iterate projects and find them in the docs.

qualifying_projects = set()
debug_info = []

for project in funding_data:
    p_name = project['Project_Name']
    p_amount = project['Amount']
    
    # Check if project is park-related
    # Keywords: park, playground
    # Some projects might have 'park' in the name (e.g., "Bluffs Park").
    # The hint says topic field contains keywords. I'll search for keywords in the name first.
    # If not in name, I might need to check the text description, but usually name is descriptive.
    # Let's check name first.
    is_park = False
    if re.search(r'\bpark\b|\bplayground\b', p_name, re.IGNORECASE):
        is_park = True
    
    # If not in name, search in text? 
    # The prompt says "For each project mentioned, you may need to extract: topic..."
    # I'll rely on name for now, and if I find the project in text, I'll check immediate context for "park".
    
    # Search for project in docs
    found_in_docs = False
    completed_in_2022 = False
    
    for doc in civic_docs:
        text = doc['text']
        # Simple string find
        idx = text.find(p_name)
        if idx != -1:
            found_in_docs = True
            # Extract context: from name occurrence to next double newline or next project header
            # Let's take a chunk of 500 chars
            context = text[idx:idx+1000]
            
            # Check for park topic in context if not in name
            if not is_park:
                if re.search(r'\bpark\b|\bplayground\b', context, re.IGNORECASE):
                    # Be careful, context might contain "legacy park" referring to location.
                    # But the prompt implies "park-related projects".
                    # Let's just flag it for now.
                    pass
            
            # Check completion status in 2022
            # Look for specific phrases
            # "Construction was completed .* 2022"
            # "Complete Construction: .* 2022"
            # "completed .* 2022" (risky, might match "completed design 2022")
            
            # Safer regexes
            construction_completed_re = re.compile(r'(construction\s+was\s+completed|complete\s+construction)[:\s]+.*?2022', re.IGNORECASE)
            
            # Also check for "completed" status in a general way if specific phrase missing
            # But the preview shows "Construction was completed November 2022".
            
            if construction_completed_re.search(context):
                completed_in_2022 = True
                
            # Exclude if it says "Complete Design: ... 2022"
            # The regex above requires "construction" keyword, so it should be safe.
            
            if completed_in_2022:
                break
    
    if is_park and completed_in_2022:
        qualifying_projects.add((p_name, int(p_amount)))
        debug_info.append(f"Match: {p_name}, Amount: {p_amount}")

total_funding = sum(amount for _, amount in qualifying_projects)

print("__RESULT__:")
print(json.dumps({"total_funding": total_funding, "projects": list(qualifying_projects), "debug": debug_info}))"""

env_args = {'var_function-call-10057184920144794313': 'file_storage/function-call-10057184920144794313.json', 'var_function-call-10057184920144796126': 'file_storage/function-call-10057184920144796126.json'}

exec(code, env_args)
