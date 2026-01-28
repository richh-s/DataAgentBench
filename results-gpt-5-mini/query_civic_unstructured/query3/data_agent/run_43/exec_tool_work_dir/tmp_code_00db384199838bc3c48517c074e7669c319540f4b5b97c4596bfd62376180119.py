code = """import json
from pathlib import Path

# Load full civic docs and funding results from previous calls
with open(var_call_K8WCGLuypwD3TFDA4oFnCzzv, 'r', encoding='utf-8') as f:
    civic_docs = json.load(f)
with open(var_call_5Jo9Dho7c1zbDpaJW0AXDqwA, 'r', encoding='utf-8') as f:
    funding_related = json.load(f)

# Combine civic docs text
all_text = "\n\n".join(d.get('text','') for d in civic_docs)
lt = all_text.lower()

# helper to infer status
def infer_status(project_name):
    pn = (project_name or '').lower()
    # exact or simple match
    idx = lt.find(pn)
    if idx == -1 and '(' in pn:
        pn_simple = pn.split('(')[0].strip()
        idx = lt.find(pn_simple)
    if idx != -1:
        context = lt[max(0, idx-300): idx+300]
        if 'complete design' in context or 'final design' in context or 'preliminary design' in context or 'finalize the design' in context:
            return 'design'
        if 'construction was completed' in context or 'notice of completion' in context or 'complete construction' in context:
            return 'completed'
        if 'currently under construction' in context:
            return 'completed'
        if 'begin construction' in context or 'advertise' in context or 'will begin' in context or 'begin construction:' in context:
            return 'not started'
        if 'not started' in context or 'identified' in context or 'waiting' in context or 'awaiting' in context:
            return 'not started'
    # fallback: check keywords
    for kw in ['outdoor warning', 'outdoor warning sirens', 'fema', 'emergency', 'latigo canyon', 'clover heights', 'encinal canyon', 'guardrail', 'storm drain master plan', 'trancas canyon']:
        if kw in pn or kw in lt:
            idx2 = lt.find(kw)
            if idx2 != -1:
                context = lt[max(0, idx2-300): idx2+300]
                if 'complete design' in context or 'final design' in context or 'preliminary design' in context:
                    return 'design'
                if 'construction was completed' in context or 'notice of completion' in context or 'complete construction' in context:
                    return 'completed'
                if 'currently under construction' in context:
                    return 'completed'
                if 'begin construction' in context or 'advertise' in context or 'will begin' in context or 'begin construction:' in context:
                    return 'not started'
                if 'not started' in context or 'identified' in context or 'waiting' in context or 'awaiting' in context:
                    return 'not started'
    return None

results = []
for r in funding_related:
    pn = r.get('Project_Name')
    fs = r.get('Funding_Source')
    try:
        amount = int(r.get('Amount'))
    except:
        try:
            amount = int(float(r.get('Amount')))
        except:
            amount = None
    status = infer_status(pn)
    results.append({'Project_Name': pn, 'Funding_Source': fs, 'Amount': amount, 'Status': status})

# sort
results = sorted(results, key=lambda x: x['Project_Name'] or '')

print('__RESULT__:')
print(json.dumps(results))"""

