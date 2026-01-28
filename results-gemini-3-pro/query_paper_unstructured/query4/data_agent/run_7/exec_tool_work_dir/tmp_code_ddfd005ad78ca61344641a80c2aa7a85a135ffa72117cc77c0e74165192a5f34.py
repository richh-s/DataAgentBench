code = """import json

with open(locals()['var_function-call-13906461946553771185'], 'r') as f:
    paper_docs = json.load(f)

debug_info = {}
debug_info["total_docs"] = len(paper_docs)

papers_2016 = []
papers_phys = []
sample_header = ""

for doc in paper_docs:
    text = doc.get('text', '')
    header = text[:1000]
    
    if "2016" in header:
        papers_2016.append(doc.get('filename'))
        
    if "physical activity" in text.lower()[:5000]:
        papers_phys.append(doc.get('filename'))

    if not sample_header:
        sample_header = header[:200]

debug_info["count_2016"] = len(papers_2016)
debug_info["count_phys"] = len(papers_phys)
debug_info["intersection"] = list(set(papers_2016).intersection(set(papers_phys)))
debug_info["sample_header"] = sample_header

print("__RESULT__:")
print(json.dumps(debug_info))"""

env_args = {'var_function-call-5218844926592326471': ['paper_docs'], 'var_function-call-5218844926592327304': ['Citations', 'sqlite_sequence'], 'var_function-call-3045611188522186041': 'file_storage/function-call-3045611188522186041.json', 'var_function-call-13906461946553771185': 'file_storage/function-call-13906461946553771185.json', 'var_function-call-3552239526712038918': 'file_storage/function-call-3552239526712038918.json', 'var_function-call-12956520315501172365': {}, 'var_function-call-11308566918737790029': 'debug_done'}

exec(code, env_args)
