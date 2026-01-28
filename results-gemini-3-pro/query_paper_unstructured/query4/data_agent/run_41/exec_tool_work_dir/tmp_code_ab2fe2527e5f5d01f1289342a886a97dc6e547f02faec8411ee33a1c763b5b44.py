code = """import json
import re

# Load the paper documents
with open(locals()['var_function-call-16322124554372865657'], 'r') as f:
    papers = json.load(f)

# Filter for papers published in 2016
# Heuristic: Look for "2016" or "'16" in the first 500 characters
# Also ensure "Physical Activity" is in the text (already done by query, but good to be sure if needed)

filtered_titles = []

for paper in papers:
    text = paper.get('text', '')
    filename = paper.get('filename', '')
    
    # Check header for year 2016
    # We look at the first 500 characters
    header = text[:500]
    
    # Check for 2016 or '16 in the context of a conference or date
    # Patterns: 
    # "2016"
    # "'16"
    # We want to avoid matching "2016" if it's part of a phone number or unrelated number, 
    # but in the header of a paper, "2016" usually denotes the year.
    
    is_2016 = False
    
    # Check explicitly for 2016
    if "2016" in header:
        is_2016 = True
    elif "'16" in header:
        # Check if it follows a typical conference acronym or month
        # This is a weaker check, but '16 usually means year in headers
        is_2016 = True
        
    # Exclusion criteria: if 2015, 2017, 2018 etc appear in the header *and* 2016 is not the main date
    # This is tricky. Let's rely on presence of 2016. 
    # However, sometimes a 2017 paper might cite a 2016 paper in the abstract/intro which is in the first 500 chars?
    # No, abstract usually doesn't have citations like [1] that expand to full text in the first 500 chars.
    # But "Copyright 2016" might appear in a paper published in early 2017?
    # Let's assume if 2016 is in the header, it's a 2016 paper.
    
    # Refined check:
    # If "2016" is in the header, it's likely 2016.
    # If "2015" or "2017" or "2018" is ALSO in the header, we need to be careful.
    # Example: "CHI 2016" -> 2016.
    # "CHI 2017... Copyright 2017" -> 2017.
    
    # Let's count year occurrences in header
    years = re.findall(r'20\d\d', header)
    if years:
        # If 2016 is present
        if '2016' in years:
            # If there are other years, check if 2016 is the "primary" one (e.g. repeated or associated with conference)
            # Simpler: if 2016 is found, accept it unless a later year is found?
            # Actually, looking at the sample 2018 paper:
            # "CHI 2018, April... 2018 Copyright..."
            # It has 2018 multiple times.
            # If a paper is from 2016, it should have 2016.
            # If it has 2016 AND 2018, it's likely 2018 (citing 2016 or copyright previous work? Unlikely in header).
            # But the sample 2018 paper does NOT have 2016 in the header.
            # So if 2016 is in the header, it's a strong signal.
            is_2016 = True
        else:
            is_2016 = False
    elif "'16" in header:
        is_2016 = True
    else:
        is_2016 = False
        
    # Double check if domain is strictly "physical activity"
    # The prompt says: "Fields like domain ... may contain multiple values"
    # and "Common domains include: ... 'physical activity'".
    # So we look for the exact phrase "physical activity" in the text.
    # The Mongo query already filtered for this, but case-insensitivity might match "Physical Activity" or "physical activity".
    # We can trust the Mongo filter for the domain.
    
    if is_2016:
        # Extract title from filename
        title = filename.replace('.txt', '')
        filtered_titles.append(title)

print("__RESULT__:")
print(json.dumps(filtered_titles))"""

env_args = {'var_function-call-4836586951926601287': ['paper_docs'], 'var_function-call-4836586951926600548': 'file_storage/function-call-4836586951926600548.json', 'var_function-call-218136711215706544': 'file_storage/function-call-218136711215706544.json', 'var_function-call-16322124554372865657': 'file_storage/function-call-16322124554372865657.json'}

exec(code, env_args)
