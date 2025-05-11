import datetime
import os
import json

class VTNaming:
    """
    A class to generate names and descriptions for VirusTotal collections
    and names for VirusTotal graphs.
    """
    def __init__(self):
        """
        Initializes the VTNaming class.
        """
        self.collection_counts = {}
        self.generated_collection_ids = []
        self.collection_descriptions = {}
        self.graph_counts = {}
        self.generated_graph_ids = []
        self.config_file = "vt_naming_config.json"  # Configuration file name
        self.load_config()  # Load configuration at initialization

    def load_config(self):
        """Loads configuration from a JSON file."""
        if os.path.exists(self.config_file):
            try:
                with open(self.config_file, "r") as f:
                    config = json.load(f)
                    self.collection_counts = config.get("collection_counts", {})
                    self.generated_collection_ids = config.get("generated_collection_ids", [])
                    self.collection_descriptions = config.get("collection_descriptions", {})
                    self.graph_counts = config.get("graph_counts", {})
                    self.generated_graph_ids = config.get("generated_graph_ids", [])
                    self.base_filename = config.get("base_filename", "vt_names.txt")
                    self.valid_collection_sources = config.get("valid_collection_sources", [])
                    self.valid_graph_sources = config.get("valid_graph_sources", [])
                    print("Configuration loaded from", self.config_file)
            except json.JSONDecodeError:
                print("Error: Invalid JSON in configuration file. Using default settings.")
                self.collection_counts = {}
                self.generated_collection_ids = []
                self.collection_descriptions = {}
                self.graph_counts = {}
                self.generated_graph_ids = []
                self.base_filename = "vt_names.txt"
                self.valid_collection_sources = []
                self.valid_graph_sources = []
        else:
            print("Configuration file not found. Using default settings.")
            self.base_filename = "vt_names.txt"
            self.valid_collection_sources = []
            self.valid_graph_sources = []

    def save_config(self):
        """Saves configuration to a JSON file."""
        config = {
            "collection_counts": self.collection_counts,
            "generated_collection_ids": self.generated_collection_ids,
            "collection_descriptions": self.collection_descriptions,
            "graph_counts": self.graph_counts,
            "generated_graph_ids": self.generated_graph_ids,
            "base_filename": self.base_filename,
            "valid_collection_sources": self.valid_collection_sources,
            "valid_graph_sources": self.valid_graph_sources,
        }
        try:
            with open(self.config_file, "w") as f:
                json.dump(config, f, indent=4)
            print("Configuration saved to", self.config_file)
        except Exception as e:
            print(f"Error saving configuration: {e}")

    def generate_collection_id(self, source, collection_date=None, description=None):
        """
        Generates a unique ID for VirusTotal collections.

        Args:
            source (str): The source of the collection.
            collection_date (datetime.date, optional): The date of the collection.
                Defaults to today.
            description (str, optional): Description of the collection.

        Returns:
            str: The generated collection ID, or None on error.
        """
        if collection_date is None:
            collection_date = datetime.date.today()
        if not isinstance(collection_date, datetime.date):
            print("Error: collection_date must be a datetime.date object.")
            return None

        if self.valid_collection_sources and source not in self.valid_collection_sources:
            print(f"Error: Invalid collection source '{source}'. Valid sources are: {self.valid_collection_sources}")
            return None

        date_str = collection_date.strftime("%Y%m%d")
        collection_number = self._get_next_collection_number(source, date_str)
        collection_id = f"COL-{source}-{date_str}-{collection_number:02d}"
        self.generated_collection_ids.append(collection_id)
        if description:
            self.collection_descriptions[collection_id] = description
        return collection_id

    def _get_next_collection_number(self, source, date_str):
        """
        Gets the next collection number for a source and date.

        Args:
            source (str): Source of the collection.
            date_str (str): Date string.

        Returns:
            int: Next collection number.
        """
        key = f"{source}|{date_str}"
        if key not in self.collection_counts:
            self.collection_counts[key] = 1
        else:
            self.collection_counts[key] += 1
        return self.collection_counts[key]

    def generate_graph_id(self, source, graph_date=None):
        """
        Generates a unique ID for VirusTotal graphs.

        Args:
            source (str): The source of the graph.
            graph_date (datetime.date, optional): The date of the graph. Defaults to today.

        Returns:
            str: The generated graph ID, or None on error.
        """
        if graph_date is None:
            graph_date = datetime.date.today()
        if not isinstance(graph_date, datetime.date):
            print("Error: graph_date must be a datetime.date object.")
            return None

        if self.valid_graph_sources and source not in self.valid_graph_sources:
            print(f"Error: Invalid graph source '{source}'. Valid sources are: {self.valid_graph_sources}")
            return None

        date_str = graph_date.strftime("%Y%m%d")
        graph_number = self._get_next_graph_number(source, date_str)
        graph_id = f"GRAPH-{source}-{date_str}-{graph_number:02d}"
        self.generated_graph_ids.append(graph_id)
        return graph_id

    def _get_next_graph_number(self, source, date_str):
        """
        Gets the next graph number for a source and date.

        Args:
            source (str): Source of the graph.
            date_str (str): Date string.

        Returns:
            int: The next graph number.
        """
        key = f"{source}|{date_str}"
        if key not in self.graph_counts:
            self.graph_counts[key] = 1
        else:
            self.graph_counts[key] += 1
        return self.graph_counts[key]

    def save_ids(self, filename=None):
        """
        Saves the generated collection and graph IDs (and descriptions) to a file.

        Args:
            filename (str, optional): The name of the file to save to.
                Defaults to the value in the configuration file.
        """
        if filename is None:
            filename = self.base_filename
        if not self.generated_collection_ids and not self.generated_graph_ids:
            print("No collection or graph IDs to save.")
            return False

        try:
            with open(filename, "w") as f:
                f.write("VirusTotal Collections:\n")
                for collection_id in self.generated_collection_ids:
                    description = self.collection_descriptions.get(collection_id, "No description")
                    f.write(f"{collection_id}: {description}\n")
                f.write("\nVirusTotal Graphs:\n")
                for graph_id in self.generated_graph_ids:
                    f.write(f"{graph_id}\n")
            print(f"IDs and descriptions saved to {filename}")
            self.save_config()
            return True
        except Exception as e:
            print(f"Error saving IDs: {e}")
            return False

    def get_collection_description(self, collection_id):
        """
        Retrieves the description for a given collection ID.

        Args:
            collection_id (str): The ID of the collection.

        Returns:
            str: The description of the collection, or None if not found.
        """
        return self.collection_descriptions.get(collection_id)

    def display_all_generated(self):
        """Displays all generated collection and graph IDs and descriptions."""
        if not self.generated_collection_ids and not self.generated_graph_ids:
            print("No collections or graphs generated yet.")
            return

        print("\nGenerated VirusTotal Collections:")
        if self.generated_collection_ids:
            for collection_id in self.generated_collection_ids:
                description = self.collection_descriptions.get(collection_id, "No description")
                print(f"- {collection_id}: {description}")
        else:
            print("  None")

        print("\nGenerated VirusTotal Graphs:")
        if self.generated_graph_ids:
            for graph_id in self.generated_graph_ids:
                print(f"- {graph_id}")
        else:
            print("  None")

