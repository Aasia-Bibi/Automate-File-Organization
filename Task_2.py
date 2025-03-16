import os
import shutil
import logging

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class FileOrganizer:
    def __init__(self, directory):
        self.directory = directory
        self.file_types = {
            "Images": [".jpg", ".jpeg", ".png", ".gif", ".bmp"],
            "Documents": [".pdf", ".docx", ".txt", ".xlsx", ".pptx"],
            "Videos": [".mp4", ".mkv", ".mov", ".avi"],
            "Music": [".mp3", ".wav", ".aac"],
            "Archives": [".zip", ".rar", ".tar", ".gz"],
            "Scripts": [".py", ".js", ".cpp", ".java", ".html", ".css"]
        }

    def organize_files(self):
        """Sort and move files into categorized folders."""
        if not os.path.exists(self.directory):
            logging.error("Directory does not exist!")
            return

        for file in os.listdir(self.directory):
            file_path = os.path.join(self.directory, file)
            if os.path.isfile(file_path):
                self.move_file(file, file_path)

        logging.info("File organization completed successfully!")

    def move_file(self, file, file_path):
        """Move file to the appropriate folder based on extension."""
        for folder, extensions in self.file_types.items():
            if any(file.lower().endswith(ext) for ext in extensions):
                dest_folder = os.path.join(self.directory, folder)
                if not os.path.exists(dest_folder):
                    os.makedirs(dest_folder)
                shutil.move(file_path, os.path.join(dest_folder, file))
                logging.info(f"Moved {file} -> {folder}/")
                return
        
        # Move unknown file types to 'Others'
        other_folder = os.path.join(self.directory, "Others")
        if not os.path.exists(other_folder):
            os.makedirs(other_folder)
        shutil.move(file_path, os.path.join(other_folder, file))
        logging.info(f"Moved {file} -> Others/")

# Example Usage
directory = "C:/Users/YourUsername/Downloads"  # Change to your target directory
organizer = FileOrganizer(directory)
organizer.organize_files()
