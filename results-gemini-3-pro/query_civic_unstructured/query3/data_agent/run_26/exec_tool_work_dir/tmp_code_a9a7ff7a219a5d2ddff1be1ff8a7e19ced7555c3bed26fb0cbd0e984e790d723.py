code = """import json
import re

# Load data
with open(locals()['var_function-call-12303763025634533980'], 'r') as f:
    funding_data = json.load(f)

with open(locals()['var_function-call-12303763025634534281'], 'r') as f:
    civic_docs = json.load(f)

# Helper to normalize names for matching
def normalize(name):
    return name.lower().strip().replace('’', "'")

# Process Funding Data
# Create a lookup dictionary. Since names in text might match names in funding (or substrings),
# we'll keep the list and search it.
# Also identify funding projects that are explicitly FEMA/Emergency related by name.
funding_projects = []
for entry in funding_data:
    name = entry['Project_Name']
    norm_name = normalize(name)
    is_fema_related = 'fema' in norm_name or 'emergency' in norm_name
    funding_projects.append({
        'original': entry,
        'norm_name': norm_name,
        'is_fema_related': is_fema_related
    })

# Process Civic Docs
extracted_projects = []

# Status mapping based on headers
# Headers in text: "Capital Improvement Projects (Design)", "Capital Improvement Projects (Construction)", "Capital Improvement Projects (Not Started)"
status_map = {
    'design': 'design',
    'construction': 'construction', # Will refine to 'completed' if text says so
    'not started': 'not started'
}

current_section_status = None

# Regex for headers
header_re = re.compile(r"Capital Improvement Projects \((Design|Construction|Not Started)\)", re.IGNORECASE)

# Iterate over docs (assuming potentially multiple, though we only saw one large one in preview)
for doc in civic_docs:
    text = doc['text']
    lines = text.split('\n')
    
    current_project_name = None
    current_project_text = []
    
    for i, line in enumerate(lines):
        line = line.strip()
        if not line:
            continue
            
        # Check for section header
        header_match = header_re.search(line)
        if header_match:
            # Save previous project if exists
            if current_project_name:
                extracted_projects.append({
                    'name': current_project_name,
                    'status_category': current_section_status,
                    'text': "\n".join(current_project_text)
                })
                current_project_name = None
                current_project_text = []
            
            section_type = header_match.group(1).lower()
            current_section_status = status_map.get(section_type, section_type)
            continue
            
        # Heuristic to identify project names:
        # If line is NOT a known key like "Updates:", "Project Schedule:", "Page", "Agenda Item", "Approved by", "To:", "Subject:", "Date"
        # AND we are inside a valid section
        # AND the line is not a bullet point (cid...) although the preview shows (cid:190) before Updates
        # The project name seems to be a standalone line.
        
        # Keywords to skip
        skip_keywords = ["Updates:", "Project Schedule:", "Project Description:", "Page ", "Agenda Item", "To:", "Prepared by:", "Approved by:", "Subject:", "Date prepared:", "Meeting date:", "RECOMMENDED ACTION:", "DISCUSSION:", "Capital Improvement Projects", "item", "commission meeting"]
        
        is_keyword = any(k.lower() in line.lower() for k in skip_keywords)
        is_bullet = line.startswith("(") or line.startswith("\u000c") # form feed
        
        if current_section_status and not is_keyword and not is_bullet and len(line) > 5:
            # Check if it looks like a project name. 
            # In the sample: "2022 Morning View Resurfacing & Storm Drain Improvements"
            # It is followed by "(cid:190) Updates:"
            # So if the NEXT non-empty line starts with "(cid:190)" or "Updates:", this is likely a project name.
            
            # Look ahead
            is_proj_name = False
            for next_line in lines[i+1:]:
                next_line = next_line.strip()
                if not next_line:
                    continue
                if "Updates" in next_line or "Project Description" in next_line or next_line.startswith("(cid"):
                    is_proj_name = True
                break
            
            if is_proj_name:
                # Save previous project
                if current_project_name:
                    extracted_projects.append({
                        'name': current_project_name,
                        'status_category': current_section_status,
                        'text': "\n".join(current_project_text)
                    })
                
                current_project_name = line
                current_project_text = []
                continue

        if current_project_name:
            current_project_text.append(line)

    # Add last project
    if current_project_name:
        extracted_projects.append({
            'name': current_project_name,
            'status_category': current_section_status,
            'text': "\n".join(current_project_text)
        })

# Now filter and match
results = []
matched_funding_indices = set()

for proj in extracted_projects:
    p_name = proj['name']
    p_text = proj['text'].lower()
    p_norm = normalize(p_name)
    
    # Check for FEMA/Emergency in text or name
    is_related = 'fema' in p_text or 'emergency' in p_text or 'fema' in p_norm or 'emergency' in p_norm
    
    # Find funding match
    funding_match = None
    # Try exact match first, then containment
    # Clean project name often doesn't have suffix
    
    for idx, fp in enumerate(funding_projects):
        # Match logic:
        # 1. Exact match of normalized names
        # 2. fp['norm_name'] starts with p_norm (e.g. "Project (FEMA)" starts with "Project")
        # 3. p_norm contains fp['norm_name'] (less likely)
        
        if p_norm == fp['norm_name'] or fp['norm_name'].startswith(p_norm):
             funding_match = fp['original']
             matched_funding_indices.add(idx)
             break
    
    # If not related by text/name, but matched a funding project that IS related (has FEMA in title), then it is related.
    if funding_match:
        f_name_norm = normalize(funding_match['Project_Name'])
        if 'fema' in f_name_norm or 'emergency' in f_name_norm:
            is_related = True
            
    if is_related:
        # Determine status
        status = proj['status_category']
        if status == 'construction':
            if 'completed' in p_text and 'construction was completed' in p_text:
                status = 'completed'
            elif 'under construction' in p_text:
                status = 'design' # The hint implies "completed" or "design" or "not started". Active construction might be lumped into "design" (ongoing) or handled separately. I'll output "under construction" to be safe, or just "design". Let's output "Construction" as extracted, it's more informative. Or mapped?
                # Hint: "Projects have three statuses: 'design', 'completed', and 'not started'".
                # If I must output one of the 3, "design" (in planning/design phase) fits "active/ongoing" better than "not started" or "completed".
                # But "Construction" is a distinct phase. 
                # Let's leave it as "Construction" but note the hint. Actually, maybe "completed" if finished.
                # Let's check the text for completion.
                pass
        
        results.append({
            'Project_Name': p_name,
            'Funding_Source': funding_match['Funding_Source'] if funding_match else None,
            'Amount': funding_match['Amount'] if funding_match else None,
            'Status': status,
            'match_source': 'text_extraction'
        })

# Also include projects from funding that are FEMA/Emergency related but NOT found in text?
# The user wants "statuses". If not in text, status is unknown.
# But maybe I should list them with status "Unknown" or "not started" (default)?
# The prompt implies we need to read docs to extract info.
# I will add them if they are definitely relevant.

for idx, fp in enumerate(funding_projects):
    if idx not in matched_funding_indices and fp['is_fema_related']:
        results.append({
            'Project_Name': fp['original']['Project_Name'],
            'Funding_Source': fp['original']['Funding_Source'],
            'Amount': fp['original']['Amount'],
            'Status': 'Unknown', # Not found in agenda status report
            'match_source': 'funding_only'
        })

print("__RESULT__:")
print(json.dumps(results))"""

