import gdown
import zipfile
import os

# File IDs from Google Drive
file_id1 = "134iXRzD1NZdnQsEumos1U2mCsDxI1_8U"
file_id2 = "1ZYs5lMixk_iKQINFsFTOsxtzlAhpnHyq"

# Create data directory
os.makedirs("data", exist_ok=True)

# Define zip file paths
zip1_path = "data/data1.zip"
zip2_path = "data/data2.zip"

# Download URLs
url1 = f"https://drive.google.com/uc?id={file_id1}"
url2 = f"https://drive.google.com/uc?id={file_id2}"

# Download zip files
print("Downloading data1.zip...")
gdown.download(url1, zip1_path, quiet=False)

print("Downloading data2.zip...")
gdown.download(url2, zip2_path, quiet=False)

# Extract zip files
print("Extracting data1.zip...")
with zipfile.ZipFile(zip1_path, 'r') as zip_ref:
    zip_ref.extractall("data/data1")

print("Extracting data2.zip...")
with zipfile.ZipFile(zip2_path, 'r') as zip_ref:
    zip_ref.extractall("data/data2")

print("Done! Datasets are in data/data1/ and data/data2/")
