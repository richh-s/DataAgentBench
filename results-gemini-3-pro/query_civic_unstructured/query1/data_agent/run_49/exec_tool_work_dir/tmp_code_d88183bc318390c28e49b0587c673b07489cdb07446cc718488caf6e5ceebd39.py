code = """import json

# Load previous results
funding_file = locals()['var_function-call-12998690230637064644']
with open(funding_file, 'r') as f:
    funding_data = json.load(f)

# Get funded project names
funded_projects = []
for row in funding_data:
    if row.get('Project_Name'):
        funded_projects.append(row['Project_Name'].strip())

# Load extracted design projects from previous step's output (I need to re-extract or use the list if I saved it?)
# I didn't save the extracted list in a file, only printed it.
# So I must re-extract.

docs_file = locals()['var_function-call-12998690230637064277']
with open(docs_file, 'r') as f:
    docs_data = json.load(f)

design_projects = set()

for doc in docs_data:
    text = doc.get('text', '')
    if not text:
        continue
    
    # Use chr(10) for newline
    lines = text.split(chr(10))
    
    in_design_section = False
    
    i = 0
    while i < len(lines):
        line = lines[i].strip()
        
        if 'Capital Improvement Projects (Design)' in line:
            in_design_section = True
            i += 1
            continue
            
        if in_design_section:
            if 'Capital Improvement Projects (' in line and '(Design)' not in line:
                in_design_section = False
                break
            if 'Disaster Recovery Projects' in line:
                in_design_section = False
                break
                
            if line:
                is_project = False
                for k in range(1, 6):
                    if i + k < len(lines):
                        next_line = lines[i+k].strip()
                        if 'Updates:' in next_line or 'Project Description:' in next_line or '(cid:190)' in next_line:
                            is_project = True
                            break
                
                if is_project:
                    if 'Page' not in line and 'Agenda' not in line:
                        design_projects.add(line)
        
        i += 1

# Fuzzy Match
matches = set()
matched_design = set()
matched_funding = set()

for dp in design_projects:
    for fp in funded_projects:
        # Check exact
        if dp == fp:
            matches.add(dp)
            matched_design.add(dp)
            matched_funding.add(fp)
        # Check substring
        elif dp in fp or fp in dp:
            # We need to be careful with short strings, but project names are usually long enough.
            # Example: "Project A" in "Project A (FEMA)"
            matches.add(fp) # Add the funding name as the canonical key
            matched_design.add(dp)
            matched_funding.add(fp)

# "Clover Heights Storm Drain" (Funding) vs "Clover Heights Storm Drainage Improvements" (Design)
# "Drain" in "Drainage Improvements" -> True? No.
# "Clover Heights Storm Drain" in "Clover Heights Storm Drainage Improvements"?
# "Storm Drain" is in "Storm Drainage"? Yes.
# "Clover Heights Storm Drain" is NOT in "Clover Heights Storm Drainage Improvements" because "Drain" vs "Drainage".
# "Drain" is a substring of "Drainage".
# But "Clover Heights Storm Drain" string is not a substring of the other full string.
# "Clover Heights Storm Drainage Improvements" contains "Clover Heights Storm Drain" only if we ignore "age".
# So simple substring won't catch "Drain" vs "Drainage".

# Let's normalized: Remove "age", "Improvements", "Project", "(FEMA...)"
# Or use token overlap.

def normalize(s):
    # Lowercase
    s = s.lower()
    # Remove parens content
    s = s.split('(')[0]
    # Remove common words
    words = s.split()
    words = [w for w in words if w not in ['project', 'improvements', 'repair', 'repairs', 'program', 'road', 'dr', 'drive', 'ave', 'avenue', 'st', 'street']]
    return set(words)

fuzzy_matches = set()

for dp in design_projects:
    if dp in matched_design:
        continue # already matched
    
    dp_tokens = normalize(dp)
    if not dp_tokens:
        continue
        
    for fp in funded_projects:
        if fp in matched_funding:
            continue
            
        fp_tokens = normalize(fp)
        if not fp_tokens:
            continue
            
        # Check intersection
        common = dp_tokens.intersection(fp_tokens)
        # If common covers most of the tokens
        if len(common) >= len(dp_tokens) * 0.8 or len(common) >= len(fp_tokens) * 0.8:
            # High overlap
            fuzzy_matches.add(fp)
            # print(f"Match: '{dp}' with '{fp}'")

final_count = len(matches) + len(fuzzy_matches)

print('__RESULT__:')
print(json.dumps({
    'exact_substring_matches': list(matches),
    'fuzzy_matches': list(fuzzy_matches),
    'total_count': final_count
}))"""

