code = """import json
import pandas as pd
import re

# Load data
meta_path = locals()['var_function-call-230048583216778633']
with open(meta_path, 'r') as f:
    metadata_records = json.load(f)
df_meta = pd.DataFrame(metadata_records)
df_meta['article_id'] = df_meta['article_id'].astype(int)

articles_path = locals()['var_function-call-2198657140293455711']
with open(articles_path, 'r') as f:
    articles_records = json.load(f)
df_articles = pd.DataFrame(articles_records)
df_articles['article_id'] = df_articles['article_id'].astype(int)

df = pd.merge(df_meta, df_articles, on='article_id', how='inner')

def classify(row):
    text = (str(row['title']) + " " + str(row['description'])).lower()
    
    keywords = {
        'World': [
            "war", "wars", "peace", "government", "governments", "president", "presidents", "minister", "ministers", "military", "bomb", "bombs", "kill", "killed", "killing", "kills", "attack", "attacks", "treaty", "treaties", "un", "united nations", 
            "country", "countries", "international", "foreign", "policy", "policies", "iraq", "syria", "iran", "israel", "palestine", "russia", "china", "europe", 
            "africa", "asia", "rebel", "rebels", "crisis", "refugee", "refugees", "election", "elections", "parliament", "leader", "leaders", "official", "officials", "troops", "police", "protest", "protests", 
            "court", "courts", "law", "laws", "nuclear", "blast", "blasts", "disaster", "disasters", "storm", "storms", "hurricane", "hurricanes", "earthquake", "earthquakes", "rescue", "aid", "hostage", "hostages", "terror", "terrorism", "terrorist", "terrorists", "vote", "votes", 
            "party", "parties", "talks", "agreement", "agreements", "summit", "summits", "border", "borders", "nation", "nations", "state", "states", "region", "regions", "global", "nato", "gaza", "afghanistan", "pakistan",
            "baghdad", "kabul", "tehran", "jerusalem", "beijing", "moscow", "london", "paris", "berlin", "tokyo", "washington", "prime minister",
            "senate", "congress", "diplomat", "diplomats", "embassy", "embassies", "suicide", "explosion", "explosions", "crash", "crashes", "u.s.", "u.s.a.", "united states", "america", "britain", "uk", "france", "germany", "japan", "korea",
            "isis", "isil", "islamic state", "boko haram", "al qaeda", "taliban",
            "ukraine", "crimea", "donbass", "kiev",
            "yemen", "libya", "nigeria", "somalia", "sudan", "south sudan", "darfur", "mali", "egypt", "cairo",
            "nepal", "kathmandu",
            "migrant", "migrants", "immigration", "immigrant", "immigrants",
            "venezuela", "brazil", "argentina", "colombia", "chile", "peru", "mexico", "farc", "corruption", "scandal",
            "greece", "greek", "athens"
        ],
        'Business': [
            "market", "markets", "stock", "stocks", "dow", "nasdaq", "wall street", "dollar", "dollars", "euro", "euros", "yen", "economy", "economies", "finance", "finances", "financial", "bank", "banks", "fed", "federal reserve", "rate", "rates", 
            "inflation", "deficit", "deficits", "budget", "budgets", "profit", "profits", "earnings", "revenue", "revenues", "loss", "losses", "sales", "trade", "trades", "company", "companies", "firm", "firms", "business", "businesses", 
            "industry", "industries", "oil", "gas", "price", "prices", "cost", "costs", "deal", "deals", "merger", "mergers", "acquisition", "acquisitions", "bid", "bids", "share", "shares", "investor", "investors", "ceo", "executive", "executives", 
            "manager", "managers", "job", "jobs", "unemployment", "labor", "work", "corp", "inc", "ltd", "airline", "airlines", "boeing", "airbus", "ford", "gm", "toyota", 
            "microsoft", "google", "apple", "intel", "ibm", "oracle", "wal-mart", "retail", "store", "stores",
            "imf", "wto", "debt", "bond", "bonds"
        ],
        'Sports': [
            "game", "games", "match", "matches", "score", "scores", "win", "wins", "winning", "won", "loss", "losses", "lost", "team", "teams", "player", "players", "coach", "coaches", "cup", "cups", "league", "leagues", "season", "seasons", "champion", "champions", "olympic", "olympics", "medal", "medals", 
            "stadium", "stadiums", "club", "clubs", "ball", "balls", "sport", "sports", "race", "races", "f1", "tennis", "football", "soccer", "basketball", "baseball", "cricket", "hockey", 
            "golf", "rugby", "boxing", "athlete", "athletes", "tournament", "tournaments", "round", "rounds", "final", "finals", "semi", "semis", "quarter", "quarters", "playoff", "playoffs", "nba", "nfl", "nhl", "mlb", 
            "fifa", "uefa", "gold", "silver", "bronze", "record", "records", "world cup"
        ],
        'Sci/Tech': [
            "technology", "technologies", "science", "sciences", "research", "study", "studies", "space", "nasa", "launch", "launches", "computer", "computers", "software", "internet", "web", "phone", "phones", 
            "mobile", "mobiles", "virus", "viruses", "discovery", "discoveries", "drug", "drugs", "health", "hospital", "hospitals", "patient", "patients", "disease", "diseases", "treatment", "treatments", "doctor", "doctors", "biology", "physics", 
            "chemistry", "chip", "chips", "server", "servers", "linux", "windows", "browser", "browsers", "search engine", "online", "digital", "network", "networks", "satellite", "satellites", 
            "telescope", "telescopes", "mars", "moon", "orbit", "robot", "robots", "gadget", "gadgets", "device", "devices", "screen", "screens", "monitor", "monitors", "keyboard", "keyboards", "mouse", "mice", "hacker", "hackers", "spam",
            "security", "patch", "patches", "update", "updates", "version", "versions", "release", "releases", "beta",
            "ebola"
        ]
    }
    
    scores = {cat: 0 for cat in keywords}
    tokens = re.findall(r'[a-z0-9\.]+', text) 
    for token in tokens:
        if token.endswith('.') and token not in ["u.s.", "u.s.a."]:
            token = token[:-1]
        for cat, kws in keywords.items():
            if token in kws:
                scores[cat] += 1
    
    best_cat = max(scores, key=scores.get)
    max_score = scores[best_cat]
    if max_score == 0:
        return "Unknown"
        
    candidates = [c for c, s in scores.items() if s == max_score]
    if len(candidates) > 1:
        priority = ['Sports', 'Sci/Tech', 'Business', 'World']
        for p in priority:
            if p in candidates:
                return p
    return best_cat

df['category'] = df.apply(classify, axis=1)

# Filter for World
df_world = df[df['category'] == 'World']

# Group by region
result = df_world['region'].value_counts()

print("__RESULT__:")
print(result.to_json())"""

