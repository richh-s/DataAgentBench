code = """import json
import re

# Load data
with open(locals()['var_function-call-1156938048168678441'], 'r') as f:
    funding_data = json.load(f)

with open(locals()['var_function-call-1156938048168679978'], 'r') as f:
    civic_docs = json.load(f)

# Create a map of project name to funding info
project_funding = {}
for item in funding_data:
    project_funding[item['Project_Name']] = item

# List of all project names to search for
# Sort by length descending to match longest names first (to avoid partial matches of substrings)
all_project_names = sorted(project_funding.keys(), key=len, reverse=True)

# Function to check relevance
def is_relevant(text, name):
    keywords = ['emergency', 'FEMA']
    text_lower = text.lower()
    name_lower = name.lower()
    for kw in keywords:
        if kw.lower() in name_lower or kw.lower() in text_lower:
            return True
    return False

# Function to determine status
def determine_status(header, text):
    header_lower = header.lower()
    text_lower = text.lower()
    
    if 'completed' in text_lower:
        return 'completed'
    
    if 'not started' in header_lower:
        return 'not started'
    
    if 'design' in header_lower:
        return 'design'
    
    if 'construction' in header_lower:
        # If in construction section but not explicitly completed, maybe it's construction?
        # Hint said: "design", "completed", "not started".
        # If it's under construction, it's not "not started" and not "completed".
        # Maybe I'll just return "construction" or fallback to "design".
        # Let's return "construction" for now to be descriptive, or "design" if forced.
        # But wait, looking at the hints "Projects have three statuses...", maybe I should map "construction" -> "design" (as in "active")?
        # Or maybe the hint implies I should look for the word "completed" to distinguish.
        # I'll stick to extracting what I see. If the header says "Construction", I'll use that.
        # But I'll prioritize explicit "completed" in text.
        return 'construction'

    return 'unknown'

results = []
seen_projects = set()

# Combine all text for easier searching or process doc by doc?
# Doc by doc is safer to preserve context.

# Headers to look for (approximate regex)
# They seem to be like "Capital Improvement Projects (Design)"
# We can track the current section while iterating lines.

section_headers = [
    r"Capital Improvement Projects \(Design\)",
    r"Capital Improvement Projects \(Construction\)",
    r"Capital Improvement Projects \(Not Started\)",
    r"Disaster Recovery Projects"
]

for doc in civic_docs:
    text = doc['text']
    # Split into lines
    lines = text.split('\n')
    
    current_section = ""
    current_status_hint = ""
    
    # We will iterate through the text and identify project blocks.
    # Since we have a list of known project names, we can search for them.
    # However, just searching for names might lose the section context.
    # Strategy: Find all indices of project names and section headers.
    
    # Let's build a list of (index, type, value)
    # type = 'header' or 'project'
    
    matches = []
    
    # Find headers
    for header_pat in section_headers:
        for m in re.finditer(header_pat, text, re.IGNORECASE):
            matches.append((m.start(), 'header', m.group()))
            
    # Find projects
    for proj_name in all_project_names:
        # Use simple string search or regex with boundary?
        # Project names might have parentheses, so escape them.
        escaped_name = re.escape(proj_name)
        # Look for the name at the start of a line or after a newline, or just generally?
        # In the preview: "2022 Morning View..." is on its own line.
        # Let's be lenient and search for the name.
        for m in re.finditer(escaped_name, text, re.IGNORECASE):
            matches.append((m.start(), 'project', proj_name))
            
    # Sort matches by position
    matches.sort(key=lambda x: x[0])
    
    # Iterate matches
    current_header = "Unknown"
    
    for i in range(len(matches)):
        start, mtype, value = matches[i]
        
        if mtype == 'header':
            current_header = value
        elif mtype == 'project':
            proj_name_key = value # This is the project name as found (might differ in case from key? No, we searched using keys)
            # Find the actual key from the funding map (we iterated over keys, so `value` is the key)
            # Wait, regex finditer with ignorecase returns the match from text, not the pattern.
            # We need the key.
            # Let's adjust the 'project' search loop to store the key.
            pass

    # Refined approach:
    # 1. Find all project occurrences with their positions.
    # 2. Find all header occurrences with their positions.
    # 3. For each project occurrence, find the preceding header.
    # 4. Extract text between this project and the next project/header.
    
    # Re-doing the matches list construction
    matches = []
    for header_pat in section_headers:
        for m in re.finditer(header_pat, text, re.IGNORECASE):
            matches.append({'pos': m.start(), 'type': 'header', 'text': m.group()})
            
    for proj_name in all_project_names:
        escaped_name = re.escape(proj_name)
        # Ensure we match the full project name, not a substring of another project (handled by sorting names by length?)
        # Yes, but we need to avoid overlapping matches. 
        # Example: "Project A" and "Project A (FEMA)"
        # If text has "Project A (FEMA)", both will match.
        # We should probably consume the text or filter overlaps.
        # Since we sorted by length desc, "Project A (FEMA)" will be found first.
        # We can store matches and filter out those contained in others?
        # Or just let them be, and handle relevance.
        # Actually, simpler: finding "Project A" inside "Project A (FEMA)" is bad.
        # But we only care about the names in our funding DB.
        
        for m in re.finditer(escaped_name, text, re.IGNORECASE):
            matches.append({'pos': m.start(), 'end': m.end(), 'type': 'project', 'key': proj_name, 'text': m.group()})
            
    matches.sort(key=lambda x: x['pos'])
    
    # Filter overlapping project matches (keep longest)
    # Iterate and remove if a match is inside a previous match
    unique_matches = []
    if matches:
        # We need to handle headers and projects together for ordering, but filtering only applies to projects overlapping projects?
        # Headers won't overlap projects usually.
        # Let's filter projects first.
        
        # Separate headers and projects
        headers = [m for m in matches if m['type'] == 'header']
        projects = [m for m in matches if m['type'] == 'project']
        
        # Filter overlapping projects
        # Since we sorted by pos, if we have overlap, one starts before or at same time.
        # If we sorted names by length desc, the longer one matches first? No, we iterate all names.
        # The matches list is sorted by position.
        
        valid_projects = []
        last_end = -1
        
        # This overlap logic is tricky. 
        # Better: keep the match that is longest if they start at same position?
        # Or if one contains another.
        # Simple heuristic: if a match starts before the previous match ends, it's an overlap.
        # Since we have "Project A (FEMA)" and "Project A", they start at same pos.
        # We want "Project A (FEMA)".
        # So for same start pos, pick longest length.
        
        # Group by start pos
        from collections import defaultdict
        by_start = defaultdict(list)
        for p in projects:
            by_start[p['pos']].append(p)
            
        # For each start pos, pick longest
        cleaned_projects = []
        for pos in sorted(by_start.keys()):
            # Sort by length desc
            options = sorted(by_start[pos], key=lambda x: x['end'] - x['pos'], reverse=True)
            best = options[0]
            # Check if this overlaps with the last added project
            if not cleaned_projects or best['pos'] >= cleaned_projects[-1]['end']:
                cleaned_projects.append(best)
            else:
                # Overlap with previous.
                # E.g. Prev: "Project A (FEMA)", Curr: "Project A" (inside). 
                # "Project A" starts at pos X. "Project A (FEMA)" starts at X.
                # We already handled same-start.
                # What if "Project B" starts at X+10, inside "Project A..."?
                # Ignore it.
                pass
                
        # Now merge headers and cleaned projects
        all_items = sorted(headers + cleaned_projects, key=lambda x: x['pos'])
        
        # Now iterate
        current_header = None
        for i, item in enumerate(all_items):
            if item['type'] == 'header':
                current_header = item['text']
            elif item['type'] == 'project':
                # Determine text for this project
                # Text is from item['end'] to next item['pos']
                start_text = item['end']
                if i + 1 < len(all_items):
                    end_text = all_items[i+1]['pos']
                else:
                    end_text = len(text)
                
                proj_text = text[start_text:end_text]
                
                # Check relevance
                # We use the key (official name) and the text
                proj_name = item['key']
                
                if is_relevant(proj_text, proj_name):
                    # Determine status
                    status = determine_status(current_header or "", proj_text)
                    
                    # Get funding info
                    f_info = project_funding.get(proj_name, {})
                    
                    # Add to results if not already added (deduplicate by name?)
                    # A project might appear in multiple docs. We should probably take the most recent or merged?
                    # For simplicity, add all and we can inspect or dedupe later.
                    # Or check extraction quality.
                    
                    # Construct record
                    record = {
                        "Project_Name": proj_name,
                        "Funding_Source": f_info.get("Funding_Source"),
                        "Amount": f_info.get("Amount"),
                        "Status": status
                    }
                    
                    # Dedupe based on Project Name
                    if proj_name not in seen_projects:
                        results.append(record)
                        seen_projects.add(proj_name)

print("__RESULT__:")
print(json.dumps(results))"""

env_args = {'var_function-call-1156938048168678441': 'file_storage/function-call-1156938048168678441.json', 'var_function-call-1156938048168679978': 'file_storage/function-call-1156938048168679978.json'}

exec(code, env_args)
