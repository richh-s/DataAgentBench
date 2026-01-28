code = """import json
import re

# Load paper docs
with open(locals()['var_function-call-14323313354234643834'], 'r') as f:
    papers = json.load(f)

# Load citations
with open(locals()['var_function-call-7764328309385985012'], 'r') as f:
    citations = json.load(f)

# Aggregate citations by title
citation_map = {}
for c in citations:
    t = c['title']
    try:
        count = int(c['citation_count'])
    except:
        count = 0
    citation_map[t] = citation_map.get(t, 0) + count

results = []

for p in papers:
    filename = p.get('filename', '')
    text = p.get('text', '')
    title = filename.replace('.txt', '')
    
    # Extract Year
    header = text[:1000] # Search first 1000 chars
    # Find 2016
    # We look for "2016" explicitly.
    # Also look for patterns like "'16" which might be "Ubicomp '16"
    
    has_2016 = '2016' in header
    has_apostrophe_16 = "'16" in header
    
    published_in_2016 = has_2016 or has_apostrophe_16
    
    # Extract Domain
    # Use first 5000 chars
    content_sample = text[:5000].lower()
    is_physical_activity = 'physical activity' in content_sample
    
    if published_in_2016 and is_physical_activity:
        total_citations = citation_map.get(title, 0)
        results.append({"title": title, "citation_count": total_citations})

print("__RESULT__:")
print(json.dumps(results))"""

env_args = {'var_function-call-8814252410451424238': ['paper_docs'], 'var_function-call-5259206578733669392': 'file_storage/function-call-5259206578733669392.json', 'var_function-call-14323313354234643834': 'file_storage/function-call-14323313354234643834.json', 'var_function-call-12161874527337870347': ['Citations', 'sqlite_sequence'], 'var_function-call-7764328309385985012': 'file_storage/function-call-7764328309385985012.json', 'var_function-call-3369097710081167039': [], 'var_function-call-6510332609486320018': [{'title': 'A Lived Informatics Model of Personal Informatics.txt', 'years': [], 'has_pa': True}, {'title': 'A Stage-based Model of Personal Informatics Systems.txt', 'years': [], 'has_pa': True}, {'title': 'A Trip to the Moon: Personalized Animated Movies for Self-reflection.txt', 'years': [], 'has_pa': False}, {'title': 'A Wee Bit More Interaction: Designing and Evaluating an Overactive Bladder App.txt', 'years': [], 'has_pa': False}, {'title': 'ArmSleeve: A Patient Monitoring System to Support Occupational Therapists in Stroke Rehabilitation.txt', 'years': [], 'has_pa': False}], 'var_function-call-5498128891951429973': "UBICOMP '15, SEPTEMBER 7–11, 2015, OSAKA, JAPAN\n\nA Lived Informatics Model of Personal Informatics \n\nDaniel A. Epstein1, An Ping2, James Fogarty1, Sean A. Munson2 \n1Computer Science & Engineering, 2Human Centered Design & Engineering \nDUB Group, University of Washington \n{depstein, jfogarty}@cs.washington.edu, {anping, smunson}@uw.edu \n\nABSTRACT \nCurrent  models  of  how  people  use  personal  informatics \nsystems are largely based in behavior change goals. They do \nnot  adequately  characteriz", 'var_function-call-2372319320552918241': []}

exec(code, env_args)
