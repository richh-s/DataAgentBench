code = """import json
# load previous extracted projects with FEMA/emergency
proj = var_call_DcNSWbehsrTYKyCqIkMrCVwE
fund = var_call_wZZC3A902D4MAeAurfTb8pZ7

# Build a mapping from funding project names to funding records (some projects have multiple funding rows)
fund_map = {}
for f in fund:
    name = f['Project_Name']
    fund_map.setdefault(name, []).append({'Funding_Source': f['Funding_Source'], 'Amount': f['Amount']})

# For each project from the docs that appears FEMA/emergency-related, try to match funding by exact match or by normalized contains
results = []
for p in proj:
    pname = p['Project_Name']
    matched = []
    # exact match
    if pname in fund_map:
        matched = fund_map[pname]
    else:
        # try fuzzy: check fund names that are substrings or contain key phrases
        pname_norm = pname.lower()
        for fname, frecs in fund_map.items():
            if fname.lower() in pname_norm or pname_norm in fname.lower():
                matched.extend(frecs)
        # also match by shared key tokens like 'Latigo', 'Corral Canyon', 'Outdoor Warning Sirens', 'Trancas Canyon', 'Guardrail Replacement'
        keys = ['latigo','corral canyon','outdoor warning','trancas canyon','guardrail']
        for k in keys:
            if k in pname.lower():
                for fname, frecs in fund_map.items():
                    if k in fname.lower():
                        matched.extend(frecs)
    # dedup matched
    unique_matched = { (m['Funding_Source'], m['Amount']) : m for m in matched }.values()
    if not unique_matched:
        # still try to find any funding records in funding DB that mention 'FEMA' and share project short name tokens
        for fname, frecs in fund_map.items():
            if 'fema' in fname.lower():
                # see if first word of project in fname is in pname
                for token in pname.split():
                    if len(token) > 4 and token.lower() in fname.lower():
                        unique_matched = frecs
                        break
    if unique_matched:
        for m in unique_matched:
            results.append({'Project_Name': pname, 'Funding_Source': m['Funding_Source'], 'Amount': m['Amount'], 'Status': p.get('status'), 'Type': p.get('type'), 'topic': p.get('topic')})
    else:
        results.append({'Project_Name': pname, 'Funding_Source': None, 'Amount': None, 'Status': p.get('status'), 'Type': p.get('type'), 'topic': p.get('topic')})

# deduplicate by Project_Name + Funding_Source
final = []
seen = set()
for r in results:
    key = (r['Project_Name'], r['Funding_Source'], r['Amount'])
    if key not in seen:
        seen.add(key)
        final.append(r)

print('__RESULT__:')
print(json.dumps(final))"""

