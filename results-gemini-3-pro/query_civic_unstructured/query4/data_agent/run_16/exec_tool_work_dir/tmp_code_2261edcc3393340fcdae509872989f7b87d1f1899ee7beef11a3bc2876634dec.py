code = """import json
import re

# Load the data
with open(locals()['var_function-call-11024242700101333530'], 'r') as f:
    civic_docs = json.load(f)

with open(locals()['var_function-call-4323330023283925201'], 'r') as f:
    funding_data = json.load(f)

# Helper to normalize project names for funding
# Suffixes to ignore for matching
suffixes = [
    r"\(FEMA Project\)", r"\(CalJPIA Project\)", r"\(CalOES Project\)",
    r"\(FEMA/CalOES Project\)", r"\(FEMA\)", r"\(CalJPIA\)", r"\(CalOES\)"
]

funding_map = {}
for entry in funding_data:
    name = entry['Project_Name']
    amount = float(entry['Amount'])
    
    # Normalize name: remove suffixes to aggregate funding under the base name
    # We will also keep the exact name just in case
    # Strategy: store all funding, and when we find a project name in text, 
    # we look for it and its variations in this list.
    pass

# Better approach: 
# Create a dictionary of {Project_Name: Amount} (exact matches)
# And maybe a normalized one.
# Let's just list the project names found in text first.

found_projects = []

# Regex for Spring 2022
spring_2022_regex = re.compile(r"(Spring 2022|March 2022|April 2022|May 2022)", re.IGNORECASE)

def extract_project_info(text):
    # Split by double newlines or headers to find blocks
    # This is tricky because the format is unstructured.
    # We rely on "(cid:190) Updates:" to identify a project block is ending/middle, and the name is before it.
    
    # Split text by (cid:190) which seems to be a bullet point character.
    # Actually, looking at the text: 
    # "Project Name\n\n(cid:190) Updates:"
    
    # Let's find all indices of "(cid:190) Updates:"
    updates_markers = [m.start() for m in re.finditer(r"\(cid:190\) Updates:", text)]
    if not updates_markers:
        return []
        
    projects = []
    
    # Also find indices of Project Descriptions if any
    desc_markers = [m.start() for m in re.finditer(r"\(cid:190\) Project Description:", text)]
    
    all_markers = sorted(updates_markers + desc_markers)
    
    # The start of the text is not necessarily a project.
    # We need to find the project name before the marker.
    # We can look backwards from the marker to the previous double newline or section header.
    
    section_headers = [
        "Capital Improvement Projects (Design)",
        "Capital Improvement Projects (Construction)",
        "Capital Improvement Projects (Not Started)",
        "Discussion",
        "Public Works Commission",
        "Agenda Report",
        "Subject:",
        "RECOMMENDED ACTION:",
        "DISCUSSION:"
    ]
    
    for i, marker in enumerate(all_markers):
        # Determine start of this block
        # It's the end of the previous block + some content, or start of file.
        # But we want the Project Name.
        # Look backwards from marker.
        
        # Extract text before marker to find name
        pre_text = text[:marker].rstrip()
        # Get the last few lines
        lines = pre_text.split('\n')
        
        # Filter out empty lines
        lines = [l.strip() for l in lines if l.strip()]
        
        if not lines:
            continue
            
        # The project name should be the last line(s) before the marker
        # But check if it is a section header
        candidate_name = lines[-1]
        
        # Sometimes name is split across lines? Unlikely for titles.
        # Check against headers
        is_header = False
        for header in section_headers:
            if header in candidate_name:
                is_header = True
                break
        
        if is_header and len(lines) > 1:
            candidate_name = lines[-2] # Try previous line
            
        # Extract the block of text for this project
        # From marker to next marker
        start_idx = marker
        if i < len(all_markers) - 1:
            end_idx = all_markers[i+1]
            # Adjust end_idx to exclude the name of the next project
            # This is hard. Let's just take the text up to the next marker for now.
            # A better heuristic: The next project name is usually just before the next marker.
            # So the content ends before the next project name.
            # However, simpler to just grep the chunk.
            block_text = text[start_idx:end_idx]
        else:
            block_text = text[start_idx:]
            
        # Check for Spring 2022 in this block
        matches = spring_2022_regex.findall(block_text)
        if matches:
            # Find context
            for match in matches:
                # Find the line containing the match
                # regex to find the line
                line_match = re.search(r"([^\n]*" + re.escape(match) + r"[^\n]*)", block_text, re.IGNORECASE)
                if line_match:
                    context = line_match.group(1).strip()
                    projects.append({
                        "name": candidate_name,
                        "context": context,
                        "date": match
                    })
                    
    return projects

all_hits = []
for doc in civic_docs:
    hits = extract_project_info(doc['text'])
    all_hits.extend(hits)

print("__RESULT__:")
print(json.dumps(all_hits))"""

env_args = {'var_function-call-5331130674983609150': 'file_storage/function-call-5331130674983609150.json', 'var_function-call-5331130674983611055': [{'Funding_ID': '1', 'Project_Name': '2021 Annual Street Maintenance', 'Funding_Source': 'Public-Private Partnership (PPP)', 'Amount': '24000'}, {'Funding_ID': '2', 'Project_Name': '2022 Annual Street Maintenance', 'Funding_Source': 'Government Grant', 'Amount': '45000'}, {'Funding_ID': '3', 'Project_Name': '2022 Morning View Resurfacing & Storm Drain Improvements', 'Funding_Source': 'State Development Grant', 'Amount': '38000'}, {'Funding_ID': '4', 'Project_Name': 'Annual Street Maintenance', 'Funding_Source': 'Corporate Sponsorship', 'Amount': '23000'}, {'Funding_ID': '5', 'Project_Name': 'Birdview Avenue Improvements', 'Funding_Source': 'National Foundation Fund', 'Amount': '79000'}], 'var_function-call-11024242700101333530': 'file_storage/function-call-11024242700101333530.json', 'var_function-call-4323330023283925201': 'file_storage/function-call-4323330023283925201.json'}

exec(code, env_args)
