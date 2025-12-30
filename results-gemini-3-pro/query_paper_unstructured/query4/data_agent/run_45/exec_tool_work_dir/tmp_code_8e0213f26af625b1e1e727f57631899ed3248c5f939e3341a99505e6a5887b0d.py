code = """import json
import re

# Load the papers from the previous step
file_path = locals()['var_function-call-1805963749802490353']
with open(file_path, 'r') as f:
    papers = json.load(f)

filtered_titles = []

# Regex for finding year 2016 in header/copyright context
# We look for 2016 in the first 1000 characters
# And ensure it's associated with a venue or copyright
venue_pattern = re.compile(r"(CHI|UbiComp|CSCW|DIS|PervasiveHealth|WWW|IUI|OzCHI|TEI|AH).{0,50}2016", re.IGNORECASE)
copyright_pattern = re.compile(r"(Copyright|©).{0,50}2016", re.IGNORECASE)
header_year_pattern = re.compile(r"2016", re.IGNORECASE) # Fallback if specific venues not found but 2016 is in the first few lines? No, risky.

# Domain check: 'physical activity' in first 3000 chars or filename
domain_pattern = re.compile(r"physical activity", re.IGNORECASE)

for p in papers:
    text = p.get('text', '')
    filename = p.get('filename', '')
    
    # Check domain
    # Often title is in filename
    if domain_pattern.search(filename) or domain_pattern.search(text[:3000]):
        # Check year
        # Look at the first 1000 characters for header info
        header = text[:1000]
        
        is_2016 = False
        if venue_pattern.search(header) or copyright_pattern.search(header):
            is_2016 = True
        
        # Double check to avoid 2018 papers that mention 2016 (like the preview)
        # If the header also contains 2014, 2015, 2017, 2018, 2019... determine which is the main one?
        # The preview paper had "CHI 2018" and "Copyright 2018". 
        # So if we find 2016 but also a later year in a similar strong position, we might need to be careful.
        # But usually "Copyright 2016" won't appear in a 2018 paper's header.
        # The preview paper didn't have "Copyright 2016" in header. It had "Since 2016" in abstract? No, "Since 2016" was not in preview.
        # The preview matched "2016" because "2016" appeared somewhere.
        # My stricter check `venue_pattern` or `copyright_pattern` should filter out the 2018 paper if it doesn't have 2016 in venue/copyright.
        
        if is_2016:
            # Extract title: filename without .txt
            title = filename.rsplit('.', 1)[0]
            filtered_titles.append(title)

print(f"DEBUG: Found {len(filtered_titles)} papers.")
print(f"DEBUG: First 5 titles: {filtered_titles[:5]}")"""

env_args = {'var_function-call-13658712290201137078': 'file_storage/function-call-13658712290201137078.json', 'var_function-call-1805963749802490353': 'file_storage/function-call-1805963749802490353.json'}

exec(code, env_args)
