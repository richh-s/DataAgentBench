code = """import json, re

path_docs = var_call_OG5mKrxRUa6HzkclVyHwauDM
with open(path_docs, 'r', encoding='utf-8') as f:
    docs = json.load(f)

begin_pat = re.compile(r"^\(cid:131\)\s*Begin\s+Construction\s*:\s*Spring\s+2022\s*$", re.IGNORECASE)

spring_projects=set()

for d in docs:
    lines=[ln.rstrip() for ln in d.get('text','').splitlines()]
    for idx, ln in enumerate(lines):
        if not begin_pat.match(ln.strip()):
            continue
        # find a candidate title by scanning upwards for a line that is isolated by blank lines around it
        title=None
        for j in range(idx-1, -1, -1):
            cand=lines[j].strip()
            if cand=='' or cand.startswith('(cid'):
                continue
            # stop if too far and haven't found blank boundary
            # accept if previous non-empty line before cand is blank (i.e., section break) OR cand followed by a blank line within next 2 lines
            prev_nonempty=None
            k=j-1
            while k>=0 and lines[k].strip()=='' :
                prev_nonempty='blank'
                break
            # check next lines after cand
            nxt_blank=False
            for k2 in range(j+1, min(len(lines), j+4)):
                if lines[k2].strip()=='' :
                    nxt_blank=True
                    break
                if lines[k2].strip().startswith('(cid:190)'):
                    nxt_blank=True
                    break
            if prev_nonempty=='blank' or nxt_blank:
                title=cand
                break
        if title:
            spring_projects.add(title)

print('__RESULT__:')
print(json.dumps(sorted(spring_projects)))"""

