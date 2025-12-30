code = """import json
import re

# Load Mongo Data
with open(locals()['var_function-call-16563647665074861239'], 'r') as f:
    civic_docs = json.load(f)

# Load Funding Data
with open(locals()['var_function-call-13407039906520759084'], 'r') as f:
    funding_data = json.load(f)

projects = []

# Process each document
for doc in civic_docs:
    text = doc['text']
    
    # Split by the specific marker usually found in the text for updates
    # The preview shows (cid:190) which is unicode \u00be. 
    # Or just "Updates:"
    # Let's normalize the text to make it easier
    text = text.replace('\u00be', '').replace('(cid:190)', '')
    
    # Split into chunks based on "Updates:"
    # Each chunk (except the last one maybe) ends with a project name for the NEXT chunk?
    # No, "Project Name" -> "Updates:" -> "Details"
    # So if we split by "Updates:", the end of the *previous* chunk contains the Project Name of the *current* section.
    
    chunks = re.split(r'Updates:', text)
    
    # The first chunk is header stuff before the first project.
    # The last chunk is the details of the last project.
    
    for i in range(1, len(chunks)):
        # The project name is at the end of chunks[i-1]
        # The details are in chunks[i] (up to the next project name)
        
        # Extract Name
        prev_chunk = chunks[i-1].strip()
        prev_lines = prev_chunk.split('\n')
        
        # Filter out empty lines
        prev_lines = [line.strip() for line in prev_lines if line.strip()]
        
        if not prev_lines:
            continue
            
        # The project name should be the last line, unless it's a multi-line name.
        # But we also need to avoid headers.
        
        # Potential headers to ignore
        ignore_headers = [
            "Capital Improvement Projects (Design)",
            "Capital Improvement Projects (Construction)",
            "Capital Improvement Projects (Not Started)",
            "Disaster Recovery Projects",
            "Public Works Commission",
            "Agenda Report",
            "Item",
            "Subject:",
            "Project Description:",
            "Project Updates:", 
            "Project Schedule:"
        ]
        
        # Iterate backwards to find a valid name line
        name = ""
        for line in reversed(prev_lines):
            if any(header in line for header in ignore_headers):
                continue
            # Also ignore page numbers like "Page 1 of 6" or "Agenda Item"
            if "Page" in line and "of" in line:
                continue
            if "Agenda Item" in line:
                continue
            if "RECOMMENDED ACTION" in line:
                continue
            
            # If line is valid, take it.
            # Sometimes name is split? Let's assume one line for now.
            name = line
            break
        
        if not name:
            continue
            
        # Extract Details from current chunk
        # current chunk goes until the start of next project name.
        # But split by "Updates:" consumed the "Updates:" token.
        # The next project name is at the end of THIS chunk.
        # So the details are at the beginning of THIS chunk.
        # Actually, split by "Updates:" makes:
        # [Header ... Proj1Name] , [ ... details ... Proj2Name] , [ ... details ... Proj3Name]
        # So chunks[i] contains the details of Proj1, followed by Proj2Name.
        # We process chunks[i] to find start date.
        
        details = chunks[i]
        
        # Find "Begin Construction:"
        # Regex for date
        st = None
        match = re.search(r'Begin Construction:\s*([A-Za-z0-9\s]+)', details, re.IGNORECASE)
        if match:
            st = match.group(1).strip()
        
        # Determine Type
        # Check keywords in Name
        p_type = "capital" # Default
        disaster_keywords = ["FEMA", "CalOES", "CalJPIA", "Woolsey", "Disaster", "Fire"]
        if any(kw.lower() in name.lower() for kw in disaster_keywords):
            p_type = "disaster"
            
        projects.append({
            "Project_Name": name,
            "type": p_type,
            "st": st
        })

# Debug: Print found projects to verify extraction
print("__RESULT__:")
print(json.dumps(projects))"""

env_args = {'var_function-call-16563647665074861239': 'file_storage/function-call-16563647665074861239.json', 'var_function-call-13407039906520759084': 'file_storage/function-call-13407039906520759084.json'}

exec(code, env_args)
