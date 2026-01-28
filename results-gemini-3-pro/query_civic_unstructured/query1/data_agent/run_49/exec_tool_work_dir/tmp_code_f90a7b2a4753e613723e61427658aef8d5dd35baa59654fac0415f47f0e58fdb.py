code = """import json

# Load funding results
funding_file = locals()['var_function-call-12998690230637064644']
with open(funding_file, 'r') as f:
    funding_data = json.load(f)

capital_funded_projects = set()
for row in funding_data:
    name = row.get('Project_Name', '').strip()
    if not name:
        continue
    # Exclude Disaster projects based on hint
    if '(FEMA' in name or '(CalOES' in name or '(CalJPIA' in name:
        continue
    capital_funded_projects.add(name)

# Load civic docs and extract
docs_file = locals()['var_function-call-12998690230637064277']
with open(docs_file, 'r') as f:
    docs_data = json.load(f)

design_projects = set()

for doc in docs_data:
    text = doc.get('text', '')
    if not text:
        continue
    
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

# Match
matches = []
for dp in design_projects:
    if dp in capital_funded_projects:
        matches.append(dp)

print('__RESULT__:')
print(json.dumps({
    'matches': matches,
    'count': len(matches)
}))"""

env_args = {'var_function-call-12998690230637064644': 'file_storage/function-call-12998690230637064644.json', 'var_function-call-12998690230637064277': 'file_storage/function-call-12998690230637064277.json', 'var_function-call-14921399092676185459': {'design_projects_found': ['the past several months to complete the engineering work, and the final', 'Storm Drain Master Plan', 'and Harbor. Staff is working out the final details of the project with', 'project and will submit to the County for review.', '(cid:131) Advertise for Bidding: December 2022', '(cid:131) Advertise for Bidding: February 2022', 'overall project costs.', 'Civic Center Water Treatment Facility Phase 2', '(cid:131) Plans and specifications have been completed', '(cid:131) Begin Construction: March 2022', '(cid:131) Begin Construction: Fall 2022', '(cid:131) A Los Angeles County Flood Control maintenance agreement is', 'final design is complete and the project will be advertised for', '(cid:131) City to request proposal from consultant for design services', 'the County and will be finalizing the design.', '(cid:131) Complete Design: February 2022', '(cid:131) An assessment engineer has been hired by the City and a new', 'March 2022', 'permanent skate park located on the Crummer/Case Court parcel adjacent', 'final approval. It is anticipated that the project will have final approval', '(cid:131) City submitted plans to CalOES for review and working with consultant', 'Clover Heights Storm Drainage Improvements', '(cid:190) Project Description: This project consists of the installation of four single-post', 'scope falls within Zuma Canyon Creek. Army Corp. of Engineers has', 'advertised for construction bids after this date. A construction manager', '(cid:131) City submitted plans to Caltrans for review and expecting comments in', '(cid:131) Begin Construction: Spring 2022', '(cid:190) Project Description: This project consists of installing a new westbound right', '(cid:131) The project requires coordination with Los Angeles County Beaches', 'by March 2022. The project will be advertised for construction bids', 'shortly after final approval. If possible, the construction of this project', '(cid:131) Staff is currently working on the design of the project and anticipates', 'project. Staff is working on the project plans to prepare for public', '(cid:131) Begin Construction: Summer 2023', '(cid:131) Project is scheduled to go out to bid next week.', '(cid:190) Project Description: This project includes designing and constructing a', 'anticipated to have a final design by March 2022. The project will be', 'the project', 'or phasing out the project', 'selected a qualified consultant. It is anticipated that the agreement will', 'review by the Council.', 'Resources review.', 'turn lane at the intersection of PCH and Trancas Canyon Road.', 'Civic Center Stormwater Diversion Structure', 'required for this project. Staff is waiting for the County’s approval of', 'manufacturers for filters that will work in the proposed project area. The', '(cid:131) City working with consultant on the design of the shoulder repairs', 'to finalize plans and specifications', '(cid:131) Complete Design: December 2021', 'the agreement.', '(cid:131) Staff mailed easement documents to property owners for review and', '(cid:131) Begin Construction: Fall 2021', 'Metro.', 'project', '(cid:131) Advertise: Summer 2023', '(cid:131) City will work with the design consultant to review design alternatives', 'Westward Beach Road Repair Project', '(cid:131) Complete Design: April 2021', 'will begin in conjunction with the PCH Median Improvement', 'property owners.', 'amenities such as trash cans, benches, tables, and restrooms.', 'cleared the project.', 'Commission will then review the project in Spring 2022 before final', 'from consultants', '(cid:131) Begin Construction: To be determined', 'assessment district will be created.', '(cid:131) Staff has submitted a request for Federal funding', '(cid:131) Staff is currently working on the final design plans', 'PCH at Trancas Canyon Road Right Turn Lane', '(cid:131) Complete Design: Spring 2022', '(cid:131) Complete Design: Spring 2023', "rehabilitation of the roadway to max 8' from R/W, add share road with", 'comments mid-April. This project required their review since the project', '(cid:131) Staff is working with the State Water Board regarding the Cultural', 'PCH Signal Synchronization System Improvements Project', 'advertised for construction bids shortly after this date.', 'evaluating the project costs.', 'manufactured biofilters. City staff is reviewing multiple biofilter', 'Resources review for the SRF funding application', 'Permanent Skate Park', 'Malibu Bluffs Park South Walkway Repairs', '(cid:131) Complete Design: March 2022', '(cid:131) Staff is reviewing the submitted proposals and will select a qualified', 'execution in July and has followed up with an additional letter to those', 'construction bids.', "Council's direction.", '(cid:131) Advertise: Spring 2023', '(cid:131) Advertise: July 2021', 'shade structures at Malibu Bluffs Park.', '(cid:131) Plans are under review by Fish and Wildlife and City is expecting', '(cid:131) Complete Design: Fall 2023', 'Marie Canyon Green Streets', 'schedule will be developed upon the completion of the Cultural', 'to review', '(cid:131) Complete Design: Spring 2021', 'sirens height and feedback from residents and the community.', 'Commission meeting for project direction due to concerns regarding', '(cid:131) Next public community meeting is scheduled for March 25th.', '(cid:131) The City has recently received Measure W funds to complete this', 'management services was approved by Council on March 14, 2022.', 'the Spring 2023.', 'consultant. It is anticipated that this agreement will go to Council in', 'manufactured biofilters. City staff', 'construction bids after approval. An agreement for construction', 'manufacturers for filters that will work in the proposed project area. It is', 'scheduled for the April 11, 2022 Council meeting.', '(cid:190) Project Description: This project includes the designing and constructing a', '(cid:131) Complete Design: Summer 2023', 'Bluffs Park Shade Structure', 'Malibu Canyon Road Traffic Study', 'Latigo Canyon Road Retaining Wall Repair Project', 'speed humps. There is room to add a pathway within the R/W per', '(cid:131) Award Contract and Begin Construction: September 2021', 'Malibu Park Drainage Improvements', '(cid:131) Staff is working with the consultant to finalize the design plans for this', '(cid:131) Begin Construction: Summer 2022', '(cid:131) Funding agreement is schedule for city council on March 27, 2023', 'Canyon Road near Harbor Vista Drive and Potter Lane to determine if any', '(cid:190) Updates:', '(cid:190) Project Description: This project will consist of a traffic study on Malibu', 'sending this project out to bid during the Spring of 2022.', '(cid:131) Begin Construction: Summer/Winter 2022', 'Trancas Canyon Park Playground', '(cid:131) Staff reviewed proposals for engineering design services and has', 'to Malibu Bluffs Park. The project would include parking and additional site', '(cid:131) Award Contract and Begin Construction: Summer 2022', '(cid:131) Begin Construction: Summer 2021', 'go to Council in April 2022 after the Funding Agreement is issued by', '(cid:131) Begin Construction: Spring 2023', 'Trancas Canyon Park Upper and Lower Slopes Repair', '(cid:131) Begin Construction: Estimated Summer 2021', 'PCH Median Improvements Project', '(cid:131) Consultant is working on final design documents.', 'feasible traffic safety improvements can be constructed at this location.', '(cid:131) Advertise: Summer 2022', '(cid:131) Advertise: Fall 2023', '(cid:190) Project Updates:', 'agreement will be sent to City Council in March.', 'bidding.', '(cid:131) Staff received bids on February 24, 2022. Award of contract is', '(cid:131) Begin Construction: Fall 2023', '(cid:131) Awaiting final FEMA/CalOES approval for scope modification', 'Westward Beach Road Improvements Project', '(cid:131) Begin Construction: Winter 2024', '(cid:131) Advertise: Spring/Summer 2022', '(cid:131) 65% design package was submitted to Caltrans in November 2020.', '(cid:131) Plans and specifications are being finalized by consultant', 'Westward Beach Road Drainage Improvements Project', 'bicycles pavement markings, delineated parallel parking spaces and', 'draft plans are expected to be completed in early 2022. The Planning', 'Outdoor Warning Signs', '2022 Morning View Resurfacing & Storm Drain Improvements', 'management.', '(cid:131) Begin Construction: Spring/Summer 2022', '(cid:131) Award Contract and Begin Construction: Spring/Summer 2022', 'seeking proposals'], 'matching_projects': ['Storm Drain Master Plan', 'Civic Center Stormwater Diversion Structure', 'PCH at Trancas Canyon Road Right Turn Lane', 'Permanent Skate Park', 'Malibu Bluffs Park South Walkway Repairs', 'Malibu Canyon Road Traffic Study', 'Latigo Canyon Road Retaining Wall Repair Project', 'PCH Median Improvements Project', 'Westward Beach Road Drainage Improvements Project', 'Outdoor Warning Signs'], 'count': 10}, 'var_function-call-8783501668985695830': {'exact_substring_matches': ['project_469', 'project_187', 'project_232', 'project_41', 'project_430', 'project_348', 'project_178', 'project_129', 'project_36', 'Storm Drain Master Plan (FEMA Project)', 'project_114', 'project_471', 'PCH at Trancas Canyon Road Right Turn Lane', 'project_392', 'project_125', 'project_166', 'project_274', 'project_458', 'project_149', 'project_101', 'project_383', 'project_66', 'project_208', 'Permanent Skate Park', 'project_80', 'Westward Beach Road Drainage Improvements Project', 'project_309', 'project_216', 'project_410', 'project_289', 'project_412', 'project_38', 'project_486', 'project_62', 'project_233', 'project_57', 'project_2', 'project_438', 'project_391', 'project_192', 'project_26', 'project_264', 'project_145', 'project_124', 'Malibu Canyon Road Traffic Study', 'project_205', 'project_136', 'project_154', 'project_127', 'project_399', 'project_64', 'project_252', 'project_85', 'project_131', 'project_4', 'project_464', 'project_488', 'project_204', 'project_480', 'project_231', 'Storm Drain Master Plan', 'project_215', 'project_33', 'project_20', 'project_499', 'project_48', 'project_206', 'project_336', 'Civic Center Stormwater Diversion Structure', 'project_423', 'project_77', 'PCH Median Improvements Project', 'project_495', 'project_109', 'project_284', 'project_303', 'project_158', 'project_315', 'project_302', 'project_28', 'project_426', 'project_196', 'project_270', 'project_441', 'project_384', 'project_222', 'project_359', 'project_478', 'project_378', 'project_249', 'project_174', 'project_5', 'project_89', 'project_183', 'project_151', 'project_18', 'project_87', 'project_95', 'project_258', 'project_123', 'project_146', 'Malibu Bluffs Park South Walkway Repairs', 'project_424', 'project_153', 'project_159', 'project_317', 'project_389', 'project_376', 'project_494', 'project_259', 'project_337', 'project_201', 'project_46', 'project_371', 'project_416', 'project_195', 'project_330', 'project_345', 'project_121', 'project_365', 'project_29', 'project_491', 'project_75', 'project_221', 'project_17', 'project_35', 'project_106', 'project_273', 'project_457', 'project_425', 'project_71', 'project_420', 'project_279', 'project_294', 'project_177', 'project_202', 'project_320', 'project_118', 'project_111', 'project_431', 'project_282', 'project_493', 'project_276', 'project_356', 'project_319', 'project_250', 'project_244', 'project_447', 'project_451', 'Clover Heights Storm Drain', 'project_247', 'project_342', 'project_61', 'project_147', 'project_8', 'project_144', 'project_227', 'project_99', 'project_245', 'project_415', 'project_466', 'project_496', 'project_388', 'project_482', 'project_325', 'project_79', 'project_307', 'Outdoor Warning Signs', 'project_372', 'project_477', 'project_408', 'project_91', 'project_92', 'project_449', 'project_361', 'project_386', 'project_305', 'project_338', 'project_170', 'project_343', 'project_397', 'project_190', 'project_402', 'project_228', 'project_138', 'project_409', 'project_285', 'project_364', 'project_126', 'project_42', 'project_59', 'project_31', 'project_193', 'Malibu Bluffs Park South Walkway', 'project_390', 'project_113', 'project_143', 'project_172', 'project_308', 'project_37', 'project_230', 'project_107', 'project_242', 'project_394', 'project_165', 'project_474', 'project_332', 'project_108', 'project_277', 'project_347', 'project_432', 'Trancas Canyon Park Playground Resurfacing', 'project_86', 'project_387', 'project_299', 'project_213', 'project_296', 'project_484', 'project_96', 'project_479', 'project_452', 'project_84', 'project_225', 'project_32', 'project_21', 'project_401', 'project_72', 'project_406', 'project_500', 'project_468', 'Latigo Canyon Road Retaining Wall Repair Project', 'project_304', 'project_50', 'project_51', 'project_255', 'project_355', 'project_335', 'project_461', 'project_444', 'project_49'], 'fuzzy_matches': ['Westward Beach Road Shoulder Repairs (CalOES Project)'], 'total_count': 241}}

exec(code, env_args)
