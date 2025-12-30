code = """import json
import re

# Load data
funding_records = []
try:
    with open(locals()['var_function-call-6082162408351623791'], 'r') as f:
        funding_records = json.load(f)
except:
    funding_records = locals()['var_function-call-6082162408351623791']

civic_docs = []
try:
    with open(locals()['var_function-call-12699093529231824248'], 'r') as f:
        civic_docs = json.load(f)
except:
    civic_docs = locals()['var_function-call-12699093529231824248']

# Helper to normalize/extract base name
def get_base_name(name):
    # Remove specific suffixes mentioned in hints or observed
    # Suffixes: (FEMA Project), (CalJPIA Project), (CalOES Project), (FEMA/CalOES Project), (FEMA)
    # Also general (...) if it looks like a suffix?
    # Let's be specific first based on hint
    name = re.sub(r'\s*\((FEMA|CalJPIA|CalOES|FEMA/CalOES|CalOES/FEMA).*?\)', '', name, flags=re.IGNORECASE)
    name = re.sub(r'\s*\(FEMA\)', '', name, flags=re.IGNORECASE)
    return name.strip()

# Set of all valid project names (full and base) to recognize in text
valid_project_names = set()
for r in funding_records:
    valid_project_names.add(r['Project_Name'])
    valid_project_names.add(get_base_name(r['Project_Name']))

# Parse text
project_status_map = {} # Name -> {status, text}

current_status = "Unknown"
current_project = None

# Combine all text (if multiple docs, though likely one main report)
full_text_lines = []
for doc in civic_docs:
    # Split by newlines
    lines = doc['text'].split('\n')
    for line in lines:
        line = line.strip()
        if not line: continue
        full_text_lines.append(line)

# Iterate lines
# Heuristic for headers: "Capital Improvement Projects (Design)" etc.
status_headers = {
    "Capital Improvement Projects (Design)": "design",
    "Capital Improvement Projects (Construction)": "construction", # Hint says "completed"? No, hint says "design", "completed", "not started".
    # Wait, the text says "Capital Improvement Projects (Construction)".
    # Projects under construction are "active" but distinct from "completed".
    # However, there is also a section "Construction was completed..." under the Construction header?
    # Let's look at text sample:
    # "Capital Improvement Projects (Construction)"
    # ... "Malibu Road Slope Repairs" ... "Updates: Project is currently under construction"
    # ... "Bluffs Park Shade Structure" ... "Updates: Construction was completed November 2022"
    # So "Construction" section contains both under-construction and completed.
    # I need to parse the description to distinguish "completed" from "under construction"?
    # Hint says statuses are "design", "completed", "not started".
    # I should try to detect "completed" in text.
    "Capital Improvement Projects (Not Started)": "not started"
}

# The sample text also has "Capital Improvement Projects (Construction)"
# But individual projects have updates like "Construction was completed..."
# So I should default to "construction" or check text for "completed".
# Wait, if the hint says statuses are "design", "completed", "not started", 
# maybe "construction" maps to something? Or maybe "completed" is the status for finished ones.
# Let's extract raw status from header first, then refine.

for line in full_text_lines:
    # Check for status header
    header_match = None
    for header, status in status_headers.items():
        if header.lower() in line.lower():
            header_match = status
            break
    
    if header_match:
        current_status = header_match
        current_project = None
        continue

    # Check for project name
    # We match against valid_project_names
    # Check exact match or close match?
    if line in valid_project_names:
        current_project = line
        if current_project not in project_status_map:
             project_status_map[current_project] = {'status': current_status, 'text': ''}
        continue
    
    # If inside a project, accumulate text
    if current_project:
        project_status_map[current_project]['text'] += " " + line

# Refine status "construction" -> "completed" if text says so
for proj, data in project_status_map.items():
    if data['status'] == 'construction':
        if 'completed' in data['text'].lower() and 'notice of completion' in data['text'].lower():
             data['status'] = 'completed'
        elif 'completed' in data['text'].lower() and 'construction was completed' in data['text'].lower():
             data['status'] = 'completed'

# Build Result
final_results = []
keywords = ['emergency', 'fema']

for record in funding_records:
    name = record['Project_Name']
    base = get_base_name(name)
    
    # Check relevance
    is_relevant = False
    
    # 1. Name check
    for kw in keywords:
        if kw in name.lower():
            is_relevant = True
            break
    
    # 2. Text check (via base name or full name)
    # Find the corresponding project data
    proj_data = project_status_map.get(name) or project_status_map.get(base)
    
    if proj_data:
        text_content = proj_data['text'].lower()
        for kw in keywords:
            if kw in text_content:
                is_relevant = True
                break
    
    if is_relevant:
        # Determine status
        status = "Unknown"
        if proj_data:
            status = proj_data['status']
        else:
            # If not in text, maybe the name implies something? 
            # Or maybe "Not Started" if we want to default? 
            # But the user asks for status. If unknown, say "Unknown" or infer.
            # However, looking at the sample, "Corral Canyon Culvert Repairs" is in funding but not clearly in the text sample.
            # But the sample is just a "Status Report". It might not list ALL projects.
            # For this task, I'll return "Unknown" or the inferred status from text.
            pass
            
        final_results.append({
            "Project_Name": name,
            "Funding_Source": record['Funding_Source'],
            "Amount": record['Amount'],
            "Status": status
        })

print("__RESULT__:")
print(json.dumps(final_results))"""

env_args = {'var_function-call-6082162408351623791': 'file_storage/function-call-6082162408351623791.json', 'var_function-call-6082162408351624496': 'file_storage/function-call-6082162408351624496.json', 'var_function-call-12699093529231824248': 'file_storage/function-call-12699093529231824248.json'}

exec(code, env_args)
