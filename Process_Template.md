&lt;ctrl98>Okay, here's the updated process description to include the VirusTotal Naming Tool:

CTI and VirusTotal Naming Utilities

Description

This suite of Python-based tools is designed to generate unique and consistent identifiers for Cyber Threat Intelligence (CTI) reports and VirusTotal resources, specifically collections and graphs. The tools follow configurable naming conventions to help organize and manage CTI data and VirusTotal artifacts effectively.

Tools

CTI Report Naming Utility: Generates identifiers for CTI reports.
VirusTotal Naming Tool: Generates identifiers for VirusTotal collections and graphs.
CTI Report Naming Utility

Features

Unique Report ID Generation: Generates report IDs based on source, report type, and date, with a sequential number for each day.
Configurable Naming Scheme: The naming scheme is source-report_type-YYYYMMDD-NN, where:
source: The source of the CTI data (e.g., "VendorA", "InternalResearch").
report_type: The type of report (e.g., "ThreatReport", "ActivityReport").
YYYYMMDD: The date of the report.
NN: A two-digit sequential number for reports generated on the same day for the same source and report type.
Report Descriptions: Allows users to add a description to each report, providing context.
Output to File: Saves generated report IDs and their descriptions to a text file.
Configuration File: Uses a JSON configuration file (cti_naming_config.json) to store settings, including:
Report number counters.
Generated report IDs and descriptions.
Output filename.
Valid report sources.
Valid report types.
Input Validation: Validates user-provided report source and report type against the values defined in the configuration file.
Display All Reports: Displays all generated report IDs and their descriptions.
Set Output Filename: Allows the user to specify the filename for saving report IDs.
Load/Save Configuration: Loads configuration at startup and saves it after changes, ensuring data persistence.
VirusTotal Naming Tool

Features

Unique Collection ID Generation: Generates unique identifiers for VirusTotal collections, including source and date.
Collection Descriptions: Allows users to add descriptions to VirusTotal collections.
Unique Graph ID Generation: Generates unique identifiers for VirusTotal graphs, including source and date.
Configurable Naming Schemes:
Collections: COL-source-YYYYMMDD-NN
Graphs: GRAPH-source-YYYYMMDD-NN
Output to File: Saves generated collection and graph IDs (and descriptions for collections) to a text file.
Configuration File: Uses a JSON configuration file (vt_naming_config.json) to store settings, including:
Counters for collections and graphs.
Generated IDs and descriptions.
Output filename.
Valid sources for collections.
Valid sources for graphs.
Input Validation: Validates user-provided sources against configured values.
Display All Generated IDs: Displays all generated collection and graph IDs (and descriptions).
Set Output Filename: Allows the user to specify the filename for saving IDs.
Load/Save Configuration: Loads configuration at startup and saves it after changes.
Configuration

Both tools use JSON configuration files to store their settings.

CTI Report Naming Utility (cti_naming_config.json):
report_counts: A dictionary that stores the count of reports generated for each source, report type, and date.
generated_report_ids: A list of all generated report IDs.
report_descriptions: A dictionary of descriptions for each report ID.
base_filename: The default filename for saving report IDs (e.g., "cti_reports.txt").
valid_sources: A list of valid report sources (e.g., ["Vendor1", "Internal", "TeamB"]).
valid_report_types: A list of valid report types (e.g., ["Threat", "Activity", "Vulnerability"]).
VirusTotal Naming Tool (vt_naming_config.json):
collection_counts: Counters for collections.
generated_collection_ids: Generated collection IDs.
collection_descriptions: Descriptions for collections.
graph_counts: Counters for graphs.
generated_graph_ids: Generated graph IDs.
base_filename: Default filename (e.g., "vt_names.txt").
valid_collection_sources: Valid sources for collections.
valid_graph_sources: Valid sources for graphs.
Example Configuration Files

cti_naming_config.json:

JSON

