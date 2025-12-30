code = """import json
import re

# Load data
with open(locals()['var_function-call-16869852261944468410'], 'r') as f:
    civic_docs = json.load(f)

with open(locals()['var_function-call-2108232826166806416'], 'r') as f:
    funding_data = json.load(f)

projects = []

# Process civic docs
for doc in civic_docs:
    text = doc['text']
    
    # Identify sections
    sections = [
        ("design", re.search(r"Capital Improvement Projects \(Design\)", text)),
        ("construction", re.search(r"Capital Improvement Projects \(Construction\)", text)),
        ("not_started", re.search(r"Capital Improvement Projects \(Not Started\)", text))
    ]
    # Sort sections by position
    sections = sorted([s for s in sections if s[1]], key=lambda x: x[1].start())
    
    # Define boundaries
    for i in range(len(sections)):
        status, match = sections[i]
        start = match.end()
        end = sections[i+1][1].start() if i+1 < len(sections) else len(text)
        section_text = text[start:end]
        
        # Parse projects within section
        # Pattern: Project Name followed by (cid:190) Updates or Project Description
        # We capture the Name
        # Note: Name might be multiple lines? usually one.
        # Looking at preview: "2022 Morning View ... \n\n(cid:190) Updates:"
        # Regex to find the start of a project entry
        project_iter = re.finditer(r"\n\n(?P<name>[^\n]+)\n\n\(cid:190\) (?:Updates|Project Description|Project Updates)", section_text)
        
        found_projects = list(project_iter)
        
        for j, proj_match in enumerate(found_projects):
            p_name = proj_match.group("name").strip()
            p_start = proj_match.start()
            # End is start of next project or end of section
            p_end = found_projects[j+1].start() if j+1 < len(found_projects) else len(section_text)
            p_text = section_text[p_start:p_end]
            
            # Determine Status
            final_status = status # Default from section
            if status == "construction":
                # Check for "completed"
                if "completed" in p_text.lower() and "under construction" not in p_text.lower():
                     # Check context of completed. "Construction was completed"
                     if re.search(r"completed", p_text, re.IGNORECASE):
                         final_status = "completed"
                elif "notice of completion" in p_text.lower():
                     final_status = "completed"
                elif "under construction" in p_text.lower():
                     final_status = "construction" # or keep as construction
            
            # Refine status strings to match hint? Hint: "design", "completed", "not started"
            # If I found "construction", I will keep it as is or map to "design" if required? 
            # I'll stick to: design, construction, completed, not started.
            
            projects.append({
                "Project_Name": p_name,
                "text": p_text,
                "status": final_status,
                "extracted_from_doc": True
            })

# Filter for FEMA/Emergency
relevant_projects = []
keywords = ['emergency', 'fema']

for p in projects:
    is_relevant = False
    # Check name
    if any(k in p['Project_Name'].lower() for k in keywords):
        is_relevant = True
    # Check text/topic
    elif any(k in p['text'].lower() for k in keywords):
        is_relevant = True
    
    if is_relevant:
        p['relevant'] = True
        relevant_projects.append(p)
    else:
        # We might still need it if Funding name has FEMA matches
        p['relevant'] = False

# Join with Funding
# Strategy: Iterate all projects. If relevant or matches a FEMA funding, include.
final_results = []

# Helper to normalize names
def norm(s):
    return s.lower().strip()

# Create a lookup for funding? No, fuzzy match needed.
# But we can iterate.

for p in projects:
    p_name = p['Project_Name']
    p_norm = norm(p_name)
    
    # Find funding
    p_funding = []
    has_fema_funding = False
    
    for f in funding_data:
        f_name = f['Project_Name']
        f_norm = norm(f_name)
        
        # Match logic
        # 1. Exact match (insensitive)
        # 2. f_name starts with p_name (e.g. "Project X (FEMA)")
        # 3. p_name starts with f_name (unlikely but possible)
        
        match = False
        if f_norm == p_norm:
            match = True
        elif f_norm.startswith(p_norm):
            match = True
        elif p_norm.startswith(f_norm):
            match = True
            
        if match:
            p_funding.append(f)
            if 'fema' in f_norm or 'emergency' in f_norm:
                has_fema_funding = True
    
    # Check relevance
    if p.get('relevant') or has_fema_funding:
        # This project is relevant
        # Combine info
        # Consolidate funding info
        # Format: Project Name, Funding Sources (list), Amounts (list or sum?), Status
        
        # User asks: "project names, funding sources, amounts, and statuses"
        # I will output one record per project, with list of sources/amounts? 
        # Or one record per funding source? 
        # "What are the project names, funding sources, amounts, and statuses..." usually implies a table.
        # I'll provide a list of dicts.
        
        if not p_funding:
            # Relevant by text, but no funding found?
            # Include it with None/0
            final_results.append({
                "Project_Name": p_name,
                "Funding_Source": None,
                "Amount": None,
                "Status": p['status']
            })
        else:
            for pf in p_funding:
                final_results.append({
                    "Project_Name": pf['Project_Name'], # Use the specific name from funding or generic? User might want the specific funding details.
                    # Actually, if I have "Project A" and funding "Project A (FEMA)", I should list "Project A (FEMA)" as the name for that row?
                    # Or group by project? 
                    # "Project names... funding sources, amounts..."
                    # Let's output the funding record's project name to be precise, and the status from the doc.
                    "Funding_Source": pf['Funding_Source'],
                    "Amount": pf['Amount'],
                    "Status": p['status']
                })

# There might be projects in Funding that are FEMA related but not in Docs?
# The prompt says "Read the civic documents... to extract project information... Join".
# So I should only return projects found in docs (or linked to them).
# I will stick to `final_results`.

print("__RESULT__:")
print(json.dumps(final_results, indent=2))"""

env_args = {'var_function-call-4927192058268625758': ['civic_docs'], 'var_function-call-4927192058268625809': ['Funding'], 'var_function-call-2108232826166805977': 'file_storage/function-call-2108232826166805977.json', 'var_function-call-2108232826166806416': 'file_storage/function-call-2108232826166806416.json', 'var_function-call-16869852261944468410': 'file_storage/function-call-16869852261944468410.json'}

exec(code, env_args)
