code = """import json
import re

# Load the large result file from the previous step
file_path = 'var_function-call-7300462932011158786.json'

try:
    with open(file_path, 'r') as f:
        data = json.load(f)
        
    print(f"Total documents: {len(data)}")
    
    # Inspect first 3 documents
    for i, doc in enumerate(data[:3]):
        print(f"\n--- Document {i} ---")
        print(f"Keys: {list(doc.keys())}")
        print(f"Filename: {doc.get('filename')}")
        text = doc.get('text', '')
        print(f"Text Start (500 chars): {text[:500]}")
        
        # Check for year patterns
        # Look for "Copyright 20xx" or "20xx"
        years = re.findall(r'\b20\d{2}\b', text[:1000])
        print(f"Years found: {years}")
        
        # Check for "Contribution" or "empirical"
        if 'empirical' in text.lower():
            print("'empirical' found in text.")
        else:
            print("'empirical' NOT found in text.")
            
        # Check for explicit metadata sections
        if "Contribution:" in text:
            print("Found 'Contribution:' label.")
            
except Exception as e:
    print(f"Error: {e}")

print("__RESULT__:")
print(json.dumps("analysis_done"))"""

env_args = {'var_function-call-12008909793186569857': ['paper_docs'], 'var_function-call-12008909793186566274': 'file_storage/function-call-12008909793186566274.json', 'var_function-call-12008909793186566787': [{'id': '1', 'title': 'Expense Control: A Gamified, Semi-Automated, Crowd-Based Approach For Receipt Capturing', 'citation_count': '4', 'citation_year': '2017'}, {'id': '2', 'title': 'Expense Control: A Gamified, Semi-Automated, Crowd-Based Approach For Receipt Capturing', 'citation_count': '95', 'citation_year': '2018'}, {'id': '3', 'title': 'Understanding My Data, Myself: Supporting Self-reflection with Ubicomp Technologies', 'citation_count': '32', 'citation_year': '2012'}, {'id': '4', 'title': 'Understanding My Data, Myself: Supporting Self-reflection with Ubicomp Technologies', 'citation_count': '29', 'citation_year': '2013'}, {'id': '5', 'title': 'Understanding My Data, Myself: Supporting Self-reflection with Ubicomp Technologies', 'citation_count': '18', 'citation_year': '2014'}], 'var_function-call-7300462932011158786': 'file_storage/function-call-7300462932011158786.json'}

exec(code, env_args)
