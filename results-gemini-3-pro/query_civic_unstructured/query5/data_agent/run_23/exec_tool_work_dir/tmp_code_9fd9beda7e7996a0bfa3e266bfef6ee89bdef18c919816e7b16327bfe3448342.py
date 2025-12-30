code = """import json
import re

# Load data
funding_data = json.load(open(locals()['var_function-call-12490776442151259677']))
civic_docs = json.load(open(locals()['var_function-call-2297309478391290844']))

# Combine all text
full_text = "\n".join([d['text'] for d in civic_docs])

# Parse projects from text
# Strategy: Split by double newlines or identify headers?
# The text looks like: "Project Name\n\n(cid:190) Updates:..."
# We can iterate through the text and find lines that look like project names from our funding list.

# Normalize funding names for matching
# Create a mapping of simplified name to full funding records
funding_map = {}
for f in funding_data:
    name = f['Project_Name']
    # Simplify: remove suffixes like (FEMA Project), (CalOES Project), etc.
    simple_name = re.sub(r'\s*\(.*?\)$', '', name).strip()
    if simple_name not in funding_map:
        funding_map[simple_name] = []
    funding_map[simple_name].append(f)

# Find projects in text
# We will look for each simple_name in the text.
# If found, we extract the context (text following the name until the next likely project header).

found_projects = []

# Get unique simple names to search
search_names = list(funding_map.keys())

# Sort by length descending to match longer names first (avoid partial matches)
search_names.sort(key=len, reverse=True)

# Helper to find start date in text snippet
def check_started_2022(text):
    # Look for "Begin Construction: <Season/Month> 2022"
    # Or "Start Date: ... 2022"
    # Or "Updates: ... began ... 2022"
    
    patterns = [
        r"Begin Construction:.*2022",
        r"Start Date:.*2022",
        r"Construction started.*2022",
        r"Work began.*2022",
        r"Awarded.*contract.*2022", # Start of execution
        r"Advertise:.*2022" # Start of bidding
    ]
    
    for pat in patterns:
        if re.search(pat, text, re.IGNORECASE):
            return True
            
    # Check for "Construction was completed ... 2022".
    # If completed in 2022, did it start in 2022?
    # Maybe check if it says "started and completed in 2022"?
    # For now, exclude "completed" unless it also says "began".
    return False

# Helper to check disaster in text snippet
def check_disaster_text(text):
    keywords = ["FEMA", "CalOES", "Disaster", "Woolsey Fire", "Recovery"]
    for k in keywords:
        if k.lower() in text.lower():
            return True
    return False

total_funding = 0
matched_projects = set()

for name in search_names:
    # Regex to find name as a header (start of line, or following newline)
    # Escape regex characters in name
    escaped_name = re.escape(name)
    # Pattern: Name followed by newline, maybe some chars, then "Updates" or "Project Schedule"
    # Or just Name and we look ahead.
    
    # We find all occurrences.
    # But names might overlap.
    
    matches = list(re.finditer(escaped_name, full_text, re.IGNORECASE))
    
    for match in matches:
        start_idx = match.start()
        # Extract a window of text after the name, say 1000 chars or until next double newline
        window = full_text[start_idx:start_idx+2000]
        
        # Check if this window actually belongs to the project (e.g. followed by "Updates:" or "Project Description:")
        if "Updates:" in window or "Project Description:" in window or "Project Schedule:" in window:
            
            # Analyze this block
            started_2022 = check_started_2022(window)
            
            # Check if text implies disaster
            is_disaster_text = check_disaster_text(window)
            
            # Now link to funding records
            records = funding_map[name]
            
            for rec in records:
                # Determine if this specific record is disaster
                rec_name = rec['Project_Name']
                is_disaster_rec = "FEMA" in rec_name or "CalOES" in rec_name or "Disaster" in rec_name or "CalJPIA" in rec_name
                
                # Combined disaster check
                # If the record is explicitly disaster, or the text context is disaster
                # AND the record name matches the text context (base name)
                
                # Rule:
                # If the project is "Disaster-related":
                # Matches if Rec is disaster OR Text is disaster.
                # However, be careful. "Capital" projects might be in text without FEMA keywords.
                # If the Rec name has FEMA, it is definitely disaster.
                # If the Rec name doesn't, but text says FEMA, maybe the project is disaster funded?
                # The Funding Source in Rec might help.
                # But let's assume if Rec or Text indicates disaster, it qualifies.
                
                is_disaster = is_disaster_rec or is_disaster_text
                
                if is_disaster and started_2022:
                    # Avoid double counting?
                    # If we have multiple text matches for the same project name (e.g. in different docs),
                    # we might add the same funding record multiple times.
                    # We should track processed funding_ids.
                    
                    fid = rec['Funding_ID']
                    if fid not in matched_projects:
                        total_funding += int(rec['Amount'])
                        matched_projects.add(fid)
                        print(f"Matched: {rec_name}, Started 2022, Disaster: {is_disaster}, Amount: {rec['Amount']}")

print("__RESULT__:")
print(json.dumps({"total_funding": total_funding, "matched_count": len(matched_projects)}))"""

env_args = {'var_function-call-12490776442151259677': 'file_storage/function-call-12490776442151259677.json', 'var_function-call-12490776442151257162': 'file_storage/function-call-12490776442151257162.json', 'var_function-call-2297309478391290844': 'file_storage/function-call-2297309478391290844.json'}

exec(code, env_args)
