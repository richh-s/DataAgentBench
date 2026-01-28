code = """import json

# Read the data from the file
data_file = 'var_functions.query_db:24'
with open(data_file, 'r') as f:
    data = json.load(f)

print('Total patents assigned to UNIV CALIFORNIA:', len(data))

# Check structure of first record
if data:
    first_rec = data[0]
    print('\nFirst record:')
    print('  Keys:', list(first_rec.keys()))
    print('  Patents_info:', first_rec['Patents_info'])
    
    # Parse citation
    import ast
    try:
        citations = ast.literal_eval(first_rec['citation']) if first_rec['citation'] else []
        print('  Number of citations:', len(citations))
        if citations:
            print('  First citation:', citations[0])
    except Exception as e:
        print('  Error parsing citation:', e)

print('\nLooking for citation patterns...')

# Extract all cited patents (publication numbers)
cited_patents = set()
for rec in data:
    try:
        citations = ast.literal_eval(rec['citation']) if rec['citation'] else []
        for cit in citations:
            if 'publication_number' in cit and cit['publication_number']:
                cited_patents.add(cit['publication_number'])
    except:
        continue

print('Unique cited patents found:', len(cited_patents))
print('Sample cited patents:', list(cited_patents)[:10])

print('\n__RESULT__:')
result = {
    'total_uc_patents': len(data),
    'unique_cited_patents': len(cited_patents),
    'sample_cited': list(cited_patents)[:5]
}
print(json.dumps(result))"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:20': [{'Patents_info': 'In US, the application (number US-202117472182-A) is owned by UNIV CALIFORNIA and has pub. number US-2022074631-A1.'}, {'Patents_info': 'UNIV CALIFORNIA holds the TW patent filing (app. number TW-107142982-A), with pub. number TW-201925402-A.'}, {'Patents_info': 'In US, the patent application (no. US-201916454755-A) is assigned to UNIV CALIFORNIA and has publication number US-11421276-B2.'}], 'var_functions.query_db:22': [{'Patents_info': 'PANASONIC IP MAN CO LTD holds the US patent application (ID US-201916293577-A), with publication number US-11081687-B2.'}, {'Patents_info': 'GLASSNER RUDOLF holds the US patent filing (application no. US-201916355911-A), with publication number US-10794458-B2.'}, {'Patents_info': 'In US, the application (ID US-201916369247-A) is owned by COVESTRO LLC and has publication no. US-11124615-B2.'}, {'Patents_info': 'In US, the patent filing (app. number US-201916369879-A) is assigned to HOMOLOGY MEDICINES INC and has pub. number US-10610606-B2.'}, {'Patents_info': 'In US, the patent application (no. US-201916373467-A) is owned by APPLETON GRP LLC and has publication number US-10957507-B2.'}, {'Patents_info': 'MEAD JOHNSON NUTRITION CO holds the US patent application (no. US-201916377667-A), with publication number US-10933114-B2.'}, {'Patents_info': 'WATERS TECHNOLOGIES CORP holds the US application (no. US-201916384272-A), with pub. number US-11169125-B2.'}, {'Patents_info': 'The US patent application (no. US-201916389545-A) is assigned to MODERNATX INC and has pub. number US-10695419-B2.'}, {'Patents_info': 'Patent application (ID US-201916393628-A) from US, owned by YOBS TECH INC, with publication no. US-10950222-B2.'}, {'Patents_info': 'The US patent filing (application number US-201916395813-A) is owned by HONDA MOTOR CO LTD and has publication number US-11168653-B2.'}, {'Patents_info': 'Patent filing (application number US-201916399064-A) from US, held by INTEL CORP, with pub. number US-10853219-B2.'}, {'Patents_info': 'UNIV EMORY holds the US patent filing (application no. US-201916400501-A), with pub. number US-11136369-B2.'}, {'Patents_info': 'In US, the patent filing (application number US-201916412428-A) is belonging to INNOLUX CORP and has publication no. US-11076136-B2.'}, {'Patents_info': 'Application (ID US-201916412740-A) from US, assigned to LEGACY RES AND DEVELOPMENT GROUP LLC, with publication no. US-10898606-B2.'}, {'Patents_info': 'EBAY INC holds the US application (no. US-201916433866-A), with publication number US-11182846-B2.'}, {'Patents_info': 'In US, the application (ID US-201916435109-A) is owned by MAHLE INT GMBH and has pub. number US-11130385-B2.'}, {'Patents_info': 'The US patent application (number US-201916441420-A) is owned by RLW VIRTUAL SOLUTIONS LLC and has publication number US-10720793-B2.'}, {'Patents_info': 'The US application (number US-201916442434-A) is assigned to BHANDARI RAJNEESH and has publication no. US-11141094-B2.'}, {'Patents_info': 'TANDEM DIABETES CARE INC holds the US patent filing (app. number US-201916444452-A), with publication number US-10918785-B2.'}, {'Patents_info': 'Patent application (number US-201916445265-A) from US, belonging to MURATA MANUFACTURING CO, with publication number US-11601114-B2.'}], 'var_functions.query_db:24': 'file_storage/functions.query_db:24.json'}

exec(code, env_args)
