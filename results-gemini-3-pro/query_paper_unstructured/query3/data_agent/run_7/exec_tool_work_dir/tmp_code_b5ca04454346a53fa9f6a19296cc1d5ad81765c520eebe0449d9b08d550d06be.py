code = """import json
import re

# Load Citations
with open(locals()['var_function-call-17351178727143063215'], 'r') as f:
    citations_data = json.load(f)

title_citations = {}
for entry in citations_data:
    t = entry['title']
    title_citations[t] = 1 # Just mark existence

# Load Paper Docs
with open(locals()['var_function-call-6826266574938027314'], 'r') as f:
    papers = json.load(f)

debug_info = []
for i, paper in enumerate(papers[:20]):
    filename = paper.get('filename', '')
    text = paper.get('text', '')
    title = filename.replace('.txt', '')
    
    header = text[:1000]
    years = re.findall(r'\b(20\d{2})\b', header)
    year = int(years[0]) if years else None
    
    is_empirical = "empirical" in text.lower()
    in_citations = title in title_citations
    
    debug_info.append({
        "title": title,
        "year": year,
        "is_empirical": is_empirical,
        "in_citations": in_citations
    })

print("__RESULT__:")
print(json.dumps(debug_info))"""

env_args = {'var_function-call-5913521790257705875': 'file_storage/function-call-5913521790257705875.json', 'var_function-call-16603125726449287240': 'file_storage/function-call-16603125726449287240.json', 'var_function-call-10308318711084612855': [{'_id': '694f5530284b10b11dc0a869', 'filename': 'A Lived Informatics Model of Personal Informatics.txt'}, {'_id': '694f5530284b10b11dc0a86a', 'filename': 'A Stage-based Model of Personal Informatics Systems.txt'}, {'_id': '694f5530284b10b11dc0a86b', 'filename': 'A Trip to the Moon: Personalized Animated Movies for Self-reflection.txt'}, {'_id': '694f5530284b10b11dc0a86c', 'filename': 'A Wee Bit More Interaction: Designing and Evaluating an Overactive Bladder App.txt'}, {'_id': '694f5530284b10b11dc0a86d', 'filename': 'ArmSleeve: A Patient Monitoring System to Support Occupational Therapists in Stroke Rehabilitation.txt'}], 'var_function-call-12915355983397043581': [{'count(*)': '1405'}], 'var_function-call-17351178727143063215': 'file_storage/function-call-17351178727143063215.json', 'var_function-call-17424668251812217862': 'file_storage/function-call-17424668251812217862.json', 'var_function-call-6826266574938027314': 'file_storage/function-call-6826266574938027314.json', 'var_function-call-7280082780151386652': []}

exec(code, env_args)