env_args = {'var_function-call-12998690230637064644': 'file_storage/function-call-12998690230637064644.json', 'var_function-call-12998690230637064277': 'file_storage/function-call-12998690230637064277.json', 'var_function-call-14921399092676185459': {'design_projects_found': ['the past several months to complete the engineering work, and the final', 'Storm Drain Master Plan', 'and Harbor. Staff is working out the final details of the project with', 'project and will submit to the County for review.', '(cid:131) Advertise for Bidding: December 2022', '(cid:131) Advertise for Bidding: February 2022', 'overall project costs.', 'Civic Center Water Treatment Facility Phase 2', '(cid:131) Plans and specifications have been completed', '(cid:131) Begin Construction: March 2022', '(cid:131) Begin Construction: Fall 2022', '(cid:131) A Los Angeles County Flood Control maintenance agreement is', 'final design is complete and the project will be advertised for', '(cid:131) City to request proposal from consultant for design services', 'the County and will be finalizing the design.', '(cid:131) Complete Design: February 2022', '(cid:131) An assessment engineer has been hired by the City and a new', 'March 2022', 'permanent skate park located on the Crummer/Case Court parcel adjacent', 'final approval. It is anticipated that the project will have final approval', '(cid:131) City submitted plans to CalOES for review and working with consultant', 'Clover Heights Storm Drainage Improvements', '(cid:190) Project Description: This project consists of the installation of four single-post', 'scope falls within Zuma Canyon Creek. Army Corp. of Engineers has', 'advertised for construction bids after this date. A construction manager', '(cid:131) City submitted plans to Caltrans for review and expecting comments in', '(cid:131) Begin Construction: Spring 2022', '(cid:190) Project Description: This project consists of installing a new westbound right', '(cid:131) The project requires coordination with Los Angeles County Beaches', 'by March 2022. The project will be advertised for construction bids', 'shortly after final approval. If possible, the construction of this project', '(cid:131) Staff is currently working on the design of the project and anticipates', 'project. Staff is working on the project plans to prepare for public', '(cid:131) Begin Construction: Summer 2023', '(cid:131) Project is scheduled to go out to bid next week.', '(cid:190) Project Description: This project includes designing and constructing a', 'anticipated to have a final design by March 2022. The project will be', 'the project', 'or phasing out the project', 'selected a qualified consultant. It is anticipated that the agreement will', 'review by the Council.', 'Resources review.', 'turn lane at the intersection of PCH and Trancas Canyon Road.', 'Civic Center Stormwater Diversion Structure', 'required for this project. Staff is waiting for the County’s approval of', 'manufacturers for filters that will work in the proposed project area. The', '(cid:131) City working with consultant on the design of the shoulder repairs', 'to finalize plans and specifications', '(cid:131) Complete Design: December 2021', 'the agreement.', '(cid:131) Staff mailed easement documents to property owners for review and', '(cid:131) Begin Construction: Fall 2021', 'Metro.', 'project', '(cid:131) Advertise: Summer 2023', '(cid:131) City will work with the design consultant to review design alternatives', 'Westward Beach Road Repair Project', '(cid:131) Complete Design: April 2021', 'will begin in conjunction with the PCH Median Improvement', 'property owners.', 'amenities such as trash cans, benches, tables, and restrooms.', 'cleared the project.', 'Commission will then review the project in Spring 2022 before final', 'from consultants', '(cid:131) Begin Construction: To be determined', 'assessment district will be created.', '(cid:131) Staff has submitted a request for Federal funding', '(cid:131) Staff is currently working on the final design plans', 'PCH at Trancas Canyon Road Right Turn Lane', '(cid:131) Complete Design: Spring 2022', '(cid:131) Complete Design: Spring 2023', "rehabilitation of the roadway to max 8' from R/W, add share road with", 'comments mid-April. This project required their review since the project', '(cid:131) Staff is working with the State Water Board regarding the Cultural', 'PCH Signal Synchronization System Improvements Project', 'advertised for construction bids shortly after this date.', 'evaluating the project costs.', 'manufactured biofilters. City staff is reviewing multiple biofilter', 'Resources review for the SRF funding application', 'Permanent Skate Park', 'Malibu Bluffs Park South Walkway Repairs', '(cid:131) Complete Design: March 2022', '(cid:131) Staff is reviewing the submitted proposals and will select a qualified', 'execution in July and has followed up with an additional letter to those', 'construction bids.', "Council's direction.", '(cid:131) Advertise: Spring 2023', '(cid:131) Advertise: July 2021', 'shade structures at Malibu Bluffs Park.', '(cid:131) Plans are under review by Fish and Wildlife and City is expecting', '(cid:131) Complete Design: Fall 2023', 'Marie Canyon Green Streets', 'schedule will be developed upon the completion of the Cultural', 'to review', '(cid:131) Complete Design: Spring 2021', 'sirens height and feedback from residents and the community.', 'Commission meeting for project direction due to concerns regarding', '(cid:131) Next public community meeting is scheduled for March 25th.', '(cid:131) The City has recently received Measure W funds to complete this', 'management services was approved by Council on March 14, 2022.', 'the Spring 2023.', 'consultant. It is anticipated that this agreement will go to Council in', 'manufactured biofilters. City staff', 'construction bids after approval. An agreement for construction', 'manufacturers for filters that will work in the proposed project area. It is', 'scheduled for the April 11, 2022 Council meeting.', '(cid:190) Project Description: This project includes the designing and constructing a', '(cid:131) Complete Design: Summer 2023', 'Bluffs Park Shade Structure', 'Malibu Canyon Road Traffic Study', 'Latigo Canyon Road Retaining Wall Repair Project', 'speed humps. There is room to add a pathway within the R/W per', '(cid:131) Award Contract and Begin Construction: September 2021', 'Malibu Park Drainage Improvements', '(cid:131) Staff is working with the consultant to finalize the design plans for this', '(cid:131) Begin Construction: Summer 2022', '(cid:131) Funding agreement is schedule for city council on March 27, 2023', 'Canyon Road near Harbor Vista Drive and Potter Lane to determine if any', '(cid:190) Updates:', '(cid:190) Project Description: This project will consist of a traffic study on Malibu', 'sending this project out to bid during the Spring of 2022.', '(cid:131) Begin Construction: Summer/Winter 2022', 'Trancas Canyon Park Playground', '(cid:131) Staff reviewed proposals for engineering design services and has', 'to Malibu Bluffs Park. The project would include parking and additional site', '(cid:131) Award Contract and Begin Construction: Summer 2022', '(cid:131) Begin Construction: Summer 2021', 'go to Council in April 2022 after the Funding Agreement is issued by', '(cid:131) Begin Construction: Spring 2023', 'Trancas Canyon Park Upper and Lower Slopes Repair', '(cid:131) Begin Construction: Estimated Summer 2021', 'PCH Median Improvements Project', '(cid:131) Consultant is working on final design documents.', 'feasible traffic safety improvements can be constructed at this location.', '(cid:131) Advertise: Summer 2022', '(cid:131) Advertise: Fall 2023', '(cid:190) Project Updates:', 'agreement will be sent to City Council in March.', 'bidding.', '(cid:131) Staff received bids on February 24, 2022. Award of contract is', '(cid:131) Begin Construction: Fall 2023', '(cid:131) Awaiting final FEMA/CalOES approval for scope modification', 'Westward Beach Road Improvements Project', '(cid:131) Begin Construction: Winter 2024', '(cid:131) Advertise: Spring/Summer 2022', '(cid:131) 65% design package was submitted to Caltrans in November 2020.', '(cid:131) Plans and specifications are being finalized by consultant', 'Westward Beach Road Drainage Improvements Project', 'bicycles pavement markings, delineated parallel parking spaces and', 'draft plans are expected to be completed in early 2022. The Planning', 'Outdoor Warning Signs', '2022 Morning View Resurfacing & Storm Drain Improvements', 'management.', '(cid:131) Begin Construction: Spring/Summer 2022', '(cid:131) Award Contract and Begin Construction: Spring/Summer 2022', 'seeking proposals'], 'matching_projects': ['Storm Drain Master Plan', 'Civic Center Stormwater Diversion Structure', 'PCH at Trancas Canyon Road Right Turn Lane', 'Permanent Skate Park', 'Malibu Bluffs Park South Walkway Repairs', 'Malibu Canyon Road Traffic Study', 'Latigo Canyon Road Retaining Wall Repair Project', 'PCH Median Improvements Project', 'Westward Beach Road Drainage Improvements Project', 'Outdoor Warning Signs'], 'count': 10}}

exec(code, env_args)
