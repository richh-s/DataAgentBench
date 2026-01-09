code = """import json
import pandas as pd
import duckdb

troubled = pd.DataFrame(var_call_3jhtKM3TnlY5CBTyNqUNLlDq)

path = var_call_zC816wh6Bv4fYPVHmPmGcjhl
with open(path, 'r') as f:
    tables = json.load(f)

table_set = set(tables)
troubled = troubled[troubled['Symbol'].isin(table_set)].copy()

con = duckdb.connect(database='stocktrade_database', read_only=True)

rows = []
for _, r in troubled.iterrows():
    sym = r['Symbol']
    q = (
        f"SELECT AVG(CAST(\"Volume\" AS DOUBLE)) AS avg_daily_volume_2008 "
        f"FROM \"{sym}\" "
        f"WHERE \"Date\" >= '2008-01-01' AND \"Date\" < '2009-01-01' "
        f"AND \"Volume\" IS NOT NULL;"
    )
    avg_vol = con.execute(q).fetchone()[0]
    if avg_vol is not None:
        rows.append({'Symbol': sym,
                     'company_name': r['company_name'],
                     'financial_status': r['financial_status'],
                     'avg_daily_volume_2008': float(avg_vol)})

con.close()

out_df = pd.DataFrame(rows)
if len(out_df) > 0:
    out_df = out_df.sort_values(['company_name', 'Symbol'])

result = out_df.to_json(orient='records')
print('__RESULT__:')
print(result)"""

