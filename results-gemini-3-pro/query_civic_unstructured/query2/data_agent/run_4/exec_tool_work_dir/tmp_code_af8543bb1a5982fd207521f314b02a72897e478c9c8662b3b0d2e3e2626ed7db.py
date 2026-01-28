code = """import json

civic_key = 'var_function-call-10494056103338850643'
marker = "(cid:190)"

with open(locals()[civic_key], 'r') as f:
    civic_docs = json.load(f)

target_name = "Malibu Park Drainage Improvements"
found_text = ""

for doc in civic_docs:
    text = doc['text']
    if target_name in text:
        # Extract the block
        lines = text.splitlines()
        for i in range(len(lines)):
            if target_name in lines[i]:
                 # Found it. Extract until next marker
                 found_text += lines[i] + "\n"
                 limit = min(i + 20, len(lines)) # Just take next 20 lines
                 for j in range(i + 1, limit):
                     if marker in lines[j] and j > i+2: # Stop at NEXT marker, not the one for this project
                         # Wait, the marker is usually immediately after name.
                         # We want to read the content OF this project.
                         # The content starts after the first marker (which is for this project) and ends at the marker for the NEXT project.
                         # My previous logic handled this.
                         pass
                     found_text += lines[j] + "\n"
                 break

print("__RESULT__:")
print(json.dumps(found_text))"""

env_args = {'var_function-call-17786645428432444760': ['civic_docs'], 'var_function-call-17786645428432443965': [{'Funding_ID': '1', 'Project_Name': '2021 Annual Street Maintenance', 'Funding_Source': 'Public-Private Partnership (PPP)', 'Amount': '24000'}, {'Funding_ID': '2', 'Project_Name': '2022 Annual Street Maintenance', 'Funding_Source': 'Government Grant', 'Amount': '45000'}, {'Funding_ID': '3', 'Project_Name': '2022 Morning View Resurfacing & Storm Drain Improvements', 'Funding_Source': 'State Development Grant', 'Amount': '38000'}, {'Funding_ID': '4', 'Project_Name': 'Annual Street Maintenance', 'Funding_Source': 'Corporate Sponsorship', 'Amount': '23000'}, {'Funding_ID': '5', 'Project_Name': 'Birdview Avenue Improvements', 'Funding_Source': 'National Foundation Fund', 'Amount': '79000'}], 'var_function-call-9932309007747960995': 'file_storage/function-call-9932309007747960995.json', 'var_function-call-10494056103338850643': 'file_storage/function-call-10494056103338850643.json', 'var_function-call-10332075929140261895': 'file_storage/function-call-10332075929140261895.json', 'var_function-call-17814162175572024946': {'completed_park_projects': ['Bluffs Park Shade Structure', 'Malibu Park Drainage Improvements'], 'total_funding': 38000.0}}

exec(code, env_args)
