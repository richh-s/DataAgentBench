code = """import json, re
funding = var_call_fAZEjzLzlurUONOLI6e1kBuK
civ = var_call_G8tF6sTzfXKC8HFo7weoXCc8

def normalize(s):
    if not s:
        return ''
    s = s.lower()
    s = re.sub(r"\(.*?\)", "", s)  # remove parenthetical content
    s = re.sub(r"[^a-z0-9]+", " ", s)
    return s.strip()

# build funding map normalized -> list of records
fund_map = {}
for r in funding:
    name = r.get('Project_Name','')
    key = normalize(name)
    fund_map.setdefault(key, []).append({'Project_Name': name, 'Funding_Source': r.get('Funding_Source'), 'Amount': r.get('Amount')})

# build civic map normalized -> status (prefer specific project-like names)
civ_map = {}
for r in civ:
    name = r.get('Project_Name','')
    status = r.get('Status')
    key = normalize(name)
    # only keep if name looks like a project (contains keywords) or contains 'fema' or 'emergency'
    low = name.lower()
    if any(k in low for k in ['fema','emergency','project','repairs','improvements','storm','guardrail','culvert','retaining','outdoor warning','sirens','trancas','latigo','corral','birdview']):
        civ_map.setdefault(key, status)

# produce joined results for funding entries
results = []
for key, recs in fund_map.items():
    # find status from civ_map by exact normalized key or by partial match
    status = civ_map.get(key)
    if not status:
        # try partial match: see if any civ_map key is substring of this key or vice versa
        for k2 in civ_map:
            if k2 and (k2 in key or key in k2):
                status = civ_map[k2]
                break
    if not status:
        status = 'unknown'
    # build funding sources list
    funds = []
    for rr in recs:
        amt = rr.get('Amount')
        try:
            amt_val = int(amt) if amt is not None else None
        except:
            try:
                amt_val = int(float(amt))
            except:
                amt_val = None
        funds.append({'Funding_Source': rr.get('Funding_Source'), 'Amount': amt_val})
    results.append({'Project_Name': recs[0]['Project_Name'], 'Funding': funds, 'Status': status})

# sort results by project name
results = sorted(results, key=lambda x: x['Project_Name'].lower())

print('__RESULT__:')
print(json.dumps(results))"""

