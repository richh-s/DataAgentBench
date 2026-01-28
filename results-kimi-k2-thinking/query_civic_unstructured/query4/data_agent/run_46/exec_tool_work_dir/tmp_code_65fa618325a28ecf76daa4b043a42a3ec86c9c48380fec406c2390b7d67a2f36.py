code = """import json
import re
from datetime import datetime

# Load the complete civic documents data
civic_docs_path = var_functions.query_db:2
with open(civic_docs_path, 'r') as f:
    civic_docs = json.load(f)

# Load the funding data
funding_path = var_functions.query_db:5
with open(funding_path, 'r') as f:
    funding_data = json.load(f)

print(f"Loaded {len(civic_docs)} civic documents and {len(funding_data)} funding records")

# Function to extract projects from text
extracted_projects = []

for doc in civic_docs:
    text = doc.get('text', '')
    filename = doc.get('filename', '')
    
    # Split text into sections to find project information
    # Look for patterns that indicate project sections
    
    # Find capital improvement projects
    capital_patterns = [
        r'Capital Improvement Projects \(Design\)(.*?)(?=Capital Improvement Projects \(Construction\)|Disaster Recovery Projects|Capital Improvement Projects \(Not Started\)|$)',
        r'Capital Improvement Projects \(Construction\)(.*?)(?=Capital Improvement Projects \(Not Started\)|Disaster Recovery Projects|$)',
        r'Capital Improvement Projects \(Not Started\)(.*?)(?=Disaster Recovery Projects|$)'
    ]
    
    # Find disaster recovery projects
    disaster_pattern = r'Disaster Recovery Projects(.*?)$'
    
    for pattern in capital_patterns:
        matches = re.findall(pattern, text, re.DOTALL | re.IGNORECASE)
        for match in matches:
            # Extract individual projects from the section
            # Projects seem to be separated by blank lines and start with project names
            project_blocks = re.split(r'\n\s*\n', match.strip())
            
            for block in project_blocks:
                if block.strip() and len(block.strip()) > 10:  # Skip empty or very short blocks
                    # Try to extract project name (usually the first line)
                    lines = block.strip().split('\n')
                    if lines:
                        project_name = lines[0].strip()
                        # Skip if it's just a category header
                        if project_name and not re.match(r'^(cid:|\u2022|â€¢)', project_name):
                            # Extract status, dates from the block
                            status = None
                            st = None
                            et = None
                            project_type = "capital"
                            
                            # Look for status indicators
                            if "Design" in pattern:
                                status = "design"
                            elif "Construction" in pattern:
                                status = "construction"  # This might map to "completed" or be a separate status
                            elif "Not Started" in pattern:
                                status = "not started"
                            
                            # Look for schedule/date information
                            schedule_match = re.search(r'Project Schedule.*?Complete Design:\s*([^\n]*)', block, re.IGNORECASE)
                            if schedule_match:
                                st = schedule_match.group(1).strip()
                            
                            schedule_match2 = re.search(r'Complete Construction:\s*([^\n]*)', block, re.IGNORECASE)
                            if schedule_match2:
                                et = schedule_match2.group(1).strip()
                            
                            # Better date extraction
                            date_matches = re.findall(r'(?:Complete Design|Advertise|Begin Construction|Complete Construction|Estimated Schedule).*?:\s*([^\n]+)', block, re.IGNORECASE)
                            if date_matches:
                                # The first date is likely the start date
                                if not st:
                                    st = date_matches[0].strip()
                                if len(date_matches) > 1 and not et:
                                    et = date_matches[-1].strip()
                            
                            # Check if this is actually a completed project (should be counted differently)
                            if "completed" in block.lower() or "construction was completed" in block.lower():
                                status = "completed"
                                # Extract completion date
                                comp_match = re.search(r'construction was completed.*?[,\s]+([^,\n]+(?:202\d|2023))', block, re.IGNORECASE)
                                if comp_match:
                                    et = comp_match.group(1).strip()
                            
                            extracted_projects.append({
                                "Project_Name": project_name,
                                "status": status,
                                "st": st,
                                "et": et,
                                "type": project_type,
                                "source_file": filename
                            })
    
    # Look for disaster recovery projects
    disaster_matches = re.findall(disaster_pattern, text, re.DOTALL | re.IGNORECASE)
    for match in disaster_matches:
        project_blocks = re.split(r'\n\s*\n', match.strip())
        
        for block in project_blocks:
            if block.strip() and len(block.strip()) > 10:
                lines = block.strip().split('\n')
                if lines:
                    project_name = lines[0].strip()
                    if project_name and not re.match(r'^(cid:|\u2022|â€¢)', project_name):
                        status = None
                        st = None
                        et = None
                        project_type = "disaster"
                        
                        # Similar date extraction for disaster projects
                        date_matches = re.findall(r'(?:Complete Design|Advertise|Begin Construction|Complete Construction|Estimated Schedule).*?:\s*([^\n]+)', block, re.IGNORECASE)
                        if date_matches:
                            if not st:
                                st = date_matches[0].strip()
                            if len(date_matches) > 1 and not et:
                                et = date_matches[-1].strip()
                        
                        if "completed" in block.lower() or "construction was completed" in block.lower():
                            status = "completed"
                            comp_match = re.search(r'construction was completed.*?[,\s]+([^,\n]+(?:202\d|2023))', block, re.IGNORECASE)
                            if comp_match:
                                et = comp_match.group(1).strip()
                        
                        extracted_projects.append({
                            "Project_Name": project_name,
                            "status": status,
                            "st": st,
                            "et": et,
                            "type": project_type,
                            "source_file": filename
                        })

# Clean up project names
for project in extracted_projects:
    # Remove common prefixes and clean up
    name = project["Project_Name"]
    name = re.sub(r'^(cid:\d+|[\u2022â€¢\-]+\s*)', '', name).strip()
    name = re.sub(r'\s+', ' ', name)
    project["Project_Name"] = name

# Filter out empty or invalid project names
valid_projects = [p for p in extracted_projects if p["Project_Name"] and len(p["Project_Name"]) > 5]

print(f"Extracted {len(valid_projects)} valid projects")

# Display first few projects to verify
for i, p in enumerate(valid_projects[:10]):
    print(f"{i+1}. Name: {p['Project_Name']}")
    print(f"   Status: {p['status']}, Type: {p['type']}")
    print(f"   Start: {p['st']}, End: {p['et']}")
    print()

# Save projects for next steps
project_data = valid_projects
funding_records = funding_data

__RESULT__:
json.dumps({
    "project_count": len(valid_projects),
    "sample_projects": valid_projects[:5]
})"""

env_args = {'var_functions.list_db:0': ['civic_docs'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json'}

exec(code, env_args)
