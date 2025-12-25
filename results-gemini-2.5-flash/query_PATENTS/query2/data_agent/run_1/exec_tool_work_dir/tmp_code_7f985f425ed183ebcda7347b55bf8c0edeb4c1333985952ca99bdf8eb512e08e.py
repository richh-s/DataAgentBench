code = """import pandas as pd
import json

data = pd.read_json(locals()['var_function-call-6623226614519656190'])
cpc_titles_data = locals()['var_function-call-12428504695965929192']

# Filter for German patents and grant date in the second half of 2019
def is_german_patent(patents_info):
    return 'DE,' in patents_info

def is_second_half_2019(grant_date):
    try:
        if isinstance(grant_date, str):
            grant_date_str = grant_date.lower()
            if 'jul' in grant_date_str or 'aug' in grant_date_str or 'sep' in grant_date_str or \
               'oct' in grant_date_str or 'nov' in grant_date_str or 'dec' in grant_date_str:
                return True
        return False
    except:
        return False

filtered_patents = data[data['Patents_info'].apply(is_german_patent) &
                        data['grant_date'].apply(is_second_half_2019)].copy()

# Extract CPC codes and filing year
cpc_filing_data = []
for index, row in filtered_patents.iterrows():
    cpc_list = json.loads(row['cpc'])
    filing_date_str = row['filing_date']
    filing_year = None
    if isinstance(filing_date_str, str):
        for part in filing_date_str.split():
            if part.isdigit() and len(part) == 4:
                filing_year = int(part)
                break
    
    for cpc_item in cpc_list:
        cpc_code = cpc_item['code']
        if len(cpc_code) >= 4 and filing_year: # Ensure it's at least level 4
            cpc_group = cpc_code[:4] # Get level 4 CPC group
            cpc_filing_data.append({'cpc_group': cpc_group, 'filing_year': filing_year})

cpc_filing_df = pd.DataFrame(cpc_filing_data)

# Group by CPC group and filing year, then count filings
filings_by_cpc_year = cpc_filing_df.groupby(['cpc_group', 'filing_year']).size().reset_index(name='filings_count')

# Calculate EMA
alpha = 0.1
ema_results = []
for cpc_group in filings_by_cpc_year['cpc_group'].unique():
    cpc_group_df = filings_by_cpc_year[filings_by_cpc_year['cpc_group'] == cpc_group].sort_values(by='filing_year')
    
    # Initialize EMA for the first year
    if not cpc_group_df.empty:
        ema = 0
        if not cpc_group_df.empty:
            ema = cpc_group_df.iloc[0]['filings_count']
            ema_results.append({
                'cpc_group': cpc_group,
                'filing_year': cpc_group_df.iloc[0]['filings_year'],
                'ema': ema
            })
        
        # Calculate EMA for subsequent years
        for i in range(1, len(cpc_group_df)):
            ema = alpha * cpc_group_df.iloc[i]['filings_count'] + (1 - alpha) * ema
            ema_results.append({
                'cpc_group': cpc_group,
                'filing_year': cpc_group_df.iloc[i]['filing_year'],
                'ema': ema
            })

ema_df = pd.DataFrame(ema_results)

# Find the best year for each CPC group
best_years = ema_df.loc[ema_df.groupby('cpc_group')['ema'].idxmax()]

# Prepare CPC titles dataframe
cpc_titles_df = pd.DataFrame(cpc_titles_data)
cpc_titles_df.rename(columns={'symbol': 'cpc_group', 'titleFull': 'full_title'}, inplace=True)

# Merge results to get full titles and best year
final_result = pd.merge(best_years, cpc_titles_df, on='cpc_group', how='left')

# Format the output
output = []
for index, row in final_result.iterrows():
    output.append({
        'full_title': row['full_title'],
        'cpc_group_code': row['cpc_group'],
        'best_year': row['filing_year']
    })

print("__RESULT__:")
print(json.dumps(output))"""

