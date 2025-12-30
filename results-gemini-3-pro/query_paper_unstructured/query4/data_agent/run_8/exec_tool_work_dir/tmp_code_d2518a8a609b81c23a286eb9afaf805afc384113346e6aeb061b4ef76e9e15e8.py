code = """import json
import re

# Load the filtered papers
with open(locals()['var_function-call-18372255859020147212'], 'r') as f:
    papers = json.load(f)

titles_2016 = []

for paper in papers:
    text = paper.get('text', '')
    filename = paper.get('filename', '')
    
    # Check for 2016 in the header/first 2000 chars
    # We look for "2016" or "'16" associated with conference names
    # But simply "2016" in the header is a strong signal for publication year.
    header_text = text[:3000] # Increased to 3000 to be safe
    
    # Regex to find 2016 not part of a number like 12016 (though unlikely in header text)
    # Looking for standalone 2016
    if re.search(r'\b2016\b', header_text):
        # Found 2016 in header.
        # Now verify "physical activity" domain.
        # It's already filtered by regex, but let's assume valid.
        title = filename.replace('.txt', '')
        titles_2016.append(title)
    elif re.search(r"'\s*16\b", header_text): # Matches '16 or ' 16
        title = filename.replace('.txt', '')
        titles_2016.append(title)

print("__RESULT__:")
print(json.dumps(titles_2016))"""

env_args = {'var_function-call-1760363004607511404': 'file_storage/function-call-1760363004607511404.json', 'var_function-call-1760363004607508631': [{'id': '1', 'title': 'Expense Control: A Gamified, Semi-Automated, Crowd-Based Approach For Receipt Capturing', 'citation_count': '4', 'citation_year': '2017'}], 'var_function-call-12400401275276692089': 'file_storage/function-call-12400401275276692089.json', 'var_function-call-18372255859020147212': 'file_storage/function-call-18372255859020147212.json'}

exec(code, env_args)
