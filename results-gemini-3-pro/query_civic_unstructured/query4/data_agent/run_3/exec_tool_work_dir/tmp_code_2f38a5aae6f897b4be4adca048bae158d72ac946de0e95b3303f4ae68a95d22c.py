code = """import json
import re

file_path = locals()['var_function-call-13876112048585230110']
with open(file_path, 'r') as f:
    docs = json.load(f)

projects = []

# Regex for start date
# Look for "Begin Construction: <Date>"
date_pattern = re.compile(r'(Begin Construction|Start Date|Construction Start|Construction Commenced|Construction began|Advertise)[:\s]+([A-Za-z0-9\s,]+)', re.IGNORECASE)
# Note: "Advertise" is usually before construction. The user asked for "Started". 
# The description says "st: Start time/date".
# In the text samples: "Begin Construction: Fall 2023", "Advertise: Fall 2023".
# I will stick to "Begin Construction" or "Construction Start" types.
# Wait, "Latigo Canyon Road Retaining Wall Repair Project ... Advertise: Spring 2023 ... Begin Construction: Summer 2023".
# If I search for "Spring 2022", and it appears in "Advertise", is that "Project Started"?
# Usually "Project Started" means the project *execution* started. But "Design" is also a phase.
# The user asks "How many projects started in Spring 2022".
# "Started" is ambiguous. It could mean "Design Started" or "Construction Started".
# But the hint says "Projects have three statuses: design, completed, not started".
# If a project is in "design", it has started.
# But if the text says "Complete Design: Summer 2023", when did it start?
# The text doesn't always have "Design Start".
# But for "Construction", it explicitly says "Begin Construction".
# Let's assume "Started" means "Begin Construction" OR if the project is in a phase that started in Spring 2022.
# However, the most definitive date is usually the one labeled.
# Let's look for any date matching "Spring 2022" associated with a start-like event.
# "Begin Construction", "Construction began".
# I will also check if there are projects that started *design* in Spring 2022?
# The prompt says "st: Start time/date".
# Let's collect all dates with their labels and then filter.

# Patterns for Spring 2022
spring_2022_patterns = ["spring 2022", "march 2022", "april 2022", "may 2022", "mar 2022", "apr 2022"]

def is_spring_2022(date_str):
    ds = date_str.lower()
    for p in spring_2022_patterns:
        if p in ds:
            return True
    return False

cid_marker = "(cid:190)"

extracted_projects = []

for doc in docs:
    text = doc.get('text', '')
    lines = text.split('\n')
    
    # Identify Start Indices
    project_start_lines = []
    for i in range(len(lines)):
        line = lines[i].strip()
        if not line: continue
        
        # Check if line is a marker or header
        if cid_marker in line: continue
        # Ignore common headers if they appear as potential names
        # But headers usually don't have a marker after them.
        
        # Check ahead for marker
        found_marker = False
        for j in range(i + 1, min(i + 5, len(lines))):
            next_line = lines[j].strip()
            if not next_line: continue
            if cid_marker in next_line and ("Updates" in next_line or "Description" in next_line or "Project" in next_line):
                found_marker = True
            break # Only check the immediate next non-empty line
        
        if found_marker:
            project_start_lines.append(i)
            
    # Extract blocks
    for k in range(len(project_start_lines)):
        start_idx = project_start_lines[k]
        end_idx = project_start_lines[k+1] if k < len(project_start_lines) - 1 else len(lines)
        
        p_name = lines[start_idx].strip()
        p_text = "\n".join(lines[start_idx+1 : end_idx])
        
        # Find all dates
        matches = date_pattern.findall(p_text)
        # matches is list of (label, date_str)
        
        start_date_found = False
        for label, date_str in matches:
            # We are interested in "Begin Construction" or "Construction Start" mostly.
            # But what if the project is "Design" and started design in Spring 2022?
            # The text often lists "Complete Design". It rarely lists "Begin Design".
            # If the user says "How many projects started in Spring 2022", and the project says "Begin Construction: Spring 2022", that's a match.
            # If it says "Advertise: Spring 2022", implies construction is later.
            # I will count a project if "Begin Construction" (or equivalent) is in Spring 2022.
            # I will exclude "Advertise" or "Complete Design".
            
            label_lower = label.lower()
            if "construction" in label_lower and ("begin" in label_lower or "start" in label_lower or "commenced" in label_lower):
                 if is_spring_2022(date_str):
                     start_date_found = True
            
        if start_date_found:
            extracted_projects.append(p_name)

print("__RESULT__:")
print(json.dumps(extracted_projects))"""

env_args = {'var_function-call-11551916714829244463': 'file_storage/function-call-11551916714829244463.json', 'var_function-call-11551916714829245086': [{'Funding_ID': '1', 'Project_Name': '2021 Annual Street Maintenance', 'Funding_Source': 'Public-Private Partnership (PPP)', 'Amount': '24000'}, {'Funding_ID': '2', 'Project_Name': '2022 Annual Street Maintenance', 'Funding_Source': 'Government Grant', 'Amount': '45000'}, {'Funding_ID': '3', 'Project_Name': '2022 Morning View Resurfacing & Storm Drain Improvements', 'Funding_Source': 'State Development Grant', 'Amount': '38000'}, {'Funding_ID': '4', 'Project_Name': 'Annual Street Maintenance', 'Funding_Source': 'Corporate Sponsorship', 'Amount': '23000'}, {'Funding_ID': '5', 'Project_Name': 'Birdview Avenue Improvements', 'Funding_Source': 'National Foundation Fund', 'Amount': '79000'}], 'var_function-call-13876112048585230110': 'file_storage/function-call-13876112048585230110.json'}

exec(code, env_args)