{
    "report_counts": {},
    "generated_report_ids": [],
    "report_descriptions": {},
    "base_filename": "cti_reports.txt",
    "valid_sources": ["Vendor1", "Vendor2", "Internal"],
    "valid_report_types": ["Threat", "Activity", "Indicator"]
}
vt_naming_config.json:

JSON

{
    "collection_counts": {},
    "generated_collection_ids": [],
    "collection_descriptions": {},
    "graph_counts": {},
    "generated_graph_ids": [],
    "base_filename": "vt_names.txt",
    "valid_collection_sources": ["Analyst1", "TeamX"],
    "valid_graph_sources": ["Analyst1", "ScriptY"]
}
Usage

Installation:

Ensure you have Python 3.6 or later installed.
Save the cti_naming.py and cti_naming_config.json files for the CTI Report Naming Utility, and the vt_naming.py and vt_naming_config.json files for the VirusTotal Naming Tool, in appropriate directories.
Configuration (Optional):

Modify the cti_naming_config.json and vt_naming_config.json files to customize the settings, including valid sources, report/collection/graph types, and default filenames. If the files do not exist, the applications will create them with default values.
Running the Tools:

Open a terminal or command prompt.
Navigate to the directory where you saved the files.
Run the desired script:
CTI Report Naming Utility: python cti_naming.py
VirusTotal Naming Tool: python vt_naming.py
Interactive Menus:

Each tool provides a command-line menu with options specific to its functionality:

CTI Report Naming Utility:

1. Generate Report ID: Prompts for source, report type, date, and description.
2. Save Report IDs to File: Saves generated IDs and descriptions.
3. Get Report Description: Retrieves a report description.
4. Set Output Filename: Sets the filename for saving.
5. Display All Reports: Displays all generated reports.
6. Exit.
VirusTotal Naming Tool:

1. Generate Collection ID: Prompts for source, date, and description.
2. Generate Graph ID: Prompts for source and date.
3. Save IDs to File: Saves generated IDs.
4. Get Collection Description: Retrieves a collection description.
5. Display All Generated IDs: Displays all generated IDs.
6. Set Output Filename: Sets the filename for saving.
7. Exit.
Example Sessions

CTI Report Naming Utility:

CTI Report Naming Utility
1.  Generate Report ID
2.  Save Report IDs to File
3.  Get Report Description
4.  Set Output Filename
5.  Display All Reports
6.  Exit
Enter your choice: 1
Enter report source (['Vendor1', 'Vendor2', 'Internal']): Internal
Enter report type (['Threat', 'Activity', 'Indicator']): Threat
Enter report date (YYYYMMDD, press Enter for today): 20240115
Enter report description (optional): Initial threat assessment
Generated Report ID: Internal-Threat-20240115-01

CTI Report Naming Utility
1.  Generate Report ID
2.  Save Report IDs to File
3.  Get Report Description
4.  Set Output Filename
5.  Display All Reports
6.  Exit
Enter your choice: 2
Enter filename to save report IDs (default: cti_reports.txt):

Report IDs and descriptions saved to cti_reports.txt

CTI Report Naming Utility
1.  Generate Report ID
2.  Save Report IDs to File
3.  Get Report Description
4.  Set Output Filename
5.  Display All Reports
6.  Exit
Enter your choice: 6
Exiting...
VirusTotal Naming Tool:

VirusTotal Naming Tool
1.  Generate Collection ID
2.  Generate Graph ID
3.  Save IDs to File
4.  Get Collection Description
5.  Display All Generated IDs
6.  Set Output Filename
7.  Exit
Enter your choice: 1
Enter collection source (['Analyst1', 'TeamX']): Analyst1
Enter collection date (YYYYMMDD, press Enter for today): 20240220
Enter collection description (optional): Files related to campaign XYZ
Generated Collection ID: COL-Analyst1-20240220-01

