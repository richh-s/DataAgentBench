code = """import json
import re

# Load variables from storage
funding = var_call_xy48n9EkXhY0prQAdNASJbCR
civic_docs_path = var_call_Z9NGZMQEp28EdZkpBmEEBrRG

# civic_docs_path is a filepath to the JSON results
with open(civic_docs_path, 'r', encoding='utf-8') as f:
    civic_docs = json.load(f)

# Normalize and prepare funding records
records = funding

results = []

for rec in records:
    proj_name = rec.get('Project_Name')
    funding_source = rec.get('Funding_Source')
    # Normalize amount to int if possible
    amt_raw = rec.get('Amount')
    try:
        amount = int(amt_raw)
    except:
        try:
            amount = int(float(amt_raw))
        except:
            amount = None

    # create base name by removing parenthetical suffixes
    base = re.sub(r"\s*\(.*?\)", "", proj_name).strip().lower()

    status_found = None
    matched_doc = None

    for doc in civic_docs:
        text = doc.get('text','').lower()
        if base in text:
            matched_doc = doc
            # find position
            pos = text.find(base)
            start = max(0, pos-500)
            end = min(len(text), pos+500)
            context = text[start:end]

            # status heuristics
            if 'completed' in context or 'construction was completed' in context or 'notice of completion' in context:
                status_found = 'completed'
            elif '(not started)' in context or 'not started' in context:
                status_found = 'not started'
            elif '(design)' in context or 'complete design' in context or 'final design' in context or 'preliminary design' in context or 'working with the consultant to finalize the design' in context:
                status_found = 'design'
            elif '(construction)' in context or 'begin construction' in context or 'under construction' in context or 'begin construction' in context:
                # map to 'construction' to reflect doc section
                status_found = 'construction'
            else:
                # search broader nearby for section headers
                # look backwards for section header within previous 2000 chars
                back_start = max(0, pos-2000)
                header_area = text[back_start:pos]
                if 'capital improvement projects (design)' in header_area or 'capital improvement projects (design)' in text:
                    status_found = 'design'
                elif 'capital improvement projects (construction)' in header_area or 'capital improvement projects (construction)' in text:
                    status_found = 'construction'
                elif 'capital improvement projects (not started)' in header_area or 'capital improvement projects (not started)' in text:
                    status_found = 'not started'
                else:
                    status_found = None
            break

    results.append({
        'Project_Name': proj_name,
        'Funding_Source': funding_source,
        'Amount': amount,
        'Status': status_found
    })

# Output JSON string
out = json.dumps(results)
print("__RESULT__:")
print(out)"""

env_args = {'var_call_j6rOjLdDlVGB2aC1VfCAnghr': ['civic_docs'], 'var_call_cf833bkFBFDJJCig6ejAhyYr': ['Funding'], 'var_call_xy48n9EkXhY0prQAdNASJbCR': [{'Funding_ID': '7', 'Project_Name': 'Birdview Avenue Improvements (FEMA/CalOES Project)', 'Funding_Source': 'Research Institution Funding', 'Amount': '14000'}, {'Funding_ID': '22', 'Project_Name': 'Clover Heights Storm Drain (FEMA Project)', 'Funding_Source': 'Local NGO Fund', 'Amount': '21000'}, {'Funding_ID': '25', 'Project_Name': 'Corral Canyon Culvert Repairs (FEMA Project)', 'Funding_Source': 'Municipal Fund', 'Amount': '43000'}, {'Funding_ID': '26', 'Project_Name': 'Corral Canyon Culvert Repairs (FEMA/CalOES Project)', 'Funding_Source': 'Taxpayer Contribution', 'Amount': '15000'}, {'Funding_ID': '28', 'Project_Name': 'Corral Canyon Road Bridge Repairs (FEMA Project)', 'Funding_Source': 'Local Business Support', 'Amount': '25000'}, {'Funding_ID': '29', 'Project_Name': 'Corral Canyon Road Bridge Repairs (FEMA/CalOES Project)', 'Funding_Source': 'Cultural Heritage Grant', 'Amount': '58000'}, {'Funding_ID': '35', 'Project_Name': 'Encinal Canyon Road Drainage Improvements (FEMA/CalOES Project)', 'Funding_Source': 'Private Sponsor', 'Amount': '94000'}, {'Funding_ID': '38', 'Project_Name': 'Guardrail Replacement Citywide (FEMA Project)', 'Funding_Source': 'Impact Investment Fund', 'Amount': '22000'}, {'Funding_ID': '39', 'Project_Name': 'Guardrail Replacement Citywide (FEMA/CalOES Project)', 'Funding_Source': 'Development Bank Loan', 'Amount': '45000'}, {'Funding_ID': '43', 'Project_Name': 'Latigo Canyon Road Culvert Repairs (FEMA Project)', 'Funding_Source': 'Federal Assistance', 'Amount': '36000'}, {'Funding_ID': '44', 'Project_Name': 'Latigo Canyon Road Culvert Repairs (FEMA/CalOES Project)', 'Funding_Source': 'National Foundation Fund', 'Amount': '44000'}, {'Funding_ID': '47', 'Project_Name': 'Latigo Canyon Road Roadway/Retaining Wall Improvements (FEMA Project)', 'Funding_Source': 'Municipal Fund', 'Amount': '91000'}, {'Funding_ID': '48', 'Project_Name': 'Latigo Canyon Road Roadway/Retaining Wall Improvements (FEMA/CalOES Project)', 'Funding_Source': 'Community Fund', 'Amount': '78000'}, {'Funding_ID': '66', 'Project_Name': 'Outdoor Warning Sirens (FEMA Project)', 'Funding_Source': 'Environmental Grant', 'Amount': '27000'}, {'Funding_ID': '67', 'Project_Name': 'Outdoor Warning Sirens (FEMA)', 'Funding_Source': 'State Development Grant', 'Amount': '81000'}, {'Funding_ID': '68', 'Project_Name': 'Outdoor Warning Sirens - Design (FEMA Project)', 'Funding_Source': 'Local Business Support', 'Amount': '43000'}, {'Funding_ID': '69', 'Project_Name': 'Outdoor Warningn Sirens - Design (FEMA Project)', 'Funding_Source': 'Technology Innovation Fund', 'Amount': '84000'}, {'Funding_ID': '82', 'Project_Name': 'Storm Drain Master Plan (FEMA Project)', 'Funding_Source': 'Environmental Grant', 'Amount': '80000'}, {'Funding_ID': '86', 'Project_Name': 'Trancas Canyon Park Planting and Irrigation Repairs (CalJPIA/FEMA Project)', 'Funding_Source': 'Infrastructure Bond', 'Amount': '44000'}, {'Funding_ID': '87', 'Project_Name': 'Trancas Canyon Park Planting and Irrigation Repairs (FEMA/CalOES Project)', 'Funding_Source': 'Infrastructure Bond', 'Amount': '92000'}], 'var_call_Z9NGZMQEp28EdZkpBmEEBrRG': 'file_storage/call_Z9NGZMQEp28EdZkpBmEEBrRG.json'}

exec(code, env_args)