env_args = {'var_function-call-16622059259501542198': ['Funding'], 'var_function-call-16622059259501542215': ['civic_docs'], 'var_function-call-3040997018406236735': 'file_storage/function-call-3040997018406236735.json', 'var_function-call-3040997018406238616': [{'Funding_ID': '1', 'Project_Name': '2021 Annual Street Maintenance', 'Funding_Source': 'Public-Private Partnership (PPP)', 'Amount': '24000'}, {'Funding_ID': '2', 'Project_Name': '2022 Annual Street Maintenance', 'Funding_Source': 'Government Grant', 'Amount': '45000'}, {'Funding_ID': '3', 'Project_Name': '2022 Morning View Resurfacing & Storm Drain Improvements', 'Funding_Source': 'State Development Grant', 'Amount': '38000'}, {'Funding_ID': '4', 'Project_Name': 'Annual Street Maintenance', 'Funding_Source': 'Corporate Sponsorship', 'Amount': '23000'}, {'Funding_ID': '5', 'Project_Name': 'Birdview Avenue Improvements', 'Funding_Source': 'National Foundation Fund', 'Amount': '79000'}], 'var_function-call-12303763025634533980': 'file_storage/function-call-12303763025634533980.json', 'var_function-call-12303763025634534281': 'file_storage/function-call-12303763025634534281.json'}

exec(code, env_args)
