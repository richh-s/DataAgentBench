code = """import json
import re

# Load data
with open(locals()['var_function-call-15899723909047088907'], 'r') as f:
    citations_data = json.load(f)
citation_map = {c['title']: int(c['citation_count']) for c in citations_data}

with open(locals()['var_function-call-3855934582646754385'], 'r') as f:
    paper_docs = json.load(f)

results = []

for doc in paper_docs:
    filename = doc['filename']
    title = filename.replace('.txt', '')
    text = doc['text']
    
    # Find all CHI occurrences with context
    matches = []
    # simplified regex to avoid syntax issues
    # finding "CHI" followed by year
    venue_match = "None"
    
    # Check for CHI Year (e.g. CHI '15, CHI 2015)
    if re.search(r'CHI\s*[\']?\d{2}', text):
        venue_match = "CHI Year"
    
    # Check for full name
    if "Conference on Human Factors in Computing Systems" in text:
        venue_match = "CHI Full Name"
        
    # Get context for manual check
    # We'll just take the first 300 chars to see if it looks like a CHI paper
    header = text[:300].replace('\n', ' ')
    
    # Check simple "CHI" presence
    has_chi = "CHI" in text
    
    results.append({
        "title": title,
        "count": citation_map.get(title, 0),
        "venue_detected": venue_match,
        "has_chi": has_chi,
        "header": header
    })

print("__RESULT__:")
print(json.dumps(results))"""

env_args = {'var_function-call-15899723909047088907': 'file_storage/function-call-15899723909047088907.json', 'var_function-call-3855934582646754385': 'file_storage/function-call-3855934582646754385.json', 'var_function-call-1503467888585593551': 16, 'var_function-call-8360086273377805930': {'total_docs': 5, 'chi_papers_count': 0, 'total_citations': 0, 'sample_chi_papers': [], 'sample_non_chi_headers': [{'title': 'A Lived Informatics Model of Personal Informatics.txt', 'header': "UBICOMP '15, SEPTEMBER 7–11, 2015, OSAKA, JAPAN\n\nA Lived Informatics Model of Personal Informatics \n\nDaniel A. Epstein1, An Ping2, James Fogarty1, Sean A. Munson2 \n1Computer Science & Engineering, 2Hu"}, {'title': 'A Stage-based Model of Personal Informatics Systems.txt', 'header': 'A Stage-Based Model of Personal Informatics Systems \nIan Li1, Anind Dey1, and Jodi Forlizzi1,2 \n1Human Computer Interaction Institute, 2School of Design \nCarnegie Mellon University, Pittsburgh, PA 152'}, {'title': 'A Trip to the Moon: Personalized Animated Movies for Self-reflection.txt', 'header': 'Fengjiao Peng\nMIT Media Lab\nCambridge, MA, USA\nfpeng@mit.edu\n\nA Trip to the Moon: Personalized Animated Movies for\nSelf-reﬂection\nVeronica Crista LaBelle\nMIT\nCambridge, MA, USA\nvlabelle@mit.edu\nRosali'}, {'title': 'A Wee Bit More Interaction: Designing and Evaluating an Overactive Bladder App.txt', 'header': 'A Wee Bit More Interaction: Designing and Evaluating  \nan Overactive Bladder App\n\nAna-Maria Salai \n Heriot-Watt University \n Edinburgh, UK \n as152@hw.ac.uk \n\nLynne Baillie \n Heriot-Watt University \n E'}, {'title': 'ArmSleeve: A Patient Monitoring System to Support Occupational Therapists in Stroke Rehabilitation.txt', 'header': 'ArmSleeve: a Patient Monitoring System to Support \nOccupational Therapists in Stroke Rehabilitation \nBernd Ploderer1,2, Justin Fong1,3, Anusha Withana1,4, Marlena Klaic1,5, Siddharth Nair1, \nVincent C'}]}, 'var_function-call-12532326232925806264': [{'title': 'A Lived Informatics Model of Personal Informatics', 'is_chi': False, 'citation_count': 77, 'chi_matches_preview': []}, {'title': 'A Stage-based Model of Personal Informatics Systems', 'is_chi': False, 'citation_count': 0, 'chi_matches_preview': []}, {'title': 'A Trip to the Moon: Personalized Animated Movies for Self-reflection', 'is_chi': False, 'citation_count': 98, 'chi_matches_preview': []}, {'title': 'A Wee Bit More Interaction: Designing and Evaluating an Overactive Bladder App', 'is_chi': True, 'citation_count': 16, 'chi_matches_preview': []}, {'title': 'ArmSleeve: A Patient Monitoring System to Support Occupational Therapists in Stroke Rehabilitation', 'is_chi': False, 'citation_count': 52, 'chi_matches_preview': []}], 'var_function-call-11043960443603343377': {'stage_citations': [{'title': 'Design Opportunities in Three Stages of Relationship Development Between Users and Self-Tracking Devices', 'count': '34'}], 'stage_paper_info': {'filename': 'A Stage-based Model of Personal Informatics Systems.txt', 'header_snippet': 'A Stage-Based Model of Personal Informatics Systems \nIan Li1, Anind Dey1, and Jodi Forlizzi1,2 \n1Human Computer Interaction Institute, 2School of Design \nCarnegie Mellon University, Pittsburgh, PA 15213 \nianli@cmu.edu, {anind, forlizzi}@cs.cmu.edu \n\nABSTRACT \nPeople  strive  to  obtain  self-knowledge.  A  class  of  systems \ncalled  personal  informatics  is  appearing  that  help  people \ncollect and reflect on personal information. However, there \nis no comprehensive list of problems that use', 'has_CHI': True, 'has_Conference': False}}}

exec(code, env_args)
