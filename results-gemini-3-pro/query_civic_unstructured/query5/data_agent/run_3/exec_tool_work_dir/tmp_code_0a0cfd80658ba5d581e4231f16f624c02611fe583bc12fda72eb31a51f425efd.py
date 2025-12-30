code = """import json
import pandas as pd
import os
import re

civic_docs_var = locals()['var_function-call-72276613876208038']
if isinstance(civic_docs_var, str) and os.path.exists(civic_docs_var):
    with open(civic_docs_var, 'r') as f:
        civic_docs = json.load(f)
else:
    civic_docs = civic_docs_var

# Combine all text
full_text = "\n".join([d['text'] for d in civic_docs])

# Funding Names
funding_names = [
    "Birdview Avenue Improvements (CalOES Project)", "Birdview Avenue Improvements (FEMA/CalOES Project)", 
    "Broad Beach Road Water Quality Infrastructure Repairs (CalJPIA Project)", 
    "Clover Heights Storm Drain (FEMA Project)", 
    "Corral Canyon Culvert Repairs (FEMA Project)", "Corral Canyon Culvert Repairs (FEMA/CalOES Project)",
    "Corral Canyon Road Bridge Repairs (FEMA Project)", "Corral Canyon Road Bridge Repairs (FEMA/CalOES Project)",
    "Encinal Canyon Road Drainage Improvements (CalOES Project)", "Encinal Canyon Road Drainage Improvements (FEMA/CalOES Project)",
    "Guardrail Replacement Citywide (FEMA Project)", "Guardrail Replacement Citywide (FEMA/CalOES Project)",
    "Latigo Canyon Road Culvert Repairs (FEMA Project)", "Latigo Canyon Road Culvert Repairs (FEMA/CalOES Project)",
    "Latigo Canyon Road Roadway/Retaining Wall Improvements (FEMA Project)", "Latigo Canyon Road Roadway/Retaining Wall Improvements (FEMA/CalOES Project)",
    "Malibu Road Slope Repairs (CalOES Project)", 
    "Outdoor Warning Sirens (FEMA Project)", "Outdoor Warning Sirens - Design (FEMA Project)", "Outdoor Warningn Sirens - Design (FEMA Project)",
    "Storm Drain Master Plan (FEMA Project)", 
    "Trancas Canyon Park Planting and Irrigation Repairs (CalJPIA/FEMA Project)", "Trancas Canyon Park Planting and Irrigation Repairs (FEMA/CalOES Project)",
    "Trancas Canyon Park Slope Stabilization Project (CalJPIA Project)", "Trancas Canyon Park Slope Stabilization Project (CalOES Project)",
    "Westward Beach Road Shoulder Repairs (CalOES Project)"
]

matches = []

for name in funding_names:
    # Find all occurrences
    # Use re.escape for name
    # Search for Name followed by ... Begin Construction: <Date>
    # We look for the name, then scan ahead for "Begin Construction" within reasonable distance (e.g. 500 chars)
    # matching the project block structure.
    
    # Simple approach: Find name, look at next 500 chars.
    idx = 0
    while True:
        idx = full_text.find(name, idx)
        if idx == -1: break
        
        context = full_text[idx:idx+1000]
        # Look for start date in context
        # Stop at next project (heuristic: look for next line starting with known header or just take first match)
        
        st_match = re.search(r'(?:Begin Construction|Start|Commence Construction)[:\s]+([A-Za-z0-9\s,]+)', context, re.IGNORECASE)
        st_date = "Not Found"
        if st_match:
            st_date = st_match.group(1).strip().split('\n')[0]
            if len(st_date) > 30: st_date = st_date[:30]
        
        matches.append({
            "name": name,
            "st": st_date,
            "context_snip": context[:200]
        })
        
        idx += 1

print("__RESULT__:")
print(json.dumps(matches))"""