env_args = {'var_call_3jhtKM3TnlY5CBTyNqUNLlDq': [{'Symbol': 'AGMH', 'company_name': 'AGM Group Holdings Inc. specializes in providing financial technology solutions and services, focusing on enhancing efficiency and performance for businesses in the financial sector.', 'market_category': 'S', 'listing_exchange': 'Q', 'financial_status': 'D'}, {'Symbol': 'AMTX', 'company_name': 'Aemetis, Inc is an advanced renewable fuels and biochemicals company, focused on producing sustainable energy solutions and reducing carbon emissions through innovative technologies.', 'market_category': 'G', 'listing_exchange': 'Q', 'financial_status': 'D'}, {'Symbol': 'APEX', 'company_name': 'Apex Global Brands Inc. specializes in creating and marketing a diverse portfolio of fashion and lifestyle brands, connecting consumers with trendy and innovative products worldwide.', 'market_category': 'S', 'listing_exchange': 'Q', 'financial_status': 'D'}, {'Symbol': 'BIOC', 'company_name': 'Biocept, Inc. specializes in developing advanced diagnostic solutions that help detect and analyze cancer cells, driving innovation in personalized medicine and cancer treatment.', 'market_category': 'S', 'listing_exchange': 'Q', 'financial_status': 'D'}, {'Symbol': 'BKYI', 'company_name': 'BIO-key International, Inc. specializes in advanced biometric solutions, providing secure and convenient identity verification systems for enterprises and consumers alike.', 'market_category': 'S', 'listing_exchange': 'Q', 'financial_status': 'D'}, {'Symbol': 'CBAT', 'company_name': 'CBAK Energy Technology, Inc. specializes in developing and manufacturing high-performance lithium-ion batteries, playing a pivotal role in powering electric vehicles and renewable energy solutions.', 'market_category': 'S', 'listing_exchange': 'Q', 'financial_status': 'D'}, {'Symbol': 'CCCL', 'company_name': 'China Ceramics Co., Ltd. specializes in manufacturing high-quality ceramic tiles, catering to both residential and commercial markets with a wide range of designs and finishes.', 'market_category': 'S', 'listing_exchange': 'Q', 'financial_status': 'D'}, {'Symbol': 'CORV', 'company_name': 'Correvio Pharma Corp., based in Canada, specializes in developing and commercializing innovative cardiovascular therapies to improve patient outcomes.', 'market_category': 'S', 'listing_exchange': 'Q', 'financial_status': 'D'}, {'Symbol': 'CPAH', 'company_name': 'CounterPath Corporation specializes in developing software solutions that enhance communication by providing seamless VoIP and unified communications applications for businesses and individuals.', 'market_category': 'S', 'listing_exchange': 'Q', 'financial_status': 'D'}, {'Symbol': 'DZSI', 'company_name': 'DASAN Zhone Solutions, Inc. specializes in providing advanced broadband access solutions, empowering telecommunications networks to deliver faster and more reliable internet services worldwide.', 'market_category': 'S', 'listing_exchange': 'Q', 'financial_status': 'D'}, {'Symbol': 'FAMI', 'company_name': 'Farmmi, Inc. specializes in the cultivation and distribution of high-quality agricultural products, with a focus on mushrooms and other nutritious foods.', 'market_category': 'S', 'listing_exchange': 'Q', 'financial_status': 'D'}, {'Symbol': 'FTFT', 'company_name': 'Future FinTech Group Inc. specializes in the development and marketing of blockchain-based products and financial technology solutions, aiming to revolutionize the digital economy with innovative applications.', 'market_category': 'S', 'listing_exchange': 'Q', 'financial_status': 'D'}, {'Symbol': 'FTR', 'company_name': 'Frontier Communications Corporation provides telecommunications services, including internet, phone, and television solutions, to residential and business customers across the United States.', 'market_category': 'Q', 'listing_exchange': 'Q', 'financial_status': 'D'}, {'Symbol': 'IDEX', 'company_name': 'Ideanomics, Inc. is at the forefront of transforming the commercial electric vehicle industry, providing comprehensive solutions that drive innovation and sustainability in transportation and energy.', 'market_category': 'S', 'listing_exchange': 'Q', 'financial_status': 'D'}, {'Symbol': 'ISDS', 'company_name': 'Invesco RAFI Strategic Developed ex-US Small Company ETF offers investors a unique opportunity to access a portfolio of small-cap stocks from developed markets outside the United States, focusing on strategic financial growth and diversification.', 'market_category': 'G', 'listing_exchange': 'Q', 'financial_status': 'D'}, {'Symbol': 'MCEP', 'company_name': 'Mid-Con Energy Partners, LP specializes in the exploration and production of oil and natural gas, focusing on maximizing energy resources across the United States.', 'market_category': 'S', 'listing_exchange': 'Q', 'financial_status': 'D'}, {'Symbol': 'NXTD', 'company_name': 'NXT-ID Inc. specializes in developing innovative technology solutions that enhance security and convenience in the fields of healthcare and electronic payments.', 'market_category': 'S', 'listing_exchange': 'Q', 'financial_status': 'D'}, {'Symbol': 'OPTT', 'company_name': 'Ocean Power Technologies, Inc. harnesses the power of the ocean to develop innovative renewable energy solutions, specializing in wave energy technology.', 'market_category': 'S', 'listing_exchange': 'Q', 'financial_status': 'D'}, {'Symbol': 'PEIX', 'company_name': 'Pacific Ethanol, Inc. specializes in producing renewable fuels and high-quality alcohol products, contributing to sustainable energy solutions and cleaner alternatives for the transportation sector.', 'market_category': 'S', 'listing_exchange': 'Q', 'financial_status': 'D'}, {'Symbol': 'RBZ', 'company_name': 'Reebonz Holding Limited is an online luxury marketplace that specializes in offering a curated selection of high-end fashion items and accessories to discerning shoppers worldwide.', 'market_category': 'G', 'listing_exchange': 'Q', 'financial_status': 'D'}, {'Symbol': 'SES', 'company_name': 'Synthesis Energy Systems, Inc. specializes in transforming low-cost carbon resources into clean energy and valuable chemical products, driving innovation in sustainable energy solutions.', 'market_category': 'S', 'listing_exchange': 'Q', 'financial_status': 'H'}, {'Symbol': 'SNSS', 'company_name': 'Sunesis Pharmaceuticals, Inc. is dedicated to developing innovative cancer therapies, striving to advance treatments that target the underlying mechanisms of the disease.', 'market_category': 'S', 'listing_exchange': 'Q', 'financial_status': 'D'}, {'Symbol': 'SPI', 'company_name': 'SPI Energy Co., Ltd. specializes in providing renewable energy solutions, focusing on solar power products and services to drive sustainable energy initiatives globally.', 'market_category': 'Q', 'listing_exchange': 'Q', 'financial_status': 'D'}, {'Symbol': 'SYPR', 'company_name': 'Sypris Solutions, Inc. specializes in providing engineering and manufacturing services for the aerospace and defense sectors, ensuring high-quality solutions for complex technological challenges.', 'market_category': 'G', 'listing_exchange': 'Q', 'financial_status': 'D'}, {'Symbol': 'VTIQW', 'company_name': 'VectoIQ Acquisition Corp. is an investment company specializing in identifying and merging with innovative technology and automotive firms to drive growth and transformation in the mobility sector.', 'market_category': 'S', 'listing_exchange': 'Q', 'financial_status': 'D'}], 'var_call_zC816wh6Bv4fYPVHmPmGcjhl': 'file_storage/call_zC816wh6Bv4fYPVHmPmGcjhl.json'}

exec(code, env_args)
