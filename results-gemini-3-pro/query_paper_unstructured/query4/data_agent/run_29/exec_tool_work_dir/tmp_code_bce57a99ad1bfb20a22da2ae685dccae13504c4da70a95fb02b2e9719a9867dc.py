code = """import json
import re

# Load data
with open(locals()['var_function-call-4420579621073480200'], 'r') as f:
    papers = json.load(f)

with open(locals()['var_function-call-4736821834278124027'], 'r') as f:
    citations = json.load(f)

# Aggregate citations
citation_map = {}
for cit in citations:
    title = cit['title']
    try:
        count = int(cit['citation_count'])
    except:
        count = 0
    if title not in citation_map:
        citation_map[title] = 0
    citation_map[title] += count

results = []
debug_years = []

for p in papers:
    filename = p['filename']
    if filename.endswith('.txt'):
        title = filename[:-4]
    else:
        title = filename
        
    text = p.get('text', '')
    header = text[:1000] # First 1000 chars should contain metadata
    
    # Check for Physical Activity (already filtered by Mongo, but good to be safe)
    if 'physical activity' not in text.lower():
        continue

    # Determine Year
    # Look for Copyright 2016, or Conference 2016
    # Regex for specific 2016 patterns in header
    # Patterns: 
    # 1. "Copyright 2016"
    # 2. "© 2016"
    # 3. "2016" at end of a line (often date)
    # 4. "CHI '16", "CHI 2016", etc.
    
    is_2016 = False
    
    # Strong indicators
    if re.search(r"Copyright\s+2016", header, re.IGNORECASE):
        is_2016 = True
    elif re.search(r"©\s+2016", header):
        is_2016 = True
    elif re.search(r"\b(CHI|UbiComp|CSCW|DIS|IUI|TEI|PervasiveHealth|WWW|OzCHI|AH)\s+['’]?16", header, re.IGNORECASE):
        is_2016 = True
    elif re.search(r"\b(CHI|UbiComp|CSCW|DIS|IUI|TEI|PervasiveHealth|WWW|OzCHI|AH).*2016", header, re.IGNORECASE):
        is_2016 = True
    elif re.search(r",\s+2016\b", header): # e.g. "September 7-11, 2016"
        is_2016 = True
    
    # Negative check: if it finds 2015, 2017, 2018 in strong positions, it's likely not 2016
    # unless 2016 is the main one.
    # Let's trust the positive indicators first.
    
    if is_2016:
        # Double check it's not 2017 with 2016 mentioned
        # e.g. "CHI 2017... copyright 2017"
        if re.search(r"Copyright\s+(2015|2017|2018)", header, re.IGNORECASE) or \
           re.search(r"©\s+(2015|2017|2018)", header):
             # If both exist, it's ambiguous, but usually the latest valid copyright matters.
             # Or maybe it's a 2017 paper citing 2016.
             # However, assuming standard ACM format, the copyright year matches publication.
             # If we found explicit "Copyright 2016", we assume 2016.
             pass

        count = citation_map.get(title, 0)
        results.append({"title": title, "citation_count": count})

# Sort by title or count? User didn't specify. I'll sort by title.
results.sort(key=lambda x: x['title'])

print("__RESULT__:")
print(json.dumps(results))"""

env_args = {'var_function-call-524279506149407119': ['paper_docs'], 'var_function-call-524279506149405588': 'file_storage/function-call-524279506149405588.json', 'var_function-call-524279506149408153': ['Citations', 'sqlite_sequence'], 'var_function-call-524279506149406622': [{'id': '1', 'title': 'Expense Control: A Gamified, Semi-Automated, Crowd-Based Approach For Receipt Capturing', 'citation_count': '4', 'citation_year': '2017'}, {'id': '2', 'title': 'Expense Control: A Gamified, Semi-Automated, Crowd-Based Approach For Receipt Capturing', 'citation_count': '95', 'citation_year': '2018'}, {'id': '3', 'title': 'Understanding My Data, Myself: Supporting Self-reflection with Ubicomp Technologies', 'citation_count': '32', 'citation_year': '2012'}, {'id': '4', 'title': 'Understanding My Data, Myself: Supporting Self-reflection with Ubicomp Technologies', 'citation_count': '29', 'citation_year': '2013'}, {'id': '5', 'title': 'Understanding My Data, Myself: Supporting Self-reflection with Ubicomp Technologies', 'citation_count': '18', 'citation_year': '2014'}], 'var_function-call-9551284447428774224': [{'count(*)': '1405'}], 'var_function-call-9551284447428775563': 'file_storage/function-call-9551284447428775563.json', 'var_function-call-4736821834278124027': 'file_storage/function-call-4736821834278124027.json', 'var_function-call-1276767600603300389': [], 'var_function-call-8853061178265091948': 'debug_done', 'var_function-call-17995316611090094079': {'total_papers': 5, 'total_citations': 1405, 'pa_count': 4, 'year_2016_count': 0, 'match_count': 0, 'sample_matches': [], 'sample_citation_titles': ['Shifting Dynamics or Breaking Sacred Traditions?: The Role of Technology in Twelve-step Fellowships', 'How to Drive a London Bus: Measuring Performance in a Mobile and Remote Workplace', 'Understanding My Data, Myself: Supporting Self-reflection with Ubicomp Technologies', 'Quantifying the Body and Caring for the Mind: Self-Tracking in Multiple Sclerosis', 'Rotating Online Behavior Change Interventions Increases Effectiveness But Also Increases Attrition'], 'test_title_in_citations': False}, 'var_function-call-4420579621073480200': 'file_storage/function-call-4420579621073480200.json'}

exec(code, env_args)
