code = """import json

# Get the list of symbols from the previous result
result_json = locals()['var_function-call-2990735679210955960']
data = json.loads(result_json)
symbols = data['all_symbols']

# Construct the query
subqueries = []
for sym in symbols:
    # Use simple string concatenation to avoid indentation issues in multi-line strings
    query_part = "SELECT '" + sym + "' as Symbol, " + \
                 "SUM(CASE WHEN Close > Open THEN 1 ELSE 0 END) as UpDays, " + \
                 "SUM(CASE WHEN Close < Open THEN 1 ELSE 0 END) as DownDays " + \
                 "FROM \"" + sym + "\" " + \
                 "WHERE Date >= '2017-01-01' AND Date <= '2017-12-31'"
    subqueries.append(query_part)

full_query = " UNION ALL ".join(subqueries)
final_query = "SELECT Symbol, UpDays, DownDays, (UpDays - DownDays) as NetUp " + \
              "FROM (" + full_query + ") " + \
              "WHERE UpDays > DownDays " + \
              "ORDER BY UpDays DESC " + \
              "LIMIT 5"

print("__RESULT__:")
print(json.dumps(final_query))"""

env_args = {'var_function-call-9844452746948468047': [{'ETF': 'Y'}, {'ETF': 'N'}], 'var_function-call-8671132249438032894': 'file_storage/function-call-8671132249438032894.json', 'var_function-call-8671132249438035785': 'file_storage/function-call-8671132249438035785.json', 'var_function-call-2990735679210955960': {'count': 234, 'preview': [{'Symbol': 'AEFC', 'Company Description': 'Aegon Funding Company LLC is part of Aegon N.V., a global financial services group offering life insurance, pensions, and asset management solutions to help people achieve a lifetime of financial security.'}, {'Symbol': 'AIN', 'Company Description': 'Albany International Corporation specializes in producing advanced materials and engineered components, serving industries such as aerospace and paper manufacturing with innovative solutions.'}, {'Symbol': 'AIV', 'Company Description': 'Apartment Investment and Management Company specializes in owning and managing a diverse portfolio of apartment communities, offering quality rental housing across various regions.'}, {'Symbol': 'AIZP', 'Company Description': 'Assurant, Inc. specializes in providing a diverse range of insurance products and services, focusing on lifestyle and housing solutions to protect what matters most to their customers.'}, {'Symbol': 'AJRD', 'Company Description': 'Aerojet Rocketdyne Holdings, Inc. specializes in developing advanced propulsion systems and aerospace technologies, playing a crucial role in powering rockets and missiles for both defense and space exploration.'}, {'Symbol': 'AL', 'Company Description': 'Air Lease Corporation specializes in leasing commercial aircraft to airlines worldwide, providing them with flexible fleet solutions and financial support.'}, {'Symbol': 'AMN', 'Company Description': 'AMN Healthcare Services Inc. specializes in providing workforce solutions and staffing services to healthcare facilities, ensuring they have access to the skilled professionals necessary for quality patient care.'}, {'Symbol': 'AMP', 'Company Description': 'Ameriprise Financial, Inc. offers comprehensive financial services, specializing in wealth management, asset management, and insurance solutions to help clients plan and achieve their financial goals.'}, {'Symbol': 'AMT', 'Company Description': 'American Tower Corporation is a leading real estate investment trust that specializes in owning, operating, and developing wireless and broadcast communication towers across the globe.'}, {'Symbol': 'ARD', 'Company Description': 'Ardagh Group S.A. specializes in manufacturing and supplying sustainable packaging solutions, with a focus on glass and metal containers for leading brands across various industries.'}], 'all_symbols': ['AEFC', 'AIN', 'AIV', 'AIZP', 'AJRD', 'AL', 'AMN', 'AMP', 'AMT', 'ARD', 'ARGD', 'ARLO', 'ASG', 'AVA', 'BANC', 'BBU', 'BBVA', 'BDXA', 'BKH', 'BKT', 'BLD', 'BNS', 'BV', 'BZH', 'CADE', 'CAE', 'CAF', 'CBT', 'CCC', 'CCZ', 'CHAP', 'CIA', 'CMA', 'CMI', 'CMSA', 'CNK', 'COTY', 'CRC', 'CRM', 'CRS', 'CSL', 'CTS', 'CUBE', 'CURO', 'CVIA', 'CVX', 'CXH', 'DAC', 'DDS', 'DDT', 'DEO', 'DGX', 'DMB', 'DTQ', 'DXC', 'EARN', 'EBS', 'EGO', 'EGY', 'EIG', 'ELF', 'EMP', 'ENLC', 'EPR', 'EPRT', 'ES', 'ESRT', 'ESS', 'ETM', 'EV', 'EVT', 'EXP', 'FMN', 'FPAC', 'FSM', 'GCO', 'GD', 'GDL', 'GDV', 'GEL', 'GJP', 'GLOB', 'GLT', 'GOL', 'GSLD', 'GTY', 'GVA', 'GWB', 'H', 'HBI', 'HDB', 'HEP', 'HIL', 'HIO', 'HIX', 'HLF', 'HLT', 'HNI', 'HRB', 'HTFA', 'IBM', 'IGR', 'IHC', 'IPG', 'IRM', 'IT', 'JGH', 'JHY', 'JKS', 'JMP', 'JNPR', 'KMB', 'KNX', 'KW', 'KYN', 'LB', 'LDOS', 'LHC', 'LHX', 'LOMA', 'MANU', 'MDLX', 'MDLY', 'MED', 'MFO', 'MGR', 'MGU', 'MHE', 'MIY', 'MKC', 'MLI', 'MNE', 'MR', 'MS', 'MTD', 'MYD', 'NFH', 'NGG', 'NJV', 'NNI', 'NNY', 'NRUC', 'NUE', 'NXN', 'OCFT', 'OEC', 'ORA', 'ORAN', 'ORCL', 'ORN', 'PAG', 'PBI', 'PFE', 'PFSI', 'PGR', 'PIM', 'PKE', 'PLAN', 'PLNT', 'PMT', 'PNM', 'PPG', 'PRSP', 'PRTY', 'PSV', 'PSXP', 'QTS', 'QUAD', 'RBC', 'RCB', 'RCI', 'RES', 'REXR', 'RH', 'RMT', 'ROG', 'ROL', 'RPAI', 'RPM', 'RQI', 'RWT', 'SAF', 'SAIL', 'SAM', 'SBR', 'SCU', 'SFUN', 'SHAK', 'SI', 'SITC', 'SJM', 'SJT', 'SJW', 'SLF', 'SMP', 'SOL', 'SPOT', 'SRC', 'SRF', 'SRT', 'SSD', 'STG', 'STL', 'STON', 'SYX', 'TBB', 'TCP', 'TDJ', 'TGP', 'TLYS', 'TNC', 'TPH', 'TRV', 'TTI', 'TUFN', 'TWTR', 'UHT', 'UIS', 'USX', 'UTL', 'VET', 'VGR', 'VHI', 'VIV', 'VKQ', 'VRT', 'VVI', 'WOR', 'WPG', 'WSM', 'X', 'YEXT', 'ZNH', 'ZTR']}}

exec(code, env_args)
