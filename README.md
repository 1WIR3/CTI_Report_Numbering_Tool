# CTI_Report_Numbering_Tool

CTI Report Naming Utility

Description

The CTI Report Naming Utility is a Python-based tool designed to generate unique and consistent report identifiers for Cyber Threat Intelligence (CTI) reports. It follows a configurable naming convention and helps organize and manage CTI data effectively.

Features

* Unique Report ID Generation: Generates report IDs based on source, report type, and date, with a sequential number for each day.
* Configurable Naming Scheme: The naming scheme is source-report_type-YYYYMMDD-NN, where:
    * source: The source of the CTI data (e.g., "VendorA", "InternalResearch").
    * report_type: The type of report (e.g., "ThreatReport", "ActivityReport").
    * YYYYMMDD: The date of the report.
    * NN: A two-digit sequential number for reports generated on the same day for the same source and report type.
* Report Descriptions: Allows users to add a description to each report, providing context.
* Output to File: Saves generated report IDs and their descriptions to a text file.
* Configuration File: Uses a JSON configuration file (cti_naming_config.json) to store settings, including:
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

The tool uses a JSON configuration file (cti_naming_config.json) to store its settings. You can customize the following:

* report_counts: A dictionary that stores the count of reports generated for each source, report type, and date. This is managed by the application.
* generated_report_ids: A list of all generated report IDs. This is managed by the application.
* report_descriptions: A dictionary of descriptions for each report ID. This is managed by the application.
* base_filename: The default filename for saving report IDs (e.g., "report_ids.txt").
* valid_sources: A list of valid report sources (e.g., ["VendorA", "InternalResearch", "TeamB"]).
* valid_report_types: A list of valid report types (e.g., ["ThreatReport", "ActivityReport", "VulnerabilityReport"]).

Example cti_naming_config.json:

{
    "report_counts": {},
    "generated_report_ids": [],
    "report_descriptions": {},
    "base_filename": "cti_reports.txt",
    "valid_sources": ["Vendor1", "Vendor2", "Internal"],
    "valid_report_types": ["Threat", "Activity", "Indicator"]
}

Usage

1.  Installation:
    * Ensure you have Python 3.6 or later installed.
    * Save the cti_naming.py script and the cti_naming_config.json file in the same directory.
2.  Configuration (Optional):
    * Modify the cti_naming_config.json file to customize the valid sources, report types, and default filename. If the file does not exist, the application will create it with default values.
3.  Running the Tool:
    * Open a terminal or command prompt.
    * Navigate to the directory where you saved the files.
    * Run the script: python cti_naming.py
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