env_args = {'var_call_OG5mKrxRUa6HzkclVyHwauDM': 'file_storage/call_OG5mKrxRUa6HzkclVyHwauDM.json', 'var_call_GSCrnvURhXDKm8mhIi6Lg1L6': 'file_storage/call_GSCrnvURhXDKm8mhIi6Lg1L6.json', 'var_call_Q0b1hUX4FlHaWWzXcAsupB2o': {'projects_started_spring_2022_count': 14, 'total_funding_usd': 87000, 'projects': ['Fire.', 'Trancas Canyon Park Planting and Irrigation Repairs (CalJPIA/FEMA Project)', 'Trancas Canyon Park Slope Stabilization Project (CalJPIA Project)', 'advertised for construction bids shortly after this date.', 'beginning in Spring 2022.', 'damaged by the Woolsey Fire.', 'facilities and roadway embankments that were damaged by the Woolsey Fire.', 'is finalizing the bid documents.', 'is working on the project plans to prepare for public bidding.', 'scheduled for the April 11, 2022 Council meeting.', 'sending this project out to bid during the Spring of 2022.', 'shade structures at Malibu Bluffs Park.', 'that was damaged by the Woolsey Fire.', 'timber with non-combustible materials.'], 'projects_missing_funding_match': ['Fire.', 'advertised for construction bids shortly after this date.', 'beginning in Spring 2022.', 'damaged by the Woolsey Fire.', 'facilities and roadway embankments that were damaged by the Woolsey Fire.', 'is finalizing the bid documents.', 'is working on the project plans to prepare for public bidding.', 'scheduled for the April 11, 2022 Council meeting.', 'sending this project out to bid during the Spring of 2022.', 'shade structures at Malibu Bluffs Park.', 'that was damaged by the Woolsey Fire.', 'timber with non-combustible materials.']}, 'var_call_rt1JNM2XioJ99vqaOqMuBNpF': [], 'var_call_ROpetkJNaEp8Da8BM4rWEQN9': [{'filename': 'malibucity_agenda__01262022-1835.txt', 'snippet': 't was prepared and will be used to size the pre-\nmanufactured biofilters. City staff is reviewing multiple biofilter\nmanufacturers for filters that will work in the proposed project area. It is\nanticipated to have a final design by March 2022. The project will be\nadvertised for construction bids shortly after this date.\n\n(cid:190) Project Schedule:\n\n(cid:131) Complete Design: March 2022\n(cid:131) Begin Construction: Spring 2022\n\nPCH Median Improvements Project\n\n(cid:190) Updates:\n\n(cid:131) The project was approved by the Planning Commission on September\n8, 2021. This project requires Caltrans approval since the work will be\non Pacific Coast Highway. The project reports and plans are being\nrouted through Caltrans for final approval. It is anticipated that the\nproject will have final approval by March 2022. The project w'}, {'filename': 'malibucity_agenda__01272021-1626.txt', 'snippet': 'lete Design: Spring 2022\n(cid:131) Begin Construction: Summer 2022\n\nLatigo Canyon Road Culvert Repairs (FEMA/CalOES Project)\n\n(cid:190) Project Description: This project consists of repairing the existing storm\ndrain on Latigo Canyon Road located approximately 2,500 feet from PCH\nthat was damaged by the Woolsey Fire.\n\n(cid:190) Estimated Schedule:\n\n(cid:131) Complete Design: Winter 2021\n(cid:131) Begin Construction: Spring 2022\n\nEncinal Canyon Road Drainage Improvements (FEMA/CalOES Project)\n\n(cid:190) Project Description: This project consists of repairing damage storm drain\nfacilities and roadway embankments that were damaged by the Woolsey\nFire.\n\n(cid:190) Estimated Schedule:\n\n(cid:131) Complete Design: Winter 2021\n(cid:131) Begin Construction: Spring 2022\n\nOutdoor Warning Sirens (FEMA)\n\n(cid:190) Project Description'}, {'filename': 'malibucity_agenda__03022021-1648.txt', 'snippet': 'lete Design: Spring 2022\n(cid:131) Begin Construction: Summer 2022\n\nLatigo Canyon Road Culvert Repairs (FEMA/CalOES Project)\n\n(cid:190) Project Description: This project consists of repairing the existing storm\ndrain on Latigo Canyon Road located approximately 2,500 feet from PCH\nthat was damaged by the Woolsey Fire.\n\n(cid:190) Estimated Schedule:\n\n(cid:131) Complete Design: Winter 2021\n(cid:131) Begin Construction: Spring 2022\n\nEncinal Canyon Road Drainage Improvements (FEMA/CalOES Project)\n\n(cid:190) Project Description: This project consists of repairing damage storm drain\nfacilities and roadway embankments that were damaged by the Woolsey\nFire.\n\n(cid:190) Estimated Schedule:\n\n(cid:131) Complete Design: Winter 2021\n(cid:131) Begin Construction: Spring 2022\n\nOutdoor Warning Sirens (FEMA Project)\n\n(cid:190) Project Des'}, {'filename': 'malibucity_agenda__03232022-1869.txt', 'snippet': 'ng 2023\n\nBluffs Park Shade Structure\n\n(cid:190) Project Description: This project consists of the installation of four single-post\n\nshade structures at Malibu Bluffs Park.\n\n(cid:190) Updates:\n\n(cid:131) Staff received bids on February 24, 2022. Award of contract is\n\nscheduled for the April 11, 2022 Council meeting.\n\n(cid:190) Estimated Schedule:\n\n(cid:131) Complete Design: February 2022\n(cid:131) Begin Construction: Spring 2022\n\nPermanent Skate Park\n\n(cid:190) Project Description: This project includes designing and constructing a\npermanent skate park located on the Crummer/Case Court parcel adjacent\nto Malibu Bluffs Park. The project would include parking and additional site\namenities such as trash cans, benches, tables, and restrooms.\n\n(cid:190) Updates:\n(cid:131)\n\nIn May 2021, the Council approved funding for additio'}, {'filename': 'malibucity_agenda__03242021-1665.txt', 'snippet': 'lete Design: Spring 2022\n(cid:131) Begin Construction: Summer 2022\n\nLatigo Canyon Road Culvert Repairs (FEMA/CalOES Project)\n\n(cid:190) Project Description: This project consists of repairing the existing storm\ndrain on Latigo Canyon Road located approximately 2,500 feet from PCH\nthat was damaged by the Woolsey Fire.\n\n(cid:190) Estimated Schedule:\n\n(cid:131) Complete Design: Winter 2021\n(cid:131) Begin Construction: Spring 2022\n\nEncinal Canyon Road Drainage Improvements (FEMA/CalOES Project)\n\n(cid:190) Project Description: This project consists of repairing damage storm drain\nfacilities and roadway embankments that were damaged by the Woolsey\nFire.\n\n(cid:190) Estimated Schedule:\n\n(cid:131) Complete Design: Winter 2021\n(cid:131) Begin Construction: Spring 2022\n\nStorm Drain Master Plan (FEMA Project)\n\n(cid:190) Project De'}], 'var_call_Fc7632hHFtrKBw5vno2P6zEs': {'count': 14, 'total_funding_usd': 87000, 'projects': ['Fire.', 'Trancas Canyon Park Planting and Irrigation Repairs (CalJPIA/FEMA Project)', 'Trancas Canyon Park Slope Stabilization Project (CalJPIA Project)', 'advertised for construction bids shortly after this date.', 'beginning in Spring 2022.', 'damaged by the Woolsey Fire.', 'facilities and roadway embankments that were damaged by the Woolsey Fire.', 'is finalizing the bid documents.', 'is working on the project plans to prepare for public bidding.', 'scheduled for the April 11, 2022 Council meeting.', 'sending this project out to bid during the Spring of 2022.', 'shade structures at Malibu Bluffs Park.', 'that was damaged by the Woolsey Fire.', 'timber with non-combustible materials.'], 'missing_funding': ['Fire.', 'advertised for construction bids shortly after this date.', 'beginning in Spring 2022.', 'damaged by the Woolsey Fire.', 'facilities and roadway embankments that were damaged by the Woolsey Fire.', 'is finalizing the bid documents.', 'is working on the project plans to prepare for public bidding.', 'scheduled for the April 11, 2022 Council meeting.', 'sending this project out to bid during the Spring of 2022.', 'shade structures at Malibu Bluffs Park.', 'that was damaged by the Woolsey Fire.', 'timber with non-combustible materials.']}}

exec(code, env_args)
