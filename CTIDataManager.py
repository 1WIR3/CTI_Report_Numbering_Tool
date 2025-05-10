import datetime
import os

class CTINaming:
    """
    A class to generate CTI report names and numbers according to a defined scheme.
    """
    def __init__(self):
        """
        Initializes the CTINaming class.
        """
        self.report_counts = {}  # Dictionary to store report counts
        self.generated_report_ids = []  # List to store the report ids
        self.report_descriptions = {}  # Dictionary to store report descriptions.
                                         # Key will be report_id, value will be description

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

        date_str = report_date.strftime("%Y%m%d")
        report_number = self._get_next_report_number(source, report_type, date_str)
        report_id = f"{source}-{report_type}-{date_str}-{report_number:02d}"
        self.generated_report_ids.append(report_id)  # store generated ids
        if description:  # Store the description, if provided
            self.report_descriptions[report_id] = description
        return report_id

    def _get_next_report_number(self, source, report_type, date_str):
        """
        Determines the next sequential report number for a given source, type, and date.

        Args:
            source (str): The source of the CTI data.
            report_type (str): The type of report.
            date_str (str): The date of the report in YYYYMMDD format.

        Returns:
            int: The next report number.
        """
        key = (source, report_type, date_str)
        if key not in self.report_counts:
            self.report_counts[key] = 1
        else:
            self.report_counts[key] += 1
        return self.report_counts[key]

    def save_report_ids(self, filename="report_ids.txt"):
        """
        Saves the generated report IDs and descriptions to a file.

        Args:
            filename (str, optional): The name of the file to save to.
                Defaults to "report_ids.txt".
        """
        if not self.generated_report_ids:
            print("No report IDs to save.")
            return False  # Return False to indicate no save happened

        try:
            with open(filename, "w") as f:
                for report_id in self.generated_report_ids:
                    description = self.report_descriptions.get(report_id, "")  # Get description, default to ""
                    f.write(f"{report_id}: {description}\n")  # Write ID and description
            print(f"Report IDs and descriptions saved to {filename}")
            return True  # return True on success
        except Exception as e:
            print(f"Error saving report IDs: {e}")
            return False  # Return False on error

    def get_report_description(self, report_id):
        """
        Retrieves the description for a given report ID.

        Args:
            report_id (str): The ID of the report.

        Returns:
            str: The description of the report, or None if not found.
        """
        return self.report_descriptions.get(report_id)


def main():
    """
    Main function to run the CTI Naming program.
    """
    namer = CTINaming()

    while True:
        print("\nCTI Report Naming Utility")
        print("1. Generate Report ID")
        print("2. Save Report IDs to File")
        print("3. Get Report Description")  # Added option to get description
        print("4. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            source = input("Enter report source: ")
            report_type = input("Enter report type: ")
            date_str = input("Enter report date (YYYYMMDD, press Enter for today): ")
            description = input("Enter report description (optional): ")  # Get description
            if date_str:
                try:
                    report_date = datetime.datetime.strptime(date_str, "%Y%m%d").date()
                except ValueError:
                    print("Invalid date format. Please use YYYYMMDD.")
                    continue
            else:
                report_date = None

            report_id = namer.generate_report_id(source, report_type, report_date, description)  # Pass description
            if report_id:
                print(f"Generated Report ID: {report_id}")
            else:
                print("Failed to generate report ID.")
        elif choice == "2":
            filename = input("Enter filename to save report IDs (default: report_ids.txt): ")
            if not filename:
                filename = "report_ids.txt"
            saved = namer.save_report_ids(filename)
            if not saved:
                print("Saving failed or no IDs to save")
        elif choice == "3":  # Implement getting the description
            report_id = input("Enter report ID: ")
            description = namer.get_report_description(report_id)
            if description:
                print(f"Description for Report ID {report_id}: {description}")
            else:
                print(f"Report ID {report_id} not found, or has no description.")
        elif choice == "4":
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