env_args = {'var_call_WKtxU0jxPJ15joDyaPmwBSnF': ['civic_docs'], 'var_call_jGUa9xleKbwSjDyorm3VrObQ': ['Funding'], 'var_call_kESzRD6axEvtHVPDcXvLTW1P': 'file_storage/call_kESzRD6axEvtHVPDcXvLTW1P.json', 'var_call_G8tF6sTzfXKC8HFo7weoXCc8': [{'Project_Name': '(cid:131) Project close out process has been initiated with FEMA/CalOES.', 'Status': 'design'}, {'Project_Name': '(cid:131) Staff finalized the design of this project.', 'Status': 'design'}, {'Project_Name': '(cid:131) Staff is finalizing the design of this project.', 'Status': 'design'}, {'Project_Name': '(cid:131) Staff is working with FEMA/CalOES to substitute the existing timber', 'Status': 'design'}, {'Project_Name': '(cid:190) Project Description: This project consisted of replacing fire damaged', 'Status': 'design'}, {'Project_Name': '(cid:190) Project Description: This project consisted of replacing fire damaged existing', 'Status': 'design'}, {'Project_Name': '(cid:190) Project Description: This project consisted of replacing the damaged', 'Status': 'design'}, {'Project_Name': '(cid:190) Project Description: This project has been cancelled as it could not get FEMA', 'Status': 'design'}, {'Project_Name': '(cid:190) Project Description: This project will be funded through a grant from FEMA', 'Status': 'design'}, {'Project_Name': '(cid:190) Project Schedule', 'Status': 'design'}, {'Project_Name': '(cid:190) Project Schedule:', 'Status': 'design'}, {'Project_Name': '(cid:190) Updates: This project will be funded through a grant from FEMA after the', 'Status': 'design'}, {'Project_Name': 'Avenue. This project is scheduled to be accepted by the Council at the', 'Status': 'completed'}, {'Project_Name': 'Clover Heights Storm Drain (FEMA Project)', 'Status': 'design'}, {'Project_Name': 'Corral Canyon Culvert Repairs (FEMA Project)', 'Status': 'design'}, {'Project_Name': 'Corral Canyon Culvert Repairs (FEMA/CalOES Project)', 'Status': 'design'}, {'Project_Name': 'Corral Canyon Road Bridge Repairs (FEMA Project)', 'Status': 'design'}, {'Project_Name': 'Disaster Projects (Completed)', 'Status': 'completed'}, {'Project_Name': 'Disaster Projects (Design)', 'Status': 'design'}, {'Project_Name': 'Disaster Projects (Not Started)', 'Status': 'not started'}, {'Project_Name': 'Guardrail Replacement Citywide (FEMA Project)', 'Status': 'design'}, {'Project_Name': 'Latigo Canyon Road Culvert Repairs (FEMA Project)', 'Status': 'design'}, {'Project_Name': 'Latigo Canyon Road Retaining Wall Repair Project', 'Status': 'completed'}, {'Project_Name': 'Latigo Canyon Road Roadway/Retaining Wall Improvements (FEMA/CalOES', 'Status': 'design'}, {'Project_Name': 'Latigo Canyon Road Roadway/Retaining Wall Improvements (FEMA/CalOES Project)', 'Status': 'design'}, {'Project_Name': 'Outdoor Warning Sirens (FEMA Project)', 'Status': 'design'}, {'Project_Name': 'Outdoor Warning Sirens (FEMA)', 'Status': 'design'}, {'Project_Name': 'Outdoor Warning Sirens - Design (FEMA Project)', 'Status': 'design'}, {'Project_Name': 'Outdoor Warningn Sirens - Design (FEMA Project)', 'Status': 'design'}, {'Project_Name': 'Storm Drain Master Plan (FEMA Project)', 'Status': 'design'}, {'Project_Name': 'Trancas Canyon Park Planting and Irrigation Repairs (CalJPIA/FEMA Project)', 'Status': 'design'}, {'Project_Name': 'Westward Beach Road.', 'Status': 'design'}, {'Project_Name': 'after the Wooley Fire. The project consists o hiring a consultant to develop', 'Status': 'design'}, {'Project_Name': 'after the Wooley Fire. The project consists of hiring a consultant to develop', 'Status': 'design'}, {'Project_Name': 'awarded a FEMA Hazard Mitigation grant to fund the design, engineering and', 'Status': 'design'}, {'Project_Name': 'culverts, debris basins, manholes, and other drainage structures within the', 'Status': 'design'}, {'Project_Name': 'drain on Latigo Canyon Road located approximately 2,500 feet from PCH', 'Status': 'design'}, {'Project_Name': 'environmental compliance needed for a shovel ready project. Phase Two of', 'Status': 'design'}, {'Project_Name': 'facilities and roadway embankments that were damaged by the Woolsey', 'Status': 'design'}, {'Project_Name': 'facilities and roadway embankments that were damaged by the Woolsey Fire.', 'Status': 'design'}, {'Project_Name': 'included the repair of a storm drainage facility on Birdview Avenue. The project was', 'Status': 'design'}, {'Project_Name': 'intersection floods and causes debris to block the road. An extended storm', 'Status': 'design'}, {'Project_Name': 'poor cell service. Phase One of the project included a sound study to', 'Status': 'design'}, {'Project_Name': 'project will be advertised for construction bids with construction', 'Status': 'design'}, {'Project_Name': 'project. Proposals will be due in February/March.', 'Status': 'design'}, {'Project_Name': 'that project.', 'Status': 'design'}, {'Project_Name': 'the Emergency Warning Sirens project will be implementation of the design', 'Status': 'design'}], 'var_call_95Gr7wPEAJ07A3PftiyulpkW': 'file_storage/call_95Gr7wPEAJ07A3PftiyulpkW.json', 'var_call_fAZEjzLzlurUONOLI6e1kBuK': [{'Project_Name': 'Birdview Avenue Improvements (FEMA/CalOES Project)', 'Funding_Source': 'Research Institution Funding', 'Amount': 14000}, {'Project_Name': 'Clover Heights Storm Drain (FEMA Project)', 'Funding_Source': 'Local NGO Fund', 'Amount': 21000}, {'Project_Name': 'Corral Canyon Culvert Repairs (FEMA Project)', 'Funding_Source': 'Municipal Fund', 'Amount': 43000}, {'Project_Name': 'Corral Canyon Culvert Repairs (FEMA/CalOES Project)', 'Funding_Source': 'Taxpayer Contribution', 'Amount': 15000}, {'Project_Name': 'Corral Canyon Road Bridge Repairs (FEMA Project)', 'Funding_Source': 'Local Business Support', 'Amount': 25000}, {'Project_Name': 'Corral Canyon Road Bridge Repairs (FEMA/CalOES Project)', 'Funding_Source': 'Cultural Heritage Grant', 'Amount': 58000}, {'Project_Name': 'Encinal Canyon Road Drainage Improvements (FEMA/CalOES Project)', 'Funding_Source': 'Private Sponsor', 'Amount': 94000}, {'Project_Name': 'Guardrail Replacement Citywide (FEMA Project)', 'Funding_Source': 'Impact Investment Fund', 'Amount': 22000}, {'Project_Name': 'Guardrail Replacement Citywide (FEMA/CalOES Project)', 'Funding_Source': 'Development Bank Loan', 'Amount': 45000}, {'Project_Name': 'Latigo Canyon Road Culvert Repairs (FEMA Project)', 'Funding_Source': 'Federal Assistance', 'Amount': 36000}, {'Project_Name': 'Latigo Canyon Road Culvert Repairs (FEMA/CalOES Project)', 'Funding_Source': 'National Foundation Fund', 'Amount': 44000}, {'Project_Name': 'Latigo Canyon Road Roadway/Retaining Wall Improvements (FEMA Project)', 'Funding_Source': 'Municipal Fund', 'Amount': 91000}, {'Project_Name': 'Latigo Canyon Road Roadway/Retaining Wall Improvements (FEMA/CalOES Project)', 'Funding_Source': 'Community Fund', 'Amount': 78000}, {'Project_Name': 'Outdoor Warning Sirens (FEMA Project)', 'Funding_Source': 'Environmental Grant', 'Amount': 27000}, {'Project_Name': 'Outdoor Warning Sirens (FEMA)', 'Funding_Source': 'State Development Grant', 'Amount': 81000}, {'Project_Name': 'Outdoor Warning Sirens - Design (FEMA Project)', 'Funding_Source': 'Local Business Support', 'Amount': 43000}, {'Project_Name': 'Outdoor Warningn Sirens - Design (FEMA Project)', 'Funding_Source': 'Technology Innovation Fund', 'Amount': 84000}, {'Project_Name': 'Storm Drain Master Plan (FEMA Project)', 'Funding_Source': 'Environmental Grant', 'Amount': 80000}, {'Project_Name': 'Trancas Canyon Park Planting and Irrigation Repairs (CalJPIA/FEMA Project)', 'Funding_Source': 'Infrastructure Bond', 'Amount': 44000}, {'Project_Name': 'Trancas Canyon Park Planting and Irrigation Repairs (FEMA/CalOES Project)', 'Funding_Source': 'Infrastructure Bond', 'Amount': 92000}]}

exec(code, env_args)
