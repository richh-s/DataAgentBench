code = """import json

# Load the result from the "count" query (which likely returned all docs)
file_key = 'var_function-call-3366737603932088961'
try:
    with open(locals()[file_key], 'r') as f:
        data = json.load(f)
    
    print("Number of documents:", len(data))
    if len(data) > 0:
        print("Keys in first document:", data[0].keys())
        # Print a snippet of the text from the first document to check for metadata again
        print("Text snippet:", data[0].get('text', '')[:500])
        
        # Check if 'contribution' word appears in the first few documents
        for i in range(min(5, len(data))):
            text = data[i].get('text', '').lower()
            print(f"Doc {i} title: {data[i].get('filename')}")
            if 'contribution' in text:
                print(f"  'contribution' found at index {text.find('contribution')}")
                # Print context
                idx = text.find('contribution')
                print(f"  Context: {text[idx:idx+100]}")
            else:
                print("  'contribution' not found")

except Exception as e:
    print(f"Error reading file: {e}")"""

env_args = {'var_function-call-13973424374790880036': 'file_storage/function-call-13973424374790880036.json', 'var_function-call-13973424374790878367': [{'id': '1', 'title': 'Expense Control: A Gamified, Semi-Automated, Crowd-Based Approach For Receipt Capturing', 'citation_count': '4', 'citation_year': '2017'}, {'id': '2', 'title': 'Expense Control: A Gamified, Semi-Automated, Crowd-Based Approach For Receipt Capturing', 'citation_count': '95', 'citation_year': '2018'}, {'id': '3', 'title': 'Understanding My Data, Myself: Supporting Self-reflection with Ubicomp Technologies', 'citation_count': '32', 'citation_year': '2012'}, {'id': '4', 'title': 'Understanding My Data, Myself: Supporting Self-reflection with Ubicomp Technologies', 'citation_count': '29', 'citation_year': '2013'}, {'id': '5', 'title': 'Understanding My Data, Myself: Supporting Self-reflection with Ubicomp Technologies', 'citation_count': '18', 'citation_year': '2014'}], 'var_function-call-3366737603932088961': 'file_storage/function-call-3366737603932088961.json'}

exec(code, env_args)
