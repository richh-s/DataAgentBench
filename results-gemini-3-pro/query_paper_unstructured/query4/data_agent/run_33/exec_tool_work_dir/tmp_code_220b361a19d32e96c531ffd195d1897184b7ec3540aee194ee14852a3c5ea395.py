code = """import json

file_path = locals()['var_function-call-16576350255932723074']
with open(file_path, 'r') as f:
    papers = json.load(f)

# Heuristic refinement
# Year 2016: Look for "2016" in the first 2000 chars. 
# Also check for "Copyright 2016" or conference acronyms with '16
# Domain "physical activity": Look for "physical activity" (case insensitive) in the text.

filtered_titles = []

for p in papers:
    text = p.get('text', '')
    filename = p.get('filename', '')
    title = filename.replace('.txt', '')
    
    # Check domain
    if 'physical activity' in text.lower():
        # Check year
        # Check first 2000 chars
        header = text[:3000]
        # Common patterns for 2016 papers:
        # "2016" usually appears in the conference date line, e.g. "May 7-12, 2016"
        # or "Copyright 2016"
        # However, checking just "2016" is a bit risky but likely sufficient for this dataset.
        if '2016' in header:
             filtered_titles.append(title)

print("__RESULT__:")
print(json.dumps(filtered_titles))"""

env_args = {'var_function-call-2366143788913111129': ['paper_docs'], 'var_function-call-2366143788913114632': ['Citations', 'sqlite_sequence'], 'var_function-call-17599226762723281444': 'file_storage/function-call-17599226762723281444.json', 'var_function-call-11399838663012174565': 'file_storage/function-call-11399838663012174565.json', 'var_function-call-6378129950907540898': [], 'var_function-call-1573942914296370840': 'Debug Info Printed', 'var_function-call-12636404193079087539': {'total_papers': 5, 'first_paper_filename': 'A Lived Informatics Model of Personal Informatics.txt', 'first_paper_text_start': "UBICOMP '15, SEPTEMBER 7–11, 2015, OSAKA, JAPAN\n\nA Lived Informatics Model of Personal Informatics \n\nDaniel A. Epstein1, An Ping2, James Fogarty1, Sean A. Munson2 \n1Computer Science & Engineering, 2Human Centered Design & Engineering \nDUB Group, University of Washington \n{depstein, jfogarty}@cs.wash", 'pa_count': 4, 'y2016_count': 1, 'intersection_count': 0}, 'var_function-call-16576350255932723074': 'file_storage/function-call-16576350255932723074.json'}

exec(code, env_args)
