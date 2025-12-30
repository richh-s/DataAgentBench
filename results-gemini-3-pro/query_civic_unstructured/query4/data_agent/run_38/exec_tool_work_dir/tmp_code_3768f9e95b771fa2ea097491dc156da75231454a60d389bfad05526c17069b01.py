code = """import json
import pandas as pd

# Load data
funding_path = locals()['var_function-call-11668788458618260347']
with open(funding_path, 'r') as f:
    funding_data = json.load(f)
df_funding = pd.DataFrame(funding_data)
df_funding['Amount'] = pd.to_numeric(df_funding['Amount'])

civic_path = locals()['var_function-call-11668788458618261250']
with open(civic_path, 'r') as f:
    civic_docs = json.load(f)

projects_found = []

def get_date_from_line(line):
    # Try case insensitive split
    line_lower = line.lower()
    if 'begin construction' in line_lower:
        # Find index
        idx = line_lower.find('begin construction')
        # Take text after
        after = line[idx + len('begin construction'):]
        # Cleanup
        after = after.lstrip(':').strip()
        return after
    return None

def is_spring_2022(date_str):
    if not date_str:
        return False
    d = date_str.lower()
    if 'spring 2022' in d or 'spring, 2022' in d:
        return True
    if '2022' in d:
        if 'spring' in d: 
            return True
        if 'march' in d or 'april' in d or 'may' in d:
            return True
        if '03/2022' in d or '04/2022' in d or '05/2022' in d:
            return True
        if '2022-03' in d or '2022-04' in d or '2022-05' in d:
            return True
    return False

for doc in civic_docs:
    lines = doc['text'].splitlines()
    
    # Identify project indices
    p_indices = []
    for i, line in enumerate(lines):
        line_s = line.strip()
        if ('Updates:' in line_s and len(line_s) < 30) or ('Project Description:' in line_s and len(line_s) < 30):
            j = i - 1
            while j >= 0 and not lines[j].strip():
                j -= 1
            if j >= 0:
                p_name = lines[j].strip()
                if not p_indices or p_indices[-1][1] != p_name:
                    p_indices.append((j, p_name))
    
    # Extract info
    for k in range(len(p_indices)):
        start_idx, p_name = p_indices[k]
        if k < len(p_indices) - 1:
            end_idx = p_indices[k+1][0]
        else:
            end_idx = len(lines)
        
        block_lines = lines[start_idx:end_idx]
        st_date = None
        for bl in block_lines:
            d = get_date_from_line(bl)
            if d:
                st_date = d
                break
        
        if is_spring_2022(st_date):
            projects_found.append({'Project_Name': p_name, 'st': st_date})

df_res = pd.DataFrame(projects_found)

# Join
if not df_res.empty:
    final_res = pd.merge(df_funding, df_res, on='Project_Name', how='inner')
    final_res = final_res.drop_duplicates(subset=['Project_Name'])
    
    count = len(final_res)
    total_funding = int(final_res['Amount'].sum())
    
    print('__RESULT__:')
    print(json.dumps({
        'count': count,
        'total_funding': total_funding,
        'projects': final_res['Project_Name'].tolist()
    }))
else:
    print('__RESULT__:')
    print(json.dumps({
        'count': 0,
        'total_funding': 0
    }))"""