env_args = {'var_function-call-230048583216778633': 'file_storage/function-call-230048583216778633.json', 'var_function-call-8260068931381035711': {'count': 6696, 'sample_ids': [13, 18, 26, 51, 52, 67, 70, 74, 86, 97], 'regions': ['Europe', 'South America', 'Africa', 'Asia', 'North America']}, 'var_function-call-7380412333144670889': {'min_id': 13, 'max_id': 127570, 'count': 6696}, 'var_function-call-7005320274688524134': [{'article_id': '0', 'title': 'Wall St. Bears Claw Back Into the Black (Reuters)', 'description': "Reuters - Short-sellers, Wall Street's dwindling\\band of ultra-cynics, are seeing green again."}, {'article_id': '1', 'title': 'Carlyle Looks Toward Commercial Aerospace (Reuters)', 'description': 'Reuters - Private investment firm Carlyle Group,\\which has a reputation for making well-timed and occasionally\\controversial plays in the defense industry, has quietly placed\\its bets on another part of the market.'}, {'article_id': '2', 'title': "Oil and Economy Cloud Stocks' Outlook (Reuters)", 'description': 'Reuters - Soaring crude prices plus worries\\about the economy and the outlook for earnings are expected to\\hang over the stock market next week during the depth of the\\summer doldrums.'}, {'article_id': '3', 'title': 'Iraq Halts Oil Exports from Main Southern Pipeline (Reuters)', 'description': 'Reuters - Authorities have halted oil export\\flows from the main pipeline in southern Iraq after\\intelligence showed a rebel militia could strike\\infrastructure, an oil official said on Saturday.'}, {'article_id': '4', 'title': 'Oil prices soar to all-time record, posing new menace to US economy (AFP)', 'description': 'AFP - Tearaway world oil prices, toppling records and straining wallets, present a new economic menace barely three months before the US presidential elections.'}], 'var_function-call-13531593010111911559': {'count': 5, 'sample': [{'article_id': '0', 'title': 'Wall St. Bears Claw Back Into the Black (Reuters)', 'description': "Reuters - Short-sellers, Wall Street's dwindling\\band of ultra-cynics, are seeing green again."}, {'article_id': '1', 'title': 'Carlyle Looks Toward Commercial Aerospace (Reuters)', 'description': 'Reuters - Private investment firm Carlyle Group,\\which has a reputation for making well-timed and occasionally\\controversial plays in the defense industry, has quietly placed\\its bets on another part of the market.'}, {'article_id': '2', 'title': "Oil and Economy Cloud Stocks' Outlook (Reuters)", 'description': 'Reuters - Soaring crude prices plus worries\\about the economy and the outlook for earnings are expected to\\hang over the stock market next week during the depth of the\\summer doldrums.'}, {'article_id': '3', 'title': 'Iraq Halts Oil Exports from Main Southern Pipeline (Reuters)', 'description': 'Reuters - Authorities have halted oil export\\flows from the main pipeline in southern Iraq after\\intelligence showed a rebel militia could strike\\infrastructure, an oil official said on Saturday.'}, {'article_id': '4', 'title': 'Oil prices soar to all-time record, posing new menace to US economy (AFP)', 'description': 'AFP - Tearaway world oil prices, toppling records and straining wallets, present a new economic menace barely three months before the US presidential elections.'}]}, 'var_function-call-864367092588596787': [], 'var_function-call-2764836307452452932': [{'_id': '69451f0991224f9718080b40', 'article_id': '13', 'title': 'Google IPO Auction Off to Rocky Start', 'description': " WASHINGTON/NEW YORK (Reuters) - The auction for Google  Inc.'s highly anticipated initial public offering got off to a  rocky start on Friday after the Web search company sidestepped  a bullet from U.S. securities regulators."}], 'var_function-call-2198657140293455711': 'file_storage/function-call-2198657140293455711.json', 'var_function-call-5208470535368002308': {'Africa': 439, 'South America': 431, 'Europe': 429, 'Asia': 426, 'North America': 420}, 'var_function-call-13767408398871841022': {'World': [{'title': 'Iraq #39;s tireless worker killed in the country she loved', 'description': 'When Margaret Hassan was kidnapped in October, her car was waved down by two men in Iraqi police uniforms. Gunmen surrounded the car and dragged Ms Hassan #39;s driver and unarmed guard from their seats.'}, {'title': 'UN Approves Oil Sanction on Sudan', 'description': 'The United Nations (UN) Security Council passed a resolution yesterday (September 18) that proposes implementing oil sanctions on Sudan if the government fails to end the crisis in its Darfur region.'}, {'title': "A Blackbird's Song", 'description': "In California, a Laotian refugee remembers the long suffering of his country's Hmong tribespeople"}, {'title': "Santomero Says Rates 'Still Stimulative' (Reuters)", 'description': 'Reuters - U.S. interest rates are still\\stimulative but should return to "more normal levels" as\\expansion continues, Philadelphia Federal Reserve President\\Anthony Santomero said on Saturday.'}, {'title': 'U.S. Plans Year-End Drive to Take Iraqi Rebel Areas', 'description': 'American commanders in Iraq say they are preparing operations to open up rebel-held areas, especially Falluja, the restive city west of Baghdad now under control of insurgents and Islamist groups.'}], 'Business': [{'title': 'Siebel releases flood of BI applications (InfoWorld)', 'description': 'InfoWorld - Capitalizing on the current trend within the enterprise to reduce the number of applications to support, Siebel Systems on Monday unveiled a package of business analytics solutions that can be deployed by IT as both extensions to current CRM applications or as stand-alone programs.'}, {'title': 'Treasuries Up in Post-Fed Rollercoaster', 'description': ' NEW YORK (Reuters) - U.S. Treasury prices seesawed on  Tuesday after the Federal Reserve raised interest rates by a  quarter-percentage point and signaled further hikes were on the  way.'}, {'title': 'Credit Suisse to merge CSFB unit into parent', 'description': 'Credit Suisse Group announced plans to merge its Credit Suisse First Boston Securities unit with the rest of the company #39;s operations and cut as many as 300 jobs.'}, {'title': 'Boeing may join Microsoft in EU antitrust fight', 'description': "Aircraft giant may argue against European antitrust regulators' order to make Microsoft give secrets to rivals."}, {'title': 'Briefly: Microsoft tests Windows Marketplace', 'description': 'roundup Plus: Nortel delays financials again...Microsoft updates SharePoint...Overture heads toward automation.'}]}, 'var_function-call-13630844574686216921': {'South America': 376, 'Africa': 368, 'Europe': 362, 'North America': 362, 'Asia': 358}}

exec(code, env_args)
