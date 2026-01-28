code = """import json
import re

# Load citations
with open(locals()['var_function-call-12437250052302532993'], 'r') as f:
    citations_data = json.load(f)

# Filter citations for 2020
citations_2020 = {}
for item in citations_data:
    if int(item['citation_count']) > 0: 
        citations_2020[item['title']] = int(item['citation_count'])

# Load paper docs
with open(locals()['var_function-call-17247428670658995703'], 'r') as f:
    paper_docs = json.load(f)

total_citations = 0
matched_papers = []

# Regex for CHI
# Match "CHI 2010", "CHI '10", "CHI 10", "CHI-10"
# \s* allows spaces. .? allows ' or space or nothing.
chi_pattern = re.compile(r"CHI\s*['\-]?\s*\d{2,4}")
human_factors_pattern = re.compile(r"Human Factors in Computing Systems")
proc_chi_pattern = re.compile(r"Proceedings of.*CHI")

for doc in paper_docs:
    filename = doc['filename']
    title = filename.rsplit('.', 1)[0]
    
    if title in citations_2020:
        text = doc['text']
        
        is_chi = False
        if chi_pattern.search(text):
            is_chi = True
        elif human_factors_pattern.search(text):
            is_chi = True
        elif proc_chi_pattern.search(text):
            is_chi = True
            
        if is_chi:
            count = citations_2020[title]
            total_citations += count
            matched_papers.append(title)

result = {
    "total_citations": total_citations,
    "matched_count": len(matched_papers),
    "sample_titles": matched_papers[:5]
}

print("__RESULT__:")
print(json.dumps(result))"""

env_args = {'var_function-call-12437250052302532993': 'file_storage/function-call-12437250052302532993.json', 'var_function-call-17247428670658995703': 'file_storage/function-call-17247428670658995703.json', 'var_function-call-767057999987748063': 16, 'var_function-call-17271081787061420733': 16, 'var_function-call-10439916293815859342': {'total_citations': 0, 'count': 0, 'titles': []}, 'var_function-call-8934908314266514909': 'Done', 'var_function-call-11988350588739506600': {'headers': [{'title': 'A Lived Informatics Model of Personal Informatics.txt', 'header': "UBICOMP '15, SEPTEMBER 7–11, 2015, OSAKA, JAPAN\n\nA Lived Informatics Model of Personal Informatics \n\nDaniel A. Epstein1, An Ping2, James Fogarty1, Sean A. Munson2 \n1Computer Science & Engineering, 2Hu"}, {'title': 'A Stage-based Model of Personal Informatics Systems.txt', 'header': 'A Stage-Based Model of Personal Informatics Systems \nIan Li1, Anind Dey1, and Jodi Forlizzi1,2 \n1Human Computer Interaction Institute, 2School of Design \nCarnegie Mellon University, Pittsburgh, PA 152'}, {'title': 'A Trip to the Moon: Personalized Animated Movies for Self-reflection.txt', 'header': 'Fengjiao Peng\nMIT Media Lab\nCambridge, MA, USA\nfpeng@mit.edu\n\nA Trip to the Moon: Personalized Animated Movies for\nSelf-reﬂection\nVeronica Crista LaBelle\nMIT\nCambridge, MA, USA\nvlabelle@mit.edu\nRosali'}], 'num_chi_matches': 0, 'sample_matches': []}}

exec(code, env_args)
