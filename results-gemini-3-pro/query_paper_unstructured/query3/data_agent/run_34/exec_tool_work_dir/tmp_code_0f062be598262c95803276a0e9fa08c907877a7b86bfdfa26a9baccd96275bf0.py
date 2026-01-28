code = """import json
import re

# Load Citations
citation_file = locals()['var_function-call-3193368456383189036']
with open(citation_file, 'r') as f:
    citations_list = json.load(f)

citation_map = {}
for item in citations_list:
    citation_map[item['title']] = item['total_citations']

# Load Papers
papers_file = locals()['var_function-call-13531993563476914468']
with open(papers_file, 'r') as f:
    papers = json.load(f)

print(f"Total papers: {len(papers)}")

for i, paper in enumerate(papers[:5]):
    filename = paper.get('filename', '')
    title = filename[:-4] if filename.endswith('.txt') else filename
    text = paper.get('text', '')
    header = text[:1000]
    
    years = re.findall(r'\b(20(?:1[7-9]|2[0-9]))\b', header)
    
    has_empirical = 'empirical' in text.lower()
    
    print(f"Paper {i}: {title}")
    print(f"  Years found: {years}")
    print(f"  Has empirical: {has_empirical}")
    print(f"  In Citation Map: {title in citation_map}")
    if title in citation_map:
        print(f"  Citations: {citation_map[title]}")

results = []
# ... (rest of logic)
print("__RESULT__:")
print(json.dumps("DEBUG"))"""

env_args = {'var_function-call-224810883549294860': 'file_storage/function-call-224810883549294860.json', 'var_function-call-9456626268790233779': ['paper_docs'], 'var_function-call-16636765420084793523': [{'_id': '694f5530284b10b11dc0a869', 'filename': 'A Lived Informatics Model of Personal Informatics.txt'}, {'_id': '694f5530284b10b11dc0a86a', 'filename': 'A Stage-based Model of Personal Informatics Systems.txt'}, {'_id': '694f5530284b10b11dc0a86b', 'filename': 'A Trip to the Moon: Personalized Animated Movies for Self-reflection.txt'}, {'_id': '694f5530284b10b11dc0a86c', 'filename': 'A Wee Bit More Interaction: Designing and Evaluating an Overactive Bladder App.txt'}, {'_id': '694f5530284b10b11dc0a86d', 'filename': 'ArmSleeve: A Patient Monitoring System to Support Occupational Therapists in Stroke Rehabilitation.txt'}], 'var_function-call-3193368456383189036': 'file_storage/function-call-3193368456383189036.json', 'var_function-call-13531993563476914468': 'file_storage/function-call-13531993563476914468.json', 'var_function-call-13038935966288007214': []}

exec(code, env_args)
