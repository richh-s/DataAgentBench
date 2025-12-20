code = """import json
import re

# Load the file
file_path = locals()['var_function-call-15783133266262002332']
with open(file_path, 'r') as f:
    articles = json.load(f)

# Define keywords
strict_sports = [
    "olympics", "olympic", "athens", "medal", "nba", "nfl", "mlb", "nhl", 
    "fifa", "uefa", "wimbledon", "super bowl", "world cup", "euro 2004", 
    "championship", "quarterback", "touchdown", "homerun", "slam dunk", 
    "gold medal", "silver medal", "bronze medal", "grand slam", "pga tour", 
    "formula one", "nascar", "doping", "dream team", "sprinter", "gymnast", 
    "swimmer", "marathon", "triathlon", "red sox", "yankees", "lakers", "pistons",
    "ryder cup", "pga", "lpga", "us open"
]

general_sports = [
    "sport", "football", "baseball", "basketball", "hockey", "tennis", "soccer", "golf", 
    "rugby", "cricket", "boxing", "f1", "team", "coach", "player", "athlete", 
    "game", "match", "cup", "league", "win", "loss", "victory", "defeat", 
    "score", "race", "driver", "playoff", "final", "semifinal", "round"
]

negative_keywords = [
    "stocks", "stock market", "economy", "oil", "prices", "profit", "earnings", 
    "investment", "shares", "dollar", "trade", "deficit", "iraq", "war", 
    "election", "president", "minister", "gaza", "israel", "palestinian", 
    "nuclear", "blast", "attack", "rebel", "militia", "bomb", "killed", 
    "government", "microsoft", "google", "intel", "linux", "software", "virus",
    "windows", "unix", "code", "developer", "logger", "java", "bug", "security", 
    "hacker", "voicemail", "wireless", "orbit", "space", "launch", "astronaut", 
    "mission", "science", "technology", "internet", "web", "computer", "server", 
    "database", "telecom", "wireless", "mobile", "cell phone"
]

def get_score(text):
    text_lower = text.lower()
    score = 0
    
    # Use regex for word boundary matching
    # Check strict
    for kw in strict_sports:
        # strict phrases can be checked as substrings usually safe
        if kw in text_lower:
            score += 10
            
    # Check general (use word boundaries)
    for kw in general_sports:
        # Regex \bkw\b
        if re.search(r'\b' + re.escape(kw) + r'\b', text_lower):
            score += 2
        
    # Check negative
    for kw in negative_keywords:
        if kw in text_lower:
            score -= 5 # Penalty
            
    return score

# Process articles
candidates = []
for art in articles:
    # Combine title and description
    content = art['title'] + " " + art['description']
    score = get_score(content)
    
    # Filter
    if score > 0:
        candidates.append({
            "title": art['title'],
            "description": art['description'],
            "len": len(art['description']),
            "score": score
        })

# Sort by length descending
candidates.sort(key=lambda x: x['len'], reverse=True)

# Output the top 5
print("__RESULT__:")
print(json.dumps(candidates[:5], indent=2))"""

