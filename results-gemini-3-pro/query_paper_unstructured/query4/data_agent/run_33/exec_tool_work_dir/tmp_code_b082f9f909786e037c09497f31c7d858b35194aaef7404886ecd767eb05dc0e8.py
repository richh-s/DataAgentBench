code = """import json

# Load the result from the previous query which fetched documents
# The key for the file path was var_function-call-11399838663012174565
file_path = locals()['var_function-call-11399838663012174565']

with open(file_path, 'r') as f:
    papers = json.load(f)

filtered_titles = []
for p in papers:
    text = p.get('text', '')
    filename = p.get('filename', '')
    title = filename.replace('.txt', '')
    
    # Check for Physical Activity
    # The hint says "For each paper, you may need to extract: domain... values may be part of a list".
    # "Common domains include: ... physical activity ..."
    # We'll check if "physical activity" appears in the text.
    if 'physical activity' in text.lower():
        # Check for Year 2016
        # Heuristic: Look for 2016 in the first 2000 characters (header/meta info)
        # or look for specific patterns like "Copyright 2016", "CHI '16", "CHI 2016"
        # To be safe, checking "2016" in the first 2000 characters is a strong signal for publication year 
        # vs a citation year (which would be in references at the end).
        # Also check "Copyright 2016" or "© 2016"
        
        header_text = text[:3000]
        if '2016' in header_text:
            filtered_titles.append(title)

print("__RESULT__:")
print(json.dumps(filtered_titles))"""

env_args = {'var_function-call-2366143788913111129': ['paper_docs'], 'var_function-call-2366143788913114632': ['Citations', 'sqlite_sequence'], 'var_function-call-17599226762723281444': 'file_storage/function-call-17599226762723281444.json', 'var_function-call-11399838663012174565': 'file_storage/function-call-11399838663012174565.json'}

exec(code, env_args)
