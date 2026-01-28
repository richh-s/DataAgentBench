code = """import json, re

# Load funding table results
with open(var_call_yEsPRJJXuUlec2ywPTYFYNZ9, 'r') as f:
    funds = json.load(f)

# Load civic docs results
with open(var_call_qAIVVBQpLbB6atIJDbCLzuG1, 'r') as f:
    docs = json.load(f)

# Filter funding records related to FEMA or emergency
candidates = []
for row in funds:
    pname = row.get('Project_Name','')
    fsrc = row.get('Funding_Source','') or ''
    if ('FEMA' in pname) or ('fema' in pname.lower()) or ('federal assistance' in fsrc.lower()) or ('emergency' in pname.lower()) or ('FEMA' in fsrc):
        amt = row.get('Amount')
        # convert amount to int if possible
        try:
            amt = int(amt)
        except:
            try:
                amt = int(str(amt).replace(',',''))
            except:
                pass
        candidates.append({'Project_Name': pname, 'Funding_Source': fsrc, 'Amount': amt})

# For each candidate, search civic docs for occurrences to infer status
def infer_status(context_text):
    text = context_text.lower()
    if re.search(r'construction (was )?completed|notice of completion|complete construction|completed', text):
        return 'completed'
    if re.search(r'under construction|begin construction|begin construction', text):
        return 'under construction'
    if re.search(r'complete design|final design|preliminary design|in the preliminary design phase|design', text):
        return 'design'
    if re.search(r'not started|not begun|not started', text):
        return 'not started'
    if re.search(r'awaiting|await|pending|approval|pending approval', text):
        return 'pending approval'
    return None

results = []
for c in candidates:
    pname = c['Project_Name']
    found = False
    status = None
    # search each doc for project name substring, case-insensitive
    for doc in docs:
        text = doc.get('text','')
        if not text:
            continue
        if re.search(re.escape(pname), text, re.I):
            found = True
            # get surrounding context around first match
            m = re.search(re.escape(pname), text, re.I)
            start = max(0, m.start()-300)
            end = min(len(text), m.end()+300)
            context = text[start:end]
            st = infer_status(context)
            if st:
                status = st
                break
    if not found:
        # try fuzzy: match by substring of first few words
        short = ' '.join(pname.split()[:4])
        for doc in docs:
            text = doc.get('text','')
            if re.search(re.escape(short), text, re.I):
                found = True
                m = re.search(re.escape(short), text, re.I)
                start = max(0, m.start()-300)
                end = min(len(text), m.end()+300)
                context = text[start:end]
                st = infer_status(context)
                if st:
                    status = st
                    break
    if not status:
        status = 'unknown'
    results.append({'Project_Name': c['Project_Name'], 'Funding_Source': c['Funding_Source'], 'Amount': c['Amount'], 'Status': status, 'Found_in_Docs': found})

print('__RESULT__:')
print(json.dumps(results))"""

