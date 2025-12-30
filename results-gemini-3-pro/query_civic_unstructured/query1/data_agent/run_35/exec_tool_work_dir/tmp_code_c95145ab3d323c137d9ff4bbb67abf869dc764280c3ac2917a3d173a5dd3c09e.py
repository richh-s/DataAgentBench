code = """import json

key_funding = "var_function-call-14384747128822080394"
key_docs = "var_function-call-12725139888695263289"

with open(locals()[key_funding], "r") as f:
    funding_data = json.load(f)
    
with open(locals()[key_docs], "r") as f:
    civic_docs = json.load(f)

# Normalize DB names slightly?
funding_map = {item["Project_Name"].strip(): float(item["Amount"]) for item in funding_data}

extracted_candidates = []
# Re-run extraction logic to get candidates
for doc in civic_docs:
    lines = doc["text"].splitlines()
    in_design = False
    for line in lines:
        line = line.strip()
        if not line: continue
        if "Capital Improvement Projects (Design)" in line:
            in_design = True
            continue
        if "Capital Improvement Projects" in line and "(Design)" not in line:
            in_design = False
        if "Disaster Recovery Projects" in line:
            in_design = False
        if in_design:
            if line.startswith("(cid:") or line.startswith("Updates:") or line.startswith("Project Schedule:") or line.startswith("Estimated Schedule:"): continue
            if "Page" in line and "of" in line: continue
            if "Agenda Item" in line: continue
            if line.endswith(":"): continue
            lower_line = line.lower()
            if "complete design" in lower_line or "begin construction" in lower_line or "advertise" in lower_line: continue
            
            extracted_candidates.append(line)

unique_candidates = set(extracted_candidates)
# Exact matches
matches = []
unmatched_candidates = []

for cand in unique_candidates:
    if cand in funding_map:
        if funding_map[cand] > 50000:
            matches.append({"name": cand, "amount": funding_map[cand], "type": "exact"})
    else:
        unmatched_candidates.append(cand)

# Fuzzy/Substring matches
fuzzy_matches = []
for cand in unmatched_candidates:
    # Skip very short candidates which are likely noise
    if len(cand) < 10:
        continue
        
    for db_name, amount in funding_map.items():
        # Check containment
        # Case insensitive
        c_lower = cand.lower()
        d_lower = db_name.lower()
        
        # Check if one is substring of other
        if c_lower in d_lower or d_lower in c_lower:
            fuzzy_matches.append({"candidate": cand, "db_name": db_name, "amount": amount})
            
print("__RESULT__:")
print(json.dumps({"exact_matches": matches, "fuzzy_matches": fuzzy_matches}))"""

