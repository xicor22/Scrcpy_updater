import requests
import wget
from zipfile import ZipFile as zp
import subprocess
import os
import shutil


def download():
    """Downloads the latest Scrcpy release from GitHub."""
    try:
        url = 'https://github.com/Genymobile/scrcpy/releases/latest'
        r = requests.get(url)
        version = r.url.split('/')[-1]
        link_0 = "https://github.com/Genymobile/scrcpy/releases/latest/download/scrcpy-win64-"
        link_1 = ".zip"
        end_link = link_0 + version + link_1
        final = os.path.join('S:', 'Tools', 'Scrcpy', 'scrcpy.zip')
        wget.download(end_link, final)
        return final
    except requests.RequestException as e:
        print(f"Download failed: {e}")
        raise


def extract(zip_path, extract_path):
    """Extracts the downloaded zip file."""
    try:
        with zp(zip_path, 'r') as zipObj:
            zipObj.extractall(extract_path)
    except Exception as e:
        print(f"Extraction failed: {e}")
        raise


def folder_loc(tools_path):
    """Gets the extracted folder name using PowerShell."""
    try:
        process = subprocess.Popen(
            ["powershell", f"cd {tools_path} ; ls"],
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE
        )
        result, error = process.communicate()
        if error:
            raise subprocess.SubprocessError(error.decode('utf-8'))
        loc = result.decode('utf-8').split()
        # Make sure we have enough items in the list
        if len(loc) < 15:
            raise IndexError("Unexpected PowerShell output format")
        return loc[14]
    except Exception as e:
        print(f"Failed to get folder location: {e}")
        raise


def move(source_folder, destination):
    """Moves files from extracted folder to destination."""
    try:
        file_list = os.listdir(source_folder)
        for f in file_list:
            src = os.path.join(source_folder, f)
            dst = os.path.join(destination, f)
            shutil.move(src, dst)
        return source_folder
    except Exception as e:
        print(f"Failed to move files: {e}")
        raise


def cleanup(folder_path, zip_path):
    """Removes temporary files and folders."""
    try:
        # Remove temporary folder and zip file
        if os.path.exists(folder_path):
            shutil.rmtree(folder_path)
        if os.path.exists(zip_path):
            os.remove(zip_path)
    except Exception as e:
        print(f"Cleanup failed: {e}")
        raise


def folder_check(folder_path):
    """Creates the target folder if it doesn't exist."""
    try:
        if not os.path.exists(folder_path):
            os.makedirs(folder_path)
    except Exception as e:
        print(f"Failed to create folder: {e}")
        raise


def main():
    tools_path = os.path.join('S:', 'Tools', 'Scrcpy')

    try:
        # Create the target directory if it doesn't exist
        folder_check(tools_path)

        # Download the latest version
        zip_path = download()
        print(f"\nDownloaded to: {zip_path}")

        # Extract the zip file
        extract(zip_path, tools_path)
        print("Extraction completed")

        # Get the extracted folder name
        folder_name = folder_loc(tools_path)
        extracted_folder = os.path.join(tools_path, folder_name)
        print(f"Found extracted folder: {extracted_folder}")

        # Move files to final location
        move(extracted_folder, tools_path)
        print("Files moved successfully")

        # Clean up temporary files
        cleanup(extracted_folder, zip_path)
        print("Cleanup completed")

        print("Update completed successfully!")

    except Exception as e:
        print(f"\nUpdate failed: {e}")
        return 1

    return 0


if __name__ == "__main__":
    exit(main())
