CTI and VirusTotal Naming Utilities

Description

This suite of Python-based tools is designed to generate unique and consistent identifiers for Cyber Threat Intelligence (CTI) reports and VirusTotal resources, specifically collections and graphs. The tools follow configurable naming conventions to help organize and manage CTI data and VirusTotal artifacts effectively.

Tools

* CTI Report Naming Utility: Generates identifiers for CTI reports.
* VirusTotal Naming Tool: Generates identifiers for VirusTotal collections and graphs.

CTI Report Naming Utility

Features

* Unique Report ID Generation: Generates report IDs based on source, report type, and date, with a sequential number for each day.
* Configurable Naming Scheme: The naming scheme is source-report\_type-YYYYMMDD-NN, where:
    * source: The source of the CTI data (e.g., "VendorA", "InternalResearch").
    * report\_type: The type of report (e.g., "ThreatReport", "ActivityReport").
    * YYYYMMDD: The date of the report.
    * NN: A two-digit sequential number for reports generated on the same day for the same source and report type.
* Report Descriptions: Allows users to add a description to each report, providing context.
* Output to File: Saves generated report IDs and their descriptions to a text file.
* Configuration File: Uses a JSON configuration file (cti\_naming\_config.json) to store settings.
* Input Validation: Validates user-provided report source and report type against the values defined in the configuration file.
* Display All Reports: Displays all generated report IDs and their descriptions.
* Set Output Filename: Allows the user to specify the filename for saving report IDs.
* Load/Save Configuration: Loads configuration at startup and saves it after changes.

VirusTotal Naming Tool

Features

* Unique Collection ID Generation: Generates unique identifiers for VirusTotal collections, including source and date.
* Collection Descriptions: Allows users to add descriptions to VirusTotal collections.
* Unique Graph ID Generation: Generates unique identifiers for VirusTotal graphs, including source and date.
* Configurable Naming Schemes:
    * Collections: COL-source-YYYYMMDD-NN
    * Graphs: GRAPH-source-YYYYMMDD-NN
* Output to File: Saves generated collection and graph IDs (and descriptions for collections) to a text file.
* Configuration File: Uses a JSON configuration file (vt\_naming\_config.json) to store settings.
* Input Validation: Validates user-provided sources against configured values.
* Display All Generated IDs: Displays all generated collection and graph IDs (and descriptions).
* Set Output Filename: Allows the user to specify the filename for saving IDs.
* Load/Save Configuration: Loads configuration at startup and saves it after changes.

Configuration

Both tools use JSON configuration files to store their settings.

* CTI Report Naming Utility (cti\_naming\_config.json):
    * report\_counts: A dictionary that stores the count of reports generated for each source, report type, and date.
    * generated\_report\_ids: A list of all generated report IDs.
    * report\_descriptions: A dictionary of descriptions for each report ID.
    * base\_filename: The default filename for saving report IDs (e.g., "cti\_reports.txt").
    * valid\_sources: A list of valid report sources (e.g., \["Vendor1", "Internal", "TeamB"]).
    * valid\_report\_types: A list of valid report types (e.g., \["Threat", "Activity", "Vulnerability"]).
* VirusTotal Naming Tool (vt\_naming\_config.json):
    * collection\_counts: Counters for collections.
    * generated\_collection\_ids: Generated collection IDs.
    * collection\_descriptions: Descriptions for collections.
    * graph\_counts: Counters for graphs.
    * generated\_graph\_ids: Generated graph IDs.
    * base\_filename: Default filename (e.g., "vt\_names.txt").
    * valid\_collection\_sources: Valid sources for collections.
    * valid\_graph\_sources: Valid sources for graphs.

Example Configuration Files

* cti\_naming\_config.json:

    {
        "report\_counts": {},
        "generated\_report\_ids": \[\],
        "report\_descriptions": {},
        "base\_filename": "cti\_reports.txt",
        "valid\_sources": \["Vendor1", "Vendor2", "Internal"\],
        "valid\_report\_types": \["Threat", "Activity", "Indicator"\]
    }