env_args = {'var_function-call-14384747128822080394': 'file_storage/function-call-14384747128822080394.json', 'var_function-call-12725139888695263289': 'file_storage/function-call-12725139888695263289.json', 'var_function-call-13500179435070439707': {'count': 10, 'matches': ['Outdoor Warning Signs', 'Permanent Skate Park', 'Storm Drain Master Plan', 'PCH Median Improvements Project', 'Malibu Bluffs Park South Walkway Repairs', 'Westward Beach Road Drainage Improvements Project', 'Malibu Canyon Road Traffic Study', 'Civic Center Stormwater Diversion Structure', 'Latigo Canyon Road Retaining Wall Repair Project', 'PCH at Trancas Canyon Road Right Turn Lane'], 'candidates': ['feasible traffic safety improvements can be constructed at this location.', 'Bluffs Park Shade Structure', 'PCH. The project reports and plans are being routed through Caltrans', 'Outdoor Warning Signs', 'overall project costs.', 'agreement will be sent to City Council in March.', 'preliminary estimated assessments in July 2021. Staff has been', 'construction bids after approval. An agreement for construction', 'Individual letters were mailed to all properties within Phase 2 with their', 'bicycles pavement markings, delineated parallel parking spaces and', 'Safety Commissions', 'communicating with the property owners regarding their proposed', 'manufactured biofilters. City staff', 'Malibu Park Drainage Improvements', 'final approval. It is anticipated that the project will have final approval', 'shade structures at Malibu Bluffs Park.', 'project and will submit to the County for review.', 'Westward Beach Road Repair Project', 'bidding.', 'execution in July and has followed up with an additional letter to those', 'management services was approved by Council on March 14, 2022.', 'Resources review.', '2022. This project requires Caltrans approval since the work will be on', 'shortly after final approval. If possible, the construction of this project', 'Westward Beach Road Improvements Project', 'meeting was held on January 20, 2022 and February 23, 2022 and', 'scope falls within Zuma Canyon Creek. Army Corp. of Engineers has', 'the project', 'anticipated to have a final design by March 2022. The project will be', 'presented to the commissions at a future date.', 'Metro.', 'routed through Caltrans for final approval. It is anticipated that the', 'seeking proposals', 'routed through Caltrans for final approval. The project will have final', 'cleared the project.', "rehabilitation of the roadway to max 8' from R/W, add share road with", 'the Spring 2023.', 'manufacturers for filters that will work in the proposed project area. It is', 'review by the Council.', 'required for this project. Staff is waiting for the County’s approval of', '8, 2021. This project requires Caltrans approval since the work will be', 'from consultants', 'Commission meeting for project direction due to concerns regarding', 'amenities such as trash cans, benches, tables, and restrooms.', 'The project reports and plans are being routed through Caltrans for', 'Trancas Canyon Park Playground', 'for final approval. It is anticipated that the project will have final', 'the process of', 'Council directed staff to withdraw the proposed project and associated', 'meeting was held on January 20, 2022. Project alternatives will be', 'to review', 'sirens height and feedback from residents and the community.', 'City will be issuing a RFQ/P for design services in the summer of 2023', '2022.', 'Permanent Skate Park', 'and Harbor. Staff is working out the final details of the project with', 'project will have final approval by March 2022. The project will be', 'and rejected all bids due to a budget shortfall', 'Storm Drain Master Plan', 'to Malibu Bluffs Park. The project would include parking and additional site', 'PCH Median Improvements Project', 'Fund program.', 'property owners.', 'project will begin in conjunction with the PCH Median Improvement', 'go to Council in April 2022 after the Funding Agreement is issued by', 'to perform construction', 'Clover Heights Storm Drainage Improvements', 'project alternatives were presented to the commissions. City staff will', 'manufacturers for filters that will work in the proposed project area. The', 'speed humps. There is room to add a pathway within the R/W per', 'of the assessment district to June 30, 2022. A new request for further', 'to develop project', 'to finalize plans and specifications', 'Commission will then review the project in Spring 2022 before final', '2022 Morning View Resurfacing & Storm Drain Improvements', 'evaluating the project costs.', 'Malibu Bluffs Park South Walkway Repairs', 'Civic Center Water Treatment Facility Phase 2', 'Coastal Development Permit and directed the Public Works and Public', 'This project requires Caltrans approval since the work will be on PCH.', 'schedule will be developed upon the completion of the Cultural', 'permanent skate park located on the Crummer/Case Court parcel adjacent', 'the agreement.', 'work related to the project. Staff has worked with the consultant over', 'management.', 'modification of the schedule has been requested.', 'bids shortly after final approval. If possible, the construction of this', 'the past several months to complete the engineering work, and the final', 'reviewed multiple biofilter', 'on Pacific Coast Highway. The project reports and plans are being', 'comments mid-April. This project required their review since the project', 'with the property owners regarding their proposed assessments.', 'will begin in conjunction with the PCH Median Improvement', 'Westward Beach Road Drainage Improvements Project', 'March 2022', 'Malibu Canyon Road Traffic Study', 'the County.', 'project', 'selected a qualified consultant. It is anticipated that the agreement will', 'Civic Center Stormwater Diversion Structure', 'assessment district will be created.', 'program.', 'Commission in February.', 'turn lane at the intersection of PCH and Trancas Canyon Road.', 'In May 2021, the Council approved funding for additional engineering', 'Latigo Canyon Road Retaining Wall Repair Project', 'the County and will be finalizing the design.', "Council's direction.", 'manufactured biofilters. City staff is reviewing multiple biofilter', 'preliminary estimated assessments. Staff has been communicating', 'of the assessment district to June 30, 2022.', 'been finalized and incorporated into GIS.', 'construction bids.', 'Resources review for the SRF funding application', 'Trancas Canyon Park Upper and Lower Slopes Repair', 'scheduled for the April 11, 2022 Council meeting.', 'Marie Canyon Green Streets', 'draft plans are expected to be completed in early 2022. The Planning', 'present the recommended design alternatives to Council on March 28,', 'or phasing out the project', 'assessments.', 'consultant. It is anticipated that this agreement will go to Council in', 'sending this project out to bid during the Spring of 2022.', 'PCH Signal Synchronization System Improvements Project', 'alternatives. A joint Public Works and Public Safety Commission', 'project. Staff is working on the project plans to prepare for public', 'PCH at Trancas Canyon Road Right Turn Lane', 'February 1, 2021.', 'Canyon Road near Harbor Vista Drive and Potter Lane to determine if any', 'September 20, 2021. At the December 13, 2021, City Council meeting,']}}

exec(code, env_args)
