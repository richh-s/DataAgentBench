code = """import json

with open(locals()['var_function-call-16179877025922844511'], 'r') as f:
    civic_docs = json.load(f)

# Find the specific document
target_doc = None
for doc in civic_docs:
    if "malibucity_agenda__01262022-1835.txt" in doc['filename']:
        target_doc = doc
        break

lines_to_print = []
if target_doc:
    text = target_doc['text']
    lines = text.splitlines()
    for i, line in enumerate(lines):
        if "Malibu Park Drainage Improvements" in line:
            # Capture context
            context = lines[i:i+15]
            lines_to_print.extend(context)

print("__RESULT__:")
print(json.dumps(lines_to_print))"""

env_args = {'var_function-call-13030964589425589265': 'file_storage/function-call-13030964589425589265.json', 'var_function-call-13030964589425590204': 'file_storage/function-call-13030964589425590204.json', 'var_function-call-16179877025922844511': 'file_storage/function-call-16179877025922844511.json', 'var_function-call-15826040215521897163': {'total': 118000, 'projects': [{'name': 'Bluffs Park Shade Structure', 'amount': 21000}, {'name': 'Permanent Skate Park', 'amount': 97000}]}, 'var_function-call-7715372612916809138': ['Doc: malibucity_agenda__01262022-1835.txt, Line: draft plans are expected to be completed in early 2022. The Planning', 'Doc: malibucity_agenda__01262022-1835.txt, Line: draft plans are expected to be completed in early 2022. The Planning', 'Doc: malibucity_agenda__03232022-1869.txt, Line: draft plans are expected to be completed in early 2022. The Planning', 'Doc: malibucity_agenda__03232022-1869.txt, Line: draft plans are expected to be completed in early 2022. The Planning'], 'var_function-call-14360294538855612841': {'total': 21000, 'projects': [{'name': 'Bluffs Park Shade Structure', 'amount': 21000}]}, 'var_function-call-5987047567736730737': ['Project: Permanent Skate Park, Doc: malibucity_agenda_03222023-2060.txt, Line: (cid:131) Complete Design: Spring 2023', 'Project: Malibu Bluffs Park South Walkway Repairs, Doc: malibucity_agenda_03222023-2060.txt, Line: (cid:131) Complete Design: Summer 2023', 'Project: Trancas Canyon Park Playground, Doc: malibucity_agenda_03222023-2060.txt, Line: (cid:131) Complete Design: Summer 2023', 'Project: Bluffs Park Shade Structure, Doc: malibucity_agenda_03222023-2060.txt, Line: (cid:190) Updates: Construction was completed November 2022. Notice of completion', 'Project: Bluffs Park Shade Structure, Doc: malibucity_agenda__01262022-1835.txt, Line: (cid:131) Complete Design: Spring 2022', 'Project: Permanent Skate Park, Doc: malibucity_agenda__01262022-1835.txt, Line: the past several months to complete the engineering work, and the final', 'Project: Permanent Skate Park, Doc: malibucity_agenda__01262022-1835.txt, Line: draft plans are expected to be completed in early 2022. The Planning', 'Project: Permanent Skate Park, Doc: malibucity_agenda__01262022-1835.txt, Line: (cid:131) Complete Design: Spring 2022', 'Project: Trancas Canyon Park Planting and Irrigation Repairs (CalJPIA/FEMA Project), Doc: malibucity_agenda__01262022-1835.txt, Line: (cid:131) Complete Design: Spring 2022', 'Project: Trancas Canyon Park Slope Stabilization Project (CalJPIA Project), Doc: malibucity_agenda__01262022-1835.txt, Line: (cid:131) Complete Design: Spring 2022', 'Project: Malibu Park Drainage Improvements, Doc: malibucity_agenda__01262022-1835.txt, Line: (cid:190) Updates: The Contractor completed the repairs to storm drains on Cuthbert', 'Project: Malibu Park Drainage Improvements, Doc: malibucity_agenda__01272021-1626.txt, Line: (cid:131) Complete Design: Spring 2021', 'Project: Bluffs Park Shade Structure, Doc: malibucity_agenda__01272021-1626.txt, Line: (cid:131) Complete Design: Summer 2021', 'Project: Trancas Canyon Park Planting and Irrigation Repairs (FEMA/CalOES Project), Doc: malibucity_agenda__01272021-1626.txt, Line: (cid:131) Complete Design: Summer 2021', 'Project: Trancas Canyon Park Slope Stabilization Project (CalOES Project), Doc: malibucity_agenda__01272021-1626.txt, Line: (cid:131) Complete Design: Spring 2021', 'Project: Malibu Park Drainage Improvements, Doc: malibucity_agenda__03022021-1648.txt, Line: (cid:131) Complete Design: February 2021', 'Project: Bluffs Park Shade Structure, Doc: malibucity_agenda__03022021-1648.txt, Line: (cid:131) Complete Design: Summer 2021', 'Project: Trancas Canyon Park Planting and Irrigation Repairs (FEMA/CalOES Project), Doc: malibucity_agenda__03022021-1648.txt, Line: (cid:131) Complete Design: Summer 2021', 'Project: Trancas Canyon Park Slope Stabilization Project (CalOES Project), Doc: malibucity_agenda__03022021-1648.txt, Line: (cid:131) Complete Design: Spring 2021', 'Project: Bluffs Park Shade Structure, Doc: malibucity_agenda__03232022-1869.txt, Line: (cid:131) Complete Design: February 2022']}

exec(code, env_args)
