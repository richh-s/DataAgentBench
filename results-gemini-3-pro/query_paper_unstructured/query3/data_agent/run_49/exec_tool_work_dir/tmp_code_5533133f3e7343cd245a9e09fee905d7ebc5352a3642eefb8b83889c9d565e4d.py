code = """import json
import re

# Load the papers from the file
with open(locals()['var_function-call-3050203900418415447'], 'r') as f:
    papers = json.load(f)

matching_titles = []

# Regex for year > 2016. Looking for 2017 to 2025.
year_pattern = re.compile(r'\b(201[7-9]|202[0-5])\b')

for paper in papers:
    text = paper.get('text', '')
    filename = paper.get('filename', '')
    title = filename.replace('.txt', '')
    
    # Check Contribution: "empirical" in text
    # Using case-insensitive search
    if 'empirical' not in text.lower():
        continue
        
    # Check Year: Look in the first 3000 chars for header info
    header_text = text[:3000]
    years_found = year_pattern.findall(header_text)
    
    if not years_found:
        # Fallback: check whole text if not found in header? 
        # Usually publication year is at the top. 
        # If I check whole text, I might find citation years.
        # Let's stick to header.
        continue
    
    # If years found, assume the paper is published in one of them.
    # Since we are filtering for > 2016, and the regex only matches 2017+, 
    # any match is good.
    # To be precise, we might want to ensure it's the *publication* year, 
    # not a reference. But usually "Copyright 2017" or "CHI 2018" appears early.
    
    matching_titles.append(title)

print("__RESULT__:")
print(json.dumps(matching_titles))"""

env_args = {'var_function-call-7133362832000802960': 'file_storage/function-call-7133362832000802960.json', 'var_function-call-7133362832000806077': [{'id': '1', 'title': 'Expense Control: A Gamified, Semi-Automated, Crowd-Based Approach For Receipt Capturing', 'citation_count': '4', 'citation_year': '2017'}], 'var_function-call-3665432082971907292': 'file_storage/function-call-3665432082971907292.json', 'var_function-call-3050203900418415447': 'file_storage/function-call-3050203900418415447.json'}

exec(code, env_args)
