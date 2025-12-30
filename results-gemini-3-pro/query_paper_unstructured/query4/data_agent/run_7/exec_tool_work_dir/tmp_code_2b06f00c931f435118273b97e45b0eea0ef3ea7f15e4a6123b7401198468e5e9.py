code = """import json

with open(locals()['var_function-call-13906461946553771185'], 'r') as f:
    paper_docs = json.load(f)

print("Total docs:", len(paper_docs))

papers_2016 = []
papers_phys = []

for doc in paper_docs:
    text = doc.get('text', '')
    header = text[:1000]
    
    if "2016" in header:
        papers_2016.append(doc.get('filename'))
        
    if "physical activity" in text.lower():
        papers_phys.append(doc.get('filename'))

print("Papers with 2016 in header:", len(papers_2016))
print("Papers with 'physical activity':", len(papers_phys))

# Intersection
intersection = set(papers_2016).intersection(set(papers_phys))
print("Intersection:", intersection)

# Print one header from papers_2016 to verify
if papers_2016:
    print("Sample header 2016 paper:", papers_2016[0])
    # Find the doc
    for doc in paper_docs:
        if doc['filename'] == papers_2016[0]:
            print(doc['text'][:500])
            break
else:
    # Print a sample header from any paper to see the year format
    print("Sample header from first paper:")
    print(paper_docs[0]['text'][:500])

print("__RESULT__:")
print(json.dumps("debug_done"))"""

env_args = {'var_function-call-5218844926592326471': ['paper_docs'], 'var_function-call-5218844926592327304': ['Citations', 'sqlite_sequence'], 'var_function-call-3045611188522186041': 'file_storage/function-call-3045611188522186041.json', 'var_function-call-13906461946553771185': 'file_storage/function-call-13906461946553771185.json', 'var_function-call-3552239526712038918': 'file_storage/function-call-3552239526712038918.json', 'var_function-call-12956520315501172365': {}}

exec(code, env_args)
