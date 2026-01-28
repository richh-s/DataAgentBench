code = """import json

funding_path = locals()['var_function-call-8835626806368298115']
docs_path = locals()['var_function-call-9685015997201823152']

with open(funding_path, 'r') as f:
    funding_records = json.load(f)

with open(docs_path, 'r') as f:
    docs = json.load(f)

full_text = " ".join([d['text'] for d in docs])

all_base_names = set()
for row in funding_records:
    name = row['Project_Name']
    if "(" in name:
        base = name.split("(")[0].strip()
    else:
        base = name
    all_base_names.add(base)

sorted_base_names = sorted(list(all_base_names), key=len, reverse=True)

total_funding = 0
matched_list = []

for row in funding_records:
    name = row['Project_Name']
    
    is_disaster = False
    suffixes = ["(FEMA", "(CalOES", "(CalJPIA", "(Woolsey"]
    if any(s in name for s in suffixes):
        is_disaster = True
    
    if "(" in name:
        base_name = name.split("(")[0].strip()
    else:
        base_name = name
    
    idx = full_text.find(base_name)
    if idx == -1:
        continue
        
    snippet = full_text[idx:idx+1500]
    
    if not is_disaster:
        context = snippet[:500]
        if "FEMA" in context or "CalOES" in context or "CalJPIA" in context:
            is_disaster = True
            
    if not is_disaster:
        continue
        
    bc_match = snippet.find("Begin Construction:")
    
    started_2022 = False
    
    if bc_match != -1:
        segment = snippet[len(base_name):bc_match]
        
        interference = False
        for other_name in sorted_base_names:
            if other_name == base_name:
                continue
            
            # Fix: Ignore if other_name is part of base_name (e.g. road name)
            if other_name in base_name:
                continue
            
            if other_name in segment:
                interference = True
                break
                    
        if not interference:
            date_str = snippet[bc_match:bc_match+50]
            if "2022" in date_str:
                started_2022 = True

    if started_2022:
        total_funding += int(row['Amount'])
        matched_list.append(name)

print(f"Total Funding: {total_funding}")
print("__RESULT__:")
print(json.dumps(total_funding))"""

