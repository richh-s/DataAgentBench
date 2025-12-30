code = """import json

path_text = locals()['var_function-call-18190371962378278332']
with open(path_text, 'r') as f:
    civic_data = json.load(f)
text = civic_data[0]['text'].lower()

# Find lines with "completed" and "2022"
matches = []
lines = text.splitlines()
for i, line in enumerate(lines):
    if "2022" in line and ("completed" in line or "completion" in line):
        # Check if it indicates project completion
        if "construction" in line or "project" in line:
            # Get context (project name)
            # Search backwards for project name
            pname = "Unknown"
            j = i - 1
            while j >= 0:
                prev = lines[j].strip()
                if "(cid:190)" in prev and "updates" in prev:
                    # Name is before this
                    k = j - 1
                    while k >= 0:
                        n = lines[k].strip()
                        if n and "page" not in n:
                            pname = n
                            break
                        k -= 1
                    break
                j -= 1
            
            matches.append({"project": pname, "line": line})

print("__RESULT__:")
print(json.dumps(matches))"""

env_args = {'var_function-call-18190371962378278332': 'file_storage/function-call-18190371962378278332.json', 'var_function-call-3926390822647844774': 'file_storage/function-call-3926390822647844774.json', 'var_function-call-17336179596749823734': [{'Project_Name': 'Bluffs Park Shade Structure', 'Amount': '21000'}, {'Project_Name': 'Bluffs Park Workout Station', 'Amount': '39000'}, {'Project_Name': 'Legacy Park Benches and Arbors Renovation', 'Amount': '41000'}, {'Project_Name': 'Legacy Park Paver Repair Project', 'Amount': '69000'}, {'Project_Name': 'Malibu Bluffs Park Roof Replacement Project', 'Amount': '44000'}, {'Project_Name': 'Malibu Bluffs Park South Walkway', 'Amount': '91000'}, {'Project_Name': 'Malibu Bluffs Park South Walkway Repairs', 'Amount': '81000'}, {'Project_Name': 'Malibu Park Drainage Improvements', 'Amount': '17000'}, {'Project_Name': 'Malibu Park Resurfacing Project', 'Amount': '14000'}, {'Project_Name': 'Malibu Park Storm Drain Repairs', 'Amount': '50000'}, {'Project_Name': 'Permanent Skate Park', 'Amount': '97000'}, {'Project_Name': 'Trancas Canyon Park Planting and Irrigation Repairs', 'Amount': '78000'}, {'Project_Name': 'Trancas Canyon Park Planting and Irrigation Repairs (CalJPIA/FEMA Project)', 'Amount': '44000'}, {'Project_Name': 'Trancas Canyon Park Planting and Irrigation Repairs (FEMA/CalOES Project)', 'Amount': '92000'}, {'Project_Name': 'Trancas Canyon Park Playground', 'Amount': '24000'}, {'Project_Name': 'Trancas Canyon Park Playground Resurfacing', 'Amount': '65000'}, {'Project_Name': 'Trancas Canyon Park Slope Stabilization Project', 'Amount': '68000'}, {'Project_Name': 'Trancas Canyon Park Slope Stabilization Project (CalJPIA Project)', 'Amount': '43000'}, {'Project_Name': 'Trancas Canyon Park Slope Stabilization Project (CalOES Project)', 'Amount': '32000'}, {'Project_Name': 'Trancas Canyon Park Upper and Lower Slopes Repair', 'Amount': '23000'}, {'Project_Name': 'Trancas Playground Resurfacing', 'Amount': '90000'}], 'var_function-call-18417157101231181788': {'total': 217000, 'projects': ['Bluffs Park Shade Structure', 'Malibu Bluffs Park South Walkway', 'Malibu Bluffs Park South Walkway Repairs', 'Trancas Canyon Park Playground']}, 'var_function-call-2874234682422263337': [{'project': 'Bluffs Park Shade Structure', 'line': '(cid:190) updates: construction was completed november 2022. notice of completion'}, {'project': 'Malibu Bluffs Park South Walkway', 'line': '(cid:190) updates: construction was completed november 2022. notice of completion'}, {'project': 'Malibu Bluffs Park South Walkway Repairs', 'line': '(cid:190) updates: construction was completed november 2022. notice of completion'}, {'project': 'Trancas Canyon Park Playground', 'line': '(cid:190) updates: construction was completed november 2022. notice of completion'}], 'var_function-call-13573649705172555645': 'point dume walkway repairs\n(cid:190) updates:\n\n(cid:131) construction was completed, november 2022\n(cid:131) notice of completion filed january 2023\n\ncapital improvement projects (not started)\n\npch median improvements at paradise cove and zuma beach\n\n(cid:190) project description: this project was identified in the 2015 pch safety study\nand includes installing new raised medians and improvements. new raised\nmedians are proposed east and west of pch and paradise cove road. the\nproposed improvements also include the relocation of the existing bus stop\nand new signage. the project will also include the installation of new raised\nmedians on pch in the areas where the double yellow lines exist in the vicinity\nof zuma beach, specifically where the yellow paddles are installed.\n\n(cid:190) project updates: city has submitted an application through measure r and is\n\nwaiting for the agreement.\n\npch crosswalk improvements at big rock drive and 20326 pch\n\n(cid:190) project description: this projec'}

exec(code, env_args)