env_args = {'var_function-call-9094127879311422366': 'file_storage/function-call-9094127879311422366.json', 'var_function-call-9094127879311422561': [{'Funding_ID': '1', 'Project_Name': '2021 Annual Street Maintenance', 'Funding_Source': 'Public-Private Partnership (PPP)', 'Amount': '24000'}, {'Funding_ID': '2', 'Project_Name': '2022 Annual Street Maintenance', 'Funding_Source': 'Government Grant', 'Amount': '45000'}, {'Funding_ID': '3', 'Project_Name': '2022 Morning View Resurfacing & Storm Drain Improvements', 'Funding_Source': 'State Development Grant', 'Amount': '38000'}, {'Funding_ID': '4', 'Project_Name': 'Annual Street Maintenance', 'Funding_Source': 'Corporate Sponsorship', 'Amount': '23000'}, {'Funding_ID': '5', 'Project_Name': 'Birdview Avenue Improvements', 'Funding_Source': 'National Foundation Fund', 'Amount': '79000'}], 'var_function-call-72276613876208038': 'file_storage/function-call-72276613876208038.json', 'var_function-call-4777212261606908531': {'total_funding': 0, 'merged_projects': [], 'projects_dump': [{'Project_Name': '(cid:131) Complete Design: Summer 2023', 'type': 'capital', 'st': None}, {'Project_Name': '(cid:131) Advertise: Fall 2023', 'type': 'capital', 'st': 'Fall 2023 PCH Median Improvements Project'}, {'Project_Name': '(cid:131) Complete Design: Summer 2023', 'type': 'capital', 'st': 'Fall 2023 Westward Beach Road Repair Project'}, {'Project_Name': '(cid:131) Complete Design: Summer 2023', 'type': 'capital', 'st': None}, {'Project_Name': '(cid:131) Advertise: Summer 2023', 'type': 'capital', 'st': 'Fall 2023 Westward Beach Road Drainage Improvement'}, {'Project_Name': '(cid:131) Advertise: Summer 2023', 'type': 'capital', 'st': 'Fall 2023 Clover Heights Storm Drainage Improvemen'}, {'Project_Name': '(cid:131) Final Design: Summer, 2023', 'type': 'capital', 'st': None}, {'Project_Name': '(cid:131) Advertise: Summer 2023', 'type': 'capital', 'st': 'Fall 2023 Latigo Canyon Road Retaining Wall Repair'}, {'Project_Name': '(cid:131) Plans and specifications have been completed', 'type': 'capital', 'st': None}, {'Project_Name': '(cid:131) Advertise: Spring 2023', 'type': 'capital', 'st': 'Summer 2023 Storm Drain Master Plan'}]}, 'var_function-call-11494957844232901297': {'total_funding': 0, 'merged_projects': [], 'projects_dump': [{'Project_Name': 'Trancas Canyon Park Playground', 'type': 'capital', 'st': 'April 2023 (cid:131) Complete Construction: Summe'}, {'Project_Name': 'Marie Canyon Green Streets', 'type': 'capital', 'st': None}, {'Project_Name': 'Point Dume Walkway Repairs', 'type': 'capital', 'st': None}, {'Project_Name': 'Marie Canyon Green Streets', 'type': 'disaster', 'st': 'Spring 2022 PCH Median Improvements Project (cid:'}, {'Project_Name': 'Birdview Avenue Improvements (CalOES Project)', 'type': 'disaster', 'st': 'April 2022 Encinal Canyon Road Drainage Improveme'}, {'Project_Name': 'Marie Canyon Green Streets', 'type': 'disaster', 'st': 'Summer 2021 PCH Median Improvements Project (cid:'}, {'Project_Name': 'Marie Canyon Green Streets', 'type': 'disaster', 'st': 'Summer 2021 PCH Median Improvements Project (cid:'}, {'Project_Name': 'Marie Canyon Green Streets', 'type': 'disaster', 'st': 'Summer 2022 PCH Median Improvements Project (cid:'}, {'Project_Name': 'Birdview Avenue Improvements (CalOES Project)', 'type': 'disaster', 'st': None}]}, 'var_function-call-6471586752170336440': {'total_funding': 79000, 'merged_list': [{'Project_Name_y': 'Birdview Avenue Improvements', 'Amount': 79000, 'st': 'April 2022 Encinal Canyon Road Drainage Improveme'}], 'debug_targets': [{'clean_name': 'Marie Canyon Green Streets', 'st': 'Spring 2022 PCH Median Improvements Project (cid:'}, {'clean_name': 'Birdview Avenue Improvements', 'st': 'April 2022 Encinal Canyon Road Drainage Improveme'}]}, 'var_function-call-15173785481582458392': 'file_storage/function-call-15173785481582458392.json', 'var_function-call-7986045742761954410': {'Malibu Road Slope Repairs': 'Malibu Road Slope Repairs\n\n(cid:190) Updates: Project is currently under construction\n(cid:190) Complete Construction: April 2023\n\nEncinal Canyon Road Repairs\n\n(cid:190) Updates: Project is currently under construction\n(cid:190) Complete Construction: Summer 2023\n\nPCH Signal Synchronization System Improvements Project\n\n(cid:190) Updates:\n\n(cid:131) On February 27, 2023, City Council awarded the contract to GMZ\n\nEngineering, Inc.\n\n(cid:190) Project Schedule:\n\n(cid:131) Begin construction: April 2023\n(cid:131) Complete Construction: Summer 2025\n\nStorm Drain Trash Screens Phase Two\n\n(cid:190) Updates:\n\n(cid:131) Project is currently out to bid. Bids are due on March 23, 2023.\n\n(cid:190) Project Schedule:\n\n(cid:131) Begin construction: Summer 2023\n(cid:131) Complete Construction: Summer 2023\n\nBluffs Park Shade Structure\n\n(cid:190) Updates: Construction was completed November 2022. Notice of completion\n\nfiled January 2023\n\nPage 4 of 6\n\nAgenda Item # 4.B.\n\n\n\n\n\n\n\n\n\n\n\nMarie Canyon Green Street', 'Latigo Canyon Road Retaining Wall': 'Latigo Canyon Road Retaining Wall Repair Project\n\n(cid:190) Updates:\n\n(cid:131) Plans and specifications have been completed\n(cid:131) Awaiting final FEMA/CalOES approval for scope modification\n\n(cid:190) Project Schedule:\n\n(cid:131) Advertise: Spring 2023\n(cid:131) Begin Construction: Summer 2023\n\nStorm Drain Master Plan\n\n(cid:190) Updates:\n\n(cid:131) Field data collection has been completed and storm drain inventory has\n\nbeen finalized and incorporated into GIS.\n\n(cid:131) Consultant working finalizing a CIP recommendation list\n\nPage 2 of 6\n\nAgenda Item # 4.B.\n\n\n\n\n\n\n\n\n\n\n\nTrancas Canyon Park Upper and Lower Slopes Repair\n\n(cid:190) Updates:\n\n(cid:131) Plans and specifications are being finalized by consultant\n\n(cid:190) Project Schedule:\n\n(cid:131) Advertise: Spring 2023\n(cid:131) Begin Construction: Summer 2023\n\nCivic Center Water Treatment Facility Phase 2\n\n(cid:190) Updates:\n\n(cid:131) Staff is working with the State Water Board regarding the Cultural\n\nResources review for the SRF '}, 'var_function-call-18266233374072304929': 'file_storage/function-call-18266233374072304929.json', 'var_function-call-14154974869137264788': [{'Project_Name': 'Birdview Avenue Improvements (CalOES Project)', 'Amount': '85000'}, {'Project_Name': 'Birdview Avenue Improvements (FEMA/CalOES Project)', 'Amount': '14000'}, {'Project_Name': 'Broad Beach Road Water Quality Infrastructure Repairs (CalJPIA Project)', 'Amount': '81000'}, {'Project_Name': 'Clover Heights Storm Drain (FEMA Project)', 'Amount': '21000'}, {'Project_Name': 'Corral Canyon Culvert Repairs (FEMA Project)', 'Amount': '43000'}, {'Project_Name': 'Corral Canyon Culvert Repairs (FEMA/CalOES Project)', 'Amount': '15000'}, {'Project_Name': 'Corral Canyon Road Bridge Repairs (FEMA Project)', 'Amount': '25000'}, {'Project_Name': 'Corral Canyon Road Bridge Repairs (FEMA/CalOES Project)', 'Amount': '58000'}, {'Project_Name': 'Encinal Canyon Road Drainage Improvements (CalOES Project)', 'Amount': '18000'}, {'Project_Name': 'Encinal Canyon Road Drainage Improvements (FEMA/CalOES Project)', 'Amount': '94000'}, {'Project_Name': 'Guardrail Replacement Citywide (FEMA Project)', 'Amount': '22000'}, {'Project_Name': 'Guardrail Replacement Citywide (FEMA/CalOES Project)', 'Amount': '45000'}, {'Project_Name': 'Latigo Canyon Road Culvert Repairs (FEMA Project)', 'Amount': '36000'}, {'Project_Name': 'Latigo Canyon Road Culvert Repairs (FEMA/CalOES Project)', 'Amount': '44000'}, {'Project_Name': 'Latigo Canyon Road Roadway/Retaining Wall Improvements (FEMA Project)', 'Amount': '91000'}, {'Project_Name': 'Latigo Canyon Road Roadway/Retaining Wall Improvements (FEMA/CalOES Project)', 'Amount': '78000'}, {'Project_Name': 'Malibu Road Slope Repairs (CalOES Project)', 'Amount': '37000'}, {'Project_Name': 'Outdoor Warning Sirens (FEMA Project)', 'Amount': '27000'}, {'Project_Name': 'Outdoor Warning Sirens (FEMA)', 'Amount': '81000'}, {'Project_Name': 'Outdoor Warning Sirens - Design (FEMA Project)', 'Amount': '43000'}, {'Project_Name': 'Outdoor Warningn Sirens - Design (FEMA Project)', 'Amount': '84000'}, {'Project_Name': 'Storm Drain Master Plan (FEMA Project)', 'Amount': '80000'}, {'Project_Name': 'Trancas Canyon Park Planting and Irrigation Repairs (CalJPIA/FEMA Project)', 'Amount': '44000'}, {'Project_Name': 'Trancas Canyon Park Planting and Irrigation Repairs (FEMA/CalOES Project)', 'Amount': '92000'}, {'Project_Name': 'Trancas Canyon Park Slope Stabilization Project (CalJPIA Project)', 'Amount': '43000'}, {'Project_Name': 'Trancas Canyon Park Slope Stabilization Project (CalOES Project)', 'Amount': '32000'}, {'Project_Name': 'Westward Beach Road Shoulder Repairs (CalOES Project)', 'Amount': '77000'}]}

exec(code, env_args)