env_args = {'var_function-call-6623226614519656190': 'file_storage/function-call-6623226614519656190.json', 'var_function-call-9406239657222584757': ['A43B', 'A61B', 'A61F', 'A61L', 'B23K', 'B41F', 'B60K', 'B60N', 'B60R', 'B60W', 'B64D', 'E02F', 'F01D', 'F02M', 'F02N', 'F04B', 'F04D', 'F05D', 'F16C', 'F16F', 'F16K', 'F17C', 'F41H', 'F42B', 'G01D', 'G01M', 'G01N', 'G02B', 'G05D', 'G08B', 'H01R', 'H02J', 'H03L', 'H04L', 'H04W', 'Y02D', 'Y02T'], 'var_function-call-6982923480119486199': [], 'var_function-call-17065823913741193205': [{'level': '2.0'}, {'level': '4.0'}, {'level': '5.0'}, {'level': '7.0'}, {'level': '8.0'}, {'level': '9.0'}, {'level': '10.0'}, {'level': '11.0'}, {'level': '12.0'}, {'level': '13.0'}, {'level': '14.0'}, {'level': '15.0'}, {'level': '16.0'}, {'level': '17.0'}, {'level': '18.0'}, {'level': '19.0'}], 'var_function-call-3724504970294373724': [{'titleFull': 'CHARACTERISTIC FEATURES OF FOOTWEAR; PARTS OF FOOTWEAR', 'symbol': 'A43B', 'level': '5.0'}, {'titleFull': 'DIAGNOSIS; SURGERY; IDENTIFICATION', 'symbol': 'A61B', 'level': '5.0'}, {'titleFull': 'FILTERS IMPLANTABLE INTO BLOOD VESSELS; PROSTHESES; DEVICES PROVIDING PATENCY TO, OR PREVENTING COLLAPSING OF, TUBULAR STRUCTURES OF THE BODY, e.g. STENTS; ORTHOPAEDIC, NURSING OR CONTRACEPTIVE DEVICES; FOMENTATION; TREATMENT OR PROTECTION OF EYES OR EARS; BANDAGES, DRESSINGS OR ABSORBENT PADS; FIRST-AID KITS', 'symbol': 'A61F', 'level': '5.0'}, {'titleFull': 'SOLDERING OR UNSOLDERING; WELDING; CLADDING OR PLATING BY SOLDERING OR WELDING; CUTTING BY APPLYING HEAT LOCALLY, e.g. FLAME CUTTING; WORKING BY LASER BEAM', 'symbol': 'B23K', 'level': '5.0'}], 'var_function-call-3596812814041938397': ['A43B', 'A61B', 'A61F', 'A61L', 'B23K', 'B41F', 'B60K', 'B60N', 'B60R', 'B60W', 'B64D', 'E02F', 'F01D', 'F02M', 'F02N', 'F04B', 'F04D', 'F05D', 'F16C', 'F16F', 'F16K', 'F17C', 'F41H', 'F42B', 'G01D', 'G01M', 'G01N', 'G02B', 'G05D', 'G08B', 'H01R', 'H02J', 'H03L', 'H04L', 'H04W', 'Y02D', 'Y02T'], 'var_function-call-12428504695965929192': [{'titleFull': 'CHARACTERISTIC FEATURES OF FOOTWEAR; PARTS OF FOOTWEAR', 'symbol': 'A43B', 'level': '5.0'}, {'titleFull': 'DIAGNOSIS; SURGERY; IDENTIFICATION', 'symbol': 'A61B', 'level': '5.0'}, {'titleFull': 'FILTERS IMPLANTABLE INTO BLOOD VESSELS; PROSTHESES; DEVICES PROVIDING PATENCY TO, OR PREVENTING COLLAPSING OF, TUBULAR STRUCTURES OF THE BODY, e.g. STENTS; ORTHOPAEDIC, NURSING OR CONTRACEPTIVE DEVICES; FOMENTATION; TREATMENT OR PROTECTION OF EYES OR EARS; BANDAGES, DRESSINGS OR ABSORBENT PADS; FIRST-AID KITS', 'symbol': 'A61F', 'level': '5.0'}, {'titleFull': 'METHODS OR APPARATUS FOR STERILISING MATERIALS OR OBJECTS IN GENERAL; DISINFECTION, STERILISATION OR DEODORISATION OF AIR; CHEMICAL ASPECTS OF BANDAGES, DRESSINGS, ABSORBENT PADS OR SURGICAL ARTICLES; MATERIALS FOR BANDAGES, DRESSINGS, ABSORBENT PADS OR SURGICAL ARTICLES', 'symbol': 'A61L', 'level': '5.0'}, {'titleFull': 'VEHICLES, VEHICLE FITTINGS, OR VEHICLE PARTS, NOT OTHERWISE PROVIDED FOR', 'symbol': 'B60R', 'level': '5.0'}, {'titleFull': 'CONJOINT CONTROL OF VEHICLE SUB-UNITS OF DIFFERENT TYPE OR DIFFERENT FUNCTION; CONTROL SYSTEMS SPECIALLY ADAPTED FOR HYBRID VEHICLES; ROAD VEHICLE DRIVE CONTROL SYSTEMS FOR PURPOSES NOT RELATED TO THE CONTROL OF A PARTICULAR SUB-UNIT', 'symbol': 'B60W', 'level': '5.0'}, {'titleFull': 'SEATS SPECIALLY ADAPTED FOR VEHICLES; VEHICLE PASSENGER ACCOMMODATION NOT OTHERWISE PROVIDED FOR', 'symbol': 'B60N', 'level': '5.0'}, {'titleFull': 'ARRANGEMENT OR MOUNTING OF PROPULSION UNITS OR OF TRANSMISSIONS IN VEHICLES; ARRANGEMENT OR MOUNTING OF PLURAL DIVERSE PRIME-MOVERS IN VEHICLES; AUXILIARY DRIVES FOR VEHICLES; INSTRUMENTATION OR DASHBOARDS FOR VEHICLES; ARRANGEMENTS IN CONNECTION WITH COOLING, AIR INTAKE, GAS EXHAUST OR FUEL SUPPLY OF PROPULSION UNITS IN VEHICLES', 'symbol': 'B60K', 'level': '5.0'}, {'titleFull': 'EQUIPMENT FOR FITTING IN OR TO AIRCRAFT; FLIGHT SUITS; PARACHUTES; ARRANGEMENT OR MOUNTING OF POWER\xa0PLANTS\xa0OR PROPULSION TRANSMISSIONS IN AIRCRAFT', 'symbol': 'B64D', 'level': '5.0'}, {'titleFull': 'DREDGING; SOIL-SHIFTING', 'symbol': 'E02F', 'level': '5.0'}, {'titleFull': 'INDEXING SCHEME FOR ASPECTS RELATING TO NON-POSITIVE-DISPLACEMENT MACHINES OR ENGINES, GAS-TURBINES OR JET-PROPULSION PLANTS', 'symbol': 'F05D', 'level': '5.0'}, {'titleFull': 'VALVES; TAPS; COCKS; ACTUATING-FLOATS; DEVICES FOR VENTING OR AERATING', 'symbol': 'F16K', 'level': '5.0'}, {'titleFull': 'SHAFTS; FLEXIBLE SHAFTS; ELEMENTS OR CRANKSHAFT MECHANISMS; ROTARY BODIES OTHER THAN GEARING ELEMENTS; BEARINGS', 'symbol': 'F16C', 'level': '5.0'}, {'titleFull': 'SPRINGS; SHOCK-ABSORBERS; MEANS FOR DAMPING VIBRATION', 'symbol': 'F16F', 'level': '5.0'}, {'titleFull': 'VESSELS FOR CONTAINING OR STORING COMPRESSED, LIQUEFIED OR SOLIDIFIED GASES; FIXED-CAPACITY GAS-HOLDERS; FILLING VESSELS WITH, OR DISCHARGING FROM VESSELS, COMPRESSED, LIQUEFIED, OR SOLIDIFIED GASES', 'symbol': 'F17C', 'level': '5.0'}, {'titleFull': 'TESTING STATIC OR DYNAMIC BALANCE OF MACHINES OR STRUCTURES; TESTING OF STRUCTURES OR APPARATUS, NOT OTHERWISE PROVIDED FOR', 'symbol': 'G01M', 'level': '5.0'}, {'titleFull': 'INVESTIGATING OR ANALYSING MATERIALS BY DETERMINING THEIR CHEMICAL OR PHYSICAL PROPERTIES', 'symbol': 'G01N', 'level': '5.0'}, {'titleFull': 'TRANSMISSION OF DIGITAL INFORMATION, e.g. TELEGRAPHIC COMMUNICATION', 'symbol': 'H04L', 'level': '5.0'}, {'titleFull': 'OPTICAL ELEMENTS, SYSTEMS OR APPARATUS', 'symbol': 'G02B', 'level': '5.0'}, {'titleFull': 'SYSTEMS FOR CONTROLLING OR REGULATING NON-ELECTRIC VARIABLES', 'symbol': 'G05D', 'level': '5.0'}, {'titleFull': 'ELECTRICALLY-CONDUCTIVE CONNECTIONS; STRUCTURAL ASSOCIATIONS OF A PLURALITY OF MUTUALLY-INSULATED ELECTRICAL CONNECTING ELEMENTS; COUPLING DEVICES; CURRENT COLLECTORS', 'symbol': 'H01R', 'level': '5.0'}, {'titleFull': 'AUTOMATIC CONTROL, STARTING, SYNCHRONISATION OR STABILISATION OF GENERATORS OF ELECTRONIC OSCILLATIONS OR PULSES', 'symbol': 'H03L', 'level': '5.0'}, {'titleFull': 'CIRCUIT ARRANGEMENTS OR SYSTEMS FOR SUPPLYING OR DISTRIBUTING ELECTRIC POWER; SYSTEMS FOR STORING ELECTRIC ENERGY', 'symbol': 'H02J', 'level': '5.0'}, {'titleFull': 'SOLDERING OR UNSOLDERING; WELDING; CLADDING OR PLATING BY SOLDERING OR WELDING; CUTTING BY APPLYING HEAT LOCALLY, e.g. FLAME CUTTING; WORKING BY LASER BEAM', 'symbol': 'B23K', 'level': '5.0'}, {'titleFull': 'PRINTING MACHINES OR PRESSES', 'symbol': 'B41F', 'level': '5.0'}, {'titleFull': 'NON-POSITIVE DISPLACEMENT MACHINES OR ENGINES, e.g. STEAM TURBINES', 'symbol': 'F01D', 'level': '5.0'}, {'titleFull': 'SUPPLYING COMBUSTION ENGINES IN GENERAL WITH COMBUSTIBLE MIXTURES OR CONSTITUENTS THEREOF', 'symbol': 'F02M', 'level': '5.0'}, {'titleFull': 'STARTING OF COMBUSTION ENGINES; STARTING AIDS FOR SUCH ENGINES, NOT OTHERWISE PROVIDED FOR', 'symbol': 'F02N', 'level': '5.0'}, {'titleFull': 'POSITIVE-DISPLACEMENT MACHINES FOR LIQUIDS; PUMPS', 'symbol': 'F04B', 'level': '5.0'}, {'titleFull': 'NON-POSITIVE-DISPLACEMENT PUMPS', 'symbol': 'F04D', 'level': '5.0'}, {'titleFull': 'ARMOUR; ARMOURED TURRETS; ARMOURED OR ARMED VEHICLES; MEANS OF ATTACK OR DEFENCE, e.g. CAMOUFLAGE, IN GENERAL', 'symbol': 'F41H', 'level': '5.0'}, {'titleFull': 'EXPLOSIVE CHARGES, e.g. FOR BLASTING, FIREWORKS, AMMUNITION', 'symbol': 'F42B', 'level': '5.0'}, {'titleFull': 'MEASURING NOT SPECIALLY ADAPTED FOR A SPECIFIC VARIABLE; ARRANGEMENTS FOR MEASURING TWO OR MORE VARIABLES NOT COVERED IN A SINGLE OTHER SUBCLASS; TARIFF METERING APPARATUS; MEASURING OR TESTING NOT OTHERWISE PROVIDED FOR', 'symbol': 'G01D', 'level': '5.0'}, {'titleFull': 'SIGNALLING OR CALLING SYSTEMS; ORDER TELEGRAPHS; ALARM SYSTEMS', 'symbol': 'G08B', 'level': '5.0'}, {'titleFull': 'CLIMATE CHANGE MITIGATION TECHNOLOGIES RELATED TO TRANSPORTATION', 'symbol': 'Y02T', 'level': '5.0'}, {'titleFull': 'WIRELESS COMMUNICATION NETWORKS', 'symbol': 'H04W', 'level': '5.0'}, {'titleFull': 'CLIMATE CHANGE MITIGATION TECHNOLOGIES IN INFORMATION AND COMMUNICATION TECHNOLOGIES [ICT], I.E. INFORMATION AND COMMUNICATION TECHNOLOGIES AIMING AT THE REDUCTION OF THEIR OWN ENERGY USE', 'symbol': 'Y02D', 'level': '5.0'}]}

exec(code, env_args)