env_args = {'var_function-call-6821876032245033894': ['Funding'], 'var_function-call-8835626806368298115': 'file_storage/function-call-8835626806368298115.json', 'var_function-call-9685015997201823152': 'file_storage/function-call-9685015997201823152.json', 'var_function-call-4907481001215634158': 1528000, 'var_function-call-13844849535074793932': [{'name': '2021 Annual Street Maintenance', 'amount': '24000', 'date_context': 'Begin Construction: Spring 2022\n\nLatigo Canyon Roa'}, {'name': 'Annual Street Maintenance', 'amount': '23000', 'date_context': 'Begin Construction: Spring 2022\n\nLatigo Canyon Roa'}, {'name': 'Birdview Avenue Improvements', 'amount': '79000', 'date_context': 'Begin Construction: April 2022\n\nEncinal Canyon Roa'}, {'name': 'Birdview Avenue Improvements (CalOES Project)', 'amount': '85000', 'date_context': 'Begin Construction: April 2022\n\nEncinal Canyon Roa'}, {'name': 'Birdview Avenue Improvements (FEMA/CalOES Project)', 'amount': '14000', 'date_context': 'Begin Construction: April 2022\n\nEncinal Canyon Roa'}, {'name': 'Broad Beach Road Water Quality Infrastructure Repairs', 'amount': '87000', 'date_context': 'Begin Construction: Spring 2022\n\nLatigo Canyon Roa'}, {'name': 'Broad Beach Road Water Quality Infrastructure Repairs (CalJPIA Project)', 'amount': '81000', 'date_context': 'Begin Construction: Spring 2022\n\nLatigo Canyon Roa'}, {'name': 'Civic Center Stormwater Diversion Structure', 'amount': '64000', 'date_context': 'Begin Construction: Spring 2022\n\nLatigo Canyon Roa'}, {'name': 'Civic Center Way Improvements', 'amount': '37000', 'date_context': 'Begin Construction: Spring 2022\n\nLatigo Canyon Roa'}, {'name': 'Corral Canyon Culvert Repairs', 'amount': '54000', 'date_context': 'Begin Construction: April 2022\n\nEncinal Canyon Roa'}, {'name': 'Corral Canyon Culvert Repairs (FEMA Project)', 'amount': '43000', 'date_context': 'Begin Construction: April 2022\n\nEncinal Canyon Roa'}, {'name': 'Corral Canyon Culvert Repairs (FEMA/CalOES Project)', 'amount': '15000', 'date_context': 'Begin Construction: April 2022\n\nEncinal Canyon Roa'}, {'name': 'Encinal Canyon Road Drainage Improvements', 'amount': '34000', 'date_context': 'Begin Construction: Fall 2022\n\nWestward Beach Road'}, {'name': 'Encinal Canyon Road Drainage Improvements (CalOES Project)', 'amount': '18000', 'date_context': 'Begin Construction: Fall 2022\n\nWestward Beach Road'}, {'name': 'Encinal Canyon Road Drainage Improvements (FEMA/CalOES Project)', 'amount': '94000', 'date_context': 'Begin Construction: Fall 2022\n\nWestward Beach Road'}, {'name': 'Latigo Canyon Road Culvert Repairs', 'amount': '57000', 'date_context': 'Begin Construction: April 2022\n\nEncinal Canyon Roa'}, {'name': 'Latigo Canyon Road Culvert Repairs (FEMA Project)', 'amount': '36000', 'date_context': 'Begin Construction: April 2022\n\nEncinal Canyon Roa'}, {'name': 'Latigo Canyon Road Culvert Repairs (FEMA/CalOES Project)', 'amount': '44000', 'date_context': 'Begin Construction: April 2022\n\nEncinal Canyon Roa'}, {'name': 'Latigo Canyon Road Roadway/Retaining Wall Improvements', 'amount': '19000', 'date_context': 'Begin Construction: April 2022\n\nTrancas Canyon Par'}, {'name': 'Latigo Canyon Road Roadway/Retaining Wall Improvements (FEMA Project)', 'amount': '91000', 'date_context': 'Begin Construction: April 2022\n\nTrancas Canyon Par'}, {'name': 'Latigo Canyon Road Roadway/Retaining Wall Improvements (FEMA/CalOES Project)', 'amount': '78000', 'date_context': 'Begin Construction: April 2022\n\nTrancas Canyon Par'}, {'name': 'Malibu Park Drainage Improvements', 'amount': '17000', 'date_context': 'Begin Construction: April 2022\n\nEncinal Canyon Roa'}, {'name': 'Trancas Canyon Park Planting and Irrigation Repairs', 'amount': '78000', 'date_context': 'Begin Construction: Spring 2022\n\nTrancas Canyon Pa'}, {'name': 'Trancas Canyon Park Planting and Irrigation Repairs (CalJPIA/FEMA Project)', 'amount': '44000', 'date_context': 'Begin Construction: Spring 2022\n\nTrancas Canyon Pa'}, {'name': 'Trancas Canyon Park Planting and Irrigation Repairs (FEMA/CalOES Project)', 'amount': '92000', 'date_context': 'Begin Construction: Spring 2022\n\nTrancas Canyon Pa'}, {'name': 'Trancas Canyon Park Slope Stabilization Project', 'amount': '68000', 'date_context': 'Begin Construction: Spring 2022\n\nStorm Drain Maste'}, {'name': 'Trancas Canyon Park Slope Stabilization Project (CalJPIA Project)', 'amount': '43000', 'date_context': 'Begin Construction: Spring 2022\n\nStorm Drain Maste'}, {'name': 'Trancas Canyon Park Slope Stabilization Project (CalOES Project)', 'amount': '32000', 'date_context': 'Begin Construction: Spring 2022\n\nStorm Drain Maste'}, {'name': 'Westward Beach Road Shoulder Repairs (CalOES Project)', 'amount': '77000', 'date_context': 'Begin Construction: Fall 2022\n(cid:131)\n\nOutdoor W'}], 'var_function-call-10686389572354069346': 927000}

exec(code, env_args)
