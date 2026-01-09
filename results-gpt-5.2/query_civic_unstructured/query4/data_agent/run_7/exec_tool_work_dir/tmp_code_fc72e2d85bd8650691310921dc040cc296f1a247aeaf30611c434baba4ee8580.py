code = """import json, re

path_docs = var_call_OG5mKrxRUa6HzkclVyHwauDM
with open(path_docs, 'r', encoding='utf-8') as f:
    docs = json.load(f)

# find occurrences of 'Begin Construction: Spring 2022'
pat = re.compile(r"Begin\s+Construction\s*:\s*Spring\s+2022", re.IGNORECASE)
examples = []
for d in docs:
    t = d.get('text','')
    if not t or 'Spring 2022' not in t:
        continue
    if pat.search(t):
        # capture a window around first match
        m = pat.search(t)
        start = max(0, m.start()-400)
        end = min(len(t), m.end()+400)
        examples.append({"filename": d.get('filename'), "snippet": t[start:end]})
        if len(examples) >= 5:
            break

print('__RESULT__:')
print(json.dumps(examples))"""

env_args = {'var_call_OG5mKrxRUa6HzkclVyHwauDM': 'file_storage/call_OG5mKrxRUa6HzkclVyHwauDM.json', 'var_call_GSCrnvURhXDKm8mhIi6Lg1L6': 'file_storage/call_GSCrnvURhXDKm8mhIi6Lg1L6.json', 'var_call_Q0b1hUX4FlHaWWzXcAsupB2o': {'projects_started_spring_2022_count': 14, 'total_funding_usd': 87000, 'projects': ['Fire.', 'Trancas Canyon Park Planting and Irrigation Repairs (CalJPIA/FEMA Project)', 'Trancas Canyon Park Slope Stabilization Project (CalJPIA Project)', 'advertised for construction bids shortly after this date.', 'beginning in Spring 2022.', 'damaged by the Woolsey Fire.', 'facilities and roadway embankments that were damaged by the Woolsey Fire.', 'is finalizing the bid documents.', 'is working on the project plans to prepare for public bidding.', 'scheduled for the April 11, 2022 Council meeting.', 'sending this project out to bid during the Spring of 2022.', 'shade structures at Malibu Bluffs Park.', 'that was damaged by the Woolsey Fire.', 'timber with non-combustible materials.'], 'projects_missing_funding_match': ['Fire.', 'advertised for construction bids shortly after this date.', 'beginning in Spring 2022.', 'damaged by the Woolsey Fire.', 'facilities and roadway embankments that were damaged by the Woolsey Fire.', 'is finalizing the bid documents.', 'is working on the project plans to prepare for public bidding.', 'scheduled for the April 11, 2022 Council meeting.', 'sending this project out to bid during the Spring of 2022.', 'shade structures at Malibu Bluffs Park.', 'that was damaged by the Woolsey Fire.', 'timber with non-combustible materials.']}, 'var_call_rt1JNM2XioJ99vqaOqMuBNpF': []}

exec(code, env_args)