env_args = {'var_function-call-10047601114484748362': [{'_id': '6944814a2d282254f98124f6', 'article_id': '0', 'title': 'Wall St. Bears Claw Back Into the Black (Reuters)', 'description': "Reuters - Short-sellers, Wall Street's dwindling\\band of ultra-cynics, are seeing green again."}, {'_id': '6944814a2d282254f98124f7', 'article_id': '1', 'title': 'Carlyle Looks Toward Commercial Aerospace (Reuters)', 'description': 'Reuters - Private investment firm Carlyle Group,\\which has a reputation for making well-timed and occasionally\\controversial plays in the defense industry, has quietly placed\\its bets on another part of the market.'}, {'_id': '6944814a2d282254f98124f8', 'article_id': '2', 'title': "Oil and Economy Cloud Stocks' Outlook (Reuters)", 'description': 'Reuters - Soaring crude prices plus worries\\about the economy and the outlook for earnings are expected to\\hang over the stock market next week during the depth of the\\summer doldrums.'}, {'_id': '6944814a2d282254f98124f9', 'article_id': '3', 'title': 'Iraq Halts Oil Exports from Main Southern Pipeline (Reuters)', 'description': 'Reuters - Authorities have halted oil export\\flows from the main pipeline in southern Iraq after\\intelligence showed a rebel militia could strike\\infrastructure, an oil official said on Saturday.'}, {'_id': '6944814a2d282254f98124fa', 'article_id': '4', 'title': 'Oil prices soar to all-time record, posing new menace to US economy (AFP)', 'description': 'AFP - Tearaway world oil prices, toppling records and straining wallets, present a new economic menace barely three months before the US presidential elections.'}], 'var_function-call-9571403557217770297': [{'_id': '6944814a2d282254f98124f6', 'article_id': '0', 'title': 'Wall St. Bears Claw Back Into the Black (Reuters)', 'description': "Reuters - Short-sellers, Wall Street's dwindling\\band of ultra-cynics, are seeing green again."}, {'_id': '6944814a2d282254f98124f7', 'article_id': '1', 'title': 'Carlyle Looks Toward Commercial Aerospace (Reuters)', 'description': 'Reuters - Private investment firm Carlyle Group,\\which has a reputation for making well-timed and occasionally\\controversial plays in the defense industry, has quietly placed\\its bets on another part of the market.'}, {'_id': '6944814a2d282254f98124f8', 'article_id': '2', 'title': "Oil and Economy Cloud Stocks' Outlook (Reuters)", 'description': 'Reuters - Soaring crude prices plus worries\\about the economy and the outlook for earnings are expected to\\hang over the stock market next week during the depth of the\\summer doldrums.'}, {'_id': '6944814a2d282254f98124f9', 'article_id': '3', 'title': 'Iraq Halts Oil Exports from Main Southern Pipeline (Reuters)', 'description': 'Reuters - Authorities have halted oil export\\flows from the main pipeline in southern Iraq after\\intelligence showed a rebel militia could strike\\infrastructure, an oil official said on Saturday.'}, {'_id': '6944814a2d282254f98124fa', 'article_id': '4', 'title': 'Oil prices soar to all-time record, posing new menace to US economy (AFP)', 'description': 'AFP - Tearaway world oil prices, toppling records and straining wallets, present a new economic menace barely three months before the US presidential elections.'}], 'var_function-call-17685011732054669785': [{'title': 'Carlyle Looks Toward Commercial Aerospace (Reuters)', 'description': 'Reuters - Private investment firm Carlyle Group,\\which has a reputation for making well-timed and occasionally\\controversial plays in the defense industry, has quietly placed\\its bets on another part of the market.', 'desc_len': 214, 'sports_score': 0, 'is_strict_sports': False}, {'title': 'Iraq Halts Oil Exports from Main Southern Pipeline (Reuters)', 'description': 'Reuters - Authorities have halted oil export\\flows from the main pipeline in southern Iraq after\\intelligence showed a rebel militia could strike\\infrastructure, an oil official said on Saturday.', 'desc_len': 195, 'sports_score': 0, 'is_strict_sports': False}, {'title': "Oil and Economy Cloud Stocks' Outlook (Reuters)", 'description': 'Reuters - Soaring crude prices plus worries\\about the economy and the outlook for earnings are expected to\\hang over the stock market next week during the depth of the\\summer doldrums.', 'desc_len': 184, 'sports_score': 0, 'is_strict_sports': False}, {'title': 'Oil prices soar to all-time record, posing new menace to US economy (AFP)', 'description': 'AFP - Tearaway world oil prices, toppling records and straining wallets, present a new economic menace barely three months before the US presidential elections.', 'desc_len': 160, 'sports_score': 2, 'is_strict_sports': False}, {'title': 'Wall St. Bears Claw Back Into the Black (Reuters)', 'description': "Reuters - Short-sellers, Wall Street's dwindling\\band of ultra-cynics, are seeing green again.", 'desc_len': 94, 'sports_score': 1, 'is_strict_sports': False}], 'var_function-call-6235476327425017915': [{'_id': '6944814a2d282254f98124f6', 'article_id': '0', 'title': 'Wall St. Bears Claw Back Into the Black (Reuters)', 'description': "Reuters - Short-sellers, Wall Street's dwindling\\band of ultra-cynics, are seeing green again."}, {'_id': '6944814a2d282254f98124f7', 'article_id': '1', 'title': 'Carlyle Looks Toward Commercial Aerospace (Reuters)', 'description': 'Reuters - Private investment firm Carlyle Group,\\which has a reputation for making well-timed and occasionally\\controversial plays in the defense industry, has quietly placed\\its bets on another part of the market.'}, {'_id': '6944814a2d282254f98124f8', 'article_id': '2', 'title': "Oil and Economy Cloud Stocks' Outlook (Reuters)", 'description': 'Reuters - Soaring crude prices plus worries\\about the economy and the outlook for earnings are expected to\\hang over the stock market next week during the depth of the\\summer doldrums.'}, {'_id': '6944814a2d282254f98124f9', 'article_id': '3', 'title': 'Iraq Halts Oil Exports from Main Southern Pipeline (Reuters)', 'description': 'Reuters - Authorities have halted oil export\\flows from the main pipeline in southern Iraq after\\intelligence showed a rebel militia could strike\\infrastructure, an oil official said on Saturday.'}, {'_id': '6944814a2d282254f98124fa', 'article_id': '4', 'title': 'Oil prices soar to all-time record, posing new menace to US economy (AFP)', 'description': 'AFP - Tearaway world oil prices, toppling records and straining wallets, present a new economic menace barely three months before the US presidential elections.'}], 'var_function-call-15783133266262002332': 'file_storage/function-call-15783133266262002332.json', 'var_function-call-3928136129825934219': [{'title': 'Pretty Log4J', 'description': '\\\\I\'ve been a big fan of Log4J  for a while now but haven\'t migrated any code\\over for one central reason.  The following line of code:\\\\    final static Logger logger = Logger.getLogger( "some.name" );\\\\... is amazingly ugly and difficult to work with.\\\\Most people use Log4J with a logger based on the classname:\\\\So we would probably see:\\\\    static Logger logger = Logger.getLogger( "org.apache.commons.feedparser.locate.FeedLocator" );\\\\Which is amazingly verbose.  A lot of developers shorten this to:\\\\    static Logger logger = Logger.getLogger( FeedLocator.class );\\\\But this still leaves us with cut and paste errors.\\\\What if we could just reduce it to:\\\\    static Logger logger = Logger.g ...\\\\', 'len': 708, 'score': 2}, {'title': "Why Windows isn't Unix", 'description': '\\\\"I first heard about this from one of the developers of the hit game SimCity, who\\told me that there was a critical bug in his application: it used memory right\\after freeing it, a major no-no that happened to work OK on DOS but would not\\work under Windows where memory that is freed is likely to be snatched up by\\another running application right away. The testers on the Windows team were\\going through various popular applications, testing them to make sure they\\worked OK, but SimCity kept crashing. They reported this to the Windows\\developers, who disassembled SimCity, stepped through it in a debugger, found\\the bug, and added special code that checked if SimCity was running, and if it\\did ...\\\\', 'len': 708, 'score': 6}, {'title': 'China Begins Countdown for Next Manned Space Flight', 'description': 'By ELAINE KURTENBACH    SHANGHAI, China (AP) -- Chinese astronauts are in the final stages of preparing for a manned space mission that will orbit the globe 14 times before returning to Earth, a state-run newspaper reported Thursday.    The launch, expected sometime this month, will initially send a manned craft, the Shenzhou 5, into an oval orbit that at its closest will be 125 miles from Earth, the Liberation Daily reported, citing "relevant channels."    After circling the earth several times, the ship will enter an orbit at about 220 miles from earth, the report said...', 'len': 580, 'score': 6}, {'title': 'Customers of Telco Companies Face Privacy Breach', 'description': 'A security advisory posted on Bugtraq demonstrates how hackers can compromise customers of T-mobile wireless and Verizon (landline) voicemail boxes. The advisory talks about the use of Caller-ID spoofing the customers number, allowing a bypass of the PIN code since the voicemail thinks that the customer is calling to check their own voicemail. According to Secure Science Corporation, there has been no response from the vendors. Comments have been posted that T-Mobile has optional PIN code protection off by default. Better turn it on. ', 'len': 540, 'score': 1}, {'title': 'DiMarco, Riley Play Way Into Ryder Cup (AP)', 'description': "AP - Chris DiMarco and Chris Riley faced knee-knocking pressure in the last round of the PGA Championship. And what did they get for their efforts? More of the same. DiMarco and Riley played themselves into the pressure-packed Ryder Cup with their performances Sunday in the year's final major. DiMarco finished second after a three-man, three-hole playoff and Riley was fourth  #151; good enough to knock Jay Haas and Steve Flesch out of the top 10 in the Ryder Cup point standings.", 'len': 483, 'score': 10}]}

exec(code, env_args)
