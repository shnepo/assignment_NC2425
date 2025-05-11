import os
import zipfile
import urllib.request

# URLs for the ZIP files hosted on GitHub Releases
train_url = "https://github.com/gabz81y/assignment_NC2425/releases/download/dataset_release/train.zip"
test_url = "https://github.com/gabz81y/assignment_NC2425/releases/download/dataset_release/test.zip"

# Local file names
train_zip = "train.zip"
test_zip = "test.zip"

# Download if not already present
def download_file(url, output_path):
    if not os.path.exists(output_path):
        print(f"Downloading {output_path}...")
        urllib.request.urlretrieve(url, output_path)
        print(f"Downloaded {output_path}")
    else:
        print(f"{output_path} already exists, skipping download.")

# Extract if folder doesn't exist
def extract_zip(zip_path, extract_to):
    if not os.path.exists(extract_to):
        print(f"Extracting {zip_path}...")
        with zipfile.ZipFile(zip_path, 'r') as zip_ref:
            zip_ref.extractall(extract_to)
        print(f"Extracted to '{extract_to}/'")
    else:
        print(f"'{extract_to}/' already exists, skipping extraction.")

# Run steps
download_file(train_url, train_zip)
download_file(test_url, test_zip)

extract_zip(train_zip, "train")
extract_zip(test_zip, "test")

# Optional cleanup
# os.remove(train_zip)
# os.remove(test_zip)

print("🎉 All done! Datasets are ready in 'train/' and 'test/'.")

