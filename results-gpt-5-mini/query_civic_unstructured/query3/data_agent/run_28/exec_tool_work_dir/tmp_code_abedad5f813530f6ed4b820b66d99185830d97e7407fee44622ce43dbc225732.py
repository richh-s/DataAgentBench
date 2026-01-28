code = """import json, re
# Load variables from storage
clean_names = var_call_f6c4OrX1ADPiRK3XZqSwT77I
# docs file path
docs_path = var_call_QxtrsIHo3FAzElPyUC4rh1RS
# funding full table path
funding_path = var_call_YK2GTFjaALiJRyaiqJp1v5Gu

with open(docs_path, 'r', encoding='utf-8') as f:
    docs = json.load(f)
with open(funding_path, 'r', encoding='utf-8') as f:
    funding = json.load(f)

keywords = ['fema','emergency','siren','outdoor warning']

# select candidates that mention FEMA or emergency-related keywords
candidates = []
for n in clean_names:
    if any(k in n.lower() for k in keywords):
        candidates.append(n)

# helper to get core name (remove parenthetical suffixes)
def core_name(s):
    s2 = re.sub(r"\(.*?\)", "", s).strip()
    return re.sub(r"\s+", " ", s2)

results = []
seen = set()
for cand in candidates:
    cand_clean = core_name(cand)
    cand_low = cand_clean.lower()
    # find funding matches
    matched_funding = []
    for fr in funding:
        fname = fr.get('Project_Name','')
        fname_low = fname.lower()
        if cand_low and (cand_low in fname_low or fname_low in cand_low):
            # parse amount to int if possible
            amt = fr.get('Amount')
            try:
                amt_val = int(amt)
            except:
                try:
                    amt_val = int(float(amt))
                except:
                    amt_val = amt
            matched_funding.append({'Funding_Source': fr.get('Funding_Source'), 'Amount': amt_val})
    # determine status by scanning docs for occurrence
    status = 'unknown'
    for doc in docs:
        text = doc.get('text','').lower()
        if cand.lower() in text or cand_clean.lower() in text:
            idx = text.find(cand_clean.lower()) if cand_clean.lower() in text else text.find(cand.lower())
            if idx == -1:
                idx = 0
            window = text[max(0, idx-300): idx+300]
            if 'disaster projects (completed)' in window or 'notice of completion' in window or 'completion date' in window or 'complete construction' in window or 'completed' in window:
                status = 'completed'
                break
            if 'disaster projects (not started)' in window or 'not started' in window:
                status = 'not started'
                break
            if 'design' in window or 'complete design' in window or 'preliminary design' in window or 'estimated schedule' in window or 'begin construction' in window or 'advertise' in window or 'awarded a fema' in window or 'dependent upon final grant approval' in window:
                status = 'design'
                break
    # if no funding matches, still include any funding records that exactly match candidate in funding list
    if not matched_funding:
        for fr in funding:
            if cand.lower() in fr.get('Project_Name','').lower():
                try:
                    amt_val = int(fr.get('Amount'))
                except:
                    try:
                        amt_val = int(float(fr.get('Amount')))
                    except:
                        amt_val = fr.get('Amount')
                matched_funding.append({'Funding_Source': fr.get('Funding_Source'), 'Amount': amt_val})
    # if still none, leave funding empty
    if not matched_funding:
        matched_funding = [None]
    for mf in matched_funding:
        pname = cand_clean
        key = (pname.lower(), mf['Funding_Source'] if mf else None, mf['Amount'] if mf else None)
        if key in seen:
            continue
        seen.add(key)
        if mf:
            results.append({'Project_Name': pname, 'Funding_Source': mf.get('Funding_Source'), 'Amount': mf.get('Amount'), 'Status': status})
        else:
            results.append({'Project_Name': pname, 'Funding_Source': None, 'Amount': None, 'Status': status})

# Sort results by Project_Name
results_sorted = sorted(results, key=lambda x: x['Project_Name'].lower())

print("__RESULT__:")
print(json.dumps(results_sorted))"""