env_args = {'var_function-call-5073457582333833681': ['civic_docs'], 'var_function-call-5073457582333837024': ['Funding'], 'var_function-call-11668788458618260347': 'file_storage/function-call-11668788458618260347.json', 'var_function-call-11668788458618261250': 'file_storage/function-call-11668788458618261250.json', 'var_function-call-7072214378694164812': {'count': 0, 'total_funding': 0}, 'var_function-call-11966727829119026580': [{'Project': '2022 Morning View Resurfacing & Storm Drain Improvements', 'Block': '(cid:190) Updates: |  | (cid:131) Staff is working with the consultant to finalize the design plans for this |  | project and will submit to the County for review. |  | (cid:190) Project Schedule: |  | (cid:131) Complete Design: Summer 2023 | (cid:131) Advertise: Fall 2023 | (cid:131) Begin Construction: Fall 2023 |  | PCH Median Improvements Project |  | (cid:190) Updates: |  | (cid:131) On September 22, 2022, the City received four (4) construction bids |  | and rejected all bids due to a budget shortfall | '}, {'Project': 'PCH Median Improvements Project', 'Block': '(cid:190) Updates: |  | (cid:131) On September 22, 2022, the City received four (4) construction bids |  | and rejected all bids due to a budget shortfall |  | (cid:131) City will work with the design consultant to review design alternatives |  | or phasing out the project |  | (cid:190) Project Schedule: |  | (cid:131) Complete Design: Summer 2023 | (cid:131) Advertise: Fall 2023 |  | Page 1 of 6 |  | Agenda Item # 4.B. |  | '}, {'Project': 'Westward Beach Road Repair Project', 'Block': '(cid:190) Updates: |  | (cid:131) City working with consultant on the design of the shoulder repairs |  | (cid:190) Project Schedule: |  | (cid:131) Complete Design: Summer 2023 | (cid:131) Advertise: Summer 2023 | (cid:131) Begin Construction: Fall 2023 |  | Westward Beach Road Drainage Improvements Project |  | (cid:190) Updates: |  | (cid:131) Plans are under review by Fish and Wildlife and City is expecting | comments mid-April. This project required their review since the project | scope falls within Zuma Canyon Creek. Army Corp. of Engineers has | cleared the project. |  | (cid:190) Project Schedule:'}, {'Project': 'Westward Beach Road Drainage Improvements Project', 'Block': '(cid:190) Updates: |  | (cid:131) Plans are under review by Fish and Wildlife and City is expecting | comments mid-April. This project required their review since the project | scope falls within Zuma Canyon Creek. Army Corp. of Engineers has | cleared the project. |  | (cid:190) Project Schedule: |  | (cid:131) Advertise: Summer 2023 | (cid:131) Begin Construction: Fall 2023 |  | Clover Heights Storm Drainage Improvements |  | (cid:190) Updates: |  | (cid:131) City submitted plans to CalOES for review and working with consultant |  | to finalize plans and specifications | '}, {'Project': 'Clover Heights Storm Drainage Improvements', 'Block': '(cid:190) Updates: |  | (cid:131) City submitted plans to CalOES for review and working with consultant |  | to finalize plans and specifications |  | (cid:190) Project Schedule: |  | (cid:131) Final Design: Summer, 2023 | (cid:131) Advertise: Summer 2023 | (cid:131) Begin Construction: Fall 2023 |  | Latigo Canyon Road Retaining Wall Repair Project |  | (cid:190) Updates: |  | (cid:131) Plans and specifications have been completed | (cid:131) Awaiting final FEMA/CalOES approval for scope modification |  | (cid:190) Project Schedule:'}, {'Project': 'Latigo Canyon Road Retaining Wall Repair Project', 'Block': '(cid:190) Updates: |  | (cid:131) Plans and specifications have been completed | (cid:131) Awaiting final FEMA/CalOES approval for scope modification |  | (cid:190) Project Schedule: |  | (cid:131) Advertise: Spring 2023 | (cid:131) Begin Construction: Summer 2023 |  | Storm Drain Master Plan |  | (cid:190) Updates: |  | (cid:131) Field data collection has been completed and storm drain inventory has |  | been finalized and incorporated into GIS. |  | (cid:131) Consultant working finalizing a CIP recommendation list | '}, {'Project': 'Storm Drain Master Plan', 'Block': '(cid:190) Updates: |  | (cid:131) Field data collection has been completed and storm drain inventory has |  | been finalized and incorporated into GIS. |  | (cid:131) Consultant working finalizing a CIP recommendation list |  | Page 2 of 6 |  | Agenda Item # 4.B. |  |  |  |  |  |  |  |  | '}, {'Project': 'Trancas Canyon Park Upper and Lower Slopes Repair', 'Block': '(cid:190) Updates: |  | (cid:131) Plans and specifications are being finalized by consultant |  | (cid:190) Project Schedule: |  | (cid:131) Advertise: Spring 2023 | (cid:131) Begin Construction: Summer 2023 |  | Civic Center Water Treatment Facility Phase 2 |  | (cid:190) Updates: |  | (cid:131) Staff is working with the State Water Board regarding the Cultural |  | Resources review for the SRF funding application | (cid:131) Staff has submitted a request for Federal funding |  | (cid:190) Project Schedule (pending the MOU extension approval): | '}, {'Project': 'Civic Center Water Treatment Facility Phase 2', 'Block': '(cid:190) Updates: |  | (cid:131) Staff is working with the State Water Board regarding the Cultural |  | Resources review for the SRF funding application | (cid:131) Staff has submitted a request for Federal funding |  | (cid:190) Project Schedule (pending the MOU extension approval): |  | (cid:131) Project is delayed due to the Cultural Resource review. Revised | schedule will be developed upon the completion of the Cultural | Resources review. |  | Permanent Skate Park |  | (cid:190) Updates: |  | (cid:131) Staff is working with the consultant to finalize the design plans for this |  | project'}, {'Project': 'Permanent Skate Park', 'Block': '(cid:190) Updates: |  | (cid:131) Staff is working with the consultant to finalize the design plans for this |  | project | (cid:190) Estimated Schedule: |  | (cid:131) Complete Design: Spring 2023 | (cid:131) Begin Construction: Winter 2024 |  | PCH at Trancas Canyon Road Right Turn Lane |  | (cid:190) Updates: |  | (cid:131) City submitted plans to Caltrans for review and expecting comments in |  | the Spring 2023. |  | (cid:190) Estimated Schedule: | '}, {'Project': 'PCH at Trancas Canyon Road Right Turn Lane', 'Block': '(cid:190) Updates: |  | (cid:131) City submitted plans to Caltrans for review and expecting comments in |  | the Spring 2023. |  | (cid:190) Estimated Schedule: |  | (cid:131) Complete Design: Fall 2023 | (cid:131) Begin Construction: Fall 2023 |  | Outdoor Warning Signs |  | (cid:190) Updates: |  | (cid:131) Project to be discussed during a joint Public Works and Public Safety | Commission meeting for project direction due to concerns regarding | sirens height and feedback from residents and the community. |  | Malibu Bluffs Park South Walkway Repairs'}], 'var_function-call-9567966621005757400': ['(cid:190) Updates:\n\n(cid:131) A hydrology report was prepared and will be used to size the pre-\nmanufactured biofilters. City staff is reviewing multiple biofilter\nmanufacturers for filters that will work in the proposed project area. It is\nanticipated to have a final design by March 2022. The project will be\nadvertised for construction bids shortly after this date.\n\n(cid:190) Project Schedule:\n', 'anticipated to have a final design by March 2022. The project will be\nadvertised for construction bids shortly after this date.\n\n(cid:190) Project Schedule:\n\n(cid:131) Complete Design: March 2022\n(cid:131) Begin Construction: Spring 2022\n\nPCH Median Improvements Project\n', 'advertised for construction bids shortly after this date.\n\n(cid:190) Project Schedule:\n\n(cid:131) Complete Design: March 2022\n(cid:131) Begin Construction: Spring 2022\n\nPCH Median Improvements Project\n\n(cid:190) Updates:', '\n(cid:131) The project was approved by the Planning Commission on September\n8, 2021. This project requires Caltrans approval since the work will be\non Pacific Coast Highway. The project reports and plans are being\nrouted through Caltrans for final approval. It is anticipated that the\nproject will have final approval by March 2022. The project will be\n\nPage 1 of 8\n\nAgenda Item # 4.A.', 'advertised for construction bids after this date. A construction manager\nagreement will be sent to City Council in March.\n\n(cid:190) Project Schedule:\n\n(cid:131) Complete Design: March 2022\n(cid:131) Begin Construction: Spring/Summer 2022\n\nPCH Signal Synchronization System Improvements Project\n', '\n(cid:131) This project will be presented to the Planning Commission in February\n2022. This project requires Caltrans approval since the work will be on\nPCH. The project reports and plans are being routed through Caltrans\nfor final approval. It is anticipated that the project will have final\napproval by March 2022. The project will be advertised for construction\nbids shortly after final approval. If possible, the construction of this\nproject will begin in conjunction with the PCH Median Improvement\nProject Schedule:\n', 'approval by March 2022. The project will be advertised for construction\nbids shortly after final approval. If possible, the construction of this\nproject will begin in conjunction with the PCH Median Improvement\nProject Schedule:\n\n(cid:131) Complete Final Design: Spring 2022\n(cid:131) Advertise: Spring/Summer 2022\n(cid:131) Award Contract and Begin Construction: Spring/Summer 2022\n\nWestward Beach Road Improvements Project', '\nto review\n\n(cid:190) Project Schedule:\n\n(cid:131) Complete Design: Spring 2022\n(cid:131) Begin Construction: Summer/Winter 2022\n\nCivic Center Water Treatment Facility Phase 2\n', '\nsending this project out to bid during the Spring of 2022.\n\n(cid:190) Estimated Schedule:\n\n(cid:131) Complete Design: Spring 2022\n(cid:131) Begin Construction: Spring 2022\n\nPermanent Skate Park\n', 'sending this project out to bid during the Spring of 2022.\n\n(cid:190) Estimated Schedule:\n\n(cid:131) Complete Design: Spring 2022\n(cid:131) Begin Construction: Spring 2022\n\nPermanent Skate Park\n\n(cid:190) Project Description: This project includes the designing and constructing a', '\nIn May 2021, the Council approved funding for additional engineering\nwork related to the project. Staff has worked with the consultant over\nthe past several months to complete the engineering work, and the final\ndraft plans are expected to be completed in early 2022. The Planning\nCommission will then review the project in Spring 2022 before final\nreview by the Council.\n\n(cid:190) Estimated Schedule:\n', 'Commission will then review the project in Spring 2022 before final\nreview by the Council.\n\n(cid:190) Estimated Schedule:\n\n(cid:131) Complete Design: Spring 2022\n(cid:131) Begin Construction: To be determined\n\nPCH at Trancas Canyon Road Right Turn Lane\n', '\n(cid:190) Updates:\n\n(cid:131) Staff is reviewing the submitted proposals and will select a qualified\nconsultant. It is anticipated that this agreement will go to Council in\nMarch 2022\n\n(cid:190) Estimated Schedule:\n\n(cid:131) Begin Design: Spring 2022', 'consultant. It is anticipated that this agreement will go to Council in\nMarch 2022\n\n(cid:190) Estimated Schedule:\n\n(cid:131) Begin Design: Spring 2022\n\nCapital Improvement Projects (Construction)\n\nThe City does not have projects in construction at this time.', 'is finalizing the bid documents.\n\n(cid:190) Project Schedule:\n\n(cid:131) Complete Design: February 2022\n(cid:131) Begin Construction: Spring 2022\n\nLatigo Canyon Road Roadway/Retaining Wall Improvements (FEMA Project)\n\n(cid:190) Updates:', 'timber with non-combustible materials.\n\n(cid:190) Project Schedule\n\n(cid:131) Complete Design: February 2022\n(cid:131) Begin Construction: April 2022\n\nTrancas Canyon Park Planting and Irrigation Repairs (CalJPIA/FEMA Project)\n\n(cid:190) Updates:', '\n(cid:131) The project consultant has started the design of this project.\n\n(cid:190) Project Schedule:\n\n(cid:131) Complete Design: Spring 2022\n(cid:131) Begin Construction: Spring 2022\n\nTrancas Canyon Park Slope Stabilization Project (CalJPIA Project)\n', '(cid:131) The project consultant has started the design of this project.\n\n(cid:190) Project Schedule:\n\n(cid:131) Complete Design: Spring 2022\n(cid:131) Begin Construction: Spring 2022\n\nTrancas Canyon Park Slope Stabilization Project (CalJPIA Project)\n\n(cid:190) Updates:', '\n(cid:131) The project consultant has started the design of this project.\n\n(cid:190) Project Schedule:\n\n(cid:131) Complete Design: Spring 2022\n(cid:131) Begin Construction: Spring 2022\n\nStorm Drain Master Plan (FEMA Project)\n', '(cid:131) The project consultant has started the design of this project.\n\n(cid:190) Project Schedule:\n\n(cid:131) Complete Design: Spring 2022\n(cid:131) Begin Construction: Spring 2022\n\nStorm Drain Master Plan (FEMA Project)\n\nPage 5 of 8'], 'var_function-call-12754973026692724822': {'count': 0, 'total_funding': 0}, 'var_function-call-17249841248482451959': [{'name': '2022 Morning View Resurfacing & Storm Drain Improvements', 'date': '131) Begin Construction'}, {'name': 'PCH Median Improvements Project', 'date': '131) Begin Construction'}, {'name': 'Westward Beach Road Repair Project', 'date': '131) Begin Construction'}, {'name': 'Westward Beach Road Drainage Improvements Project', 'date': '131) Begin Construction'}, {'name': 'Clover Heights Storm Drainage Improvements', 'date': '131) Begin Construction'}, {'name': 'Latigo Canyon Road Retaining Wall Repair Project', 'date': '131) Begin Construction'}, {'name': 'Storm Drain Master Plan', 'date': None}, {'name': 'Trancas Canyon Park Upper and Lower Slopes Repair', 'date': '131) Begin Construction'}, {'name': 'Civic Center Water Treatment Facility Phase 2', 'date': None}, {'name': 'Permanent Skate Park', 'date': '131) Begin Construction'}, {'name': 'PCH at Trancas Canyon Road Right Turn Lane', 'date': '131) Begin Construction'}, {'name': 'Outdoor Warning Signs', 'date': None}, {'name': 'Malibu Bluffs Park South Walkway Repairs', 'date': None}, {'name': 'Trancas Canyon Park Playground', 'date': None}, {'name': 'feasible traffic safety improvements can be constructed at this location.', 'date': None}, {'name': 'PCH Signal Synchronization System Improvements Project', 'date': '131) Begin construction'}, {'name': 'Storm Drain Trash Screens Phase Two', 'date': '131) Begin construction'}, {'name': 'Marie Canyon Green Streets', 'date': None}, {'name': 'Broad Beach Road Water Quality Repair', 'date': None}, {'name': 'Point Dume Walkway Repairs', 'date': None}]}

exec(code, env_args)