def main():
    """
    Main function to run the VirusTotal Naming Tool.
    """
    namer = VTNaming()

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
    print("VirusTotal Naming Tool")

    while True:
        print("\nOptions:")
        print("1. Generate Collection ID")
        print("2. Generate Graph ID")
        print("3. Save IDs to File")
        print("4. Get Collection Description")
        print("5. Display All Generated IDs")
        print("6. Set Output Filename")
        print("7. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            source = input(f"Enter collection source ({namer.valid_collection_sources}): ")
            date_str = input("Enter collection date (YYYYMMDD, press Enter for today): ")
            description = input("Enter collection description (optional): ")
            if date_str:
                try:
                    collection_date = datetime.datetime.strptime(date_str, "%Y%m%d").date()
                except ValueError:
                    print("Invalid date format. Please use %Y%m%d.")
                    continue
            else:
                collection_date = None
            collection_id = namer.generate_collection_id(source, collection_date, description)
            if collection_id:
                print(f"Generated Collection ID: {collection_id}")
            else:
                print("Failed to generate Collection ID")
        elif choice == "2":
            source = input(f"Enter graph source ({namer.valid_graph_sources}): ")
            date_str = input("Enter graph date (YYYYMMDD, press Enter for today): ")
            if date_str:
                try:
                    graph_date = datetime.datetime.strptime(date_str, "%Y%m%d").date()
                except ValueError:
                    print("Invalid date format. Please use %Y%m%d.")
                    continue
            else:
                graph_date = None
            graph_id = namer.generate_graph_id(source, graph_date)
            if graph_id:
                print(f"Generated Graph ID: {graph_id}")
            else:
                print("Failed to generate Graph ID")
        elif choice == "3":
            filename = input(f"Enter filename to save IDs (default: {namer.base_filename}): ")
            if not filename:
                filename = namer.base_filename
            saved = namer.save_ids(filename)
            if not saved:
                print("Saving failed.")
        elif choice == "4":
            collection_id = input("Enter collection ID: ")
            description = namer.get_collection_description(collection_id)
            if description:
                print(f"Description for Collection ID {collection_id}: {description}")
            else:
                print(f"Collection ID {collection_id} not found, or has no description.")
        elif choice == "5":
            namer.display_all_generated()
        elif choice == "6":
            new_filename = input("Enter new filename to save IDs: ")
            namer.base_filename = new_filename
            namer.save_config()
            print(f"Output filename set to {new_filename}")
        elif choice == "7":
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please try again.")
        namer.save_config()
    input("Press Enter to continue...")

if __name__ == "__main__":
    main()

