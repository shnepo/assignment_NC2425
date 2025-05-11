import gdown
import zipfile
import os

# File IDs from Google Drive
file_id1 = "134iXRzD1NZdnQsEumos1U2mCsDxI1_8U"  # data1.zip
file_id2 = "1ZYs5lMixk_iKQINFsFTOsxtzlAhpnHyq"  # data2.zip

# Paths
zip1_path = "data1.zip"
zip2_path = "data2.zip"

# Download URLs
url1 = f"https://drive.google.com/uc?id={file_id1}"
url2 = f"https://drive.google.com/uc?id={file_id2}"

# Download zip files
print("Downloading data1.zip (train)...")
gdown.download(url1, zip1_path, quiet=False)

print("Downloading data2.zip (test)...")
gdown.download(url2, zip2_path, quiet=False)

# Extract to correct folders
print("Extracting to 'train/'...")
with zipfile.ZipFile(zip1_path, 'r') as zip_ref:
    zip_ref.extractall("train")

print("Extracting to 'test/'...")
with zipfile.ZipFile(zip2_path, 'r') as zip_ref:
    zip_ref.extractall("test")

# Optional: delete zip files to save space
# os.remove(zip1_path)
# os.remove(zip2_path)

print("Done! Datasets available in 'train/' and 'test/' folders.")

