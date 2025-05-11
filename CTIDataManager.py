import datetime
import os
import json  # Import the json module

class CTINaming:
    """
    A class to generate CTI report names and numbers according to a defined scheme.
    """
    def __init__(self):
        """
        Initializes the CTINaming class.
        """
        self.report_counts = {}
        self.generated_report_ids = []
        self.report_descriptions = {}
        self.config_file = "cti_naming_config.json"  # Configuration file name
        self.load_config()  # Load configuration at initialization

    def load_config(self):
        """Loads configuration from a JSON file."""
        if os.path.exists(self.config_file):
            try:
                with open(self.config_file, "r") as f:
                    config = json.load(f)
                    # Load settings, providing defaults if they are not in the config file
                    self.report_counts = config.get("report_counts", {})
                    self.generated_report_ids = config.get("generated_report_ids", [])
                    self.report_descriptions = config.get("report_descriptions", {})
                    self.base_filename = config.get("base_filename", "report_ids.txt")  # Default filename
                    self.valid_sources = config.get("valid_sources", [])  # Load valid sources
                    self.valid_report_types = config.get("valid_report_types", [])  # Load valid types
                    print("Configuration loaded from", self.config_file)
            except json.JSONDecodeError:
                print("Error: Invalid JSON in configuration file.  Using default settings.")
                self.report_counts = {}
                self.generated_report_ids = []
                self.report_descriptions = {}
                self.base_filename = "report_ids.txt"
                self.valid_sources = []
                self.valid_report_types = []
        else:
            print("Configuration file not found. Using default settings.")
            self.base_filename = "report_ids.txt"  # Default filename
            self.valid_sources = []  # Default to empty list if not in config
            self.valid_report_types = []

    def save_config(self):
        """Saves configuration to a JSON file."""
        config = {
            "report_counts": self.report_counts,
            "generated_report_ids": self.generated_report_ids,
            "report_descriptions": self.report_descriptions,
            "base_filename": self.base_filename,
            "valid_sources": self.valid_sources,  # Save valid sources
            "valid_report_types": self.valid_report_types,  # Save valid report types
        }
        try:
            with open(self.config_file, "w") as f:
                json.dump(config, f, indent=4)
            print("Configuration saved to", self.config_file)
        except Exception as e:
            print(f"Error saving configuration: {e}")

    def generate_report_id(self, source, report_type, report_date=None, description=None):
        """
        Generates a unique report ID based on the naming convention.

        Args:
            source (str): The source of the CTI data.
            report_type (str): The type of report.
            report_date (datetime.date, optional): The date of the report.  If None, defaults to today.
            description (str, optional): A description of the report. Defaults to None.

        Returns:
            str: The generated report ID, or None on error.
        """
        if report_date is None:
            report_date = datetime.date.today()
        if not isinstance(report_date, datetime.date):
            print("Error: report_date must be a datetime.date object.")
            return None

        if self.valid_sources and source not in self.valid_sources:
            print(f"Error: Invalid report source '{source}'.  Valid sources are: {self.valid_sources}")
            return None

        if self.valid_report_types and report_type not in self.valid_report_types:
            print(f"Error: Invalid report type '{report_type}'.  Valid report types are: {self.valid_report_types}")
            return None
        date_str = report_date.strftime("%Y%m%d")
        report_number = self._get_next_report_number(source, report_type, date_str)
        report_id = f"{source}-{report_type}-{date_str}-{report_number:02d}"
        self.generated_report_ids.append(report_id)
        if description:
            self.report_descriptions[report_id] = description
        return report_id

    def _get_next_report_number(self, source, report_type, date_str):
        """
        Determines the next sequential report number for a given source, type, and date.

        Args:
            source (str): The source of the CTI data.
            report_type (str): The type of report.
            date_str (str): The date of the report in %Y%m%d format.

        Returns:
            int: The next report number.
        """
        key = f"{source}|{report_type}|{date_str}"  # Changed to string
        if key not in self.report_counts:
            self.report_counts[key] = 1
        else:
            self.report_counts[key] += 1
        return self.report_counts[key]

    def save_report_ids(self, filename=None):
        """
        Saves the generated report IDs and descriptions to a file.

        Args:
            filename (str, optional): The name of the file to save to.
                Defaults to the value in the configuration file, or "report_ids.txt" if not configured.
        """
        if filename is None:
            filename = self.base_filename  # Use filename from config

        if not self.generated_report_ids:
            print("No report IDs to save.")
            return False

        try:
            with open(filename, "w") as f:
                for report_id in self.generated_report_ids:
                    description = self.report_descriptions.get(report_id, "")
                    f.write(f"{report_id}: {description}\n")
            print(f"Report IDs and descriptions saved to {filename}")
            self.save_config()
            return True
        except Exception as e:
            print(f"Error saving report IDs: {e}")
            return False

    def get_report_description(self, report_id):
        """
        Retrieves the description for a given report ID.

        Args:
            report_id (str): The ID of the report.

        Returns:
            str: The description of the report, or None if not found.
        """
        return self.report_descriptions.get(report_id)

    def display_all_reports(self):
        """Displays all generated report IDs and their descriptions."""
        if not self.generated_report_ids:
            print("No reports generated yet.")
            return

        print("\nGenerated Reports:")
        for report_id in self.generated_report_ids:
            description = self.report_descriptions.get(report_id, "No description")
            print(f"- {report_id}: {description}")

