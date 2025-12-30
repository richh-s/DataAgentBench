code = """import json
import re

# Load the data
with open(locals()['var_function-call-11024242700101333530'], 'r') as f:
    civic_docs = json.load(f)

# Regex for Spring 2022
spring_2022_regex = re.compile(r"(Spring 2022|March 2022|April 2022|May 2022)", re.IGNORECASE)

def extract_project_info(text):
    # Find all indices of "(cid:190) Updates:" or "(cid:190) Project Description:"
    # We will iterate through lines to find these markers
    lines = text.split('\n')
    projects = []
    
    current_project_name = None
    
    # We will look for lines that look like project names.
    # A project name is usually a line that is NOT a bullet point, NOT a known header, and is followed eventually by a marker.
    
    section_headers = [
        "Capital Improvement Projects (Design)",
        "Capital Improvement Projects (Construction)",
        "Capital Improvement Projects (Not Started)",
        "Discussion",
        "Public Works Commission",
        "Agenda Report",
        "Subject:",
        "RECOMMENDED ACTION:",
        "DISCUSSION:",
        "Item",
        "Page ",
        "Agenda Item"
    ]
    
    # A cleaner approach: split text by double newlines to get paragraphs.
    # Identify paragraphs that are project names.
    # Identify paragraphs containing date info.
    
    # Let's use the marker approach again but simpler.
    # Find positions of markers
    markers = []
    for m in re.finditer(r"\(cid:190\) (Updates|Project Description):", text):
        markers.append(m.start())
        
    if not markers:
        return []
        
    for i, marker_start in enumerate(markers):
        # Look backwards for name
        # Slice text up to marker
        pre_text = text[:marker_start].rstrip()
        # Get last non-empty line
        pre_lines = [l.strip() for l in pre_text.split('\n') if l.strip()]
        
        candidate_name = "Unknown"
        if pre_lines:
            candidate_name = pre_lines[-1]
            # Check if it's a header
            for header in section_headers:
                if header in candidate_name or candidate_name.startswith("Page") or "Agenda Item" in candidate_name:
                    if len(pre_lines) > 1:
                        candidate_name = pre_lines[-2]
                    break
        
        # Look forwards for content
        start_content = marker_start
        end_content = markers[i+1] if i < len(markers) - 1 else len(text)
        content = text[start_content:end_content]
        
        # Check for Spring 2022
        matches = spring_2022_regex.findall(content)
        for match in matches:
             # Get context line
             line_match = re.search(r"([^\n]*" + re.escape(match) + r"[^\n]*)", content, re.IGNORECASE)
             context = line_match.group(1).strip() if line_match else ""
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
