code = """import json

# Get the list of tables from the previous tool result
# It's in a file
with open('var_function-call-11740613577733516459.json', 'r') as f:
    tables = json.load(f)

# My symbols
symbols_info = [
    {"Symbol": "AGMH", "Company Description": "AGM Group Holdings Inc. ..."},
    {"Symbol": "AMTX", "Company Description": "Aemetis, Inc ..."},
    {"Symbol": "APEX", "Company Description": "Apex Global Brands Inc. ..."},
    {"Symbol": "BIOC", "Company Description": "Biocept, Inc. ..."},
    {"Symbol": "BKYI", "Company Description": "BIO-key International, Inc. ..."},
    {"Symbol": "CBAT", "Company Description": "CBAK Energy Technology, Inc. ..."},
    {"Symbol": "CCCL", "Company Description": "China Ceramics Co., Ltd. ..."},
    {"Symbol": "CORV", "Company Description": "Correvio Pharma Corp., ..."},
    {"Symbol": "CPAH", "Company Description": "CounterPath Corporation ..."},
    {"Symbol": "DZSI", "Company Description": "DASAN Zhone Solutions, Inc. ..."},
    {"Symbol": "FAMI", "Company Description": "Farmmi, Inc. ..."},
    {"Symbol": "FTFT", "Company Description": "Future FinTech Group Inc. ..."},
    {"Symbol": "FTR", "Company Description": "Frontier Communications Corporation ..."},
    {"Symbol": "IDEX", "Company Description": "Ideanomics, Inc. ..."},
    {"Symbol": "ISDS", "Company Description": "Invesco RAFI Strategic Developed ex-US Small Company ETF ..."},
    {"Symbol": "MCEP", "Company Description": "Mid-Con Energy Partners, LP ..."},
    {"Symbol": "NXTD", "Company Description": "NXT-ID Inc. ..."},
    {"Symbol": "OPTT", "Company Description": "Ocean Power Technologies, Inc. ..."},
    {"Symbol": "PEIX", "Company Description": "Pacific Ethanol, Inc. ..."},
    {"Symbol": "RBZ", "Company Description": "Reebonz Holding Limited ..."},
    {"Symbol": "SES", "Company Description": "Synthesis Energy Systems, Inc. ..."},
    {"Symbol": "SNSS", "Company Description": "Sunesis Pharmaceuticals, Inc. ..."},
    {"Symbol": "SPI", "Company Description": "SPI Energy Co., Ltd. ..."},
    {"Symbol": "SYPR", "Company Description": "Sypris Solutions, Inc. ..."},
    {"Symbol": "VTIQW", "Company Description": "VectoIQ Acquisition Corp. ..."}
]

# Extract symbol names
target_symbols = [s['Symbol'] for s in symbols_info]

# Filter
valid_symbols = [s for s in target_symbols if s in tables]

# Construct query
if not valid_symbols:
    print('__RESULT__:')
    print(json.dumps("NO_VALID_SYMBOLS"))
else:
    parts = []
    for s in valid_symbols:
        # DuckDB: Date is str 'YYYY-MM-DD'. Filter by '2008'.
        # Also need volume > 0 check? "have trading volume in 2008" -> count(Volume) > 0 or similar.
        # But we need to report avg volume. If no volume, avg is null.
        # So we can just select avg. If it's null, we filter it out later.
        parts.append(f"SELECT '{s}' as Symbol, AVG(Volume) as AvgVolume FROM \"{s}\" WHERE Date LIKE '2008%' AND Volume IS NOT NULL")
    
    final_query = " UNION ALL ".join(parts)
    print('__RESULT__:')
    print(json.dumps(final_query))"""

