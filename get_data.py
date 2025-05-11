import gdown
import zipfile
import os

# File IDs from Google Drive
file_id_train = "1ZYs5lMixk_iKQINFsFTOsxtzlAhpnHyq"  # train.zip
file_id_test = "134iXRzD1NZdnQsEumos1U2mCsDxI1_8U"   # test.zip

# Output filenames
train_zip_path = "train.zip"
test_zip_path = "test.zip"

# Direct download URLs
url_train = f"https://drive.google.com/uc?id={file_id_train}"
url_test = f"https://drive.google.com/uc?id={file_id_test}"

# Download ZIP files with fuzzy=True to bypass virus scan warning
print("Downloading train.zip...")
gdown.download(url_train, train_zip_path, quiet=False, fuzzy=True)

print("Downloading test.zip...")
gdown.download(url_test, test_zip_path, quiet=False, fuzzy=True)

# Extract ZIP files
print("Extracting train.zip to 'train/'...")
with zipfile.ZipFile(train_zip_path, 'r') as zip_ref:
    zip_ref.extractall("train")

print("Extracting test.zip to 'test/'...")
with zipfile.ZipFile(test_zip_path, 'r') as zip_ref:
    zip_ref.extractall("test")

# Optional: remove ZIP files to save space
# os.remove(train_zip_path)
# os.remove(test_zip_path)

print("Done! Datasets are ready in 'train/' and 'test/' folders.")
