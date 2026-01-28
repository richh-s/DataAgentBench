code = """import json
import re

# Load data
with open(locals()['var_function-call-16869852261944468410'], 'r') as f:
    civic_docs = json.load(f)

with open(locals()['var_function-call-2108232826166806416'], 'r') as f:
    funding_data = json.load(f)

projects = []

for doc in civic_docs:
    text = doc['text']
    
    # Identify sections
    # Using single quotes for regex strings
    sections = [
        ("design", re.search(r'Capital Improvement Projects \(Design\)', text)),
        ("construction", re.search(r'Capital Improvement Projects \(Construction\)', text)),
        ("not_started", re.search(r'Capital Improvement Projects \(Not Started\)', text))
    ]
    sections = sorted([s for s in sections if s[1]], key=lambda x: x[1].start())
    
    for i in range(len(sections)):
        status, match = sections[i]
        start = match.end()
        end = sections[i+1][1].start() if i+1 < len(sections) else len(text)
        section_text = text[start:end]
        
        # Regex to find projects
        # Escaping backslashes: \\n in python string is \n. In regex r'\n' matches newline.
        # Pattern: Newline, Newline, Name, Newline, Newline, (cid:190), space, Updates/Description
        pattern = r'\n\n(?P<name>[^\n]+)\n\n\(cid:190\) (?:Updates|Project Description|Project Updates)'
        
        project_iter = re.finditer(pattern, section_text)
        found_projects = list(project_iter)
        
        for j, proj_match in enumerate(found_projects):
            p_name = proj_match.group("name").strip()
            p_start = proj_match.start()
            p_end = found_projects[j+1].start() if j+1 < len(found_projects) else len(section_text)
            p_text = section_text[p_start:p_end]
            
            final_status = status
            p_text_lower = p_text.lower()
            
            if status == "construction":
                if "construction was completed" in p_text_lower or "notice of completion" in p_text_lower:
                    final_status = "completed"
                elif "completed" in p_text_lower and "under construction" not in p_text_lower:
                     # Heuristic: if it says "completed" and not "under construction", it's likely completed.
                     final_status = "completed"
                elif "under construction" in p_text_lower:
                     final_status = "construction"
            
            projects.append({
                "Project_Name": p_name,
                "text": p_text,
                "status": final_status
            })

# Filter and Join
final_results = []
keywords = ['emergency', 'fema']

for p in projects:
    p_name = p['Project_Name']
    p_text_lower = p['text'].lower()
    p_name_lower = p_name.lower()
    
    is_relevant = any(k in p_name_lower for k in keywords) or any(k in p_text_lower for k in keywords)
    
    # Find funding
    p_funding = []
    has_fema_funding = False
    
    for f in funding_data:
        f_name = f['Project_Name']
        f_name_lower = f_name.lower()
        
        # Check matching
        match = False
        if f_name_lower == p_name_lower:
            match = True
        elif f_name_lower.startswith(p_name_lower):
            match = True
        elif p_name_lower.startswith(f_name_lower):
             # Only match if the length difference is small or sensible?
             # e.g. "Project X" matches "Project X"
             match = True
             
        if match:
            p_funding.append(f)
            if 'fema' in f_name_lower or 'emergency' in f_name_lower:
                has_fema_funding = True
    
    if is_relevant or has_fema_funding:
        if not p_funding:
            final_results.append({
                "Project_Name": p_name,
                "Funding_Source": None,
                "Amount": None,
                "Status": p['status']
            })
        else:
            for pf in p_funding:
                final_results.append({
                    "Project_Name": pf['Project_Name'],
                    "Funding_Source": pf['Funding_Source'],
                    "Amount": pf['Amount'],
                    "Status": p['status']
                })

print("__RESULT__:")
print(json.dumps(final_results, indent=2))"""

env_args = {'var_function-call-4927192058268625758': ['civic_docs'], 'var_function-call-4927192058268625809': ['Funding'], 'var_function-call-2108232826166805977': 'file_storage/function-call-2108232826166805977.json', 'var_function-call-2108232826166806416': 'file_storage/function-call-2108232826166806416.json', 'var_function-call-16869852261944468410': 'file_storage/function-call-16869852261944468410.json'}

exec(code, env_args)