env_args = {'var_function-call-16250764067497076823': ['stockinfo'], 'var_function-call-6963375376971243659': [{'Listing Exchange': 'P', 'Financial Status': 'None', 'Market Category': 'Not applicable or not NASDAQ-listed'}, {'Listing Exchange': 'Q', 'Financial Status': 'N', 'Market Category': 'G'}, {'Listing Exchange': 'Q', 'Financial Status': 'N', 'Market Category': 'Q'}, {'Listing Exchange': 'Z', 'Financial Status': 'None', 'Market Category': 'Not applicable or not NASDAQ-listed'}, {'Listing Exchange': 'A', 'Financial Status': 'None', 'Market Category': 'Not applicable or not NASDAQ-listed'}, {'Listing Exchange': 'N', 'Financial Status': 'None', 'Market Category': 'Not applicable or not NASDAQ-listed'}, {'Listing Exchange': 'Q', 'Financial Status': 'D', 'Market Category': 'S'}, {'Listing Exchange': 'Q', 'Financial Status': 'N', 'Market Category': 'S'}, {'Listing Exchange': 'Q', 'Financial Status': 'D', 'Market Category': 'G'}, {'Listing Exchange': 'Q', 'Financial Status': 'D', 'Market Category': 'Q'}, {'Listing Exchange': 'Q', 'Financial Status': 'H', 'Market Category': 'S'}], 'var_function-call-8058022467157903308': [{'Symbol': 'AGMH', 'Company Description': 'AGM Group Holdings Inc. specializes in providing financial technology solutions and services, focusing on enhancing efficiency and performance for businesses in the financial sector.'}, {'Symbol': 'AMTX', 'Company Description': 'Aemetis, Inc is an advanced renewable fuels and biochemicals company, focused on producing sustainable energy solutions and reducing carbon emissions through innovative technologies.'}, {'Symbol': 'APEX', 'Company Description': 'Apex Global Brands Inc. specializes in creating and marketing a diverse portfolio of fashion and lifestyle brands, connecting consumers with trendy and innovative products worldwide.'}, {'Symbol': 'BIOC', 'Company Description': 'Biocept, Inc. specializes in developing advanced diagnostic solutions that help detect and analyze cancer cells, driving innovation in personalized medicine and cancer treatment.'}, {'Symbol': 'BKYI', 'Company Description': 'BIO-key International, Inc. specializes in advanced biometric solutions, providing secure and convenient identity verification systems for enterprises and consumers alike.'}, {'Symbol': 'CBAT', 'Company Description': 'CBAK Energy Technology, Inc. specializes in developing and manufacturing high-performance lithium-ion batteries, playing a pivotal role in powering electric vehicles and renewable energy solutions.'}, {'Symbol': 'CCCL', 'Company Description': 'China Ceramics Co., Ltd. specializes in manufacturing high-quality ceramic tiles, catering to both residential and commercial markets with a wide range of designs and finishes.'}, {'Symbol': 'CORV', 'Company Description': 'Correvio Pharma Corp., based in Canada, specializes in developing and commercializing innovative cardiovascular therapies to improve patient outcomes.'}, {'Symbol': 'CPAH', 'Company Description': 'CounterPath Corporation specializes in developing software solutions that enhance communication by providing seamless VoIP and unified communications applications for businesses and individuals.'}, {'Symbol': 'DZSI', 'Company Description': 'DASAN Zhone Solutions, Inc. specializes in providing advanced broadband access solutions, empowering telecommunications networks to deliver faster and more reliable internet services worldwide.'}, {'Symbol': 'FAMI', 'Company Description': 'Farmmi, Inc. specializes in the cultivation and distribution of high-quality agricultural products, with a focus on mushrooms and other nutritious foods.'}, {'Symbol': 'FTFT', 'Company Description': 'Future FinTech Group Inc. specializes in the development and marketing of blockchain-based products and financial technology solutions, aiming to revolutionize the digital economy with innovative applications.'}, {'Symbol': 'FTR', 'Company Description': 'Frontier Communications Corporation provides telecommunications services, including internet, phone, and television solutions, to residential and business customers across the United States.'}, {'Symbol': 'IDEX', 'Company Description': 'Ideanomics, Inc. is at the forefront of transforming the commercial electric vehicle industry, providing comprehensive solutions that drive innovation and sustainability in transportation and energy.'}, {'Symbol': 'ISDS', 'Company Description': 'Invesco RAFI Strategic Developed ex-US Small Company ETF offers investors a unique opportunity to access a portfolio of small-cap stocks from developed markets outside the United States, focusing on strategic financial growth and diversification.'}, {'Symbol': 'MCEP', 'Company Description': 'Mid-Con Energy Partners, LP specializes in the exploration and production of oil and natural gas, focusing on maximizing energy resources across the United States.'}, {'Symbol': 'NXTD', 'Company Description': 'NXT-ID Inc. specializes in developing innovative technology solutions that enhance security and convenience in the fields of healthcare and electronic payments.'}, {'Symbol': 'OPTT', 'Company Description': 'Ocean Power Technologies, Inc. harnesses the power of the ocean to develop innovative renewable energy solutions, specializing in wave energy technology.'}, {'Symbol': 'PEIX', 'Company Description': 'Pacific Ethanol, Inc. specializes in producing renewable fuels and high-quality alcohol products, contributing to sustainable energy solutions and cleaner alternatives for the transportation sector.'}, {'Symbol': 'RBZ', 'Company Description': 'Reebonz Holding Limited is an online luxury marketplace that specializes in offering a curated selection of high-end fashion items and accessories to discerning shoppers worldwide.'}, {'Symbol': 'SES', 'Company Description': 'Synthesis Energy Systems, Inc. specializes in transforming low-cost carbon resources into clean energy and valuable chemical products, driving innovation in sustainable energy solutions.'}, {'Symbol': 'SNSS', 'Company Description': 'Sunesis Pharmaceuticals, Inc. is dedicated to developing innovative cancer therapies, striving to advance treatments that target the underlying mechanisms of the disease.'}, {'Symbol': 'SPI', 'Company Description': 'SPI Energy Co., Ltd. specializes in providing renewable energy solutions, focusing on solar power products and services to drive sustainable energy initiatives globally.'}, {'Symbol': 'SYPR', 'Company Description': 'Sypris Solutions, Inc. specializes in providing engineering and manufacturing services for the aerospace and defense sectors, ensuring high-quality solutions for complex technological challenges.'}, {'Symbol': 'VTIQW', 'Company Description': 'VectoIQ Acquisition Corp. is an investment company specializing in identifying and merging with innovative technology and automotive firms to drive growth and transformation in the mobility sector.'}], 'var_function-call-11740613577733516459': 'file_storage/function-call-11740613577733516459.json'}

exec(code, env_args)
