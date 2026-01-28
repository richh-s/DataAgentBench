code = """import json
import pandas as pd
import re

# Load the languages file to identify Swift repositories
with open('var_functions.query_db:16', 'r') as f:
    languages_data = json.load(f)

# Load the Swift files contents
with open('var_functions.query_db:18', 'r') as f:
    swift_files = json.load(f)

print('Total Swift repositories: ' + str(len(languages_data)))
print('Total Swift files: ' + str(len(swift_files)))

# Create a set of Swift repository names for quick lookup
swift_repos = set(row['repo_name'] for row in languages_data)
print('Unique Swift repository names: ' + str(len(swift_repos)))

# Process Swift files - extract copy counts
file_copy_counts = []

for file in swift_files:
    # Check if file is from a Swift repository
    if file['sample_repo_name'] in swift_repos:
        # Parse the repo_data_description to get copy count
        desc = file['repo_data_description']
        
        # Extract copy count using regex
        match = re.search(r'(appears|duplicated|copied)\s+(\d+)\s+times', desc)
        if match:
            copy_count = int(match.group(2))
            file_copy_counts.append({
                'id': file['id'],
                'repo_name': file['sample_repo_name'],
                'path': file['sample_path'],
                'description': desc,
                'copy_count': copy_count
            })

# Find file with max copies
if file_copy_counts:
    max_copies = max(f['copy_count'] for f in file_copy_counts)
    most_copied_files = [f for f in file_copy_counts if f['copy_count'] == max_copies]
    
    print('Maximum copy count: ' + str(max_copies))
    print('Number of files with max copies: ' + str(len(most_copied_files)))
    
    # Show the files with max copies
    for f in most_copied_files[:10]:  # Show first 10
        print('\nFile: ' + f['path'])
        print('Repository: ' + f['repo_name'])
        print('Copy count: ' + str(f['copy_count']))

result = {'files_processed': len(file_copy_counts), 'max_copies': max_copies if file_copy_counts else 0}
print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.list_db:0': ['languages', 'repos', 'licenses'], 'var_functions.query_db:2': [{'id': 'b03a39b4e07f98073fcf2fbe945bf1291cbfeca7', 'content': '//\n//  Record.swift\n//  Shared CoreData\n//\n//  Created by Konstantin Koval on 24/12/14.\n//  Copyright (c) 2014 Konstantin Koval. All rights reserved.\n//\n\nimport Foundation\nimport CoreData\n\n@objc(Record)\npublic class Record: NSManagedObject {\n\n    @NSManaged public var timestamp: NSDate\n\n}\n', 'sample_repo_name': 'kostiakoval/WatchKit-Apps', 'sample_ref': 'refs/heads/master', 'sample_path': '5- Shared-CoreData/SharedKit/Record.swift', 'sample_symlink_target': 'None', 'repo_data_description': 'With a file size of 290 bytes and sample mode 33188, this non-binary file is duplicated 8 times.'}, {'id': '3909cba31dd8c36766ee8efd9299c75a7e9f8721', 'content': '// RUN: not %target-swift-frontend %s -parse\n\n// Distributed under the terms of the MIT license\n// Test case submitted to project by https://github.com/practicalswift (practicalswift)\n// Test case found by fuzzing\n\nimport a}class S<T{func a<h{func b<T where h.g=a}}if{struct v\n', 'sample_repo_name': 'slavapestov/swift', 'sample_ref': 'refs/heads/master', 'sample_path': 'validation-test/compiler_crashers_fixed/27617-swift-markasobjc.swift', 'sample_symlink_target': 'None', 'repo_data_description': 'A 277-byte non-binary file appearing 8 times, with sample mode code 33188.'}, {'id': 'f7a67dcc0bda7a58e7e1a37d483bfd06e5ff9208', 'content': '//\n//  AppDelegate.swift\n//  Example\n//\n//  Created by Gunay Mert Karadogan on 29/7/15.\n//  Copyright (c) 2015 Gunay Mert Karadogan. All rights reserved.\n//\n\nimport UIKit\n\n@UIApplicationMain\nclass AppDelegate: UIResponder, UIApplicationDelegate {\n\n    var window: UIWindow?\n\n\n    func application(application: UIApplication, didFinishLaunchingWithOptions launchOptions: [NSObject: AnyObject]?) -> Bool {\n        // Override point for customization after application launch.\n        return true\n    }\n\n    func applicationWillResignActive(application: UIApplication) {\n        // Sent when the application is about to move from active to inactive state. This can occur for certain types of temporary interruptions (such as an incoming phone call or SMS message) or when the user quits the application and it begins the transition to the background state.\n        // Use this method to pause ongoing tasks, disable timers, and throttle down OpenGL ES frame rates. Games should use this method to pause the game.\n    }\n\n    func applicationDidEnterBackground(application: UIApplication) {\n        // Use this method to release shared resources, save user data, invalidate timers, and store enough application state information to restore your application to its current state in case it is terminated later.\n        // If your application supports background execution, this method is called instead of applicationWillTerminate: when the user quits.\n    }\n\n    func applicationWillEnterForeground(application: UIApplication) {\n        // Called as part of the transition from the background to the inactive state; here you can undo many of the changes made on entering the background.\n    }\n\n    func applicationDidBecomeActive(application: UIApplication) {\n        // Restart any tasks that were paused (or not yet started) while the application was inactive. If the application was previously in the background, optionally refresh the user interface.\n    }\n\n    func applicationWillTerminate(application: UIApplication) {\n        // Called when the application is about to terminate. Save data if appropriate. See also applicationDidEnterBackground:.\n    }\n\n\n}\n\n', 'sample_repo_name': 'gmertk/BusyNavigationBar', 'sample_ref': 'refs/heads/master', 'sample_path': 'BusyNavigationBar/Example/AppDelegate.swift', 'sample_symlink_target': 'None', 'repo_data_description': 'This file has a size of 2161 bytes, is non-binary, and appears 9 times with sample mode 33188.'}, {'id': '15492da9a0490415a84fa6c1a7957e473ebfa4db', 'content': '// Distributed under the terms of the MIT license\n// Test case submitted to project by https://github.com/practicalswift (practicalswift)\n// Test case found by fuzzing\n\nstruct Q{struct B{}struct B<T where B:A{}struct B<T where T:e{struct B\n', 'sample_repo_name': 'practicalswift/swift-compiler-crashes', 'sample_ref': 'refs/heads/master', 'sample_path': 'crashes-duplicates/25255-swift-typechecker-checkinheritanceclause.swift', 'sample_symlink_target': 'None', 'repo_data_description': 'With a file size of 240 bytes and sample mode 33188, this non-binary file is duplicated 10 times.'}, {'id': '41d65e7ae98cc15b6e5eacfd11568e1a851b6add', 'content': '// Distributed under the terms of the MIT license\n// Test case submitted to project by https://github.com/practicalswift (practicalswift)\n// Test case found by fuzzing\n\nstruct S<T where h:a{class a{let f=Void}let f=o{\n', 'sample_repo_name': 'practicalswift/swift-compiler-crashes', 'sample_ref': 'refs/heads/master', 'sample_path': 'crashes-duplicates/26498-swift-sourcefile-lookupcache-lookupvalue.swift', 'sample_symlink_target': 'None', 'repo_data_description': 'A 218-byte non-binary file appearing 10 times, with sample mode code 33188.'}], 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json', 'var_functions.query_db:6': 'file_storage/functions.query_db:6.json', 'var_functions.query_db:16': 'file_storage/functions.query_db:16.json', 'var_functions.query_db:18': 'file_storage/functions.query_db:18.json'}

exec(code, env_args)
