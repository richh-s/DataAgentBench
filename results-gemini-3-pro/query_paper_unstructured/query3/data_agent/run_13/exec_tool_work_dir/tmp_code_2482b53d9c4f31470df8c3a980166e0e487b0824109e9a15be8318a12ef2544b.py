code = """import json
import re

# Load the papers
with open('var_function-call-11757020696500287229.json', 'r') as f:
    papers = json.load(f)

matching_titles = []

for paper in papers:
    text = paper['text']
    filename = paper['filename']
    title = filename.replace('.txt', '')
    
    # Extract Year
    # Look for 4 digit year in first 1000 chars
    year_match = re.search(r'\b20\d\d\b', text[:1000])
    year = 0
    if year_match:
        year = int(year_match.group(0))
    else:
        # Try 'YY format if preceded by venue name or just 'YY
        # e.g. " '15 "
        short_year = re.search(r"'\d\d", text[:500])
        if short_year:
            y = int(short_year.group(0)[1:])
            year = 2000 + y

    # Check for "empirical" contribution
    # We'll check if "empirical" is in the text
    has_empirical = "empirical" in text.lower()
    
    # Debug print
    print(f"Title: {title}, Year: {year}, Empirical: {has_empirical}")
    
    if year > 2016 and has_empirical:
        matching_titles.append(title)

print("__RESULT__:")
print(json.dumps(matching_titles))"""

env_args = {'var_function-call-4508703165533921554': ['paper_docs'], 'var_function-call-6558568440617970776': 'file_storage/function-call-6558568440617970776.json', 'var_function-call-12977520170952019892': 'file_storage/function-call-12977520170952019892.json', 'var_function-call-3057315164006980337': [{'_id': '694f5530284b10b11dc0a869', 'filename': 'A Lived Informatics Model of Personal Informatics.txt'}, {'_id': '694f5530284b10b11dc0a86a', 'filename': 'A Stage-based Model of Personal Informatics Systems.txt'}, {'_id': '694f5530284b10b11dc0a86b', 'filename': 'A Trip to the Moon: Personalized Animated Movies for Self-reflection.txt'}, {'_id': '694f5530284b10b11dc0a86c', 'filename': 'A Wee Bit More Interaction: Designing and Evaluating an Overactive Bladder App.txt'}, {'_id': '694f5530284b10b11dc0a86d', 'filename': 'ArmSleeve: A Patient Monitoring System to Support Occupational Therapists in Stroke Rehabilitation.txt'}], 'var_function-call-11757020696500287229': 'file_storage/function-call-11757020696500287229.json'}

exec(code, env_args)
