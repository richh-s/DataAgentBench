code = """import json
import re

# Load funding data
with open(locals()['var_function-call-9362456295631069052']) as f:
    funding_data = json.load(f)

# Get high funding project names
# Filter is already done in SQL, so just take all names
high_funding_projects = {item['Project_Name'] for item in funding_data}

# Load civic docs
with open(locals()['var_function-call-12811906272455444713']) as f:
    docs = json.load(f)

matched_projects = set()

debug_info = []

for doc in docs:
    text = doc.get('text', '')
    if not text:
        continue
        
    # Normalize whitespace to single spaces
    norm_text = re.sub(r'\s+', ' ', text)
    
    # Locate the Capital Design section
    # Header: "Capital Improvement Projects (Design)"
    header = "Capital Improvement Projects (Design)"
    
    start_indices = [m.start() for m in re.finditer(re.escape(header), norm_text, re.IGNORECASE)]
    
    for start_idx in start_indices:
        # Define the search area start
        content_start = start_idx + len(header)
        
        # Determine the end of this section
        # We look for the next major header.
        # Possible next headers based on document structure:
        # "Capital Improvement Projects (Construction)"
        # "Capital Improvement Projects (Not Started)"
        # "Disaster Recovery Projects"
        # "New Projects"
        # Or even "Agenda Item" if it's the last section.
        
        # Let's find the nearest subsequent header
        stoppers = [
            "Capital Improvement Projects (Construction)",
            "Capital Improvement Projects (Not Started)",
            "Disaster Recovery Projects",
            "Agenda Item" # Sometimes acts as a footer/new section
        ]
        
        end_idx = len(norm_text)
        
        for stop in stoppers:
            # Find stopper after content_start
            # Use case insensitive search
            match = re.search(re.escape(stop), norm_text[content_start:], re.IGNORECASE)
            if match:
                stop_idx = content_start + match.start()
                if stop_idx < end_idx:
                    end_idx = stop_idx
        
        section_text = norm_text[content_start:end_idx]
        
        # Check for each high funding project in this section
        for proj in high_funding_projects:
            # Normalize project name
            norm_proj = re.sub(r'\s+', ' ', proj)
            
            # Simple substring match
            # To avoid partial word matches (e.g. matching "Park" in "Parker"), we might want boundaries
            # But "Birdview Avenue Improvements" is long enough.
            # Let's try exact string match first.
            if norm_proj in section_text:
                matched_projects.add(proj)
                # debug_info.append(f"Found '{proj}' in doc {doc.get('filename')} section.")

print("__RESULT__:")
print(json.dumps(len(matched_projects)))"""

env_args = {'var_function-call-9362456295631069052': 'file_storage/function-call-9362456295631069052.json', 'var_function-call-9362456295631066849': 'file_storage/function-call-9362456295631066849.json', 'var_function-call-12811906272455444713': 'file_storage/function-call-12811906272455444713.json'}

exec(code, env_args)
