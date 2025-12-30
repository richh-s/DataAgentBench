code = """import json
import re

citations_file = locals()['var_function-call-332096647494284469']
papers_file = locals()['var_function-call-17780921743028822586']

with open(citations_file, 'r') as f:
    citations_data = json.load(f)

with open(papers_file, 'r') as f:
    papers_data = json.load(f)

# Create citation map
citation_map = {}
for item in citations_data:
    try:
        count = int(item['total_citations'])
    except:
        count = 0
    citation_map[item['title']] = count

results = []
count_2016 = 0
count_pa = 0

for paper in papers_data:
    text = paper.get('text', '')
    filename = paper.get('filename', '')
    title = filename.replace('.txt', '')
    
    header_text = text[:2000]
    
    # Year Extraction
    # Check for 2016 in header
    is_2016 = False
    if '2016' in header_text:
        is_2016 = True
    else:
        # Check specific conference headers
        venues = ["CHI", "Ubicomp", "CSCW", "DIS", "PervasiveHealth", "WWW", "IUI", "OzCHI", "TEI", "AH"]
        pattern = r"(" + "|".join(venues) + r").*?'16"
        if re.search(pattern, header_text, re.IGNORECASE):
            is_2016 = True
            
    if is_2016:
        count_2016 += 1
        
    # Domain Extraction
    is_pa = "physical activity" in text.lower()
    
    if is_pa:
        count_pa += 1
        
    if is_2016 and is_pa:
        # Get citations
        if title in citation_map:
            results.append({"title": title, "citation_count": citation_map[title]})

# Sort results
results.sort(key=lambda x: x['title'])

print("__RESULT__:")
print(json.dumps(results))"""

env_args = {'var_function-call-332096647494284469': 'file_storage/function-call-332096647494284469.json', 'var_function-call-332096647494285302': 'file_storage/function-call-332096647494285302.json', 'var_function-call-9719230712903826217': 'file_storage/function-call-9719230712903826217.json', 'var_function-call-9839691519987756055': [], 'var_function-call-7088723840574718985': [], 'var_function-call-7953638107575930825': {'total_citations': 259, 'total_papers': 5, 'years_in_header': {'2014': 0, '2015': 1, '2016': 0, '2017': 0}, 'pa_count': 4, 'common_titles': 5, 'sample_paper_titles': ['A Wee Bit More Interaction: Designing and Evaluating an Overactive Bladder App', 'ArmSleeve: A Patient Monitoring System to Support Occupational Therapists in Stroke Rehabilitation', 'A Stage-based Model of Personal Informatics Systems'], 'sample_citation_titles': ['What Health Topics Older Adults Want to Track: A Participatory Design Study', 'Communicating Uncertainty in Fertility Prognosis', 'Understanding the Adoption of Quantified Self-tracking Wearable Devices in the Organization Environment: An Empirical Case Study']}, 'var_function-call-17780921743028822586': 'file_storage/function-call-17780921743028822586.json'}

exec(code, env_args)
