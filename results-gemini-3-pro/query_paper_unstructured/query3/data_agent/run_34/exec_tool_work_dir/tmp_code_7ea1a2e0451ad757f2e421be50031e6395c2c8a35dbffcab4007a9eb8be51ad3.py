code = """import json
import re

# Load Citations
citation_file = locals()['var_function-call-3193368456383189036']
with open(citation_file, 'r') as f:
    citations_list = json.load(f)

citation_map = {}
for item in citations_list:
    try:
        val = int(item['total_citations'])
    except:
        val = 0
    citation_map[item['title']] = val

# Load Papers
papers_file = locals()['var_function-call-13531993563476914468']
with open(papers_file, 'r') as f:
    papers = json.load(f)

results = []
debug_info = []

for paper in papers:
    filename = paper.get('filename', '')
    if not filename.endswith('.txt'):
        continue
    title = filename[:-4]
    
    text = paper.get('text', '')
    
    # Search for year in a larger chunk, e.g., first 10000 chars
    # or just the whole text if not too huge.
    # Papers are usually 10-20k chars.
    chunk = text[:10000]
    
    # Regex for year 2017-2024
    years = re.findall(r'\b(20(?:1[7-9]|2[0-4]))\b', chunk)
    
    pub_year = 0
    if years:
        # Try to find a year > 2016
        # We prefer years that appear early, but "CHI 2018" might be later.
        # Let's take the set of years and see if any > 2016.
        # If multiple, picking the "publication" year is tricky.
        # Usually the venue year is the publication year.
        # If we find 2018, it's likely published in 2018.
        valid_years = [int(y) for y in years if int(y) > 2016]
        if valid_years:
            # Take the most frequent? Or the first?
            # Usually the copyright line has the year.
            pub_year = valid_years[0] 
    
    if pub_year == 0:
        # Debug why no year found
        if len(debug_info) < 5:
            debug_info.append({"title": title, "error": "No valid year > 2016 found", "years_found": years})
        continue
        
    if 'empirical' not in text.lower():
        if len(debug_info) < 5:
            debug_info.append({"title": title, "error": "No 'empirical' in text"})
        continue
        
    count = citation_map.get(title, 0)
    
    results.append({"title": title, "citation_count": count})

# If results are still empty, return debug info
if not results:
    print("__RESULT__:")
    print(json.dumps(debug_info))
else:
    # Sort and print
    results.sort(key=lambda x: x['citation_count'], reverse=True)
    print("__RESULT__:")
    print(json.dumps(results))"""

env_args = {'var_function-call-224810883549294860': 'file_storage/function-call-224810883549294860.json', 'var_function-call-9456626268790233779': ['paper_docs'], 'var_function-call-16636765420084793523': [{'_id': '694f5530284b10b11dc0a869', 'filename': 'A Lived Informatics Model of Personal Informatics.txt'}, {'_id': '694f5530284b10b11dc0a86a', 'filename': 'A Stage-based Model of Personal Informatics Systems.txt'}, {'_id': '694f5530284b10b11dc0a86b', 'filename': 'A Trip to the Moon: Personalized Animated Movies for Self-reflection.txt'}, {'_id': '694f5530284b10b11dc0a86c', 'filename': 'A Wee Bit More Interaction: Designing and Evaluating an Overactive Bladder App.txt'}, {'_id': '694f5530284b10b11dc0a86d', 'filename': 'ArmSleeve: A Patient Monitoring System to Support Occupational Therapists in Stroke Rehabilitation.txt'}], 'var_function-call-3193368456383189036': 'file_storage/function-call-3193368456383189036.json', 'var_function-call-13531993563476914468': 'file_storage/function-call-13531993563476914468.json', 'var_function-call-13038935966288007214': [], 'var_function-call-12102494195742263056': 'DEBUG'}

exec(code, env_args)
