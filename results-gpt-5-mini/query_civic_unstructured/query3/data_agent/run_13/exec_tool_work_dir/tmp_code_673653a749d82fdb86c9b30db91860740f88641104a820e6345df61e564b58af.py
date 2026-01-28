code = """import json
import re
from pathlib import Path

# Load civic docs query result from file path provided in storage
civic_docs_path = Path(var_call_1dycdWjdCJ60Y3sMhxoBVKFE)
with civic_docs_path.open('r', encoding='utf-8') as f:
    civic_docs = json.load(f)

funding_records = var_call_6PC54d4BBrkrKdZE7W134DO1

# Topic keywords from database description
topic_keywords = ['park', 'road', 'FEMA', 'fire', 'emergency warning', 'drainage', 'storm drain', 'highway', 'bridge', 'playground', 'water treatment', 'guardrail', 'sirens', 'outdoor warning', 'warning']

results = []

for fr in funding_records:
    proj_name = fr.get('Project_Name')
    funding_source = fr.get('Funding_Source')
    amount = fr.get('Amount')

    # Normalize core project name by removing parenthetical suffixes
    core_name = re.sub(r"\s*\(.*?\)\s*", "", proj_name).strip()
    # Build regex pattern to search for the core name or important tokens
    core_escaped = re.escape(core_name)
    pattern = re.compile(core_escaped, re.I)

    found = False
    status = None
    found_topics = set()
    ptype = None

    for doc in civic_docs:
        text = doc.get('text','')
        if pattern.search(text):
            found = True
            m = pattern.search(text)
            idx = m.start()
            context = text[max(0, idx-300): idx+300]

            if re.search(r'notice of completion|construction was completed|complete construction|completed', context, re.I):
                status = 'completed'
            elif re.search(r'under construction|begin construction|beginning construction|award the contract|awarded the contract|construction', context, re.I):
                status = 'design'
            elif re.search(r'complete design|final design|preliminary design|design plans|design', context, re.I):
                status = 'design'
            elif re.search(r'not started|identified|to be|will be', context, re.I):
                status = 'not started'

            if re.search(r'FEMA|CalOES|CalJPIA|disaster|fire|Woolsey', context, re.I) or re.search(r'FEMA|CalOES|CalJPIA|disaster|fire|Woolsey', proj_name, re.I):
                ptype = 'disaster'
            elif re.search(r'Capital Improvement|Capital Improvement Projects|Capital Improvement Program', context, re.I):
                ptype = 'capital'

            for kw in topic_keywords:
                if re.search(re.escape(kw), context, re.I) or re.search(re.escape(kw), text, re.I):
                    found_topics.add(kw)
            break

    if not found:
        tokens = [t for t in re.split(r'[^A-Za-z0-9]+', core_name) if len(t)>3]
        token_pattern = re.compile(r'(' + r'|'.join([re.escape(t) for t in tokens]) + r')', re.I) if tokens else None
        for doc in civic_docs:
            text = doc.get('text','')
            if token_pattern and token_pattern.search(text):
                found = True
                context = text
                if re.search(r'notice of completion|construction was completed|complete construction|completed', context, re.I):
                    status = 'completed'
                elif re.search(r'under construction|begin construction|construction', context, re.I):
                    status = 'design'
                elif re.search(r'complete design|final design|preliminary design|design plans|design', context, re.I):
                    status = 'design'
                elif re.search(r'not started|identified|to be|will be', context, re.I):
                    status = 'not started'

                if re.search(r'FEMA|CalOES|CalJPIA|disaster|fire|Woolsey', context, re.I) or re.search(r'FEMA|CalOES|CalJPIA|disaster|fire|Woolsey', proj_name, re.I):
                    ptype = 'disaster'
                elif re.search(r'Capital Improvement|Capital Improvement Projects|Capital Improvement Program', context, re.I):
                    ptype = 'capital'

                for kw in topic_keywords:
                    if re.search(re.escape(kw), context, re.I):
                        found_topics.add(kw)
                break

    # Convert amount to int when possible
    try:
        amt_val = int(amount)
    except Exception:
        try:
            amt_val = int(float(amount))
        except Exception:
            amt_val = amount

    result_entry = {
        'Project_Name': proj_name,
        'Funding_Source': funding_source,
        'Amount': amt_val,
        'Status': status if status is not None else None,
        'Type': ptype if ptype is not None else None,
        'Topics': sorted(list(found_topics))
    }
    results.append(result_entry)

# Print results in required format
print("__RESULT__:")
print(json.dumps(results))"""