env_args = {'var_call_QxtrsIHo3FAzElPyUC4rh1RS': 'file_storage/call_QxtrsIHo3FAzElPyUC4rh1RS.json', 'var_call_nk3UJd1gvwIdkU5NgDjoZ9tX': 'file_storage/call_nk3UJd1gvwIdkU5NgDjoZ9tX.json', 'var_call_f6c4OrX1ADPiRK3XZqSwT77I': ['Awaiting final FEMA/CalOES approval for scope modification', 'Latigo Canyon Road Roadway/Retaining Wall Improvements (FEMA Project)', 'Staff is also working with FEMA/CalOES to substitute the existing', 'Trancas Canyon Park Planting and Irrigation Repairs (CalJPIA/FEMA Project)', 'Project Description: This project will be funded through a grant from FEMA', 'drains, culverts, debris basins, manholes, and other drainage structures', 'Guardrail Replacement Citywide (FEMA Project)', 'guardrail throughout the City as a result of the Woolsey Fire.', 'Corral Canyon Road Bridge Repairs (FEMA Project)', 'fencing and repairing the damaged embankment adjacent to the bridge.', 'Corral Canyon Culvert Repairs (FEMA Project)', 'Project Description: This project has been cancelled as it could not get FEMA', 'Clover Heights Storm Drain (FEMA Project)', 'Latigo Canyon Road Culvert Repairs (FEMA Project)', 'Project Description: This project consists of repairing the existing storm drain', 'Outdoor Warningn Sirens - Design (FEMA Project)', 'Project Description: An Emergency Warning Siren system will improve the', 'the Emergency Warning Sirens project will be implementation of the design', 'awarded a FEMA Hazard Mitigation grant to fund the design, engineering and', 'plan, including purchasing, installing, and testing the sirens. The City will', 'Trancas Canyon Park Planting and Irrigation Repairs (FEMA/CalOES Project)', 'Birdview Avenue Improvements (FEMA/CalOES Project)', 'Guardrail Replacement Citywide (FEMA/CalOES Project)', 'Latigo Canyon Road Culvert Repairs (FEMA/CalOES Project)', 'Outdoor Warning Sirens (FEMA)', 'Complete Design: Dependent upon final grant approval from FEMA', 'Outdoor Warning Sirens (FEMA Project)', 'Storm Drain Master Plan (FEMA Project)', 'infrastructure requirements, and siren sound range. The City has been', 'determine the optimal number and locations of individual sirens, power and', 'Latigo Canyon Road Roadway/Retaining Wall Improvements (FEMA/CalOES', 'Updates: This project will be funded through a grant from FEMA after the', 'bridge.', 'Corral Canyon Culvert Repairs (FEMA/CalOES Project)', 'Staff is working with FEMA/CalOES to substitute the existing timber', 'guardrails within the project limits.', 'Outdoor Warning Sirens - Design (FEMA Project)', 'Advertise: Fall 2023 (dependent upon FEMA/CalOES approval)', 'Project close out process has been initiated with FEMA/CalOES.', 'Advertise: Spring 2024 (dependent upon FEMA/CalOES approval)', 'Begin Construction: Summer 2024 (dependent upon FEMA/CalOES', 'Advertise: (dependent upon FEMA/CalOES approval)', 'Begin Construction: (dependent upon FEMA/CalOES approval)', 'Project Description: This project is funded through a grant from FEMA after'], 'var_call_iNpkxmKmPItNk2kCNqBKXSom': ['Funding'], 'var_call_YK2GTFjaALiJRyaiqJp1v5Gu': 'file_storage/call_YK2GTFjaALiJRyaiqJp1v5Gu.json', 'var_call_BETRXzm9RmKj3j3EAzRg1zqx': [{'Project_Name': '2022 Morning View Resurfacing & Storm Drain Improvements', 'Funding_Source': 'State Development Grant', 'Amount': 38000}, {'Project_Name': 'Birdview Avenue Improvements', 'Funding_Source': 'National Foundation Fund', 'Amount': 79000}, {'Project_Name': 'Birdview Avenue Improvements (CalOES Project)', 'Funding_Source': 'International Aid', 'Amount': 85000}, {'Project_Name': 'Birdview Avenue Improvements (FEMA/CalOES Project)', 'Funding_Source': 'Research Institution Funding', 'Amount': 14000}, {'Project_Name': 'Citywide Guardrail Replacement', 'Funding_Source': 'Infrastructure Bond', 'Amount': 30000}, {'Project_Name': 'Clover Heights Storm Drain', 'Funding_Source': 'Infrastructure Bond', 'Amount': 53000}, {'Project_Name': 'Clover Heights Storm Drain (FEMA Project)', 'Funding_Source': 'Local NGO Fund', 'Amount': 21000}, {'Project_Name': 'Clover Heights Storm Drainage Improvements', 'Funding_Source': 'Development Bank Loan', 'Amount': 22000}, {'Project_Name': 'Corral Canyon Culvert Repairs', 'Funding_Source': 'Federal Assistance', 'Amount': 54000}, {'Project_Name': 'Corral Canyon Culvert Repairs (FEMA Project)', 'Funding_Source': 'Municipal Fund', 'Amount': 43000}, {'Project_Name': 'Corral Canyon Culvert Repairs (FEMA/CalOES Project)', 'Funding_Source': 'Taxpayer Contribution', 'Amount': 15000}, {'Project_Name': 'Corral Canyon Road Bridge Repairs', 'Funding_Source': 'Technology Innovation Fund', 'Amount': 68000}, {'Project_Name': 'Corral Canyon Road Bridge Repairs (FEMA Project)', 'Funding_Source': 'Local Business Support', 'Amount': 25000}, {'Project_Name': 'Corral Canyon Road Bridge Repairs (FEMA/CalOES Project)', 'Funding_Source': 'Cultural Heritage Grant', 'Amount': 58000}, {'Project_Name': 'Encinal Canyon 60-inch Storm Drain Repairs', 'Funding_Source': 'Municipal Fund', 'Amount': 56000}, {'Project_Name': 'Encinal Canyon Road Drainage Improvements (FEMA/CalOES Project)', 'Funding_Source': 'Private Sponsor', 'Amount': 94000}, {'Project_Name': 'Guardrail Replacement Citywide', 'Funding_Source': 'International Aid', 'Amount': 39000}, {'Project_Name': 'Guardrail Replacement Citywide (FEMA Project)', 'Funding_Source': 'Impact Investment Fund', 'Amount': 22000}, {'Project_Name': 'Guardrail Replacement Citywide (FEMA/CalOES Project)', 'Funding_Source': 'Development Bank Loan', 'Amount': 45000}, {'Project_Name': 'Latigo Canyon Road Culvert Repairs', 'Funding_Source': 'Community Fund', 'Amount': 57000}, {'Project_Name': 'Latigo Canyon Road Culvert Repairs (FEMA Project)', 'Funding_Source': 'Federal Assistance', 'Amount': 36000}, {'Project_Name': 'Latigo Canyon Road Culvert Repairs (FEMA/CalOES Project)', 'Funding_Source': 'National Foundation Fund', 'Amount': 44000}, {'Project_Name': 'Latigo Canyon Road Retaining Wall Repair Project', 'Funding_Source': 'Educational Sponsorship', 'Amount': 97000}, {'Project_Name': 'Latigo Canyon Road Roadway/Retaining Wall Improvements', 'Funding_Source': 'Public-Private Partnership (PPP)', 'Amount': 19000}, {'Project_Name': 'Latigo Canyon Road Roadway/Retaining Wall Improvements (FEMA Project)', 'Funding_Source': 'Municipal Fund', 'Amount': 91000}, {'Project_Name': 'Latigo Canyon Road Roadway/Retaining Wall Improvements (FEMA/CalOES Project)', 'Funding_Source': 'Community Fund', 'Amount': 78000}, {'Project_Name': 'Malibu Park Storm Drain Repairs', 'Funding_Source': 'Taxpayer Contribution', 'Amount': 50000}, {'Project_Name': 'Outdoor Warning Signs', 'Funding_Source': 'Urban Renewal Fund', 'Amount': 92000}, {'Project_Name': 'Outdoor Warning Sirens', 'Funding_Source': 'Social Impact Investment', 'Amount': 28000}, {'Project_Name': 'Outdoor Warning Sirens (FEMA Project)', 'Funding_Source': 'Environmental Grant', 'Amount': 27000}, {'Project_Name': 'Outdoor Warning Sirens (FEMA)', 'Funding_Source': 'State Development Grant', 'Amount': 81000}, {'Project_Name': 'Outdoor Warning Sirens - Design (FEMA Project)', 'Funding_Source': 'Local Business Support', 'Amount': 43000}, {'Project_Name': 'Outdoor Warningn Sirens - Design (FEMA Project)', 'Funding_Source': 'Technology Innovation Fund', 'Amount': 84000}, {'Project_Name': 'PCH at Trancas Canyon Road Right Turn Lane', 'Funding_Source': 'Corporate Sponsorship', 'Amount': 90000}, {'Project_Name': 'Storm Drain Master Plan', 'Funding_Source': 'Social Impact Investment', 'Amount': 77000}, {'Project_Name': 'Storm Drain Master Plan (FEMA Project)', 'Funding_Source': 'Environmental Grant', 'Amount': 80000}, {'Project_Name': 'Storm Drain Trash Screens', 'Funding_Source': 'Impact Investment Fund', 'Amount': 11000}, {'Project_Name': 'Storm Drain Trash Screens Phase Two', 'Funding_Source': 'National Foundation Fund', 'Amount': 24000}, {'Project_Name': 'Trancas Canyon Park Planting and Irrigation Repairs', 'Funding_Source': 'National Foundation Fund', 'Amount': 78000}, {'Project_Name': 'Trancas Canyon Park Planting and Irrigation Repairs (CalJPIA/FEMA Project)', 'Funding_Source': 'Infrastructure Bond', 'Amount': 44000}, {'Project_Name': 'Trancas Canyon Park Planting and Irrigation Repairs (FEMA/CalOES Project)', 'Funding_Source': 'Infrastructure Bond', 'Amount': 92000}, {'Project_Name': 'Trancas Canyon Park Playground', 'Funding_Source': 'Crowdfunding', 'Amount': 24000}, {'Project_Name': 'Trancas Canyon Park Playground Resurfacing', 'Funding_Source': 'Philanthropic Donation', 'Amount': 65000}, {'Project_Name': 'Trancas Canyon Park Slope Stabilization Project', 'Funding_Source': 'Community Fund', 'Amount': 68000}, {'Project_Name': 'Trancas Canyon Park Slope Stabilization Project (CalJPIA Project)', 'Funding_Source': 'Government Grant', 'Amount': 43000}, {'Project_Name': 'Trancas Canyon Park Slope Stabilization Project (CalOES Project)', 'Funding_Source': 'International Organization Grant', 'Amount': 32000}, {'Project_Name': 'Trancas Canyon Park Upper and Lower Slopes Repair', 'Funding_Source': 'International Organization Grant', 'Amount': 23000}]}

exec(code, env_args)
