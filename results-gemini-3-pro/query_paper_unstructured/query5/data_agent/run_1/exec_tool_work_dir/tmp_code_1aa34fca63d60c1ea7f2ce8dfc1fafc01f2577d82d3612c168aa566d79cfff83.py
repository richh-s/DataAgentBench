code = """import json

with open(locals()['var_function-call-12437250052302532993'], 'r') as f:
    citations_data = json.load(f)

target = "A Stage-Based Model of Personal Informatics Systems"
citation_info = next((item for item in citations_data if item['title'] == target), None)

with open(locals()['var_function-call-17247428670658995703'], 'r') as f:
    paper_docs = json.load(f)

doc_info = {}
doc = next((d for d in paper_docs if d['filename'] == target + ".txt"), None)
if doc:
    doc_info["header"] = doc['text'][:500]
    doc_info["contains_CHI"] = "CHI" in doc['text']
    doc_info["contains_CHI_2010"] = "CHI 2010" in doc['text']
    doc_info["contains_CHI_10"] = "CHI '10" in doc['text']

result = {
    "citation_info": citation_info,
    "doc_info": doc_info
}

print("__RESULT__:")
print(json.dumps(result))"""

env_args = {'var_function-call-12437250052302532993': 'file_storage/function-call-12437250052302532993.json', 'var_function-call-17247428670658995703': 'file_storage/function-call-17247428670658995703.json', 'var_function-call-767057999987748063': 16, 'var_function-call-17271081787061420733': 16, 'var_function-call-10439916293815859342': {'total_citations': 0, 'count': 0, 'titles': []}, 'var_function-call-8934908314266514909': 'Done', 'var_function-call-11988350588739506600': {'headers': [{'title': 'A Lived Informatics Model of Personal Informatics.txt', 'header': "UBICOMP '15, SEPTEMBER 7–11, 2015, OSAKA, JAPAN\n\nA Lived Informatics Model of Personal Informatics \n\nDaniel A. Epstein1, An Ping2, James Fogarty1, Sean A. Munson2 \n1Computer Science & Engineering, 2Hu"}, {'title': 'A Stage-based Model of Personal Informatics Systems.txt', 'header': 'A Stage-Based Model of Personal Informatics Systems \nIan Li1, Anind Dey1, and Jodi Forlizzi1,2 \n1Human Computer Interaction Institute, 2School of Design \nCarnegie Mellon University, Pittsburgh, PA 152'}, {'title': 'A Trip to the Moon: Personalized Animated Movies for Self-reflection.txt', 'header': 'Fengjiao Peng\nMIT Media Lab\nCambridge, MA, USA\nfpeng@mit.edu\n\nA Trip to the Moon: Personalized Animated Movies for\nSelf-reﬂection\nVeronica Crista LaBelle\nMIT\nCambridge, MA, USA\nvlabelle@mit.edu\nRosali'}], 'num_chi_matches': 0, 'sample_matches': []}, 'var_function-call-4743684363527587673': {'total_citations': 243, 'matched_count': 4, 'sample_titles': ['A Lived Informatics Model of Personal Informatics', 'A Trip to the Moon: Personalized Animated Movies for Self-reflection', 'A Wee Bit More Interaction: Designing and Evaluating an Overactive Bladder App', 'ArmSleeve: A Patient Monitoring System to Support Occupational Therapists in Stroke Rehabilitation']}, 'var_function-call-8693525776825362795': 'Debug Done'}

exec(code, env_args)
