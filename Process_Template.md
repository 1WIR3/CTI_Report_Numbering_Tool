#CTI Data Management Tools

##CTI Report Naming Utility

Description

The CTI Report Naming Utility is a Python-based tool designed to generate unique and consistent report identifiers for Cyber Threat Intelligence (CTI) reports. It follows a configurable naming convention and helps organize and manage CTI data effectively.

Features

* Unique Report ID Generation: Generates report IDs based on source, report type, and date, with a sequential number for each day.
* Configurable Naming Scheme: The naming scheme is source-report\_type-YYYYMMDD-NN, where:
    * source: The source of the CTI data (e.g., "VendorA", "InternalResearch").
    * report\_type: The type of report (e.g., "ThreatReport", "ActivityReport").
    * YYYYMMDD: The date of the report.
    * NN: A two-digit sequential number for reports generated on the same day for the same source and report type.
* Report Descriptions: Allows users to add a description to each report, providing context.
* Output to File: Saves generated report IDs and their descriptions to a text file.
* Configuration File: Uses a JSON configuration file (cti\_naming\_config.json) to store settings, including:
    * Report number counters.
    * Generated report IDs and descriptions.
    * Output filename.
    * Valid report sources.
    * Valid report types.
* Input Validation: Validates user-provided report source and report type against the values defined in the configuration file.
* Display All Reports: Displays all generated report IDs and their descriptions.
* Set Output Filename: Allows the user to specify the filename for saving report IDs.
* Load/Save Configuration: Loads configuration at startup and saves it after changes, ensuring data persistence.

Configuration

The tool uses a JSON configuration file (cti\_naming\_config.json) to store its settings. You can customize the following:

* report\_counts: A dictionary that stores the count of reports generated for each source, report type, and date. This is managed by the application.
* generated\_report\_ids: A list of all generated report IDs. This is managed by the application.
* report\_descriptions: A dictionary of descriptions for each report ID. This is managed by the application.
* base\_filename: The default filename for saving report IDs (e.g., "report\_ids.txt").
* valid\_sources: A list of valid report sources (e.g., \["VendorA", "InternalResearch", "TeamB"]).
* valid\_report\_types: A list of valid report types (e.g., \["ThreatReport", "ActivityReport", "VulnerabilityReport"]).

Example cti\_naming\_config.json:

{
    "report\_counts": {},
    "generated_report_ids": \[\],
    "report\_descriptions": {},
    "base\_filename": "cti\_reports.txt",
    "valid\_sources": \["Vendor1", "Vendor2", "Internal"\],
    "valid\_report\_types": \["Threat", "Activity", "Indicator"\]
}

Usage

1.  Installation:
    * Ensure you have Python 3.6 or later installed.
    * Save the cti\_naming.py script and the cti\_naming\_config.json file in the same directory.
2.  Configuration (Optional):
    * Modify the cti\_naming\_config.json file to customize the valid sources, report types, and default filename. If the file does not exist, the application will create it with default values.
3.  Running the Tool:
    * Open a terminal or command prompt.
    * Navigate to the directory where you saved the files.
    * Run the script: python cti\_naming.py
4.  Interactive Menu:
    The tool provides a command-line menu with the following options:
    * 1\. Generate Report ID:
        * Prompts you to enter the report source, report type, report date (YYYYMMDD format, press Enter for today), and an optional description.
        * Validates the source and report type against the configured values.
        * Generates a unique report ID and displays it.
    * 2\. Save Report IDs to File:
        * Prompts you to enter a filename to save the generated report IDs and descriptions (default: the value set in the config file).
        * Saves the data to the specified file.
    * 3\. Get Report Description:
        * Prompts you to enter a report ID.
        * Retrieves and displays the description for the given report ID.
    * 4\. Set Output Filename:
        * Prompts you to enter a new filename for saving report IDs.
        * Updates the configuration file with the new filename.
    * 5\. Display All Reports:
        * Displays all generated report IDs and their descriptions.
    * 6\. Exit:
        * Exits the application.

Example Session

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
Enter filename to save report IDs (default: cti\_reports.txt):

Report IDs and descriptions saved to cti\_reports.txt

CTI Report Naming Utility

1.  Generate Report ID
2.  Save Report IDs to File
3.  Get Report Description
4.  Set Output Filename
5.  Display All Reports
6.  Exit
Enter your choice: 6
Exiting...

##   Using the Tool in a CMMI/DoD CM Process for MITRE CTI Authoring

Here's a process for integrating the CTI Report Naming Utility into a CMMI-like or DoD Configuration Management (CM) process, specifically for use with a MITRE CTI authoring tool:

**1. Configuration Identification:**

* Define Report Types:
    * Establish a controlled vocabulary of report types relevant to your organization and the MITRE ATT&CK framework (e.g., Threat Report, Intrusion Analysis, Campaign Report).  Align these with the tool's `valid_report_types` in `cti_naming_config.json`.
    * Define data sources.  Align these with the tool's `valid_sources` in  `cti_naming_config.json`.
* Set Naming Convention:
    * The tool enforces `source-report_type-YYYYMMDD-NN`.  Document this as the official naming convention in your CM plan.
* Establish Configuration Items (CIs):
    * Treat each CTI report as a CI.  The generated Report ID becomes the unique identifier for each CI.
* Version Control:
     * While the tool itself doesn't handle versioning, your CM system should.  Incorporate the Report ID into your versioning scheme (e.g., ReportID\_v1.0, ReportID\_v1.1).

**2. Configuration Control:**

* Report Creation:
    * When a CTI analyst creates a new report using the MITRE CTI authoring tool:
        * The analyst uses the CTI Report Naming Utility to generate the Report ID.
        * The analyst enters the required data (source, report type, date, description) into the CTI Report Naming Utility.
        * The tool generates the unique Report ID.
        * The analyst includes the Report ID in the CTI report document (e.g., in the document header or metadata).
        * The CTI report and its associated Report ID are then managed under your organization's CM system. This includes version control, change control, and storage.
* Change Control:
    * If the CTI report needs to be updated:
        * Follow your organization's change control process.
        * The CM system will create a new version of the CTI report, incorporating the original Report ID and a version number.
* Documentation:
     * Document the process in a CM Plan.

**3. Configuration Status Accounting:**

* Record Keeping:
    * Maintain a record of all generated Report IDs and their associated metadata (source, report type, date, description) within the CM system.  The tool can save to a file, but this should be integrated into a more robust CM database.
* Reporting:
    * Generate reports from the CM system to track the status of CTI reports, including their Report IDs, versions, and any changes.

**4. Configuration Audit:**

* Audits:
    * Periodically audit the CTI report repository to ensure that:
        * All reports have valid Report IDs.
        * Report IDs are being used correctly in accordance with the naming convention.
        * The CM process is being followed.

This process ensures that CTI reports are managed in a controlled and consistent manner, aligning with CMMI and DoD CM principles.
