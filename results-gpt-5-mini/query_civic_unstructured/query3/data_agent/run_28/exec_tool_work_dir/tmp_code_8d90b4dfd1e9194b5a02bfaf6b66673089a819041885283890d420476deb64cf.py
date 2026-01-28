code = """import json, re
# Load civic docs query result from file
path = var_call_QxtrsIHo3FAzElPyUC4rh1RS
with open(path, 'r', encoding='utf-8') as f:
    docs = json.load(f)

# Load funding matches from earlier query (available as variable)
funding_matches = var_call_BETRXzm9RmKj3j3EAzRg1zqx

# Keywords to identify FEMA/emergency projects
key_re = re.compile(r'fema|emergency|siren|outdoor warning|guardrail|culvert|storm drain|trancas canyon|latigo canyon|corral canyon|birdview', re.I)

projects = {}

for doc in docs:
    lines = doc.get('text','').splitlines()
    n = len(lines)
    for i, line in enumerate(lines):
        if key_re.search(line):
            # Try to find a project title nearby: search upward upto 6 lines and downward upto 2 lines
            title = None
            # downward also may have title, but usually title is standalone line containing 'Project' or '(FEMA' or 'Sirens'
            # search within window [-6, +2]
            for j in range(max(0, i-6), min(n, i+3)):
                candidate = lines[j].strip()
                if not candidate: continue
                # clean candidate
                cand = re.sub(r"\(cid:\d+\)", "", candidate).strip()
                if len(cand) < 5: continue
                # heuristics for title: contains 'Project' or 'Repairs' or endswith '(FEMA Project)' or contains 'Sirens' or 'Replacement Citywide' or 'Improvements'
                if re.search(r'project\b|repairs?|improvements?|replacement|sirens|storm drain|culvert|guardrail|bridge|planting and irrigation|retaining wall|master plan', cand, re.I):
                    title = cand
                    # prefer the line that itself contains FEMA/emergency keywords
                    if j == i:
                        break
            if not title:
                # fallback: use the line itself cleaned
                title = re.sub(r"\(cid:\d+\)", "", lines[i]).strip()
            # determine status by scanning nearby lines for status cues
            status = 'unknown'
            window_start = max(0, i-10)
            window_end = min(n, i+10)
            window_text = "\n".join(lines[window_start:window_end]).lower()
            # check completed
            if re.search(r'disaster projects \(completed\)|completed|complete construction|completion date:|notice of completion|project is complete', window_text):
                status = 'completed'
            elif re.search(r'disaster projects \(not started\)|not started|disaster projects \(not started\)', window_text):
                status = 'not started'
            elif re.search(r'design|complete design|preliminary design|estimated schedule|begin construction:|advertise:|awarded a fema hazard mitigation grant|dependent upon final grant approval', window_text):
                # if also contains phrases indicating future (Begin Construction: Fall 2023, Advertise:), treat as design
                status = 'design'
            # normalize title whitespace
            title = re.sub(r"\s+", " ", title).strip()
            key = title.lower()
            if key not in projects:
                projects[key] = {'Project_Name': title, 'Status': status, 'Funding': []}
            else:
                # upgrade unknown status if found more specific
                if projects[key]['Status'] == 'unknown' and status != 'unknown':
                    projects[key]['Status'] = status

# Now join with funding_matches
# funding_matches is list of dicts with Project_Name, Funding_Source, Amount
for f in funding_matches:
    fname = f.get('Project_Name','')
    fl = fname.lower()
    matched = False
    for pkey, pval in projects.items():
        pn = pval['Project_Name'].lower()
        # match if funding name contains project name or vice versa
        if pn in fl or fl in pn or re.sub(r"\s+", " ", pn) == re.sub(r"\s+", " ", fl):
            pval['Funding'].append({'Funding_Source': f.get('Funding_Source'), 'Amount': f.get('Amount')})
            matched = True
    # also include funding for projects that may be in funding list but not found in docs; but only if they match keywords
    if not matched and key_re.search(fname):
        # add new project entry
        key = fname.lower()
        if key not in projects:
            projects[key] = {'Project_Name': fname, 'Status': 'unknown', 'Funding': [{'Funding_Source': f.get('Funding_Source'), 'Amount': f.get('Amount')}]} 

# Prepare final list
result = []
for p in projects.values():
    if not key_re.search(p['Project_Name']):
        # ensure project name itself speaks to keyword
        pass
    # if no funding entries, include one record with None funding
    if p['Funding']:
        for fund in p['Funding']:
            result.append({'Project_Name': p['Project_Name'], 'Funding_Source': fund.get('Funding_Source'), 'Amount': fund.get('Amount'), 'Status': p['Status']})
    else:
        result.append({'Project_Name': p['Project_Name'], 'Funding_Source': None, 'Amount': None, 'Status': p['Status']})

# sort result by Project_Name
result_sorted = sorted(result, key=lambda x: x['Project_Name'].lower())

print('__RESULT__:')
print(json.dumps(result_sorted))"""

