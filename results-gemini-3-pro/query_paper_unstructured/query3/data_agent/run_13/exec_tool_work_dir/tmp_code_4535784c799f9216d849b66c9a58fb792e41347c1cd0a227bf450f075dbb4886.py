code = """import json
import re

# Get the file path from the previous result
file_path = locals()['var_function-call-11757020696500287229']

# Load the papers
with open(file_path, 'r') as f:
    papers = json.load(f)

matching_titles = []

print("Processing papers...")
for paper in papers:
    text = paper['text']
    filename = paper['filename']
    title = filename.replace('.txt', '')
    
    # Extract Year
    # Look for 4 digit year in first 1000 chars
    # Prioritize "Copyright 20xx" or "Venue 20xx"
    # Simple search for 20xx
    year = 0
    # Search for 2017, 2018, 2019, 2020, 2021, ...
    # Be more specific: " 20\d\d"
    matches = re.findall(r'\b(20\d\d)\b', text[:2000])
    if matches:
        # Take the first one found, assuming header info comes first
        year = int(matches[0])
    else:
        # Try 'YY format
        short_year = re.search(r"\b'\d\d\b", text[:500])
        if short_year:
             y = int(short_year.group(0)[1:])
             year = 2000 + y

    # Check for "empirical" contribution
    # We'll check if "empirical" is in the text
    # Also check if it's explicitly mentioned as contribution if possible
    # But for now, simple containment
    has_empirical = "empirical" in text.lower()
    
    print(f"Title: {title}, Year: {year}, Empirical: {has_empirical}")
    
    if year > 2016 and has_empirical:
        matching_titles.append(title)

print("__RESULT__:")
print(json.dumps(matching_titles))"""

env_args = {'var_function-call-4508703165533921554': ['paper_docs'], 'var_function-call-6558568440617970776': 'file_storage/function-call-6558568440617970776.json', 'var_function-call-12977520170952019892': 'file_storage/function-call-12977520170952019892.json', 'var_function-call-3057315164006980337': [{'_id': '694f5530284b10b11dc0a869', 'filename': 'A Lived Informatics Model of Personal Informatics.txt'}, {'_id': '694f5530284b10b11dc0a86a', 'filename': 'A Stage-based Model of Personal Informatics Systems.txt'}, {'_id': '694f5530284b10b11dc0a86b', 'filename': 'A Trip to the Moon: Personalized Animated Movies for Self-reflection.txt'}, {'_id': '694f5530284b10b11dc0a86c', 'filename': 'A Wee Bit More Interaction: Designing and Evaluating an Overactive Bladder App.txt'}, {'_id': '694f5530284b10b11dc0a86d', 'filename': 'ArmSleeve: A Patient Monitoring System to Support Occupational Therapists in Stroke Rehabilitation.txt'}], 'var_function-call-11757020696500287229': 'file_storage/function-call-11757020696500287229.json'}

exec(code, env_args)
