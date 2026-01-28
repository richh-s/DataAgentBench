code = """import json

# Load funding data
with open('/tmp/tmp8opjs8_m.json', 'r') as f:
    funding_data = json.load(f)

# Load civic documents data
with open('/tmp/tmpg5k2n9mq.json', 'r') as f:
    civic_docs_data = json.load(f)

print("Funding records loaded: " + str(len(funding_data)))
print("Civic documents loaded: " + str(len(civic_docs_data)))

# List park-related funding projects
park_funding = []
for item in funding_data:
    if 'park' in item['Project_Name'].lower():
        park_funding.append(item)

print("\nPark-related funding projects: " + str(len(park_funding)))
for item in park_funding:
    print(item['Project_Name'] + ": $" + str(item['Amount']))

# Search for park projects completed in 2022
print("\nSearching civic documents...")

potential_matches = []

for doc in civic_docs_data:
    text = doc['text']
    
    # Check if this document has park projects completed in 2022
    has_park = 'park' in text.lower()
    has_completed = 'completed' in text.lower()
    has_2022 = '2022' in text or 'November 2022' in text
    
    if has_park and has_completed and has_2022:
        print("Found document with park projects completed in 2022: " + doc['filename'])
        
        # Look for Bluffs Park Shade Structure specifically mentioned
        if 'Bluffs Park Shade Structure' in text:
            print("  - Found: Bluffs Park Shade Structure")
            if 'completed November 2022' in text:
                print("    * Completed in November 2022 - MATCH!")
                potential_matches.append('Bluffs Park Shade Structure')

# Check funding for matched projects
total_amount = 0
for fund_item in park_funding:
    if fund_item['Project_Name'] in potential_matches:
        amount = int(fund_item['Amount'])
        total_amount += amount
        print("\nFUNDING MATCHED: " + fund_item['Project_Name'] + " - $" + str(amount))

print("\nTotal funding for park projects completed in 2022: $" + str(total_amount))"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.query_db:1': 'file_storage/functions.query_db:1.json', 'var_functions.query_db:14': 'file_storage/functions.query_db:14.json', 'var_functions.query_db:15': 'file_storage/functions.query_db:15.json'}

exec(code, env_args)
