code = """import json
import re

# Load the result from the previous query (the file path provided in the previous turn)
# The previous turn's key was var_function-call-1041647607165487633
file_path = locals()['var_function-call-1041647607165487633']

with open(file_path, 'r') as f:
    papers = json.load(f)

food_papers = []

def extract_keywords(text):
    # Try to find "Author Keywords" block
    match = re.search(r'Author Keywords\s*\n(.*?)(?:\n\n|\n[A-Z][A-Z\s]+)', text, re.DOTALL | re.IGNORECASE)
    if match:
        return match.group(1)
    return ""

for paper in papers:
    title = paper['filename'].replace('.txt', '')
    text = paper['text']
    
    # Check title
    if 'food' in title.lower():
        food_papers.append(title)
        continue
        
    # Check keywords
    keywords = extract_keywords(text)
    if 'food' in keywords.lower():
        food_papers.append(title)
        continue

print(f"__RESULT__:\n{json.dumps(food_papers)}")"""

env_args = {'var_function-call-17948406739355176464': 'file_storage/function-call-17948406739355176464.json', 'var_function-call-1041647607165485382': ['Citations', 'sqlite_sequence'], 'var_function-call-1041647607165487633': 'file_storage/function-call-1041647607165487633.json'}

exec(code, env_args)
