import gdown
import zipfile
import os

# File IDs from Google Drive
file_id_train = "1ZYs5lMixk_iKQINFsFTOsxtzlAhpnHyq"  # train.zip
file_id_test = "134iXRzD1NZdnQsEumos1U2mCsDxI1_8U"   # test.zip

# Download paths
train_zip_path = "train.zip"
test_zip_path = "test.zip"

# URLs for direct download
url_train = f"https://drive.google.com/uc?id={file_id_train}"
url_test = f"https://drive.google.com/uc?id={file_id_test}"

# Download ZIPs
print("Downloading train.zip...")
gdown.download(url_train, train_zip_path, quiet=False)

print("Downloading test.zip...")
gdown.download(url_test, test_zip_path, quiet=False)

# Extract ZIPs
print("Extracting train.zip to 'train/'...")
with zipfile.ZipFile(train_zip_path, 'r') as zip_ref:
    zip_ref.extractall("train")

print("Extracting test.zip to 'test/'...")
with zipfile.ZipFile(test_zip_path, 'r') as zip_ref:
    zip_ref.extractall("test")

# Remove ZIPs to save space -- optional (uncomment to improve computional efficieny)
# os.remove(train_zip_path)
# os.remove(test_zip_path)

print("✅ Done! Folders 'train/' and 'test/' are ready."