env_args = {'var_call_Xnnh54iL6cs5wg7PT2JhApXO': 'file_storage/call_Xnnh54iL6cs5wg7PT2JhApXO.json', 'var_call_PjOpgR2htSTRpdl1SaZYtAQk': {'doc_count': 5}, 'var_call_DcNSWbehsrTYKyCqIkMrCVwE': [{'Project_Name': 'Latigo Canyon Road Retaining Wall Repair Project', 'topic': 'FEMA, road', 'type': 'disaster', 'status': 'completed'}, {'Project_Name': 'Latigo Canyon Road Roadway/Retaining Wall Improvements (FEMA Project)', 'topic': 'FEMA, road', 'type': 'disaster', 'status': 'design'}, {'Project_Name': 'Trancas Canyon Park Planting and Irrigation Repairs (CalJPIA/FEMA Project)', 'topic': 'FEMA, park', 'type': 'disaster', 'status': 'design'}, {'Project_Name': 'Storm Drain Master Plan (FEMA Project)', 'topic': 'FEMA, storm drain', 'type': 'disaster', 'status': 'design'}, {'Project_Name': 'after the Woolsey Fire. The City will create a complete inventory of storm', 'topic': 'FEMA, drainage, fire, storm drain', 'type': 'disaster', 'status': 'unknown'}, {'Project_Name': 'Guardrail Replacement Citywide (FEMA Project)', 'topic': 'FEMA, fire, guardrail', 'type': 'disaster', 'status': 'unknown'}, {'Project_Name': 'guardrail throughout the City as a result of the Woolsey Fire.', 'topic': 'FEMA, bridge, fire, guardrail, road', 'type': 'disaster', 'status': 'unknown'}, {'Project_Name': 'fencing and repairing the damaged embankment adjacent to the bridge.', 'topic': 'FEMA, bridge, fire, road', 'type': 'disaster', 'status': 'unknown'}, {'Project_Name': 'Corral Canyon Culvert Repairs (FEMA Project)', 'topic': 'FEMA, bridge, fire', 'type': 'disaster', 'status': 'unknown'}, {'Project_Name': 'January 24, 2022 meeting.', 'topic': 'FEMA, road, storm drain', 'type': 'disaster', 'status': 'completed'}, {'Project_Name': 'project. Proposals will be due in February/March.', 'topic': 'FEMA, fire, road, storm drain', 'type': 'disaster', 'status': 'unknown'}, {'Project_Name': 'Outdoor Warningn Sirens - Design (FEMA Project)', 'topic': 'FEMA, emergency, emergency warning', 'type': 'disaster', 'status': 'design'}, {'Project_Name': 'awarded a FEMA Hazard Mitigation grant to fund the design, engineering and', 'topic': 'FEMA, emergency, emergency warning', 'type': 'disaster', 'status': 'unknown'}, {'Project_Name': 'environmental compliance needed for a shovel ready project. Phase Two of', 'topic': 'FEMA, emergency, emergency warning', 'type': 'disaster', 'status': 'unknown'}, {'Project_Name': 'Latigo Canyon Road Roadway/Retaining Wall Improvements (FEMA/CalOES', 'topic': 'FEMA, road', 'type': 'disaster', 'status': 'unknown'}, {'Project_Name': 'Project)', 'topic': 'FEMA', 'type': 'disaster', 'status': 'unknown'}, {'Project_Name': 'Trancas Canyon Park Planting and Irrigation Repairs (FEMA/CalOES Project)', 'topic': 'FEMA, park', 'type': 'disaster', 'status': 'design'}, {'Project_Name': 'Birdview Avenue Improvements (FEMA/CalOES Project)', 'topic': 'FEMA, park', 'type': 'disaster', 'status': 'design'}, {'Project_Name': 'Disaster Projects (Completed)', 'topic': 'FEMA, fire, guardrail', 'type': 'disaster', 'status': 'completed'}, {'Project_Name': 'Corral Canyon Culvert Repairs (FEMA/CalOES Project)', 'topic': 'FEMA, road, storm drain', 'type': 'disaster', 'status': 'unknown'}, {'Project_Name': 'Disaster Projects (Not Started)', 'topic': 'FEMA, road, storm drain', 'type': 'disaster', 'status': 'not started'}, {'Project_Name': 'Latigo Canyon Road Culvert Repairs (FEMA/CalOES Project)', 'topic': 'FEMA, fire, road, storm drain', 'type': 'disaster', 'status': 'design'}, {'Project_Name': 'Encinal Canyon Road Drainage Improvements (FEMA/CalOES Project)', 'topic': 'FEMA, drainage, fire, road, storm drain', 'type': 'disaster', 'status': 'design'}, {'Project_Name': 'Outdoor Warning Sirens (FEMA)', 'topic': 'FEMA, fire', 'type': 'disaster', 'status': 'design'}, {'Project_Name': 'a plan that includes the evaluation of a siren system and possible locations.', 'topic': 'FEMA, fire', 'type': 'disaster', 'status': 'design'}, {'Project_Name': 'Latigo Canyon Road Roadway/Retaining Wall Improvements (FEMA/CalOES Project)', 'topic': 'FEMA, road', 'type': 'disaster', 'status': 'unknown'}, {'Project_Name': 'Outdoor Warning Sirens (FEMA Project)', 'topic': 'FEMA, fire', 'type': 'disaster', 'status': 'design'}, {'Project_Name': 'Corral Canyon Road Bridge Repairs (FEMA Project)', 'topic': 'FEMA, bridge, fire, road', 'type': 'disaster', 'status': 'unknown'}, {'Project_Name': 'Proposals are due in April 14, 2022.', 'topic': 'FEMA, fire, road, storm drain', 'type': 'disaster', 'status': 'unknown'}, {'Project_Name': 'infrastructure requirements, and siren sound range. The City has been', 'topic': 'FEMA', 'type': 'disaster', 'status': 'unknown'}, {'Project_Name': 'the Emergency Warning Sirens project will be implementation of the design', 'topic': 'emergency, emergency warning', 'type': 'capital', 'status': 'unknown'}, {'Project_Name': 'accepted by the Council on January 24, 2022', 'topic': 'FEMA, drainage, road, storm drain', 'type': 'disaster', 'status': 'unknown'}], 'var_call_NIqhp7R1SAbB87R981uSU6Ls': ['Funding'], 'var_call_glSYZYwLQMyMdqjsKM4IaUco': 'file_storage/call_glSYZYwLQMyMdqjsKM4IaUco.json', 'var_call_wZZC3A902D4MAeAurfTb8pZ7': [{'Project_Name': 'Birdview Avenue Improvements (FEMA/CalOES Project)', 'Funding_Source': 'Research Institution Funding', 'Amount': 14000}, {'Project_Name': 'Clover Heights Storm Drain (FEMA Project)', 'Funding_Source': 'Local NGO Fund', 'Amount': 21000}, {'Project_Name': 'Corral Canyon Culvert Repairs (FEMA Project)', 'Funding_Source': 'Municipal Fund', 'Amount': 43000}, {'Project_Name': 'Corral Canyon Culvert Repairs (FEMA/CalOES Project)', 'Funding_Source': 'Taxpayer Contribution', 'Amount': 15000}, {'Project_Name': 'Corral Canyon Road Bridge Repairs (FEMA Project)', 'Funding_Source': 'Local Business Support', 'Amount': 25000}, {'Project_Name': 'Corral Canyon Road Bridge Repairs (FEMA/CalOES Project)', 'Funding_Source': 'Cultural Heritage Grant', 'Amount': 58000}, {'Project_Name': 'Encinal Canyon Road Drainage Improvements (FEMA/CalOES Project)', 'Funding_Source': 'Private Sponsor', 'Amount': 94000}, {'Project_Name': 'Guardrail Replacement Citywide (FEMA Project)', 'Funding_Source': 'Impact Investment Fund', 'Amount': 22000}, {'Project_Name': 'Guardrail Replacement Citywide (FEMA/CalOES Project)', 'Funding_Source': 'Development Bank Loan', 'Amount': 45000}, {'Project_Name': 'Latigo Canyon Road Culvert Repairs (FEMA Project)', 'Funding_Source': 'Federal Assistance', 'Amount': 36000}, {'Project_Name': 'Latigo Canyon Road Culvert Repairs (FEMA/CalOES Project)', 'Funding_Source': 'National Foundation Fund', 'Amount': 44000}, {'Project_Name': 'Latigo Canyon Road Roadway/Retaining Wall Improvements (FEMA Project)', 'Funding_Source': 'Municipal Fund', 'Amount': 91000}, {'Project_Name': 'Latigo Canyon Road Roadway/Retaining Wall Improvements (FEMA/CalOES Project)', 'Funding_Source': 'Community Fund', 'Amount': 78000}, {'Project_Name': 'Outdoor Warning Sirens (FEMA Project)', 'Funding_Source': 'Environmental Grant', 'Amount': 27000}, {'Project_Name': 'Outdoor Warning Sirens (FEMA)', 'Funding_Source': 'State Development Grant', 'Amount': 81000}, {'Project_Name': 'Outdoor Warning Sirens - Design (FEMA Project)', 'Funding_Source': 'Local Business Support', 'Amount': 43000}, {'Project_Name': 'Outdoor Warningn Sirens - Design (FEMA Project)', 'Funding_Source': 'Technology Innovation Fund', 'Amount': 84000}, {'Project_Name': 'Storm Drain Master Plan (FEMA Project)', 'Funding_Source': 'Environmental Grant', 'Amount': 80000}, {'Project_Name': 'Trancas Canyon Park Planting and Irrigation Repairs (CalJPIA/FEMA Project)', 'Funding_Source': 'Infrastructure Bond', 'Amount': 44000}, {'Project_Name': 'Trancas Canyon Park Planting and Irrigation Repairs (FEMA/CalOES Project)', 'Funding_Source': 'Infrastructure Bond', 'Amount': 92000}]}

exec(code, env_args)
