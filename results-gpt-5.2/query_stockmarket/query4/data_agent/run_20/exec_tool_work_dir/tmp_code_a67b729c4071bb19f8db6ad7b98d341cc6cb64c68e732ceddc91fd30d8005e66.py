code = """import json
syms_str = json.loads(var_call_rPj3N2NF4PTD7QLzomvqeF1w)['sql_in_list']
symbols = [s.strip().strip("'") for s in syms_str.split(',') if s.strip()]
chunks = [symbols[i:i+60] for i in range(0, len(symbols), 60)]
queries = []
for chunk in chunks:
    unions = []
    for sym in chunk:
        unions.append("SELECT '"+sym+"' AS symbol, \"Open\", \"Close\" FROM "+sym+" WHERE \"Date\">='2017-01-01' AND \"Date\"<'2018-01-01'")
    union_sql = "\\nUNION ALL\\n".join(unions)
    q = (
        "WITH counts AS (\\n"
        "  SELECT symbol,\\n"
        "         SUM(CASE WHEN \\\"Close\\\" > \\\"Open\\\" THEN 1 ELSE 0 END) AS up_days,\\n"
        "         SUM(CASE WHEN \\\"Close\\\" < \\\"Open\\\" THEN 1 ELSE 0 END) AS down_days\\n"
        "  FROM (\\n"+union_sql+"\\n  ) t\\n"
        "  GROUP BY symbol\\n"
        ")\\n"
        "SELECT symbol, up_days, down_days, (up_days - down_days) AS net_up\\n"
        "FROM counts\\n"
        "WHERE up_days > down_days\\n"
        "ORDER BY net_up DESC"
    )
    queries.append(q)
print('__RESULT__:')
print(json.dumps({'n_chunks': len(chunks), 'first_query_preview': queries[0][:500], 'queries': queries}))"""

env_args = {'var_call_NI0trbOoYA9FdfK8rJaJwdX1': 'file_storage/call_NI0trbOoYA9FdfK8rJaJwdX1.json', 'var_call_rPj3N2NF4PTD7QLzomvqeF1w': {'n_symbols': 234, 'sql_in_list': "'AEFC','AIN','AIV','AIZP','AJRD','AL','AMN','AMP','AMT','ARD','ARGD','ARLO','ASG','AVA','BANC','BBU','BBVA','BDXA','BKH','BKT','BLD','BNS','BV','BZH','CADE','CAE','CAF','CBT','CCC','CCZ','CHAP','CIA','CMA','CMI','CMSA','CNK','COTY','CRC','CRM','CRS','CSL','CTS','CUBE','CURO','CVIA','CVX','CXH','DAC','DDS','DDT','DEO','DGX','DMB','DTQ','DXC','EARN','EBS','EGO','EGY','EIG','ELF','EMP','ENLC','EPR','EPRT','ES','ESRT','ESS','ETM','EV','EVT','EXP','FMN','FPAC','FSM','GCO','GD','GDL','GDV','GEL','GJP','GLOB','GLT','GOL','GSLD','GTY','GVA','GWB','H','HBI','HDB','HEP','HIL','HIO','HIX','HLF','HLT','HNI','HRB','HTFA','IBM','IGR','IHC','IPG','IRM','IT','JGH','JHY','JKS','JMP','JNPR','KMB','KNX','KW','KYN','LB','LDOS','LHC','LHX','LOMA','MANU','MDLX','MDLY','MED','MFO','MGR','MGU','MHE','MIY','MKC','MLI','MNE','MR','MS','MTD','MYD','NFH','NGG','NJV','NNI','NNY','NRUC','NUE','NXN','OCFT','OEC','ORA','ORAN','ORCL','ORN','PAG','PBI','PFE','PFSI','PGR','PIM','PKE','PLAN','PLNT','PMT','PNM','PPG','PRSP','PRTY','PSV','PSXP','QTS','QUAD','RBC','RCB','RCI','RES','REXR','RH','RMT','ROG','ROL','RPAI','RPM','RQI','RWT','SAF','SAIL','SAM','SBR','SCU','SFUN','SHAK','SI','SITC','SJM','SJT','SJW','SLF','SMP','SOL','SPOT','SRC','SRF','SRT','SSD','STG','STL','STON','SYX','TBB','TCP','TDJ','TGP','TLYS','TNC','TPH','TRV','TTI','TUFN','TWTR','UHT','UIS','USX','UTL','VET','VGR','VHI','VIV','VKQ','VRT','VVI','WOR','WPG','WSM','X','YEXT','ZNH','ZTR'", 'sql_in_list_len': 1439}, 'var_call_w5MAyhP4qf7DyjcvWiZaSNV3': [{'symbol': 'AAAU'}, {'symbol': 'AADR'}, {'symbol': 'AAME'}, {'symbol': 'AAWW'}, {'symbol': 'AAXJ'}], 'var_call_cAVBaqTHsZWcXNvhvtGY4N5A': [{'symbol': 'AIN', 'up_days': '143.0', 'down_days': '101.0', 'net_up': '42.0'}]}

exec(code, env_args)