* vt\_naming\_config.json:

    {
        "collection\_counts": {},
        "generated\_collection\_ids": \[\],
        "collection\_descriptions": {},
        "graph\_counts": {},
        "generated\_graph\_ids": \[\],
        "base\_filename": "vt\_names.txt",
        "valid\_collection\_sources": \["Analyst1", "TeamX"\],
        "valid\_graph\_sources": \["Analyst1", "ScriptY"\]
    }

Usage

1.  Installation:

    * Ensure you have Python 3.6 or later installed.
    * Save the .py script and the corresponding .json configuration file in a directory.

2.  Configuration (Optional):

    * Modify the cti\_naming\_config.json and vt\_naming\_config.json files to customize the settings. If the files do not exist, the applications will create them with default values.

3.  Running the Tools:

    * Open a terminal or command prompt.
    * Navigate to the directory where you saved the files.
    * Run the desired script:
        * CTI Report Naming Utility: python cti\_naming.py
        * VirusTotal Naming Tool: python vt\_naming.py

4.  Interactive Menus:

    * Each tool provides a command-line menu with options specific to its functionality.

### CTI Report Naming Utility

    CTI Report Naming Utility
    1.  Generate Report ID
    2.  Save Report IDs to File
    3.  Get Report Description
    4.  Set Output Filename
    5.  Display All Reports
    6.  Exit
    Enter your choice:

### VirusTotal Naming Tool

    VirusTotal Naming Tool
    1.  Generate Collection ID
    2.  Generate Graph ID
    3.  Save IDs to File
    4.  Get Collection Description
    5.  Display All Generated IDs
    6.  Set Output Filename
    7.  Exit
    Enter your choice:

Using the Tools in a CMMI/DoD CM Process for MITRE CTI Authoring

Here's a process for integrating the CTI Report Naming Utility and the VirusTotal Naming Tool into a CMMI-like or DoD Configuration Management (CM) process, specifically for use with a MITRE CTI authoring tool:

1.  Configuration Identification:

    * Define Report Types:
        * Establish a controlled vocabulary of report types relevant to your organization and the MITRE ATT\&CK framework.
        * Align these with the tool's valid\_report\_types in cti\_naming\_config.json.
    * Define Collection/Graph Sources:
        * Establish controlled vocabularies for sources of VirusTotal collections and graphs.
        * Align these with valid\_collection\_sources and valid\_graph\_sources in vt\_naming\_config.json.
    * Set Naming Conventions:
        * The tools enforce the following:
            * CTI Reports: source-report\_type-YYYYMMDD-NN
            * VirusTotal Collections: COL-source-YYYYMMDD-NN
            * VirusTotal Graphs: GRAPH-source-YYYYMMDD-NN
        * Document these as the official naming conventions in your CM plan.
    * Establish Configuration Items (CIs):
        * Treat each CTI report, VirusTotal collection, and VirusTotal graph as a CI. The generated identifiers become the unique identifiers for these CIs.
    * Version Control:
        * While the tools themselves don't handle versioning, your CM system should. Incorporate the generated identifiers into your versioning scheme (e.g., ReportID\_v1.0, CollectionID\_v1.1, GraphID\_v2.0).

2.  Configuration Control:

    * Report/Collection/Graph Creation:
        * When a CTI analyst creates a new report using the MITRE CTI authoring tool, or creates a VirusTotal collection/graph:
            * The analyst uses the appropriate naming tool to generate the identifier.
            * The analyst enters the required data into the naming tool.
            * The tool generates the unique identifier.
            * The analyst includes the identifier in the CTI report document or in the VirusTotal resource's metadata.
            * The resource and its associated identifier are then managed under your organization's CM system.
    * Change Control:
        * If a resource needs to be updated:
            * Follow your organization's change control process.
            * The CM system will create a new version of the resource, incorporating the original identifier and a version number.
    * Documentation:
        * Document the process in a CM Plan.

3.  Configuration Status Accounting:

    * Record Keeping:
        * Maintain a record of all generated identifiers and their associated metadata within the CM system.
    * Reporting:
        * Generate reports from the CM system to track the status of resources, including their identifiers, versions, and any changes.

4.  Configuration Audit:

    * Audits:
        * Periodically audit the resource repositories to ensure that:
            * All items have valid identifiers.
            * Identifiers are being used correctly.
            * The CM process is being followed.
