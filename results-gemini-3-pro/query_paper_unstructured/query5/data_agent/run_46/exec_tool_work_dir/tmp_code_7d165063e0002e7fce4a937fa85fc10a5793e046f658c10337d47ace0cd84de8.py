code = """import json
import re

# Load citations
citations_path = locals()['var_function-call-7904474651748754030']
with open(citations_path, 'r') as f:
    citations = json.load(f)

# Load paper docs
papers_path = locals()['var_function-call-17007904567241461401']
with open(papers_path, 'r') as f:
    papers = json.load(f)

chi_papers = set()
debug_info = []

regex = re.compile(r"\bCHI\s+(?:'?[0-9]{2}|20[0-9]{2}|Conference)\b")
regex_full = re.compile(r"Conference on Human Factors in Computing Systems", re.IGNORECASE)

for p in papers:
    text = p.get('text', '')
    filename = p.get('filename', '')
    title = filename.replace('.txt', '')
    
    # Check first 3000 chars
    header = text[:3000]
    
    match = False
    match_str = ""
    m = regex.search(header)
    if m:
        match = True
        match_str = m.group(0)
    elif regex_full.search(header):
        match = True
        match_str = "Full Title"
        
    if match:
        chi_papers.add(title)
        debug_info.append({"title": title, "match": match_str})

# Get citations
results = []
total_citations = 0

for c in citations:
    if c['title'] in chi_papers:
        count = int(c['citation_count'])
        total_citations += count
        results.append({"title": c['title'], "count": count})

# Sort results by count desc
results.sort(key=lambda x: x['count'], reverse=True)

print("__RESULT__:")
print(json.dumps({"total": total_citations, "papers": results, "debug_count": len(results)}))"""

env_args = {'var_function-call-7904474651748754030': 'file_storage/function-call-7904474651748754030.json', 'var_function-call-7904474651748757041': ['paper_docs'], 'var_function-call-17007904567241461401': 'file_storage/function-call-17007904567241461401.json', 'var_function-call-17338515431943549083': 0, 'var_function-call-3882758267004127089': ["UBICOMP '15, SEPTEMBER 7–11, 2015, OSAKA, JAPAN\n\nA Lived Informatics Model of Personal Informatics \n\nDaniel A. Epstein1, An Ping2, James Fogarty1, Sean A. Munson2 \n1Computer Science & Engineering, 2Hu", 'A Stage-Based Model of Personal Informatics Systems \nIan Li1, Anind Dey1, and Jodi Forlizzi1,2 \n1Human Computer Interaction Institute, 2School of Design \nCarnegie Mellon University, Pittsburgh, PA 152', 'Fengjiao Peng\nMIT Media Lab\nCambridge, MA, USA\nfpeng@mit.edu\n\nA Trip to the Moon: Personalized Animated Movies for\nSelf-reﬂection\nVeronica Crista LaBelle\nMIT\nCambridge, MA, USA\nvlabelle@mit.edu\nRosali', 'A Wee Bit More Interaction: Designing and Evaluating  \nan Overactive Bladder App\n\nAna-Maria Salai \n Heriot-Watt University \n Edinburgh, UK \n as152@hw.ac.uk \n\nLynne Baillie \n Heriot-Watt University \n E', 'ArmSleeve: a Patient Monitoring System to Support \nOccupational Therapists in Stroke Rehabilitation \nBernd Ploderer1,2, Justin Fong1,3, Anusha Withana1,4, Marlena Klaic1,5, Siddharth Nair1, \nVincent C'], 'var_function-call-16749428879592176110': 'file_storage/function-call-16749428879592176110.json', 'var_function-call-13008448883570274800': 16}

exec(code, env_args)
