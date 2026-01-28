code = """import json
import re

# Load data
with open(locals()['var_function-call-15899723909047088907'], 'r') as f:
    citations_data = json.load(f)

with open(locals()['var_function-call-3855934582646754385'], 'r') as f:
    paper_docs = json.load(f)

citation_map = {item['title']: int(item['citation_count']) for item in citations_data}

results = []
total_citation_count_for_chi = 0

for doc in paper_docs:
    filename = doc['filename']
    text = doc['text']
    title = filename.replace('.txt', '')
    
    # Check venue in full text
    # Regex: Look for CHI 20xx or CHI 'xx or Proceedings of ... CHI
    # or just \bCHI\b
    
    # Let's find all occurrences of CHI in the text to see context
    matches = re.findall(r'.{0,20}\bCHI\b.{0,20}', text)
    
    is_chi = False
    # logic: if "CHI" appears with year or "Proceedings", or "Conference", it's likely.
    # Note: "Human-Computer Interaction" does NOT contain "\bCHI\b".
    # But "CHI" might be in references.
    # We want the paper's venue.
    # Usually in the first page (header/footer) or first few lines.
    
    # Improved check:
    # 1. Check first 2000 chars (Header/Footer of first page)
    # 2. Look for specific patterns: "CHI '", "CHI 20", "CHI Conference"
    
    header = text[:3000]
    if re.search(r'\bCHI\b', header):
        is_chi = True
    elif re.search(r'Conference on Human Factors in Computing Systems', header, re.IGNORECASE):
        is_chi = True
        
    citation_count = citation_map.get(title, 0)
    
    if is_chi:
        total_citation_count_for_chi += citation_count
        
    results.append({
        'title': title,
        'is_chi': is_chi,
        'citation_count': citation_count,
        'chi_matches_preview': matches[:3] if matches else []
    })

print("__RESULT__:")
print(json.dumps(results))"""

env_args = {'var_function-call-15899723909047088907': 'file_storage/function-call-15899723909047088907.json', 'var_function-call-3855934582646754385': 'file_storage/function-call-3855934582646754385.json', 'var_function-call-1503467888585593551': 16, 'var_function-call-8360086273377805930': {'total_docs': 5, 'chi_papers_count': 0, 'total_citations': 0, 'sample_chi_papers': [], 'sample_non_chi_headers': [{'title': 'A Lived Informatics Model of Personal Informatics.txt', 'header': "UBICOMP '15, SEPTEMBER 7–11, 2015, OSAKA, JAPAN\n\nA Lived Informatics Model of Personal Informatics \n\nDaniel A. Epstein1, An Ping2, James Fogarty1, Sean A. Munson2 \n1Computer Science & Engineering, 2Hu"}, {'title': 'A Stage-based Model of Personal Informatics Systems.txt', 'header': 'A Stage-Based Model of Personal Informatics Systems \nIan Li1, Anind Dey1, and Jodi Forlizzi1,2 \n1Human Computer Interaction Institute, 2School of Design \nCarnegie Mellon University, Pittsburgh, PA 152'}, {'title': 'A Trip to the Moon: Personalized Animated Movies for Self-reflection.txt', 'header': 'Fengjiao Peng\nMIT Media Lab\nCambridge, MA, USA\nfpeng@mit.edu\n\nA Trip to the Moon: Personalized Animated Movies for\nSelf-reﬂection\nVeronica Crista LaBelle\nMIT\nCambridge, MA, USA\nvlabelle@mit.edu\nRosali'}, {'title': 'A Wee Bit More Interaction: Designing and Evaluating an Overactive Bladder App.txt', 'header': 'A Wee Bit More Interaction: Designing and Evaluating  \nan Overactive Bladder App\n\nAna-Maria Salai \n Heriot-Watt University \n Edinburgh, UK \n as152@hw.ac.uk \n\nLynne Baillie \n Heriot-Watt University \n E'}, {'title': 'ArmSleeve: A Patient Monitoring System to Support Occupational Therapists in Stroke Rehabilitation.txt', 'header': 'ArmSleeve: a Patient Monitoring System to Support \nOccupational Therapists in Stroke Rehabilitation \nBernd Ploderer1,2, Justin Fong1,3, Anusha Withana1,4, Marlena Klaic1,5, Siddharth Nair1, \nVincent C'}]}}

exec(code, env_args)
