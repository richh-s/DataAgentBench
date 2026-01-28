code = """import json
import re

citations_path = locals()['var_function-call-12939429308500753230']
with open(citations_path, 'r') as f:
    citations = json.load(f)

papers_path = locals()['var_function-call-16000447345319300331']
with open(papers_path, 'r') as f:
    papers = json.load(f)

print(f"DEBUG: Total papers loaded: {len(papers)}")

chi_titles = set()
for p in papers:
    text = p.get('text', '')
    header = text[:2000] # Check first 2000 chars
    
    # Heuristic: CHI paper if 'CHI' appears in header in specific formats
    # 1. "CHI 'YY"
    # 2. "CHI 20YY"
    # 3. "CHI Conference"
    # 4. "Proceedings of the ... CHI"
    # 5. "CHI <Year>"
    # 6. "Conference on Human Factors in Computing Systems"
    
    # Regex to capture CHI followed by year or 'Conference' or used as a venue name
    # We use a broad regex but check for typical venue patterns
    # The UbiComp example: "UBICOMP '15"
    # So "CHI '15" or "CHI 2015"
    
    if re.search(r'\bCHI\s*[\'’]?\d{2,4}\b', header) or \
       "Conference on Human Factors in Computing Systems" in header or \
       "CHI Conference" in header:
       title = p.get('filename', '').replace('.txt', '')
       chi_titles.add(title)

print(f"DEBUG: Identified {len(chi_titles)} CHI papers.")
# print(f"DEBUG: Sample CHI titles: {list(chi_titles)[:5]}")

total_citations = 0
for c in citations:
    title = c.get('title')
    count = c.get('citation_count')
    try:
        count = int(count)
    except:
        count = 0
        
    if title in chi_titles:
        total_citations += count

print("__RESULT__:")
print(total_citations)"""

env_args = {'var_function-call-16274009200495380828': 'file_storage/function-call-16274009200495380828.json', 'var_function-call-12939429308500753230': 'file_storage/function-call-12939429308500753230.json', 'var_function-call-13758046956340935094': 0, 'var_function-call-9966761655225880711': [], 'var_function-call-14800163327184198750': ['A Lived Informatics Model of Personal Informatics.txt'], 'var_function-call-11830425974286538439': 'file_storage/function-call-11830425974286538439.json', 'var_function-call-2236700066034859830': 0, 'var_function-call-12172345065077617984': {'status': 'debug complete'}, 'var_function-call-10740177925653751964': {'total_papers': 5, 'total_citations': 188, 'overlap_count': 4, 'samples': [{'title': 'A Lived Informatics Model of Personal Informatics.txt', 'found_chi': True, 'index': 61983, 'snippet': 'CHI 20, 5 (2013), 1-27. \n\n4.  Bentley, F. and Toll'}, {'title': 'A Stage-based Model of Personal Informatics Systems.txt', 'found_chi': True, 'index': 2811, 'snippet': 'CHI 2010, April 10–15, 2010, Atlanta, Georgia, USA'}, {'title': 'A Trip to the Moon: Personalized Animated Movies for Self-reflection.txt', 'found_chi': True, 'index': 2513, 'snippet': 'CHI 2018, April 21–26, 2018, Montréal, QC, Canada\n'}, {'title': 'A Wee Bit More Interaction: Designing and Evaluating an Overactive Bladder App.txt', 'found_chi': True, 'index': 1625, 'snippet': 'CHI \nConference on Human Factors in Computing Syst'}, {'title': 'ArmSleeve: A Patient Monitoring System to Support Occupational Therapists in Stroke Rehabilitation.txt', 'found_chi': True, 'index': 63159, 'snippet': 'CHI Conference on Human Factors in Computing \nSyst'}], 'chi_candidates_count': 0, 'chi_candidates_sample': []}, 'var_function-call-16000447345319300331': 'file_storage/function-call-16000447345319300331.json'}

exec(code, env_args)