env_args = {'var_call_1dycdWjdCJ60Y3sMhxoBVKFE': 'file_storage/call_1dycdWjdCJ60Y3sMhxoBVKFE.json', 'var_call_6PC54d4BBrkrKdZE7W134DO1': [{'Funding_ID': '7', 'Project_Name': 'Birdview Avenue Improvements (FEMA/CalOES Project)', 'Funding_Source': 'Research Institution Funding', 'Amount': '14000'}, {'Funding_ID': '22', 'Project_Name': 'Clover Heights Storm Drain (FEMA Project)', 'Funding_Source': 'Local NGO Fund', 'Amount': '21000'}, {'Funding_ID': '25', 'Project_Name': 'Corral Canyon Culvert Repairs (FEMA Project)', 'Funding_Source': 'Municipal Fund', 'Amount': '43000'}, {'Funding_ID': '26', 'Project_Name': 'Corral Canyon Culvert Repairs (FEMA/CalOES Project)', 'Funding_Source': 'Taxpayer Contribution', 'Amount': '15000'}, {'Funding_ID': '28', 'Project_Name': 'Corral Canyon Road Bridge Repairs (FEMA Project)', 'Funding_Source': 'Local Business Support', 'Amount': '25000'}, {'Funding_ID': '29', 'Project_Name': 'Corral Canyon Road Bridge Repairs (FEMA/CalOES Project)', 'Funding_Source': 'Cultural Heritage Grant', 'Amount': '58000'}, {'Funding_ID': '35', 'Project_Name': 'Encinal Canyon Road Drainage Improvements (FEMA/CalOES Project)', 'Funding_Source': 'Private Sponsor', 'Amount': '94000'}, {'Funding_ID': '38', 'Project_Name': 'Guardrail Replacement Citywide (FEMA Project)', 'Funding_Source': 'Impact Investment Fund', 'Amount': '22000'}, {'Funding_ID': '39', 'Project_Name': 'Guardrail Replacement Citywide (FEMA/CalOES Project)', 'Funding_Source': 'Development Bank Loan', 'Amount': '45000'}, {'Funding_ID': '43', 'Project_Name': 'Latigo Canyon Road Culvert Repairs (FEMA Project)', 'Funding_Source': 'Federal Assistance', 'Amount': '36000'}, {'Funding_ID': '44', 'Project_Name': 'Latigo Canyon Road Culvert Repairs (FEMA/CalOES Project)', 'Funding_Source': 'National Foundation Fund', 'Amount': '44000'}, {'Funding_ID': '47', 'Project_Name': 'Latigo Canyon Road Roadway/Retaining Wall Improvements (FEMA Project)', 'Funding_Source': 'Municipal Fund', 'Amount': '91000'}, {'Funding_ID': '48', 'Project_Name': 'Latigo Canyon Road Roadway/Retaining Wall Improvements (FEMA/CalOES Project)', 'Funding_Source': 'Community Fund', 'Amount': '78000'}, {'Funding_ID': '66', 'Project_Name': 'Outdoor Warning Sirens (FEMA Project)', 'Funding_Source': 'Environmental Grant', 'Amount': '27000'}, {'Funding_ID': '67', 'Project_Name': 'Outdoor Warning Sirens (FEMA)', 'Funding_Source': 'State Development Grant', 'Amount': '81000'}, {'Funding_ID': '68', 'Project_Name': 'Outdoor Warning Sirens - Design (FEMA Project)', 'Funding_Source': 'Local Business Support', 'Amount': '43000'}, {'Funding_ID': '69', 'Project_Name': 'Outdoor Warningn Sirens - Design (FEMA Project)', 'Funding_Source': 'Technology Innovation Fund', 'Amount': '84000'}, {'Funding_ID': '82', 'Project_Name': 'Storm Drain Master Plan (FEMA Project)', 'Funding_Source': 'Environmental Grant', 'Amount': '80000'}, {'Funding_ID': '86', 'Project_Name': 'Trancas Canyon Park Planting and Irrigation Repairs (CalJPIA/FEMA Project)', 'Funding_Source': 'Infrastructure Bond', 'Amount': '44000'}, {'Funding_ID': '87', 'Project_Name': 'Trancas Canyon Park Planting and Irrigation Repairs (FEMA/CalOES Project)', 'Funding_Source': 'Infrastructure Bond', 'Amount': '92000'}]}

exec(code, env_args)
