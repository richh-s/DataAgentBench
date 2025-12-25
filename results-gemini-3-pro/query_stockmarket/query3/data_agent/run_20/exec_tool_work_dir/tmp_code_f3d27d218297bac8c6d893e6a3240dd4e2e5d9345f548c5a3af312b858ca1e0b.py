code = """import json

# Load the result of query_db (symbols)
symbols_data = locals()['var_function-call-12950663281948337446']
# symbols_data is a list of dicts: [{"Symbol": "...", "Company Description": "..."}, ...]

# Load the result of list_db (tables)
tables_file = locals()['var_function-call-15486944145380244518']
with open(tables_file, 'r') as f:
    tables_list = json.load(f)

# Filter symbols
valid_symbols = []
symbol_map = {} # Map symbol to description
for item in symbols_data:
    sym = item['Symbol']
    if sym in tables_list:
        valid_symbols.append(sym)
        symbol_map[sym] = item['Company Description']

# Construct the UNION query
# Use "Volume" column. Check date format. Assuming 'YYYY-MM-DD'.
# Query: SELECT '<sym>' as Symbol, AVG(Volume) as AvgVolume FROM <sym> WHERE Date LIKE '2008-%'
# And verify if any rows exist.
# DuckDB SQL construction:
queries = []
for sym in valid_symbols:
    # We want AVG(Volume) where year is 2008.
    # We also need to ensure there is "trading volume", i.e. not all zero? 
    # The prompt says "have trading volume in 2008".
    # I'll just get the AVG. If it's NULL, it means no records.
    # If it's 0, it means volume was 0.
    q = f"SELECT '{sym}' as Symbol, AVG(Volume) as AvgVolume FROM \"{sym}\" WHERE Date LIKE '2008-%'"
    queries.append(q)

if queries:
    final_query = " UNION ALL ".join(queries)
else:
    final_query = "SELECT NULL as Symbol, NULL as AvgVolume WHERE 1=0"

print("__RESULT__:")
print(json.dumps({"query": final_query, "symbol_map": symbol_map}))"""