env_args = {'var_call_qAIVVBQpLbB6atIJDbCLzuG1': 'file_storage/call_qAIVVBQpLbB6atIJDbCLzuG1.json', 'var_call_9XqkdZByJi6RxZrjYs0ZzDwM': {'projects': [], 'project_names': []}, 'var_call_h6RMsOfq9KsOyjkk2vXzWxby': [], 'var_call_ZYw4QbztdDMR87vrZbu4Rtsi': [{'filename': 'malibucity_agenda_03222023-2060.txt', 'text_preview': 'Public Works Commission\nAgenda Report\n\nPublic Works\nCommission Meeting\n03-22-23\nItem\n4.B.\n\nTo:\n\nChair Dittrich and Members of the Public Works Commission\n\nPrepared by:\n\nJorge Rubalcava, Senior Civil Engineer\n\nApproved by:\n\nRob DuBoux, Public Works Director/City Engineer\n\nDate prepared: March 15, 2023\n\nMeeting date: March 22, 2023\n\nSubject:\n\nCapital Improvement Projects and Disaster Recovery Projects Status\nReport\n\nRECOMMENDED ACTION: Receive and file report on the status of the City’s current and\nupcoming Capital Improvement Projects and Disaster Recovery Projects.\n\nDISCUSSION: Staff will provide a status update on the following active projects in the\nFiscal Year 2022-2023 Capital Improvement Program:\n\nCapital Improvement Projects (Design)\n\n2022 Morning View Resurfacing & Storm Drain Improvements\n\n(cid:190) Updates:\n\n(cid:131) Staff is working with the consultant to finalize the design plans for this\n\nproject and will submit to the County for review.\n\n(cid:190) Project Schedule:\n\n(cid:'}, {'filename': 'malibucity_agenda__01262022-1835.txt', 'text_preview': 'Public Works Commission\nAgenda Report\n\nPublic Works\nCommission Meeting\n10-27-21\nItem\n4.A.\n\nTo:\n\nChair Simmens and Members of the Public Works Commission\n\nPrepared by:\n\nTroy Spayd, Assistant Public Works Director/City Engineer\n\nApproved by:\n\nRob DuBoux, Public Works Director/City Engineer\n\nDate prepared: October 21, 2021\n\nMeeting date: October 27, 2021\n\nSubject:\n\nCapital Improvement Projects and Disaster Recovery Projects Status\nReport\n\nRECOMMENDED ACTION: Receive and file report on the status of the City’s current and\nupcoming Capital Improvements Projects and Disaster Recovery Projects.\n\nDISCUSSION: Staff will provide a status update on the following active projects in the\nFiscal Year 2021-2022 Capital Improvement Program:\n\nCapital Improvement Projects (Design)\n\nMarie Canyon Green Streets\n(cid:190) Updates:\n\n(cid:131) A hydrology report was prepared and will be used to size the pre-\nmanufactured biofilters. City staff is reviewing multiple biofilter\nmanufacturers for filters that will'}, {'filename': 'malibucity_agenda__01272021-1626.txt', 'text_preview': 'Public Works Commission\nAgenda Report\n\nPublic Works\nCommission Meeting\n01-27-21\nItem\n4.A.\n\nTo:\n\nChair Merrick and Members of the Public Works Commission\n\nPrepared by:\n\nRobert DuBoux, Public Works Director/City Engineer\n\nDate prepared:\n\nJanuary 22, 2021\n\nMeeting date: January 27, 2021\n\nSubject:\n\nCapital Improvement Projects and Disaster Recovery Projects Status\nReport\n\nRECOMMENDED ACTION: Receive and file report on the status of the City’s current and\nupcoming Capital Improvements Projects and Disaster Recovery Projects.\n\nDISCUSSION: Staff will provide a status update on the following active projects in the\nFiscal Year 2020-2021 Capital Improvement Program:\n\nCapital Improvement Projects (Design)\n\nMarie Canyon Green Streets\n(cid:190) Updates:\n\n(cid:131) The City has recently received Measure W funds to complete this\nproject. Staff is working on the project plans to prepare for public\nbidding.\n\n(cid:190) Project Schedule:\n\n(cid:131) Complete Design: April 2021\n(cid:131) Begin Construction'}], 'var_call_TojRoaj9Q3pFpgc173e94L16': ['Funding'], 'var_call_yEsPRJJXuUlec2ywPTYFYNZ9': 'file_storage/call_yEsPRJJXuUlec2ywPTYFYNZ9.json', 'var_call_K4CO2bW5rKuNni4avoxSD6oI': [{'Project_Name': 'Birdview Avenue Improvements (FEMA/CalOES Project)', 'Funding_Source': 'Research Institution Funding', 'Amount': 14000}, {'Project_Name': 'Clover Heights Storm Drain (FEMA Project)', 'Funding_Source': 'Local NGO Fund', 'Amount': 21000}, {'Project_Name': 'Corral Canyon Culvert Repairs (FEMA Project)', 'Funding_Source': 'Municipal Fund', 'Amount': 43000}, {'Project_Name': 'Corral Canyon Culvert Repairs (FEMA/CalOES Project)', 'Funding_Source': 'Taxpayer Contribution', 'Amount': 15000}, {'Project_Name': 'Corral Canyon Road Bridge Repairs (FEMA Project)', 'Funding_Source': 'Local Business Support', 'Amount': 25000}, {'Project_Name': 'Corral Canyon Road Bridge Repairs (FEMA/CalOES Project)', 'Funding_Source': 'Cultural Heritage Grant', 'Amount': 58000}, {'Project_Name': 'Encinal Canyon Road Drainage Improvements (FEMA/CalOES Project)', 'Funding_Source': 'Private Sponsor', 'Amount': 94000}, {'Project_Name': 'Guardrail Replacement Citywide (FEMA Project)', 'Funding_Source': 'Impact Investment Fund', 'Amount': 22000}, {'Project_Name': 'Guardrail Replacement Citywide (FEMA/CalOES Project)', 'Funding_Source': 'Development Bank Loan', 'Amount': 45000}, {'Project_Name': 'Latigo Canyon Road Culvert Repairs (FEMA Project)', 'Funding_Source': 'Federal Assistance', 'Amount': 36000}, {'Project_Name': 'Latigo Canyon Road Culvert Repairs (FEMA/CalOES Project)', 'Funding_Source': 'National Foundation Fund', 'Amount': 44000}, {'Project_Name': 'Latigo Canyon Road Roadway/Retaining Wall Improvements (FEMA Project)', 'Funding_Source': 'Municipal Fund', 'Amount': 91000}, {'Project_Name': 'Latigo Canyon Road Roadway/Retaining Wall Improvements (FEMA/CalOES Project)', 'Funding_Source': 'Community Fund', 'Amount': 78000}, {'Project_Name': 'Outdoor Warning Sirens (FEMA Project)', 'Funding_Source': 'Environmental Grant', 'Amount': 27000}, {'Project_Name': 'Outdoor Warning Sirens (FEMA)', 'Funding_Source': 'State Development Grant', 'Amount': 81000}, {'Project_Name': 'Outdoor Warning Sirens - Design (FEMA Project)', 'Funding_Source': 'Local Business Support', 'Amount': 43000}, {'Project_Name': 'Outdoor Warningn Sirens - Design (FEMA Project)', 'Funding_Source': 'Technology Innovation Fund', 'Amount': 84000}, {'Project_Name': 'Storm Drain Master Plan (FEMA Project)', 'Funding_Source': 'Environmental Grant', 'Amount': 80000}, {'Project_Name': 'Trancas Canyon Park Planting and Irrigation Repairs (CalJPIA/FEMA Project)', 'Funding_Source': 'Infrastructure Bond', 'Amount': 44000}, {'Project_Name': 'Trancas Canyon Park Planting and Irrigation Repairs (FEMA/CalOES Project)', 'Funding_Source': 'Infrastructure Bond', 'Amount': 92000}, {'Project_Name': 'Corral Canyon Culvert Repairs', 'Funding_Source': 'Federal Assistance', 'Amount': 54000}, {'Project_Name': 'Westward Beach Road Repair Project', 'Funding_Source': 'Federal Assistance', 'Amount': 30000}, {'Project_Name': 'project_227', 'Funding_Source': 'Federal Assistance', 'Amount': 78000}, {'Project_Name': 'project_396', 'Funding_Source': 'Federal Assistance', 'Amount': 18000}, {'Project_Name': 'project_425', 'Funding_Source': 'Federal Assistance', 'Amount': 91000}, {'Project_Name': 'project_134', 'Funding_Source': 'Federal Assistance', 'Amount': 32000}, {'Project_Name': 'project_412', 'Funding_Source': 'Federal Assistance', 'Amount': 62000}, {'Project_Name': 'project_332', 'Funding_Source': 'Federal Assistance', 'Amount': 65000}]}

exec(code, env_args)
