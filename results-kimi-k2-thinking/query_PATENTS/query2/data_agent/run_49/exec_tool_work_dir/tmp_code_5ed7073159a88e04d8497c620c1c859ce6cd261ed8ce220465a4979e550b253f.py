code = """import json
import re

file_path = locals()['var_functions.query_db:28']
with open(file_path, 'r') as f:
    german_patents_all_years = json.load(f)

def get_cpc_level4(cpc_code):
    if not cpc_code:
        return None
    cpc_code = cpc_code.strip()
    match = re.match(r'^([A-Z][0-9]{2}[A-Z][0-9]{1,3})', cpc_code)
    if match:
        return match.group(1)
    if '/' in cpc_code:
        parts = cpc_code.split('/')
        main_part = parts[0]
        if len(main_part) >= 4:
            return main_part
    return cpc_code[:5] if len(cpc_code) >= 5 else None

month_map = {
    'jan': 1, 'feb': 2, 'mar': 3, 'apr': 4, 'may': 5, 'jun': 6,
    'jul': 7, 'aug': 8, 'sep': 9, 'oct': 10, 'nov': 11, 'dec': 12
}

patents_by_year = {}
cpc_to_full_titles = {}

for patent in german_patents_all_years:
    patents_info = patent.get('Patents_info', '')
    grant_date = patent.get('grant_date', '')
    cpc = patent.get('cpc', '[]')
    title_localized = patent.get('title_localized', '[]')
    
    if not grant_date or grant_date.strip() == '':
        continue
    
    year_match = re.search(r'(20\d{2})', grant_date)
    if not year_match:
        continue
    
    year = int(year_match.group(1))
    
    month = None
    grant_date_lower = grant_date.lower()
    for month_name, month_num in month_map.items():
        if month_name in grant_date_lower:
            month = month_num
            break
    
    if not month:
        continue
    
    try:
        title_list = json.loads(title_localized) if isinstance(title_localized, str) else title_localized
        title = ''
        if title_list and len(title_list) > 0:
            for lang_pref in ['de', 'en']:
                for t in title_list:
                    if t.get('language') == lang_pref and t.get('text'):
                        title = t.get('text')
                        break
                if title:
                    break
            if not title and title_list[0].get('text'):
                title = title_list[0].get('text')
    except:
        title = ''
    
    try:
        cpc_list = json.loads(cpc) if isinstance(cpc, str) else cpc
        if not isinstance(cpc_list, list):
            cpc_list = []
    except:
        cpc_list = []
    
    cpc_codes = [item.get('code') for item in cpc_list if isinstance(item, dict) and item.get('code')]
    
    if not cpc_codes:
        continue
    
    if year == 2019 and month >= 7:
        if year not in patents_by_year:
            patents_by_year[year] = {}
        
        for cpc_code in cpc_codes:
            level4_code = get_cpc_level4(cpc_code)
            if level4_code:
                if level4_code not in patents_by_year[year]:
                    patents_by_year[year][level4_code] = 0
                patents_by_year[year][level4_code] += 1
                
                if level4_code not in cpc_to_full_titles and title:
                    cpc_to_full_titles[level4_code] = title

available_years = sorted(list(patents_by_year.keys()))
total_cpc_groups = sum(len(cpc_counts) for cpc_counts in patents_by_year.values())

result = {
    'available_years': available_years,
    'total_cpc_groups': total_cpc_groups,
    'patents_2019_h2': patents_by_year.get(2019, {}),
    'cpc_groups_2019': len(patents_by_year.get(2019, {})),
    'sample_titles': {k: cpc_to_full_titles.get(k, '') for k in list(cpc_to_full_titles.keys())[:5]}
}

print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.list_db:0': ['publicationinfo'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json', 'var_functions.execute_python:8': {'total_german_patents': 1, 'sample_patents': [{'patents_info': 'In DE, the application (number DE-102007032978-A) is held by HEIDELBERGER DRUCKMASCH AG and has publication number DE-102007032978-B4.', 'grant_date': 'dated 21st November 2019', 'grant_month': 11, 'cpc_codes': ['B41F21/102', 'B41F22/00', 'B41F21/00']}]}, 'var_functions.query_db:10': 'file_storage/functions.query_db:10.json', 'var_functions.query_db:12': 'file_storage/functions.query_db:12.json', 'var_functions.execute_python:14': {'total_german_patents_h2_2019': 34, 'sample_patents': [{'patents_info': 'In DE, the application (number DE-102007032978-A) is held by HEIDELBERGER DRUCKMASCH AG and has publication number DE-102007032978-B4.', 'grant_date': 'dated 21st November 2019', 'grant_month': 11, 'cpc_codes': ['B41F21/102', 'B41F22/00', 'B41F21/00'], 'title': 'Trommel zum Fördern eines Bogens', 'publication_date': '21st November 2019'}, {'patents_info': 'The DE patent application (no. DE-102010042467-A) is owned by CONTINENTAL AUTOMOTIVE GMBH and has pub. number DE-102010042467-B4.', 'grant_date': '5th of December, 2019', 'grant_month': 12, 'cpc_codes': ['F02D41/3005', 'F02D41/20', 'F02M65/005', 'F02D41/00', 'F02D41/20', 'F02D41/20'], 'title': 'Ermittlung des Öffnungszeitpunkts eines Steuerventils eines indirekt angetriebenen Kraftstoffinjektors', 'publication_date': 'December the 5th, 2019'}, {'patents_info': 'In DE, the patent filing (application no. DE-112014003420-T) is assigned to TOYOTA MOTOR CO LTD and has publication number DE-112014003420-B4.', 'grant_date': '22nd of August, 2019', 'grant_month': 8, 'cpc_codes': ['F02M59/102', 'F02M55/04', 'F02M55/04', 'F02M59/102', 'F02M59/44', 'F02M59/06', 'F04B53/001', 'F02M59/368', 'F04B53/001', 'F02M59/44', 'F02M59/368', 'F02M59/06'], 'title': 'Pulsationsdämpfer und Hochdruckkraftstoffpumpe', 'publication_date': 'on August 22nd, 2019'}]}, 'var_functions.query_db:18': [{'symbol': 'B04', 'titleFull': 'CENTRIFUGAL APPARATUS OR MACHINES FOR CARRYING-OUT PHYSICAL OR CHEMICAL PROCESSES', 'level': '4.0'}, {'symbol': 'B23', 'titleFull': 'MACHINE TOOLS; METAL-WORKING NOT OTHERWISE PROVIDED FOR', 'level': '4.0'}, {'symbol': 'B30', 'titleFull': 'PRESSES', 'level': '4.0'}, {'symbol': 'B21', 'titleFull': 'MECHANICAL METAL-WORKING WITHOUT ESSENTIALLY REMOVING MATERIAL; PUNCHING METAL', 'level': '4.0'}, {'symbol': 'B25', 'titleFull': 'HAND TOOLS; PORTABLE POWER-DRIVEN TOOLS; MANIPULATORS', 'level': '4.0'}, {'symbol': 'B99', 'titleFull': 'SUBJECT MATTER NOT OTHERWISE PROVIDED FOR IN THIS SECTION', 'level': '4.0'}, {'symbol': 'B29', 'titleFull': 'WORKING OF PLASTICS; WORKING OF SUBSTANCES IN A PLASTIC STATE IN GENERAL', 'level': '4.0'}, {'symbol': 'B33', 'titleFull': 'ADDITIVE MANUFACTURING TECHNOLOGY', 'level': '4.0'}, {'symbol': 'C22', 'titleFull': 'METALLURGY; FERROUS OR NON-FERROUS ALLOYS; TREATMENT OF ALLOYS OR NON-FERROUS METALS', 'level': '4.0'}, {'symbol': 'D99', 'titleFull': 'SUBJECT MATTER NOT OTHERWISE PROVIDED FOR IN THIS SECTION', 'level': '4.0'}], 'var_functions.execute_python:22': {'total_german_patents_all': 68, 'german_patents_h2_2019': 34, 'years_available': [2019], 'sample_patents': [{'patents_info': 'In DE, the application (number DE-102007032978-A) is held by HEIDELBERGER DRUCKMASCH AG and has publication number DE-102007032978-B4.', 'grant_date': 'dated 21st November 2019', 'grant_month': 11, 'grant_year': 2019, 'cpc_codes': ['B41F21/102', 'B41F22/00', 'B41F21/00'], 'title': 'Trommel zum Fördern eines Bogens'}, {'patents_info': 'The DE patent application (no. DE-102010042467-A) is owned by CONTINENTAL AUTOMOTIVE GMBH and has pub. number DE-102010042467-B4.', 'grant_date': '5th of December, 2019', 'grant_month': 12, 'grant_year': 2019, 'cpc_codes': ['F02D41/3005', 'F02D41/20', 'F02M65/005', 'F02D41/00', 'F02D41/20', 'F02D41/20'], 'title': 'Ermittlung des Öffnungszeitpunkts eines Steuerventils eines indirekt angetriebenen Kraftstoffinjektors'}, {'patents_info': 'In DE, the patent filing (application no. DE-112014003420-T) is assigned to TOYOTA MOTOR CO LTD and has publication number DE-112014003420-B4.', 'grant_date': '22nd of August, 2019', 'grant_month': 8, 'grant_year': 2019, 'cpc_codes': ['F02M59/102', 'F02M55/04', 'F02M55/04', 'F02M59/102', 'F02M59/44', 'F02M59/06', 'F04B53/001', 'F02M59/368', 'F04B53/001', 'F02M59/44', 'F02M59/368', 'F02M59/06'], 'title': 'Pulsationsdämpfer und Hochdruckkraftstoffpumpe'}]}, 'var_functions.query_db:24': 'file_storage/functions.query_db:24.json', 'var_functions.execute_python:26': {'total_cpc_groups': 114, 'top_cpc_groups': [['C04B223', 32], ['H04W52', 12], ['C04B35', 12], ['B29C204', 11], ['H04L1', 10], ['H01J49', 10], ['F02D41', 9], ['H04W72', 9], ['F02M59', 8], ['A61F5', 6], ['H03L7', 6], ['B29C49', 5], ['G02B15', 5], ['G02B23', 5], ['H04L5', 4]], 'cpc_to_titles': {'B41F21': 'Trommel zum Fördern eines Bogens', 'B41F22': 'Trommel zum Fördern eines Bogens', 'F02D41': 'Ermittlung des Öffnungszeitpunkts eines Steuerventils eines indirekt angetriebenen Kraftstoffinjektors', 'F02M65': 'Ermittlung des Öffnungszeitpunkts eines Steuerventils eines indirekt angetriebenen Kraftstoffinjektors', 'F02M59': 'Pulsationsdämpfer und Hochdruckkraftstoffpumpe', 'F02M55': 'Pulsationsdämpfer und Hochdruckkraftstoffpumpe', 'F04B53': 'Pulsationsdämpfer und Hochdruckkraftstoffpumpe', 'G01D11': 'Verfahren zur Herstellung eines Bauteiles, Bauteil und Drucksensor', 'B23K1': 'Verfahren zur Herstellung eines Bauteiles, Bauteil und Drucksensor', 'B63B21': 'Wasserkraftwerk', 'H04W72': 'Sub-Frame-Zuteilung für energieeffiziente LTE', 'H04L5': 'Sub-Frame-Zuteilung für energieeffiziente LTE', 'H04L1': 'Sub-Frame-Zuteilung für energieeffiziente LTE', 'H04W52': 'Sub-Frame-Zuteilung für energieeffiziente LTE', 'H04W76': 'Sub-Frame-Zuteilung für energieeffiziente LTE', 'Y02D30': 'Sub-Frame-Zuteilung für energieeffiziente LTE', 'B66C23': 'Landfahrzeug mit einem Chassis und einer Mehrzahl von daran angebrachten Eckstützeinheiten', 'E02F9': 'Landfahrzeug mit einem Chassis und einer Mehrzahl von daran angebrachten Eckstützeinheiten', 'B60S9': 'Landfahrzeug mit einem Chassis und einer Mehrzahl von daran angebrachten Eckstützeinheiten', 'F02D15': 'Verfahren zum Betreiben einer Verbrennungskraftmaschine eines Kraftfahrzeugs sowie Verbrennungskraftmaschine', 'F02D13': 'Verfahren zum Betreiben einer Verbrennungskraftmaschine eines Kraftfahrzeugs sowie Verbrennungskraftmaschine', 'Y02T10': 'Verfahren zum Betreiben einer Verbrennungskraftmaschine eines Kraftfahrzeugs sowie Verbrennungskraftmaschine', 'F16C33': 'Getriebevorrichtung der oszillierend innen eingreifenden Bauart', 'A47J37': 'Mobiles Backbrett', 'A21C9': 'Mobiles Backbrett', 'A61F5': 'Fußplatte und Orthese', 'A43B17': 'Fußplatte und Orthese', 'A43B7': 'Fußplatte und Orthese', 'A43B13': 'Fußplatte und Orthese', 'F24B5': 'Verfahren zum Betrieb einer Brenneinrichtung sowie Brenneinrichtung', 'F23L15': 'Verfahren zum Betrieb einer Brenneinrichtung sowie Brenneinrichtung', 'F23L1': 'Verfahren zum Betrieb einer Brenneinrichtung sowie Brenneinrichtung', 'F23B60': 'Verfahren zum Betrieb einer Brenneinrichtung sowie Brenneinrichtung', 'F23B50': 'Verfahren zum Betrieb einer Brenneinrichtung sowie Brenneinrichtung', 'F23N1': 'Verfahren zum Betrieb einer Brenneinrichtung sowie Brenneinrichtung', 'Y02E20': 'Verfahren zum Betrieb einer Brenneinrichtung sowie Brenneinrichtung', 'H01J49': 'Verfahren zur Ionenherstellung', 'G01M1': 'Verfahren zur Bestimmung einer Unwucht eines wellenelastischen Rotors anhand der Ausbiegung', 'F05D227': 'Verfahren zur Bestimmung einer Unwucht eines wellenelastischen Rotors anhand der Ausbiegung', 'F04D29': 'Verfahren zur Bestimmung einer Unwucht eines wellenelastischen Rotors anhand der Ausbiegung', 'F05D226': 'Verfahren zur Bestimmung einer Unwucht eines wellenelastischen Rotors anhand der Ausbiegung', 'F16F15': 'Verfahren zur Bestimmung einer Unwucht eines wellenelastischen Rotors anhand der Ausbiegung', 'F01D5': 'Verfahren zur Bestimmung einer Unwucht eines wellenelastischen Rotors anhand der Ausbiegung', 'H01R35': 'Steckverbindungsdose und Passagierversorgungsmodul', 'B64D11': 'Steckverbindungsdose und Passagierversorgungsmodul', 'H01R220': 'Steckverbindungsdose und Passagierversorgungsmodul', 'H01R24': 'Steckverbindungsdose und Passagierversorgungsmodul', 'H01R13': 'Steckverbindungsdose und Passagierversorgungsmodul', 'B60R16': 'Steckverbindungsdose und Passagierversorgungsmodul', 'H01L23': 'Leistungshalbleitermodul', 'H01L292': 'Leistungshalbleitermodul', 'H01L25': 'Leistungshalbleitermodul', 'B62D25': 'Struktureinrichtung für ein Fahrzeug', 'B62D21': 'Struktureinrichtung für ein Fahrzeug', 'F02N220': 'Verfahren und System zum Anlassen eines Verbrennungsmotors eines Kraftwagens', 'F02N230': 'Verfahren und System zum Anlassen eines Verbrennungsmotors eines Kraftwagens', 'F02N11': 'Verfahren und System zum Anlassen eines Verbrennungsmotors eines Kraftwagens', 'B60K6': 'Verfahren und System zum Anlassen eines Verbrennungsmotors eines Kraftwagens', 'B60W30': 'Verfahren und System zum Anlassen eines Verbrennungsmotors eines Kraftwagens', 'C04B223': 'Verfahren zur Herstellung von Gadoliniumoxysulfid (Gd2O2S) - Szintillationskeramiken', 'C04B35': 'Verfahren zur Herstellung von Gadoliniumoxysulfid (Gd2O2S) - Szintillationskeramiken', 'C09K11': 'Verfahren zur Herstellung von Gadoliniumoxysulfid (Gd2O2S) - Szintillationskeramiken', 'C04B40': 'Verfahren zur Herstellung von Gadoliniumoxysulfid (Gd2O2S) - Szintillationskeramiken', 'B29C49': 'Blasvorrichtung zum Expandieren von Behältnissen', 'B29C204': 'Blasvorrichtung zum Expandieren von Behältnissen', 'B29C294': 'Blasvorrichtung zum Expandieren von Behältnissen', 'A61B209': 'Medizinische Einrichtung und Verfahren zur Überwachung der Reinigung von dessen Oberfläche', 'G01N27': 'Medizinische Einrichtung und Verfahren zur Überwachung der Reinigung von dessen Oberfläche', 'A61L2': 'Medizinische Einrichtung und Verfahren zur Überwachung der Reinigung von dessen Oberfläche', 'A61B90': 'Medizinische Einrichtung und Verfahren zur Überwachung der Reinigung von dessen Oberfläche', 'G01N202': 'Bandpassfilter für Licht mit variabler unterer und oberer Grenzwellenlänge', 'G02B5': 'Bandpassfilter für Licht mit variabler unterer und oberer Grenzwellenlänge', 'G02B21': 'Bandpassfilter für Licht mit variabler unterer und oberer Grenzwellenlänge', 'G02B26': 'Bandpassfilter für Licht mit variabler unterer und oberer Grenzwellenlänge', 'H01F27': 'Zündspuleneinrichtung für Verbrennungskraftmaschine', 'F02P15': 'Zündspuleneinrichtung für Verbrennungskraftmaschine', 'H01F38': 'Zündspuleneinrichtung für Verbrennungskraftmaschine', 'F02P3': 'Zündspuleneinrichtung für Verbrennungskraftmaschine', 'G02B15': 'Endoskop-Vergrößerungsoptik und Endoskop', 'A61B1': 'Endoskop-Vergrößerungsoptik und Endoskop', 'G02B13': 'Endoskop-Vergrößerungsoptik und Endoskop', 'G02B23': 'Endoskop-Vergrößerungsoptik und Endoskop', 'Y10T70': 'Elektronischer Schlüssel für ein Fahrzeug', 'G07C9': 'Elektronischer Schlüssel für ein Fahrzeug', 'B29D99': 'Elektronischer Schlüssel für ein Fahrzeug', 'H01H9': 'Elektronischer Schlüssel für ein Fahrzeug', 'B29C45': 'Elektronischer Schlüssel für ein Fahrzeug', 'H01H200': 'Elektronischer Schlüssel für ein Fahrzeug', 'E05B19': 'Elektronischer Schlüssel für ein Fahrzeug', 'F02D35': 'Verfahren zur Überwachung eines Zylinderdrucksensors', 'G01L23': 'Verfahren zur Überwachung eines Zylinderdrucksensors', 'F02D225': 'Verfahren zur Überwachung eines Zylinderdrucksensors', 'G01L27': 'Verfahren zur Überwachung eines Zylinderdrucksensors', 'F02D220': 'Verfahren zur Überwachung eines Zylinderdrucksensors', 'G01F23': 'Widerstandsplatte und mit der Widerstandsplatte versehene Flüssigkeitspegel-Detektionsvorrichtung', 'F16H37': 'Getriebeanordnung', 'F16H220': 'Getriebeanordnung', 'F16H3': 'Getriebeanordnung', 'B60K23': 'Hilfsantriebsradseitige zuschaltbare Differentialeinheit für ein Fahrzeug mit Vierradantrieb', 'B60K17': 'Hilfsantriebsradseitige zuschaltbare Differentialeinheit für ein Fahrzeug mit Vierradantrieb', 'F16D202': 'Hilfsantriebsradseitige zuschaltbare Differentialeinheit für ein Fahrzeug mit Vierradantrieb', 'F16D201': 'Hilfsantriebsradseitige zuschaltbare Differentialeinheit für ein Fahrzeug mit Vierradantrieb', 'F16D27': 'Hilfsantriebsradseitige zuschaltbare Differentialeinheit für ein Fahrzeug mit Vierradantrieb', 'H02J1': 'Tragbare Fernbedienungsvorrichtung', 'H02J7': 'Tragbare Fernbedienungsvorrichtung', 'H04L7': 'Phasendetektor', 'H03L7': 'Phasendetektor', 'B60N220': 'Kraftfahrzeugsitz', 'B60N2': 'Kraftfahrzeugsitz', 'E02F3': 'Vorrichtung und Verfahren zum Koppeln von einem Anbaugerät an einem Fahrzeug', 'F42B3': 'Vorrichtung und Verfahren zum Koppeln von einem Anbaugerät an einem Fahrzeug', 'F41H11': 'Vorrichtung und Verfahren zum Koppeln von einem Anbaugerät an einem Fahrzeug', 'G08B19': 'Leuchtenbaldachin zum Detektieren und Signalisieren unterschiedlicher Gefahrensituationen', 'G08B17': 'Leuchtenbaldachin zum Detektieren und Signalisieren unterschiedlicher Gefahrensituationen'}}, 'var_functions.query_db:28': 'file_storage/functions.query_db:28.json'}

exec(code, env_args)
