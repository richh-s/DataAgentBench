code = """import json
import pandas as pd
import os

civic_docs_var = locals()['var_function-call-72276613876208038']
if isinstance(civic_docs_var, str) and os.path.exists(civic_docs_var):
    with open(civic_docs_var, 'r') as f:
        civic_docs = json.load(f)
else:
    civic_docs = civic_docs_var

text = civic_docs[0]['text']

targets = [
    "Birdview Avenue Improvements",
    "Encinal Canyon Road Drainage Improvements",
    "Malibu Road Slope Repairs",
    "Trancas Canyon Park Slope Stabilization",
    "Latigo Canyon Road Retaining Wall"
]

results = {}
for t in targets:
    idx = text.find(t)
    if idx != -1:
        # Get 500 chars around
        start = max(0, idx)
        end = min(len(text), idx + 1000)
        results[t] = text[start:end]

print("__RESULT__:")
print(json.dumps(results))"""

env_args = {'var_function-call-9094127879311422366': 'file_storage/function-call-9094127879311422366.json', 'var_function-call-9094127879311422561': [{'Funding_ID': '1', 'Project_Name': '2021 Annual Street Maintenance', 'Funding_Source': 'Public-Private Partnership (PPP)', 'Amount': '24000'}, {'Funding_ID': '2', 'Project_Name': '2022 Annual Street Maintenance', 'Funding_Source': 'Government Grant', 'Amount': '45000'}, {'Funding_ID': '3', 'Project_Name': '2022 Morning View Resurfacing & Storm Drain Improvements', 'Funding_Source': 'State Development Grant', 'Amount': '38000'}, {'Funding_ID': '4', 'Project_Name': 'Annual Street Maintenance', 'Funding_Source': 'Corporate Sponsorship', 'Amount': '23000'}, {'Funding_ID': '5', 'Project_Name': 'Birdview Avenue Improvements', 'Funding_Source': 'National Foundation Fund', 'Amount': '79000'}], 'var_function-call-72276613876208038': 'file_storage/function-call-72276613876208038.json', 'var_function-call-4777212261606908531': {'total_funding': 0, 'merged_projects': [], 'projects_dump': [{'Project_Name': '(cid:131) Complete Design: Summer 2023', 'type': 'capital', 'st': None}, {'Project_Name': '(cid:131) Advertise: Fall 2023', 'type': 'capital', 'st': 'Fall 2023 PCH Median Improvements Project'}, {'Project_Name': '(cid:131) Complete Design: Summer 2023', 'type': 'capital', 'st': 'Fall 2023 Westward Beach Road Repair Project'}, {'Project_Name': '(cid:131) Complete Design: Summer 2023', 'type': 'capital', 'st': None}, {'Project_Name': '(cid:131) Advertise: Summer 2023', 'type': 'capital', 'st': 'Fall 2023 Westward Beach Road Drainage Improvement'}, {'Project_Name': '(cid:131) Advertise: Summer 2023', 'type': 'capital', 'st': 'Fall 2023 Clover Heights Storm Drainage Improvemen'}, {'Project_Name': '(cid:131) Final Design: Summer, 2023', 'type': 'capital', 'st': None}, {'Project_Name': '(cid:131) Advertise: Summer 2023', 'type': 'capital', 'st': 'Fall 2023 Latigo Canyon Road Retaining Wall Repair'}, {'Project_Name': '(cid:131) Plans and specifications have been completed', 'type': 'capital', 'st': None}, {'Project_Name': '(cid:131) Advertise: Spring 2023', 'type': 'capital', 'st': 'Summer 2023 Storm Drain Master Plan'}]}, 'var_function-call-11494957844232901297': {'total_funding': 0, 'merged_projects': [], 'projects_dump': [{'Project_Name': 'Trancas Canyon Park Playground', 'type': 'capital', 'st': 'April 2023 (cid:131) Complete Construction: Summe'}, {'Project_Name': 'Marie Canyon Green Streets', 'type': 'capital', 'st': None}, {'Project_Name': 'Point Dume Walkway Repairs', 'type': 'capital', 'st': None}, {'Project_Name': 'Marie Canyon Green Streets', 'type': 'disaster', 'st': 'Spring 2022 PCH Median Improvements Project (cid:'}, {'Project_Name': 'Birdview Avenue Improvements (CalOES Project)', 'type': 'disaster', 'st': 'April 2022 Encinal Canyon Road Drainage Improveme'}, {'Project_Name': 'Marie Canyon Green Streets', 'type': 'disaster', 'st': 'Summer 2021 PCH Median Improvements Project (cid:'}, {'Project_Name': 'Marie Canyon Green Streets', 'type': 'disaster', 'st': 'Summer 2021 PCH Median Improvements Project (cid:'}, {'Project_Name': 'Marie Canyon Green Streets', 'type': 'disaster', 'st': 'Summer 2022 PCH Median Improvements Project (cid:'}, {'Project_Name': 'Birdview Avenue Improvements (CalOES Project)', 'type': 'disaster', 'st': None}]}, 'var_function-call-6471586752170336440': {'total_funding': 79000, 'merged_list': [{'Project_Name_y': 'Birdview Avenue Improvements', 'Amount': 79000, 'st': 'April 2022 Encinal Canyon Road Drainage Improveme'}], 'debug_targets': [{'clean_name': 'Marie Canyon Green Streets', 'st': 'Spring 2022 PCH Median Improvements Project (cid:'}, {'clean_name': 'Birdview Avenue Improvements', 'st': 'April 2022 Encinal Canyon Road Drainage Improveme'}]}, 'var_function-call-15173785481582458392': 'file_storage/function-call-15173785481582458392.json'}

exec(code, env_args)
