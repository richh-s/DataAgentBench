code = """import json
import re

papers_path = locals()['var_function-call-17007904567241461401']
with open(papers_path, 'r') as f:
    papers = json.load(f)

debug_out = {}

# Find "A Stage-Based Model..."
target_paper = None
for p in papers:
    if "Stage-Based Model" in p['filename']:
        target_paper = p
        break

if target_paper:
    text = target_paper['text']
    idx = text.find("CHI 2010")
    debug_out["found_index"] = idx
    if idx != -1:
        snippet = text[idx-10:idx+20]
        debug_out["snippet"] = snippet
        
        regex = re.compile(r"CHI\s+(?:'?[0-9]{2}|20[0-9]{2}|Conference)")
        match = regex.search(snippet)
        debug_out["snippet_match"] = str(match)
        
        header = text[:3000]
        match_header = regex.search(header)
        debug_out["header_match"] = str(match_header)
        debug_out["header_len"] = len(header)
        # Check if index is within header
        debug_out["is_in_header"] = idx < 3000

print("__RESULT__:")
print(json.dumps(debug_out))"""

env_args = {'var_function-call-7904474651748754030': 'file_storage/function-call-7904474651748754030.json', 'var_function-call-7904474651748757041': ['paper_docs'], 'var_function-call-17007904567241461401': 'file_storage/function-call-17007904567241461401.json', 'var_function-call-17338515431943549083': 0, 'var_function-call-3882758267004127089': ["UBICOMP '15, SEPTEMBER 7–11, 2015, OSAKA, JAPAN\n\nA Lived Informatics Model of Personal Informatics \n\nDaniel A. Epstein1, An Ping2, James Fogarty1, Sean A. Munson2 \n1Computer Science & Engineering, 2Hu", 'A Stage-Based Model of Personal Informatics Systems \nIan Li1, Anind Dey1, and Jodi Forlizzi1,2 \n1Human Computer Interaction Institute, 2School of Design \nCarnegie Mellon University, Pittsburgh, PA 152', 'Fengjiao Peng\nMIT Media Lab\nCambridge, MA, USA\nfpeng@mit.edu\n\nA Trip to the Moon: Personalized Animated Movies for\nSelf-reﬂection\nVeronica Crista LaBelle\nMIT\nCambridge, MA, USA\nvlabelle@mit.edu\nRosali', 'A Wee Bit More Interaction: Designing and Evaluating  \nan Overactive Bladder App\n\nAna-Maria Salai \n Heriot-Watt University \n Edinburgh, UK \n as152@hw.ac.uk \n\nLynne Baillie \n Heriot-Watt University \n E', 'ArmSleeve: a Patient Monitoring System to Support \nOccupational Therapists in Stroke Rehabilitation \nBernd Ploderer1,2, Justin Fong1,3, Anusha Withana1,4, Marlena Klaic1,5, Siddharth Nair1, \nVincent C'], 'var_function-call-16749428879592176110': 'file_storage/function-call-16749428879592176110.json', 'var_function-call-13008448883570274800': 16, 'var_function-call-16605389762593211804': {'total': 16, 'papers': [{'title': 'A Wee Bit More Interaction: Designing and Evaluating an Overactive Bladder App', 'count': 16}], 'debug_count': 1}, 'var_function-call-16952685088804943931': {'chi_papers_found': [], 'total_docs': 5, 'total_citations_records': 188}, 'var_function-call-5902922130843711665': 'Debug Done'}

exec(code, env_args)
