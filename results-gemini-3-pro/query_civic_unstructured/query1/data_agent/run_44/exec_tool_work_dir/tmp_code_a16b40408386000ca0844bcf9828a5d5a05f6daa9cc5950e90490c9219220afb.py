code = """import json
import pandas as pd

# Load funding data
funding_file = locals()['var_function-call-6902551004111180448']
with open(funding_file, 'r') as f:
    funding_data = json.load(f)
df_funding = pd.DataFrame(funding_data)
# Filter for > 50000 just in case the query didn't do it (it did, but good to ensure)
df_funding['Amount'] = df_funding['Amount'].astype(int)
high_funding_projects = df_funding[df_funding['Amount'] > 50000]['Project_Name'].tolist()

# Load civic docs
civic_file = locals()['var_function-call-6902551004111182541']
with open(civic_file, 'r') as f:
    civic_data = json.load(f)

# Find the document with the latest date (03222023)
target_doc = None
for doc in civic_data:
    if "03222023" in doc['filename']:
        target_doc = doc
        break

if not target_doc:
    # Fallback to the first one if not found (though we saw it in preview)
    target_doc = civic_data[0]

text = target_doc['text']

# Parsing logic
lines = text.split('\n')
design_projects = []
in_design_section = False
buffer_line = None

# Markers that indicate the start of a project block (the line BEFORE is the name)
block_markers = ["(cid:190) Updates:", "(cid:190) Project Description:", "Updates:", "Project Description:"]

# Section markers
design_header = "Capital Improvement Projects (Design)"
next_headers = ["Capital Improvement Projects (Construction)", "Capital Improvement Projects (Not Started)", "Disaster Recovery Projects"]

for i, line in enumerate(lines):
    line = line.strip()
    if not line:
        continue
    
    if design_header in line:
        in_design_section = True
        continue
    
    # Check if we are leaving the section
    if in_design_section:
        for header in next_headers:
            if header in line:
                in_design_section = False
                break
        if not in_design_section:
            break
            
        # Identifying project names
        # Logic: If current line is a marker, the previous non-empty line was the project name
        is_marker = False
        for marker in block_markers:
            if line.startswith(marker):
                is_marker = True
                break
        
        if is_marker:
            if buffer_line:
                # buffer_line is the project name
                # Clean up name?
                name = buffer_line.strip()
                # Exclude if it's a page number or artifacts
                if "Page" not in name and "Agenda Item" not in name:
                     design_projects.append(name)
                buffer_line = None # Consumed
        else:
            # This line might be a project name or part of the content if we missed a marker
            # But the structure is Name -> Marker -> Content
            # So we store this line as a candidate.
            # If the next relevant line is a marker, this was the name.
            # If the next relevant line is NOT a marker (e.g. another name or content), 
            # then the previous buffer_line was probably not a project name (or we missed something).
            # But in this list format, Names are followed by Updates/Desc.
            buffer_line = line

# Deduplicate found projects
design_projects = sorted(list(set(design_projects)))

# Find intersection
matches = []
for proj in design_projects:
    if proj in high_funding_projects:
        matches.append(proj)
    else:
        # Try simple normalization if exact match fails
        # e.g. "Project Name" vs "Project Name (FEMA)"? 
        # But SQLite names have suffixes. The doc names might not.
        # Or doc names might have suffixes.
        # Let's check if proj is a substring of any high_funding_project or vice versa
        pass

print("__RESULT__:")
print(json.dumps({
    "design_projects_extracted": design_projects,
    "high_funding_projects_count": len(high_funding_projects),
    "matches": matches,
    "match_count": len(matches)
}))"""

env_args = {'var_function-call-12023591803711719665': ['Funding'], 'var_function-call-12023591803711719498': ['civic_docs'], 'var_function-call-6902551004111180448': 'file_storage/function-call-6902551004111180448.json', 'var_function-call-6902551004111182541': 'file_storage/function-call-6902551004111182541.json', 'var_function-call-17629615109180015549': 'file_storage/function-call-17629615109180015549.json', 'var_function-call-13245772916019581985': [{'_id': '694eef5c4ec675b6b5f5a285', 'filename': 'malibucity_agenda_03222023-2060.txt'}, {'_id': '694eef5c4ec675b6b5f5a286', 'filename': 'malibucity_agenda__01262022-1835.txt'}, {'_id': '694eef5c4ec675b6b5f5a287', 'filename': 'malibucity_agenda__01272021-1626.txt'}, {'_id': '694eef5c4ec675b6b5f5a288', 'filename': 'malibucity_agenda__03022021-1648.txt'}, {'_id': '694eef5c4ec675b6b5f5a289', 'filename': 'malibucity_agenda__03232022-1869.txt'}]}

exec(code, env_args)
