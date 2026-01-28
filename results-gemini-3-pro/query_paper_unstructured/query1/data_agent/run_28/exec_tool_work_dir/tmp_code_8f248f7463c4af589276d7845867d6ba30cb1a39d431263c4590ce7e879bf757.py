code = """import json
import re

citations_path = locals()['var_function-call-12816615437608771062']
with open(citations_path, 'r') as f:
    citations = json.load(f)

papers_path = locals()['var_function-call-6011285741143756461']
with open(papers_path, 'r') as f:
    papers = json.load(f)

print(f"Total papers: {len(papers)}")
print(f"Total citations records: {len(citations)}")

# Check title matching
p_titles = [p['filename'].replace('.txt', '') for p in papers[:5]]
c_titles = [c['title'] for c in citations[:5]]
print(f"Sample Paper Titles: {p_titles}")
print(f"Sample Citation Titles: {c_titles}")

# Check for 'food' in text
food_mention_count = 0
for p in papers:
    if 'food' in p['text'].lower():
        food_mention_count += 1

print(f"Papers mentioning 'food' in text: {food_mention_count}")

# Check Keyword extraction for a paper that mentions food
for p in papers:
    if 'food' in p['text'].lower():
        print(f"--- Processing paper: {p['filename']} ---")
        match = re.search(r"Author Keywords\s*(.*?)\s*(?:ACM Classification Keywords|INTRODUCTION|Index Terms|ABSTRACT|General Terms)", p['text'], re.DOTALL | re.IGNORECASE)
        if match:
            print(f"Extracted Keywords: {match.group(1)[:200]}...")
        else:
            print("Keywords extraction failed.")
            # Print area around "Author Keywords" if present
            start = p['text'].lower().find("author keywords")
            if start != -1:
                print(f"Context around 'Author Keywords': {p['text'][start:start+200]}...")
            else:
                print("'Author Keywords' not found in text.")
        
        # Stop after 3 examples
        if food_mention_count > 0: # just to use the variable
            break

print("__RESULT__:")
print(json.dumps("debug done"))"""

env_args = {'var_function-call-1408029875395216778': 'file_storage/function-call-1408029875395216778.json', 'var_function-call-12816615437608771062': 'file_storage/function-call-12816615437608771062.json', 'var_function-call-6011285741143756461': 'file_storage/function-call-6011285741143756461.json', 'var_function-call-4970845110660497664': 0}

exec(code, env_args)