VirusTotal Naming Tool
1.  Generate Collection ID
2.  Generate Graph ID
3.  Save IDs to File
4.  Get Collection Description
5.  Display All Generated IDs
6.  Set Output Filename
7.  Exit
Enter your choice: 2
Enter graph source (['Analyst1', 'ScriptY']): ScriptY
Enter graph date (YYYYMMDD, press Enter for today): 20240220
Generated Graph ID: GRAPH-ScriptY-20240220-01

VirusTotal Naming Tool
1.  Generate Collection ID
2.  Generate Graph ID
3.  Save IDs to File
4.  Get Collection Description
5.  Display All Generated IDs
6.  Set Output Filename
7.  Exit
Enter your choice: 3
Enter filename to save IDs (default: vt_names.txt):
IDs and descriptions saved to vt_names.txt

VirusTotal Naming Tool
1.  Generate Collection ID
2.  Generate Graph ID
3.  Save IDs to File
4.  Get Collection Description
5.  Display All Generated IDs
6.  Set Output Filename
7.  Exit
Enter your choice: 7
Exiting...
Using the Tools in a CMMI/DoD CM Process for MITRE CTI Authoring

Here's a process for integrating the CTI Report Naming Utility and the VirusTotal Naming Tool into a CMMI-like or DoD Configuration Management (CM) process, specifically for use with a MITRE CTI authoring tool:

1. Configuration Identification:

Define Report Types:
Establish a controlled vocabulary of report types relevant to your organization and the MITRE ATT&amp;CK framework (e.g., Threat Report, Intrusion Analysis, Campaign Report). Align these with the tool's valid_report_types in cti_naming_config.json.
Define data sources. Align these with the tool's valid_sources in cti_naming_config.json.
Define Collection/Graph Sources:
Establish controlled vocabularies for sources of VirusTotal collections and graphs (e.g., "Analyst1", "TeamX", "AutomationScript"). Align these with valid_collection_sources and valid_graph_sources in vt_naming_config.json.
Set Naming Conventions:
The tools enforce the following:
CTI Reports: source-report_type-YYYYMMDD-NN
VirusTotal Collections: COL-source-YYYYMMDD-NN
VirusTotal Graphs: GRAPH-source-YYYYMMDD-NN
Document these as the official naming conventions in your CM plan.
Establish Configuration Items (CIs):
Treat each CTI report, VirusTotal collection, and VirusTotal graph as a CI. The generated identifiers become the unique identifiers for these CIs.
Version Control:
While the tools themselves don't handle versioning, your CM system should. Incorporate the generated identifiers into your versioning scheme (e.g., ReportID_v1.0, CollectionID_v1.1, GraphID_v2.0).
2. Configuration Control:

Report/Collection/Graph Creation:
When a CTI analyst creates a new report using the MITRE CTI authoring tool, or creates a VirusTotal collection/graph:
The analyst uses the appropriate naming tool to generate the identifier.
The analyst enters the required data (source, report/collection/graph type, date, description) into the naming tool.
The tool generates the unique identifier.
The analyst includes the identifier in the CTI report document or in the VirusTotal resource's metadata.
The resource and its associated identifier are then managed under your organization's CM system. This includes version control, change control, and storage.
Change Control:
If a CTI report or VirusTotal collection/graph needs to be updated:
Follow your organization's change control process.
The CM system will create a new version of the resource, incorporating the original identifier and a version number.
Documentation:
Document the process in a CM Plan.
3. Configuration Status Accounting:

Record Keeping:
Maintain a record of all generated identifiers and their associated metadata (source, type/date, description) within the CM system. The tools can save to files, but this should ideally be integrated into a more robust CM database.
Reporting:
Generate reports from the CM system to track the status of CTI reports, VirusTotal collections, and VirusTotal graphs, including their identifiers, versions, and any changes.
4. Configuration Audit:

Audits:
Periodically audit the resource repositories to ensure that:
All items have valid identifiers.
Identifiers are being used correctly in accordance with the naming conventions.
The CM process is being followed.
