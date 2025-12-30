code = """import json
import re

with open(locals()['var_function-call-6893631717039984758'], 'r') as f:
    paper_docs = json.load(f)

food_domain_papers = []
for doc in paper_docs:
    text = doc['text']
    title = doc['filename'].replace('.txt', '')
    
    # Attempt to find a line starting with 'domain:' or 'domains:' case-insensitively
    match = re.search(r'^\s*domains?:\s*(.*?)(?:\n|$)', text, re.IGNORECASE | re.MULTILINE)
    if match:
        domains_str = match.group(1)
        # Check if 'food' is present in the extracted domains string (case-insensitive)
        if 'food' in domains_str.lower():
            food_domain_papers.append(title)
    else:
        # Fallback: if explicit 'domain:' line not found, check if 'food' appears in the abstract or keywords section
        # This is a heuristic and might pick up false positives, but necessary if structured domain info is missing.
        # Let's try to focus on sections that might indicate the topic more strongly.
        # For now, let's keep the initial broad search if a specific domain line is not found.
        # If the direct domain match fails, we can reconsider a more general search for 'food' in the text later.
        pass # For now, we strictly look for 'domain: food' or similar.

print("__RESULT__:")
print(json.dumps(food_domain_papers))"""

env_args = {'var_function-call-8792593880583760035': ['paper_docs'], 'var_function-call-9978232910626699419': [], 'var_function-call-6497029258880074568': ['Citations', 'sqlite_sequence'], 'var_function-call-6893631717039984758': 'file_storage/function-call-6893631717039984758.json', 'var_function-call-9273036665786985738': [], 'var_function-call-14011650007027942934': []}

exec(code, env_args)
