code = """import json
import re

# Load Citations
with open(locals()['var_function-call-17351178727143063215'], 'r') as f:
    citations_data = json.load(f)

# Aggregate citations by title
title_citations = {}
for entry in citations_data:
    t = entry['title']
    c = int(entry['citation_count'])
    title_citations[t] = title_citations.get(t, 0) + c

# Load Paper Docs
with open(locals()['var_function-call-6826266574938027314'], 'r') as f:
    papers = json.load(f)

results = []

for paper in papers:
    filename = paper.get('filename', '')
    text = paper.get('text', '')
    title = filename.replace('.txt', '')
    
    # Extract Year
    # Look for 20xx in the first 500 characters
    header = text[:1000]
    years = re.findall(r'\b(20\d{2})\b', header)
    
    if not years:
        # Try finding 'YY e.g. '17
        short_years = re.findall(r"'\d{2}", header)
        # This is risky, '15 might mean something else.
        # But usually academic headers have the full year.
        # Let's rely on 4-digit years.
        year = None
    else:
        # Take the first 20xx found.
        # Sometimes there might be multiple, e.g. "2015 ... 2014". The venue year is usually first.
        year = int(years[0])
        
    # Extract Contribution
    # Check for "empirical"
    is_empirical = "empirical" in text.lower()
    
    # Filter
    if year and year > 2016 and is_empirical:
        count = title_citations.get(title, 0)
        results.append({"title": title, "total_citation_count": count})

# Sort results by citation count descending for better presentation, though not required.
results.sort(key=lambda x: x['total_citation_count'], reverse=True)

print("__RESULT__:")
print(json.dumps(results))"""

env_args = {'var_function-call-5913521790257705875': 'file_storage/function-call-5913521790257705875.json', 'var_function-call-16603125726449287240': 'file_storage/function-call-16603125726449287240.json', 'var_function-call-10308318711084612855': [{'_id': '694f5530284b10b11dc0a869', 'filename': 'A Lived Informatics Model of Personal Informatics.txt'}, {'_id': '694f5530284b10b11dc0a86a', 'filename': 'A Stage-based Model of Personal Informatics Systems.txt'}, {'_id': '694f5530284b10b11dc0a86b', 'filename': 'A Trip to the Moon: Personalized Animated Movies for Self-reflection.txt'}, {'_id': '694f5530284b10b11dc0a86c', 'filename': 'A Wee Bit More Interaction: Designing and Evaluating an Overactive Bladder App.txt'}, {'_id': '694f5530284b10b11dc0a86d', 'filename': 'ArmSleeve: A Patient Monitoring System to Support Occupational Therapists in Stroke Rehabilitation.txt'}], 'var_function-call-12915355983397043581': [{'count(*)': '1405'}], 'var_function-call-17351178727143063215': 'file_storage/function-call-17351178727143063215.json', 'var_function-call-17424668251812217862': 'file_storage/function-call-17424668251812217862.json', 'var_function-call-6826266574938027314': 'file_storage/function-call-6826266574938027314.json'}

exec(code, env_args)
