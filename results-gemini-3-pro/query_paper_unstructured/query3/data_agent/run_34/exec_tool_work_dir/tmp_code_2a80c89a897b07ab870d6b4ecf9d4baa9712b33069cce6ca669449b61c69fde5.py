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

# Regex: Preceded by non-digit or start, Year 2017-2024, Followed by non-digit or end
# We use capturing group for the year.
year_pattern = re.compile(r'(?:^|\D)(20(?:1[7-9]|2[0-4]))(?:\D|$)')

for paper in papers:
    filename = paper.get('filename', '')
    if not filename.endswith('.txt'):
        continue
    title = filename[:-4]
    
    text = paper.get('text', '')
    
    # Check "empirical"
    if 'empirical' not in text.lower():
        continue

    # Extract Year
    # Search in the first 20,000 characters to cover headers and intro
    chunk = text[:20000]
    matches = year_pattern.findall(chunk)
    
    if not matches:
        continue
        
    # Filter years > 2016
    valid_years = [int(y) for y in matches if int(y) > 2016]
    
    if not valid_years:
        continue
        
    # If we found valid years, we assume the paper is published > 2016
    # (Since we also filtered by regex in Mongo)
    
    # Get citations
    count = citation_map.get(title, 0)
    
    # Add to results
    results.append({"title": title, "total_citation_count": count})

# Sort by citation count descending
results.sort(key=lambda x: x['total_citation_count'], reverse=True)

print("__RESULT__:")
print(json.dumps(results))"""

env_args = {'var_function-call-224810883549294860': 'file_storage/function-call-224810883549294860.json', 'var_function-call-9456626268790233779': ['paper_docs'], 'var_function-call-16636765420084793523': [{'_id': '694f5530284b10b11dc0a869', 'filename': 'A Lived Informatics Model of Personal Informatics.txt'}, {'_id': '694f5530284b10b11dc0a86a', 'filename': 'A Stage-based Model of Personal Informatics Systems.txt'}, {'_id': '694f5530284b10b11dc0a86b', 'filename': 'A Trip to the Moon: Personalized Animated Movies for Self-reflection.txt'}, {'_id': '694f5530284b10b11dc0a86c', 'filename': 'A Wee Bit More Interaction: Designing and Evaluating an Overactive Bladder App.txt'}, {'_id': '694f5530284b10b11dc0a86d', 'filename': 'ArmSleeve: A Patient Monitoring System to Support Occupational Therapists in Stroke Rehabilitation.txt'}], 'var_function-call-3193368456383189036': 'file_storage/function-call-3193368456383189036.json', 'var_function-call-13531993563476914468': 'file_storage/function-call-13531993563476914468.json', 'var_function-call-13038935966288007214': [], 'var_function-call-12102494195742263056': 'DEBUG', 'var_function-call-11442590404274087377': [{'title': 'A Trip to the Moon: Personalized Animated Movies for Self-reflection', 'error': 'No valid year > 2016 found', 'years_found': []}, {'title': 'A Wee Bit More Interaction: Designing and Evaluating an Overactive Bladder App', 'error': 'No valid year > 2016 found', 'years_found': []}, {'title': 'Common Barriers to the Use of Patient-Generated Data Across Clinical Settings', 'error': 'No valid year > 2016 found', 'years_found': []}, {'title': 'Communicating Uncertainty in Fertility Prognosis', 'error': 'No valid year > 2016 found', 'years_found': []}, {'title': 'Computational Approaches Toward Integrating Quantified Self Sensing and Social Media', 'error': 'No valid year > 2016 found', 'years_found': []}], 'var_function-call-6830701130609361220': {'title': 'A Trip to the Moon: Personalized Animated Movies for Self-reflection.txt', 'text_len': 54376, 'prefix': 'Fengjiao Peng\nMIT Media Lab\nCambridge, MA, USA\nfpeng@mit.edu\n\nA Trip to the Moon: Personalized Animated Movies for\nSelf-reﬂection\nVeronica Crista LaBelle\nMIT\nCambridge, MA, USA\nvlabelle@mit.edu\nRosalind W. Picard\nMIT Media Lab\nCambridge, MA, USA\npicard@media.mit.edu\n\nEmily Christen Yue\nHarvard University\nCambridge, MA, USA\neyue@college.harvard.edu\n\nABSTRACT\nSelf-tracking physiological and psychological data poses the\nchallenge of presentation and interpretation. Insightful nar-\nratives for self-', 'chi_2018_index': 2513, 'context': 'CHI 2018, April 21–26, 2018, Montréal, QC, Canada\n© 2018 Copyright held by the owner/author(s). Publ', 'regex_2018_count': 33, 'regex_complex_found': []}}

exec(code, env_args)
