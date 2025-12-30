code = """import json
import re

# Load data
civic_docs = json.load(open('var_function-call-3208934928829351036.json'))
funding_docs = json.load(open('var_function-call-14892292881911513259.json'))

# Get project names
funding_map = {item['Project_Name']: item['Amount'] for item in funding_docs}
project_names_list = list(funding_map.keys())

# Regex for date
# Matches: Spring 2022, March 2022, etc. (case insensitive)
# Also handling "March, 2022" or "March 15, 2022"
date_re = re.compile(r'(?i)\b(Spring|March|April|May)\b.{0,10}\b2022\b|\b2022\b.{0,10}\b(Spring|March|April|May)\b')

# Regex for start/begin
start_re = re.compile(r'(?i)(Begin|Start|Advertise|Award|Commence)')
# Regex for exclude
exclude_re = re.compile(r'(?i)(Complete|Finish|End|Completion|Closure)')

found_projects = set()

debug_info = []

for doc in civic_docs:
    text = doc['text']
    
    # Identify project locations
    matches = []
    for pname in project_names_list:
        # Escape for regex
        pname_esc = re.escape(pname)
        # Find all matches
        for m in re.finditer(pname_esc, text):
            matches.append({
                'start': m.start(),
                'end': m.end(),
                'name': pname
            })
    
    if not matches:
        continue
        
    # Filter overlapping matches: prefer longer names
    # Sort by start (asc), then by length (desc)
    matches.sort(key=lambda x: (x['start'], -(x['end'] - x['start'])))
    
    final_matches = []
    last_end = -1
    for m in matches:
        if m['start'] >= last_end:
            final_matches.append(m)
            last_end = m['end']
        # Else: this match overlaps/is inside the previous one (since we sorted by start then length desc), skip it
        # Wait, if we have "Project A" starting at 10 and "Project A Extended" starting at 10.
        # Sorted: "Project A Extended" comes first (same start, longer). We take it.
        # "Project A" comes second. Start 10 < End of prev. Skip. Correct.
        # What if "Project A" is at 100, and "Project B" is at 105?
        # If "Project A" ends at 120, "Project B" is skipped.
        # This assumes Project Names don't overlap in text unless they are the same entity.
        # In this context, headings are distinct. This logic is acceptable.
    
    # Process segments
    for i in range(len(final_matches)):
        pname = final_matches[i]['name']
        start_idx = final_matches[i]['end'] # Text after the name
        
        # End of segment is start of next project
        if i + 1 < len(final_matches):
            end_idx = final_matches[i+1]['start']
        else:
            end_idx = len(text)
            
        segment = text[start_idx:end_idx]
        
        # Check for dates in segment
        # We split by lines to check line context
        lines = segment.split('\n')
        for line in lines:
            line_clean = line.strip()
            if not line_clean:
                continue
                
            if date_re.search(line_clean):
                if exclude_re.search(line_clean):
                    continue
                if start_re.search(line_clean):
                    # Found a start date match
                    found_projects.add(pname)
                    debug_info.append(f"Match: {pname} | Line: {line_clean}")
                    break # Found for this project in this doc, move to next project

# Calculate totals
count = 0
total_funding = 0
matched_projects = []

for pname in found_projects:
    if pname in funding_map:
        count += 1
        total_funding += funding_map[pname]
        matched_projects.append(pname)

print(f"Debug Found: {len(found_projects)}")
# print(debug_info)

result = {
    "count": count,
    "total_funding": total_funding,
    "projects": matched_projects
}

print("__RESULT__:")
print(json.dumps(result))"""

env_args = {'var_function-call-14897974976340963418': 'file_storage/function-call-14897974976340963418.json', 'var_function-call-14892292881911513259': 'file_storage/function-call-14892292881911513259.json', 'var_function-call-3208934928829351036': 'file_storage/function-call-3208934928829351036.json'}

exec(code, env_args)
