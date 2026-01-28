code = """import json

# Load citations data
file_path_citations = locals()['var_function-call-3647625760159840601']
with open(file_path_citations, 'r') as f:
    citations_data = json.load(f)

# Load paper docs
file_path_papers = locals()['var_function-call-7977022267260973965']
with open(file_path_papers, 'r') as f:
    paper_docs = json.load(f)

# Create a dictionary for quick lookup of paper text by filename
# Filename is the key. Text is the value.
paper_map = {doc['filename']: doc['text'] for doc in paper_docs}

acm_citations = []
missing_papers = 0

for item in citations_data:
    title = item['title']
    citation_count = int(item['citation_count'])
    filename = title + ".txt"
    
    if filename in paper_map:
        text = paper_map[filename]
        # Check for ACM in the text
        # To be slightly more robust, we might look for "ACM" as a word, 
        # but the prompt implies extraction. "ACM" is usually a substring.
        if "ACM" in text:
            acm_citations.append(citation_count)
    else:
        missing_papers += 1

if acm_citations:
    average_citations = sum(acm_citations) / len(acm_citations)
else:
    average_citations = 0

print(f"DEBUG: Found {len(acm_citations)} ACM papers out of {len(citations_data)} cited papers.")
print(f"DEBUG: Missing papers in Mongo: {missing_papers}")

print("__RESULT__:")
print(json.dumps(average_citations))"""

env_args = {'var_function-call-5264272901715907644': ['Citations', 'sqlite_sequence'], 'var_function-call-5264272901715907989': ['paper_docs'], 'var_function-call-3647625760159840601': 'file_storage/function-call-3647625760159840601.json', 'var_function-call-16517880119813488158': 158, 'var_function-call-6596666326870079897': 'file_storage/function-call-6596666326870079897.json', 'var_function-call-7977022267260973965': 'file_storage/function-call-7977022267260973965.json'}

exec(code, env_args)
