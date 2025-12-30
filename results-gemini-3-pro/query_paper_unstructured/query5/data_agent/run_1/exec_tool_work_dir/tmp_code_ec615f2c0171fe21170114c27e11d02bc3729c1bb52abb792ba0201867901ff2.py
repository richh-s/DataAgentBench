code = """import json
import re

# Load paper docs
with open(locals()['var_function-call-17247428670658995703'], 'r') as f:
    paper_docs = json.load(f)

target_title = "A Stage-based Model of Personal Informatics Systems.txt"
target_doc = next((d for d in paper_docs if d['filename'] == target_title), None)

result = {}
if target_doc:
    text = target_doc['text']
    # Find all occurrences of "CHI"
    matches = [m.span() for m in re.finditer(r"CHI", text)]
    
    # Extract context for each match
    contexts = []
    for start, end in matches:
        ctx = text[max(0, start-50):min(len(text), end+50)]
        contexts.append(ctx.replace("\n", " "))
    
    result["contexts"] = contexts[:10]
    result["found_chi_2010"] = "CHI 2010" in text or "CHI '10" in text

print("__RESULT__:")
print(json.dumps(result))"""

env_args = {'var_function-call-12437250052302532993': 'file_storage/function-call-12437250052302532993.json', 'var_function-call-17247428670658995703': 'file_storage/function-call-17247428670658995703.json', 'var_function-call-767057999987748063': 16, 'var_function-call-17271081787061420733': 16, 'var_function-call-10439916293815859342': {'total_citations': 0, 'count': 0, 'titles': []}, 'var_function-call-8934908314266514909': 'Done', 'var_function-call-11988350588739506600': {'headers': [{'title': 'A Lived Informatics Model of Personal Informatics.txt', 'header': "UBICOMP '15, SEPTEMBER 7–11, 2015, OSAKA, JAPAN\n\nA Lived Informatics Model of Personal Informatics \n\nDaniel A. Epstein1, An Ping2, James Fogarty1, Sean A. Munson2 \n1Computer Science & Engineering, 2Hu"}, {'title': 'A Stage-based Model of Personal Informatics Systems.txt', 'header': 'A Stage-Based Model of Personal Informatics Systems \nIan Li1, Anind Dey1, and Jodi Forlizzi1,2 \n1Human Computer Interaction Institute, 2School of Design \nCarnegie Mellon University, Pittsburgh, PA 152'}, {'title': 'A Trip to the Moon: Personalized Animated Movies for Self-reflection.txt', 'header': 'Fengjiao Peng\nMIT Media Lab\nCambridge, MA, USA\nfpeng@mit.edu\n\nA Trip to the Moon: Personalized Animated Movies for\nSelf-reﬂection\nVeronica Crista LaBelle\nMIT\nCambridge, MA, USA\nvlabelle@mit.edu\nRosali'}], 'num_chi_matches': 0, 'sample_matches': []}}

exec(code, env_args)