env_args = {'var_call_QxtrsIHo3FAzElPyUC4rh1RS': 'file_storage/call_QxtrsIHo3FAzElPyUC4rh1RS.json', 'var_call_nk3UJd1gvwIdkU5NgDjoZ9tX': 'file_storage/call_nk3UJd1gvwIdkU5NgDjoZ9tX.json', 'var_call_f6c4OrX1ADPiRK3XZqSwT77I': ['Awaiting final FEMA/CalOES approval for scope modification', 'Latigo Canyon Road Roadway/Retaining Wall Improvements (FEMA Project)', 'Staff is also working with FEMA/CalOES to substitute the existing', 'Trancas Canyon Park Planting and Irrigation Repairs (CalJPIA/FEMA Project)', 'Project Description: This project will be funded through a grant from FEMA', 'drains, culverts, debris basins, manholes, and other drainage structures', 'Guardrail Replacement Citywide (FEMA Project)', 'guardrail throughout the City as a result of the Woolsey Fire.', 'Corral Canyon Road Bridge Repairs (FEMA Project)', 'fencing and repairing the damaged embankment adjacent to the bridge.', 'Corral Canyon Culvert Repairs (FEMA Project)', 'Project Description: This project has been cancelled as it could not get FEMA', 'Clover Heights Storm Drain (FEMA Project)', 'Latigo Canyon Road Culvert Repairs (FEMA Project)', 'Project Description: This project consists of repairing the existing storm drain', 'Outdoor Warningn Sirens - Design (FEMA Project)', 'Project Description: An Emergency Warning Siren system will improve the', 'the Emergency Warning Sirens project will be implementation of the design', 'awarded a FEMA Hazard Mitigation grant to fund the design, engineering and', 'plan, including purchasing, installing, and testing the sirens. The City will', 'Trancas Canyon Park Planting and Irrigation Repairs (FEMA/CalOES Project)', 'Birdview Avenue Improvements (FEMA/CalOES Project)', 'Guardrail Replacement Citywide (FEMA/CalOES Project)', 'Latigo Canyon Road Culvert Repairs (FEMA/CalOES Project)', 'Outdoor Warning Sirens (FEMA)', 'Complete Design: Dependent upon final grant approval from FEMA', 'Outdoor Warning Sirens (FEMA Project)', 'Storm Drain Master Plan (FEMA Project)', 'infrastructure requirements, and siren sound range. The City has been', 'determine the optimal number and locations of individual sirens, power and', 'Latigo Canyon Road Roadway/Retaining Wall Improvements (FEMA/CalOES', 'Updates: This project will be funded through a grant from FEMA after the', 'bridge.', 'Corral Canyon Culvert Repairs (FEMA/CalOES Project)', 'Staff is working with FEMA/CalOES to substitute the existing timber', 'guardrails within the project limits.', 'Outdoor Warning Sirens - Design (FEMA Project)', 'Advertise: Fall 2023 (dependent upon FEMA/CalOES approval)', 'Project close out process has been initiated with FEMA/CalOES.', 'Advertise: Spring 2024 (dependent upon FEMA/CalOES approval)', 'Begin Construction: Summer 2024 (dependent upon FEMA/CalOES', 'Advertise: (dependent upon FEMA/CalOES approval)', 'Begin Construction: (dependent upon FEMA/CalOES approval)', 'Project Description: This project is funded through a grant from FEMA after'], 'var_call_iNpkxmKmPItNk2kCNqBKXSom': ['Funding'], 'var_call_YK2GTFjaALiJRyaiqJp1v5Gu': 'file_storage/call_YK2GTFjaALiJRyaiqJp1v5Gu.json', 'var_call_BETRXzm9RmKj3j3EAzRg1zqx': [{'Project_Name': '2022 Morning View Resurfacing & Storm Drain Improvements', 'Funding_Source': 'State Development Grant', 'Amount': 38000}, {'Project_Name': 'Birdview Avenue Improvements', 'Funding_Source': 'National Foundation Fund', 'Amount': 79000}, {'Project_Name': 'Birdview Avenue Improvements (CalOES Project)', 'Funding_Source': 'International Aid', 'Amount': 85000}, {'Project_Name': 'Birdview Avenue Improvements (FEMA/CalOES Project)', 'Funding_Source': 'Research Institution Funding', 'Amount': 14000}, {'Project_Name': 'Citywide Guardrail Replacement', 'Funding_Source': 'Infrastructure Bond', 'Amount': 30000}, {'Project_Name': 'Clover Heights Storm Drain', 'Funding_Source': 'Infrastructure Bond', 'Amount': 53000}, {'Project_Name': 'Clover Heights Storm Drain (FEMA Project)', 'Funding_Source': 'Local NGO Fund', 'Amount': 21000}, {'Project_Name': 'Clover Heights Storm Drainage Improvements', 'Funding_Source': 'Development Bank Loan', 'Amount': 22000}, {'Project_Name': 'Corral Canyon Culvert Repairs', 'Funding_Source': 'Federal Assistance', 'Amount': 54000}, {'Project_Name': 'Corral Canyon Culvert Repairs (FEMA Project)', 'Funding_Source': 'Municipal Fund', 'Amount': 43000}, {'Project_Name': 'Corral Canyon Culvert Repairs (FEMA/CalOES Project)', 'Funding_Source': 'Taxpayer Contribution', 'Amount': 15000}, {'Project_Name': 'Corral Canyon Road Bridge Repairs', 'Funding_Source': 'Technology Innovation Fund', 'Amount': 68000}, {'Project_Name': 'Corral Canyon Road Bridge Repairs (FEMA Project)', 'Funding_Source': 'Local Business Support', 'Amount': 25000}, {'Project_Name': 'Corral Canyon Road Bridge Repairs (FEMA/CalOES Project)', 'Funding_Source': 'Cultural Heritage Grant', 'Amount': 58000}, {'Project_Name': 'Encinal Canyon 60-inch Storm Drain Repairs', 'Funding_Source': 'Municipal Fund', 'Amount': 56000}, {'Project_Name': 'Encinal Canyon Road Drainage Improvements (FEMA/CalOES Project)', 'Funding_Source': 'Private Sponsor', 'Amount': 94000}, {'Project_Name': 'Guardrail Replacement Citywide', 'Funding_Source': 'International Aid', 'Amount': 39000}, {'Project_Name': 'Guardrail Replacement Citywide (FEMA Project)', 'Funding_Source': 'Impact Investment Fund', 'Amount': 22000}, {'Project_Name': 'Guardrail Replacement Citywide (FEMA/CalOES Project)', 'Funding_Source': 'Development Bank Loan', 'Amount': 45000}, {'Project_Name': 'Latigo Canyon Road Culvert Repairs', 'Funding_Source': 'Community Fund', 'Amount': 57000}, {'Project_Name': 'Latigo Canyon Road Culvert Repairs (FEMA Project)', 'Funding_Source': 'Federal Assistance', 'Amount': 36000}, {'Project_Name': 'Latigo Canyon Road Culvert Repairs (FEMA/CalOES Project)', 'Funding_Source': 'National Foundation Fund', 'Amount': 44000}, {'Project_Name': 'Latigo Canyon Road Retaining Wall Repair Project', 'Funding_Source': 'Educational Sponsorship', 'Amount': 97000}, {'Project_Name': 'Latigo Canyon Road Roadway/Retaining Wall Improvements', 'Funding_Source': 'Public-Private Partnership (PPP)', 'Amount': 19000}, {'Project_Name': 'Latigo Canyon Road Roadway/Retaining Wall Improvements (FEMA Project)', 'Funding_Source': 'Municipal Fund', 'Amount': 91000}, {'Project_Name': 'Latigo Canyon Road Roadway/Retaining Wall Improvements (FEMA/CalOES Project)', 'Funding_Source': 'Community Fund', 'Amount': 78000}, {'Project_Name': 'Malibu Park Storm Drain Repairs', 'Funding_Source': 'Taxpayer Contribution', 'Amount': 50000}, {'Project_Name': 'Outdoor Warning Signs', 'Funding_Source': 'Urban Renewal Fund', 'Amount': 92000}, {'Project_Name': 'Outdoor Warning Sirens', 'Funding_Source': 'Social Impact Investment', 'Amount': 28000}, {'Project_Name': 'Outdoor Warning Sirens (FEMA Project)', 'Funding_Source': 'Environmental Grant', 'Amount': 27000}, {'Project_Name': 'Outdoor Warning Sirens (FEMA)', 'Funding_Source': 'State Development Grant', 'Amount': 81000}, {'Project_Name': 'Outdoor Warning Sirens - Design (FEMA Project)', 'Funding_Source': 'Local Business Support', 'Amount': 43000}, {'Project_Name': 'Outdoor Warningn Sirens - Design (FEMA Project)', 'Funding_Source': 'Technology Innovation Fund', 'Amount': 84000}, {'Project_Name': 'PCH at Trancas Canyon Road Right Turn Lane', 'Funding_Source': 'Corporate Sponsorship', 'Amount': 90000}, {'Project_Name': 'Storm Drain Master Plan', 'Funding_Source': 'Social Impact Investment', 'Amount': 77000}, {'Project_Name': 'Storm Drain Master Plan (FEMA Project)', 'Funding_Source': 'Environmental Grant', 'Amount': 80000}, {'Project_Name': 'Storm Drain Trash Screens', 'Funding_Source': 'Impact Investment Fund', 'Amount': 11000}, {'Project_Name': 'Storm Drain Trash Screens Phase Two', 'Funding_Source': 'National Foundation Fund', 'Amount': 24000}, {'Project_Name': 'Trancas Canyon Park Planting and Irrigation Repairs', 'Funding_Source': 'National Foundation Fund', 'Amount': 78000}, {'Project_Name': 'Trancas Canyon Park Planting and Irrigation Repairs (CalJPIA/FEMA Project)', 'Funding_Source': 'Infrastructure Bond', 'Amount': 44000}, {'Project_Name': 'Trancas Canyon Park Planting and Irrigation Repairs (FEMA/CalOES Project)', 'Funding_Source': 'Infrastructure Bond', 'Amount': 92000}, {'Project_Name': 'Trancas Canyon Park Playground', 'Funding_Source': 'Crowdfunding', 'Amount': 24000}, {'Project_Name': 'Trancas Canyon Park Playground Resurfacing', 'Funding_Source': 'Philanthropic Donation', 'Amount': 65000}, {'Project_Name': 'Trancas Canyon Park Slope Stabilization Project', 'Funding_Source': 'Community Fund', 'Amount': 68000}, {'Project_Name': 'Trancas Canyon Park Slope Stabilization Project (CalJPIA Project)', 'Funding_Source': 'Government Grant', 'Amount': 43000}, {'Project_Name': 'Trancas Canyon Park Slope Stabilization Project (CalOES Project)', 'Funding_Source': 'International Organization Grant', 'Amount': 32000}, {'Project_Name': 'Trancas Canyon Park Upper and Lower Slopes Repair', 'Funding_Source': 'International Organization Grant', 'Amount': 23000}]}

exec(code, env_args)
