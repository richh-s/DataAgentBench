code = """import json
import re

# Get the financially troubled stocks data
fin_data = locals().get('var_functions.query_db:0', [])
print('Financial data count:', len(fin_data))

# Extract symbols from financial data
nasdaq_symbols = []
for stock in fin_data:
    if isinstance(stock, dict) and 'Symbol' in stock:
        nasdaq_symbols.append(stock['Symbol'])

print('Nasdaq symbols count:', len(nasdaq_symbols))
print('Sample symbols:', nasdaq_symbols[:10])

# Get tables info - it's a file path
tables_path = locals().get('var_functions.list_db:2', '')
print('Tables path type:', type(tables_path))
if isinstance(tables_path, str) and '.json' in tables_path:
    try:
        with open(tables_path, 'r') as f:
            tables_list = json.load(f)
        print('Loaded tables list type:', type(tables_list))
        print('Tables list length:', len(tables_list))
        
        # Extract table names from the format "name": "..."
        available_tables = []
        for item in tables_list:
            if isinstance(item, dict) and 'name' in item:
                available_tables.append(item['name'])
        
        print('Available tables extracted:', len(available_tables))
        print('Sample tables:', available_tables[:10])
        
        # Find intersection
        intersection = list(set(nasdaq_symbols) & set(available_tables))
        print('Matching stocks:', len(intersection))
        print('Matching:', sorted(intersection))
        
        result = {
            'nasdaq_troubled': sorted(nasdaq_symbols),
            'available_tickers': len(available_tables),
            'matching_stocks': sorted(intersection),
            'count': len(intersection)
        }
        print('__RESULT__:')
        print(json.dumps(result))
        
    except Exception as e:
        print('Error loading tables:', e)
        print('__RESULT__:')
        print(json.dumps({'error': str(e)}))
else:
    print('Unexpected tables_path format')
    print('__RESULT__:')
    print(json.dumps({'error': 'unexpected format'}))"""