env_args = {'var_call_owt1CJlXOW5XHdAgyXm7RWEF': 'file_storage/call_owt1CJlXOW5XHdAgyXm7RWEF.json', 'var_call_nGx2atNIB0SdTXF5VUqvFXNi': 'file_storage/call_nGx2atNIB0SdTXF5VUqvFXNi.json', 'var_call_575iBL723EDmXFioDtbQt63H': 'ok', 'var_call_5Jo9Dho7c1zbDpaJW0AXDqwA': [{'Funding_ID': '7', 'Project_Name': 'Birdview Avenue Improvements (FEMA/CalOES Project)', 'Funding_Source': 'Research Institution Funding', 'Amount': '14000'}, {'Funding_ID': '22', 'Project_Name': 'Clover Heights Storm Drain (FEMA Project)', 'Funding_Source': 'Local NGO Fund', 'Amount': '21000'}, {'Funding_ID': '25', 'Project_Name': 'Corral Canyon Culvert Repairs (FEMA Project)', 'Funding_Source': 'Municipal Fund', 'Amount': '43000'}, {'Funding_ID': '26', 'Project_Name': 'Corral Canyon Culvert Repairs (FEMA/CalOES Project)', 'Funding_Source': 'Taxpayer Contribution', 'Amount': '15000'}, {'Funding_ID': '28', 'Project_Name': 'Corral Canyon Road Bridge Repairs (FEMA Project)', 'Funding_Source': 'Local Business Support', 'Amount': '25000'}, {'Funding_ID': '29', 'Project_Name': 'Corral Canyon Road Bridge Repairs (FEMA/CalOES Project)', 'Funding_Source': 'Cultural Heritage Grant', 'Amount': '58000'}, {'Funding_ID': '35', 'Project_Name': 'Encinal Canyon Road Drainage Improvements (FEMA/CalOES Project)', 'Funding_Source': 'Private Sponsor', 'Amount': '94000'}, {'Funding_ID': '38', 'Project_Name': 'Guardrail Replacement Citywide (FEMA Project)', 'Funding_Source': 'Impact Investment Fund', 'Amount': '22000'}, {'Funding_ID': '39', 'Project_Name': 'Guardrail Replacement Citywide (FEMA/CalOES Project)', 'Funding_Source': 'Development Bank Loan', 'Amount': '45000'}, {'Funding_ID': '43', 'Project_Name': 'Latigo Canyon Road Culvert Repairs (FEMA Project)', 'Funding_Source': 'Federal Assistance', 'Amount': '36000'}, {'Funding_ID': '44', 'Project_Name': 'Latigo Canyon Road Culvert Repairs (FEMA/CalOES Project)', 'Funding_Source': 'National Foundation Fund', 'Amount': '44000'}, {'Funding_ID': '47', 'Project_Name': 'Latigo Canyon Road Roadway/Retaining Wall Improvements (FEMA Project)', 'Funding_Source': 'Municipal Fund', 'Amount': '91000'}, {'Funding_ID': '48', 'Project_Name': 'Latigo Canyon Road Roadway/Retaining Wall Improvements (FEMA/CalOES Project)', 'Funding_Source': 'Community Fund', 'Amount': '78000'}, {'Funding_ID': '64', 'Project_Name': 'Outdoor Warning Signs', 'Funding_Source': 'Urban Renewal Fund', 'Amount': '92000'}, {'Funding_ID': '65', 'Project_Name': 'Outdoor Warning Sirens', 'Funding_Source': 'Social Impact Investment', 'Amount': '28000'}, {'Funding_ID': '66', 'Project_Name': 'Outdoor Warning Sirens (FEMA Project)', 'Funding_Source': 'Environmental Grant', 'Amount': '27000'}, {'Funding_ID': '67', 'Project_Name': 'Outdoor Warning Sirens (FEMA)', 'Funding_Source': 'State Development Grant', 'Amount': '81000'}, {'Funding_ID': '68', 'Project_Name': 'Outdoor Warning Sirens - Design (FEMA Project)', 'Funding_Source': 'Local Business Support', 'Amount': '43000'}, {'Funding_ID': '69', 'Project_Name': 'Outdoor Warningn Sirens - Design (FEMA Project)', 'Funding_Source': 'Technology Innovation Fund', 'Amount': '84000'}, {'Funding_ID': '73', 'Project_Name': 'PCH Overhead Warning Signs', 'Funding_Source': 'International Organization Grant', 'Amount': '73000'}, {'Funding_ID': '82', 'Project_Name': 'Storm Drain Master Plan (FEMA Project)', 'Funding_Source': 'Environmental Grant', 'Amount': '80000'}, {'Funding_ID': '86', 'Project_Name': 'Trancas Canyon Park Planting and Irrigation Repairs (CalJPIA/FEMA Project)', 'Funding_Source': 'Infrastructure Bond', 'Amount': '44000'}, {'Funding_ID': '87', 'Project_Name': 'Trancas Canyon Park Planting and Irrigation Repairs (FEMA/CalOES Project)', 'Funding_Source': 'Infrastructure Bond', 'Amount': '92000'}], 'var_call_K8WCGLuypwD3TFDA4oFnCzzv': 'file_storage/call_K8WCGLuypwD3TFDA4oFnCzzv.json'}

exec(code, env_args)