def main():
    """
    Main function to run the CTI Naming program.
    """
    namer = CTINaming()

    # Add ASCII art here
    print(r"""
▐▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▌
▐  ____          _   _        ____                       ▌
▐ / ___|__ _ ___| |_| | ___  | __ ) _ __ __ ___   _____  ▌
▐| |   / _` / __| __| |/ _ \ |  _ \| '__/ _` \ \ / / _ \ ▌
▐| |__| (_| \__ \ |_| |  __/ | |_) | | | (_| |\ V / (_) |▌
▐ \____\__,_|___/\__|_|\___| |____/|_|  \__,_| \_/ \___/ ▌
▐▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▌
    """)
    print("CTI Report Naming Utility")

    while True:
        print("\nOptions:")
        print("1. Generate Report ID")
        print("2. Save Report IDs to File")
        print("3. Get Report Description")
        print("4. Set Output Filename")
        print("5. Display All Reports")  # Added option to display all reports
        print("6. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            source = input(f"Enter report source ({namer.valid_sources}): ")
            report_type = input(f"Enter report type ({namer.valid_report_types}): ")
            date_str = input("Enter report date (YYYYMMDD, press Enter for today): ")
            description = input("Enter report description (optional): ")
            if date_str:
                try:
                    report_date = datetime.datetime.strptime(date_str, "%Y%m%d").date()
                except ValueError:
                    print("Invalid date format. Please use %Y%m%d.")
                    continue
            else:
                report_date = None

            report_id = namer.generate_report_id(source, report_type, report_date, description)
            if report_id:
                print(f"Generated Report ID: {report_id}")
            else:
                print("Failed to generate report ID.")  # Error message from generate_report_id
        elif choice == "2":
            filename = input(f"Enter filename to save report IDs (default: {namer.base_filename}): ")
            if not filename:
                filename = namer.base_filename
            saved = namer.save_report_ids(filename)
            if not saved:
                print("Saving failed or no IDs to save")
        elif choice == "3":
            report_id = input("Enter report ID: ")
            description = namer.get_report_description(report_id)
            if description:
                print(f"Description for Report ID {report_id}: {description}")
            else:
                print(f"Report ID {report_id} not found, or has no description.")
        elif choice == "4":
            new_filename = input("Enter new filename for saving report IDs: ")
            namer.base_filename = new_filename
            namer.save_config()
            print(f"Output filename set to {new_filename}")
        elif choice == "5":
            namer.display_all_reports()
        elif choice == "6":
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please try again.")
        namer.save_config() #save after every operation to persist
    input("Press Enter to continue...")  # Add this line to pause
if __name__ == "__main__":
    main()