env_args = {'var_functions.query_db:0': [{'Symbol': 'AGMH', 'Financial Status': 'D', 'Market Category': 'S', 'Company Description': 'AGM Group Holdings Inc. specializes in providing financial technology solutions and services, focusing on enhancing efficiency and performance for businesses in the financial sector.'}, {'Symbol': 'AMTX', 'Financial Status': 'D', 'Market Category': 'G', 'Company Description': 'Aemetis, Inc is an advanced renewable fuels and biochemicals company, focused on producing sustainable energy solutions and reducing carbon emissions through innovative technologies.'}, {'Symbol': 'APEX', 'Financial Status': 'D', 'Market Category': 'S', 'Company Description': 'Apex Global Brands Inc. specializes in creating and marketing a diverse portfolio of fashion and lifestyle brands, connecting consumers with trendy and innovative products worldwide.'}, {'Symbol': 'BIOC', 'Financial Status': 'D', 'Market Category': 'S', 'Company Description': 'Biocept, Inc. specializes in developing advanced diagnostic solutions that help detect and analyze cancer cells, driving innovation in personalized medicine and cancer treatment.'}, {'Symbol': 'BKYI', 'Financial Status': 'D', 'Market Category': 'S', 'Company Description': 'BIO-key International, Inc. specializes in advanced biometric solutions, providing secure and convenient identity verification systems for enterprises and consumers alike.'}, {'Symbol': 'CBAT', 'Financial Status': 'D', 'Market Category': 'S', 'Company Description': 'CBAK Energy Technology, Inc. specializes in developing and manufacturing high-performance lithium-ion batteries, playing a pivotal role in powering electric vehicles and renewable energy solutions.'}, {'Symbol': 'CCCL', 'Financial Status': 'D', 'Market Category': 'S', 'Company Description': 'China Ceramics Co., Ltd. specializes in manufacturing high-quality ceramic tiles, catering to both residential and commercial markets with a wide range of designs and finishes.'}, {'Symbol': 'CORV', 'Financial Status': 'D', 'Market Category': 'S', 'Company Description': 'Correvio Pharma Corp., based in Canada, specializes in developing and commercializing innovative cardiovascular therapies to improve patient outcomes.'}, {'Symbol': 'CPAH', 'Financial Status': 'D', 'Market Category': 'S', 'Company Description': 'CounterPath Corporation specializes in developing software solutions that enhance communication by providing seamless VoIP and unified communications applications for businesses and individuals.'}, {'Symbol': 'DZSI', 'Financial Status': 'D', 'Market Category': 'S', 'Company Description': 'DASAN Zhone Solutions, Inc. specializes in providing advanced broadband access solutions, empowering telecommunications networks to deliver faster and more reliable internet services worldwide.'}, {'Symbol': 'FAMI', 'Financial Status': 'D', 'Market Category': 'S', 'Company Description': 'Farmmi, Inc. specializes in the cultivation and distribution of high-quality agricultural products, with a focus on mushrooms and other nutritious foods.'}, {'Symbol': 'FTFT', 'Financial Status': 'D', 'Market Category': 'S', 'Company Description': 'Future FinTech Group Inc. specializes in the development and marketing of blockchain-based products and financial technology solutions, aiming to revolutionize the digital economy with innovative applications.'}, {'Symbol': 'FTR', 'Financial Status': 'D', 'Market Category': 'Q', 'Company Description': 'Frontier Communications Corporation provides telecommunications services, including internet, phone, and television solutions, to residential and business customers across the United States.'}, {'Symbol': 'IDEX', 'Financial Status': 'D', 'Market Category': 'S', 'Company Description': 'Ideanomics, Inc. is at the forefront of transforming the commercial electric vehicle industry, providing comprehensive solutions that drive innovation and sustainability in transportation and energy.'}, {'Symbol': 'ISDS', 'Financial Status': 'D', 'Market Category': 'G', 'Company Description': 'Invesco RAFI Strategic Developed ex-US Small Company ETF offers investors a unique opportunity to access a portfolio of small-cap stocks from developed markets outside the United States, focusing on strategic financial growth and diversification.'}, {'Symbol': 'MCEP', 'Financial Status': 'D', 'Market Category': 'S', 'Company Description': 'Mid-Con Energy Partners, LP specializes in the exploration and production of oil and natural gas, focusing on maximizing energy resources across the United States.'}, {'Symbol': 'NXTD', 'Financial Status': 'D', 'Market Category': 'S', 'Company Description': 'NXT-ID Inc. specializes in developing innovative technology solutions that enhance security and convenience in the fields of healthcare and electronic payments.'}, {'Symbol': 'OPTT', 'Financial Status': 'D', 'Market Category': 'S', 'Company Description': 'Ocean Power Technologies, Inc. harnesses the power of the ocean to develop innovative renewable energy solutions, specializing in wave energy technology.'}, {'Symbol': 'PEIX', 'Financial Status': 'D', 'Market Category': 'S', 'Company Description': 'Pacific Ethanol, Inc. specializes in producing renewable fuels and high-quality alcohol products, contributing to sustainable energy solutions and cleaner alternatives for the transportation sector.'}, {'Symbol': 'RBZ', 'Financial Status': 'D', 'Market Category': 'G', 'Company Description': 'Reebonz Holding Limited is an online luxury marketplace that specializes in offering a curated selection of high-end fashion items and accessories to discerning shoppers worldwide.'}, {'Symbol': 'SES', 'Financial Status': 'H', 'Market Category': 'S', 'Company Description': 'Synthesis Energy Systems, Inc. specializes in transforming low-cost carbon resources into clean energy and valuable chemical products, driving innovation in sustainable energy solutions.'}, {'Symbol': 'SNSS', 'Financial Status': 'D', 'Market Category': 'S', 'Company Description': 'Sunesis Pharmaceuticals, Inc. is dedicated to developing innovative cancer therapies, striving to advance treatments that target the underlying mechanisms of the disease.'}, {'Symbol': 'SPI', 'Financial Status': 'D', 'Market Category': 'Q', 'Company Description': 'SPI Energy Co., Ltd. specializes in providing renewable energy solutions, focusing on solar power products and services to drive sustainable energy initiatives globally.'}, {'Symbol': 'SYPR', 'Financial Status': 'D', 'Market Category': 'G', 'Company Description': 'Sypris Solutions, Inc. specializes in providing engineering and manufacturing services for the aerospace and defense sectors, ensuring high-quality solutions for complex technological challenges.'}, {'Symbol': 'VTIQW', 'Financial Status': 'D', 'Market Category': 'S', 'Company Description': 'VectoIQ Acquisition Corp. is an investment company specializing in identifying and merging with innovative technology and automotive firms to drive growth and transformation in the mobility sector.'}], 'var_functions.list_db:2': 'file_storage/functions.list_db:2.json', 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json', 'var_functions.execute_python:14': {'test': 'success'}, 'var_functions.execute_python:16': {'symbols_count': 25, 'tables_type': "<class 'str'>"}, 'var_functions.execute_python:18': {'matching_stocks': [], 'total_financial': 25, 'total_available': 0, 'match_count': 0}, 'var_functions.query_db:20': [], 'var_functions.query_db:22': 'file_storage/functions.query_db:22.json'}

exec(code, env_args)