env_args = {'var_function-call-15362751375383500860': [{'Financial Status': 'None'}, {'Financial Status': 'N'}, {'Financial Status': 'D'}, {'Financial Status': 'H'}], 'var_function-call-15040188796128934882': [{'Listing Exchange': 'P', 'Market Category': 'Not applicable or not NASDAQ-listed'}, {'Listing Exchange': 'Q', 'Market Category': 'G'}, {'Listing Exchange': 'Q', 'Market Category': 'Q'}, {'Listing Exchange': 'Z', 'Market Category': 'Not applicable or not NASDAQ-listed'}, {'Listing Exchange': 'A', 'Market Category': 'Not applicable or not NASDAQ-listed'}, {'Listing Exchange': 'N', 'Market Category': 'Not applicable or not NASDAQ-listed'}, {'Listing Exchange': 'Q', 'Market Category': 'S'}], 'var_function-call-12950663281948337446': [{'Symbol': 'AGMH', 'Company Description': 'AGM Group Holdings Inc. specializes in providing financial technology solutions and services, focusing on enhancing efficiency and performance for businesses in the financial sector.'}, {'Symbol': 'AMTX', 'Company Description': 'Aemetis, Inc is an advanced renewable fuels and biochemicals company, focused on producing sustainable energy solutions and reducing carbon emissions through innovative technologies.'}, {'Symbol': 'APEX', 'Company Description': 'Apex Global Brands Inc. specializes in creating and marketing a diverse portfolio of fashion and lifestyle brands, connecting consumers with trendy and innovative products worldwide.'}, {'Symbol': 'BIOC', 'Company Description': 'Biocept, Inc. specializes in developing advanced diagnostic solutions that help detect and analyze cancer cells, driving innovation in personalized medicine and cancer treatment.'}, {'Symbol': 'BKYI', 'Company Description': 'BIO-key International, Inc. specializes in advanced biometric solutions, providing secure and convenient identity verification systems for enterprises and consumers alike.'}, {'Symbol': 'CBAT', 'Company Description': 'CBAK Energy Technology, Inc. specializes in developing and manufacturing high-performance lithium-ion batteries, playing a pivotal role in powering electric vehicles and renewable energy solutions.'}, {'Symbol': 'CCCL', 'Company Description': 'China Ceramics Co., Ltd. specializes in manufacturing high-quality ceramic tiles, catering to both residential and commercial markets with a wide range of designs and finishes.'}, {'Symbol': 'CORV', 'Company Description': 'Correvio Pharma Corp., based in Canada, specializes in developing and commercializing innovative cardiovascular therapies to improve patient outcomes.'}, {'Symbol': 'CPAH', 'Company Description': 'CounterPath Corporation specializes in developing software solutions that enhance communication by providing seamless VoIP and unified communications applications for businesses and individuals.'}, {'Symbol': 'DZSI', 'Company Description': 'DASAN Zhone Solutions, Inc. specializes in providing advanced broadband access solutions, empowering telecommunications networks to deliver faster and more reliable internet services worldwide.'}, {'Symbol': 'FAMI', 'Company Description': 'Farmmi, Inc. specializes in the cultivation and distribution of high-quality agricultural products, with a focus on mushrooms and other nutritious foods.'}, {'Symbol': 'FTFT', 'Company Description': 'Future FinTech Group Inc. specializes in the development and marketing of blockchain-based products and financial technology solutions, aiming to revolutionize the digital economy with innovative applications.'}, {'Symbol': 'FTR', 'Company Description': 'Frontier Communications Corporation provides telecommunications services, including internet, phone, and television solutions, to residential and business customers across the United States.'}, {'Symbol': 'IDEX', 'Company Description': 'Ideanomics, Inc. is at the forefront of transforming the commercial electric vehicle industry, providing comprehensive solutions that drive innovation and sustainability in transportation and energy.'}, {'Symbol': 'ISDS', 'Company Description': 'Invesco RAFI Strategic Developed ex-US Small Company ETF offers investors a unique opportunity to access a portfolio of small-cap stocks from developed markets outside the United States, focusing on strategic financial growth and diversification.'}, {'Symbol': 'MCEP', 'Company Description': 'Mid-Con Energy Partners, LP specializes in the exploration and production of oil and natural gas, focusing on maximizing energy resources across the United States.'}, {'Symbol': 'NXTD', 'Company Description': 'NXT-ID Inc. specializes in developing innovative technology solutions that enhance security and convenience in the fields of healthcare and electronic payments.'}, {'Symbol': 'OPTT', 'Company Description': 'Ocean Power Technologies, Inc. harnesses the power of the ocean to develop innovative renewable energy solutions, specializing in wave energy technology.'}, {'Symbol': 'PEIX', 'Company Description': 'Pacific Ethanol, Inc. specializes in producing renewable fuels and high-quality alcohol products, contributing to sustainable energy solutions and cleaner alternatives for the transportation sector.'}, {'Symbol': 'RBZ', 'Company Description': 'Reebonz Holding Limited is an online luxury marketplace that specializes in offering a curated selection of high-end fashion items and accessories to discerning shoppers worldwide.'}, {'Symbol': 'SES', 'Company Description': 'Synthesis Energy Systems, Inc. specializes in transforming low-cost carbon resources into clean energy and valuable chemical products, driving innovation in sustainable energy solutions.'}, {'Symbol': 'SNSS', 'Company Description': 'Sunesis Pharmaceuticals, Inc. is dedicated to developing innovative cancer therapies, striving to advance treatments that target the underlying mechanisms of the disease.'}, {'Symbol': 'SPI', 'Company Description': 'SPI Energy Co., Ltd. specializes in providing renewable energy solutions, focusing on solar power products and services to drive sustainable energy initiatives globally.'}, {'Symbol': 'SYPR', 'Company Description': 'Sypris Solutions, Inc. specializes in providing engineering and manufacturing services for the aerospace and defense sectors, ensuring high-quality solutions for complex technological challenges.'}, {'Symbol': 'VTIQW', 'Company Description': 'VectoIQ Acquisition Corp. is an investment company specializing in identifying and merging with innovative technology and automotive firms to drive growth and transformation in the mobility sector.'}], 'var_function-call-15486944145380244518': 'file_storage/function-call-15486944145380244518.json'}

exec(code, env_args)
