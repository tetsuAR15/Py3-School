import os

def delete_tilde_files_in_documents():
    # Get the user's home directory
    home_directory = os.path.expanduser("~")
    documents_directory = os.path.join(home_directory, "Documents")

    # Get file in the Documents directory
    for filename in os.listdir(documents_directory):
        # Gent the full path of a file
        file_path = os.path.join(documents_directory, filename)
        
        # Check if it is a backup file and a file
        if filename.endswith('~') and os.path.isfile(file_path):
            try:
                os.remove(file_path)  # remove file
                print(f'Deleted: {file_path}')
            except Exception as e:
                print(f'Error deleting {file_path}: {e}')

if __name__ == "__main__":
    delete_tilde_files_in_documents()
