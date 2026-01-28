code = """import json
import re

# Load data
with open(locals()['var_function-call-8460811092792669481'], 'r') as f:
    funding_data = json.load(f)

with open(locals()['var_function-call-8460811092792670416'], 'r') as f:
    civic_docs = json.load(f)

# Create a mapping of project name to funding amount
project_funding = {}
for item in funding_data:
    # item['Amount'] is a string or int? Preview showed string "24000".
    amt = int(item['Amount'])
    # Handle duplicates? If multiple entries for same name, sum them? 
    # Usually names are unique in Funding table based on ID. 
    # But let's assume unique names or sum if repeated.
    name = item['Project_Name'].strip()
    project_funding[name] = project_funding.get(name, 0) + amt

# Sort names by length descending to match longest first
sorted_names = sorted(project_funding.keys(), key=len, reverse=True)

# Helper to check date
def is_spring_2022(date_str):
    if not date_str: return False
    ds = date_str.lower()
    # Check for 2022
    if "2022" not in ds:
        return False
    
    # Check for Spring or months
    if "spring" in ds:
        return True
    
    # Months: March, April, May
    months = ["march", "april", "may"]
    for m in months:
        if m in ds:
            return True
            
    # Numeric: 03, 04, 05 with separators
    # strict regex for date formats?
    # 03/2022, 2022-03
    if re.search(r"03/\d{2,4}", ds) or re.search(r"04/\d{2,4}", ds) or re.search(r"05/\d{2,4}", ds):
        return True
    if re.search(r"2022-03", ds) or re.search(r"2022-04", ds) or re.search(r"2022-05", ds):
        return True
        
    return False

matched_projects = set()

for doc in civic_docs:
    text = doc['text']
    
    # Find project occurrences
    # We want to segment the text.
    # Store (start_index, project_name)
    found = []
    
    # To avoid overlapping (e.g. finding "Project A" inside "Project A Phase 2"),
    # Since we sorted by length, we can mask the text or just check indices.
    # Simple approach: find all, then resolve.
    # Better: Use a list of disjoint spans.
    
    # However, Python's find() is simple. 
    # Let's iterate through sorted names. If found, mark the region as occupied.
    
    occupied = [False] * len(text)
    doc_projects = [] # (start_idx, name)
    
    for name in sorted_names:
        start = 0
        while True:
            idx = text.find(name, start)
            if idx == -1:
                break
            
            # Check if this region is free
            # We only care if the name is a distinct header? 
            # Or just mentioned? The prompt implies extraction.
            # Assuming headers in Agenda.
            # Let's check if the region is mostly free.
            # Actually, just adding them and sorting by index is usually enough for "blocks".
            # The "Longest Match" logic handles the sub-name issue naturally if we assume headers are exact matches.
            
            # One issue: "Project A" vs "Project A (FEMA)". 
            # If "Project A (FEMA)" is in text, `text.find("Project A")` will also find it at the same index.
            # We should prefer the longer match.
            # Check if we already have a longer match starting at this index?
            
            is_overlap = False
            for existing_start, existing_name in doc_projects:
                existing_end = existing_start + len(existing_name)
                current_end = idx + len(name)
                # Check overlap
                if max(existing_start, idx) < min(existing_end, current_end):
                    is_overlap = True
                    break
            
            if not is_overlap:
                doc_projects.append((idx, name))
                # Mark occupied? Doing it via the list check above.
            
            start = idx + 1
            
    doc_projects.sort(key=lambda x: x[0])
    
    # Now process blocks
    for i in range(len(doc_projects)):
        start_idx, name = doc_projects[i]
        # End of block is start of next project or end of text
        end_idx = doc_projects[i+1][0] if i+1 < len(doc_projects) else len(text)
        
        block = text[start_idx:end_idx]
        
        # Look for start date in this block
        # Patterns: "Begin Construction:", "Start Date:", "Construction Start:"
        # "Advertise" is not start.
        
        match = re.search(r"Begin Construction:([^\n]*)", block, re.IGNORECASE)
        date_str = ""
        if match:
            date_str = match.group(1).strip()
        else:
            # Maybe it's "Construction start:"
            match = re.search(r"Construction Start:([^\n]*)", block, re.IGNORECASE)
            if match:
                date_str = match.group(1).strip()
            else:
                # Maybe "Date:" inside a "Schedule" section?
                # "Project Schedule:\n... Begin Construction: ..." matched by first regex (multiline search? No, block contains newlines)
                # re.search searches the whole string. '.' does not match newline by default.
                # So `Begin Construction:([^\n]*)` matches until end of line. This is good.
                pass
        
        # What if the date is on the next line?
        # "Begin Construction:\nFall 2023"
        if not date_str:
             match = re.search(r"Begin Construction:\s*\n\s*([^\n]*)", block, re.IGNORECASE)
             if match:
                 date_str = match.group(1).strip()
                 
        if is_spring_2022(date_str):
            matched_projects.add(name)

# Calculate totals
total_amt = 0
count = 0
final_projects = []

for name in matched_projects:
    if name in project_funding:
        total_amt += project_funding[name]
        count += 1
        final_projects.append(name)

result = {
    "count": count,
    "total_funding": total_amt,
    "projects": final_projects
}

print("__RESULT__:")
print(json.dumps(result))"""

env_args = {'var_function-call-15438762544756245875': 'file_storage/function-call-15438762544756245875.json', 'var_function-call-15438762544756246872': [{'Funding_ID': '1', 'Project_Name': '2021 Annual Street Maintenance', 'Funding_Source': 'Public-Private Partnership (PPP)', 'Amount': '24000'}, {'Funding_ID': '2', 'Project_Name': '2022 Annual Street Maintenance', 'Funding_Source': 'Government Grant', 'Amount': '45000'}, {'Funding_ID': '3', 'Project_Name': '2022 Morning View Resurfacing & Storm Drain Improvements', 'Funding_Source': 'State Development Grant', 'Amount': '38000'}, {'Funding_ID': '4', 'Project_Name': 'Annual Street Maintenance', 'Funding_Source': 'Corporate Sponsorship', 'Amount': '23000'}, {'Funding_ID': '5', 'Project_Name': 'Birdview Avenue Improvements', 'Funding_Source': 'National Foundation Fund', 'Amount': '79000'}], 'var_function-call-8460811092792669481': 'file_storage/function-call-8460811092792669481.json', 'var_function-call-8460811092792670416': 'file_storage/function-call-8460811092792670416.json'}

exec(code, env_args)
