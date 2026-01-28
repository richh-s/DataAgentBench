code = """import json
import re

# Get data from storage
data_key = 'var_functions.query_db:28'
if data_key in locals():
    data_var = locals()[data_key]
    print(f"Data type: {type(data_var)}")
    
    # Try to load records
    if isinstance(data_var, str):
        import os
        if os.path.exists(data_var):
            with open(data_var, 'r') as f:
                records = json.load(f)
        else:
            # Try as JSON string
            records = json.loads(data_var)
    else:
        records = data_var
    
    print(f"Records loaded: {len(records)}")
    
    # Show data structure
    if records:
        print("First record structure:")
        rec = records[0]
        for key in rec.keys():
            print(f"  {key}: {type(rec[key])}")
            
        # Show sample CPC data
        if 'cpc' in rec:
            cpc_str = rec['cpc']
            try:
                cpc_list = json.loads(cpc_str)
                print(f"  CPC codes in first record: {len(cpc_list)}")
                for item in cpc_list[:3]:
                    print(f"    {item}")
            except:
                print(f"  CPC string (unparsed): {cpc_str[:100]}")
        
        # Show publication date
        if 'publication_date' in rec:
            print(f"  Publication date: {rec['publication_date']}")
        
        # Extract some sample data for analysis
        patent_data = []
        for record in records:
            pub_date = record.get('publication_date', '')
            year_match = re.search(r'(\d{4})', pub_date)
            if year_match:
                year = int(year_match.group(1))
                cpc_str = record.get('cpc', '[]')
                try:
                    cpc_list = json.loads(cpc_str)
                    for cpc_item in cpc_list:
                        cpc_code = cpc_item.get('code', '')
                        if cpc_code:
                            patent_data.append({'cpc': cpc_code, 'year': year})
                except:
                    continue
        
        print(f"\nExtracted {len(patent_data)} patent classifications with years")
        if patent_data:
            print("Sample entries:", patent_data[:5])
        
        # Unique CPC codes
        unique_codes = set(item['cpc'] for item in patent_data)
        print(f"Unique CPC codes: {len(unique_codes)}")
        print("Sample unique codes:", list(unique_codes)[:10])
        
        # Extract level 5 codes
        level_5_codes = set()
        for code in unique_codes:
            if '/' in code:
                main_part = code.split('/')[0]
                # Remove trailing digits
                i = len(main_part) - 1
                while i >= 0 and main_part[i].isdigit():
                    i -= 1
                level_5 = main_part[:i+1]
                if len(level_5) >= 3:  # Valid CPC code
                    level_5_codes.add(level_5)
            else:
                # Already a group-level code
                if len(code) >= 3:
                    level_5_codes.add(code)
        
        print(f"Level 5 codes: {len(level_5_codes)}")
        print("Sample level 5 codes:", list(level_5_codes)[:10])

else:
    print("Data key not found in storage")

result_msg = f"Analyzed {len(records) if 'records' in locals() else 0} records"
print("__RESULT__:")
print(json.dumps(result_msg))"""

env_args = {'var_functions.list_db:0': ['publicationinfo'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:6': [{'symbol': 'A01H', 'level': '5.0', 'titleFull': 'NEW PLANTS OR NON-TRANSGENIC PROCESSES FOR OBTAINING THEM; PLANT REPRODUCTION BY TISSUE CULTURE TECHNIQUES'}, {'symbol': 'A01F', 'level': '5.0', 'titleFull': 'PROCESSING OF HARVESTED PRODUCE; HAY OR STRAW PRESSES; DEVICES FOR STORING AGRICULTURAL OR HORTICULTURAL PRODUCE'}, {'symbol': 'A01C', 'level': '5.0', 'titleFull': 'PLANTING; SOWING; FERTILISING'}, {'symbol': 'A01G', 'level': '5.0', 'titleFull': 'HORTICULTURE; CULTIVATION OF VEGETABLES, FLOWERS, RICE, FRUIT, VINES, HOPS OR SEAWEED; FORESTRY; WATERING'}, {'symbol': 'A23J', 'level': '5.0', 'titleFull': 'PROTEIN COMPOSITIONS FOR FOODSTUFFS; WORKING-UP PROTEINS FOR FOODSTUFFS; PHOSPHATIDE COMPOSITIONS FOR FOODSTUFFS'}, {'symbol': 'A01N', 'level': '5.0', 'titleFull': 'PRESERVATION OF BODIES OF HUMANS OR ANIMALS OR PLANTS OR PARTS THEREOF; BIOCIDES, e.g. AS DISINFECTANTS, AS PESTICIDES OR AS HERBICIDES; PEST REPELLANTS OR ATTRACTANTS; PLANT GROWTH REGULATORS'}, {'symbol': 'A01P', 'level': '5.0', 'titleFull': 'BIOCIDAL, PEST REPELLANT, PEST ATTRACTANT OR PLANT GROWTH REGULATORY ACTIVITY OF CHEMICAL COMPOUNDS OR PREPARATIONS'}, {'symbol': 'A01D', 'level': '5.0', 'titleFull': 'HARVESTING; MOWING'}, {'symbol': 'A01L', 'level': '5.0', 'titleFull': 'SHOEING OF ANIMALS'}, {'symbol': 'A01K', 'level': '5.0', 'titleFull': 'ANIMAL HUSBANDRY; AVICULTURE; APICULTURE; PISCICULTURE; FISHING; REARING OR BREEDING ANIMALS, NOT OTHERWISE PROVIDED FOR; NEW BREEDS OF ANIMALS'}], 'var_functions.query_db:8': 'file_storage/functions.query_db:8.json', 'var_functions.execute_python:24': 'initialized', 'var_functions.query_db:28': 'file_storage/functions.query_db:28.json'}

exec(code, env_args)
