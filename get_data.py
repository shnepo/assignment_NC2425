import os
import zipfile
import urllib.request
import shutil

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

# Extract ZIP with flattening (removes top-level folder)
def extract_zip_flat(zip_path, target_folder):
    print(f"Extracting {zip_path} into '{target_folder}/' with flattening...")
    with zipfile.ZipFile(zip_path, 'r') as zip_ref:
        for member in zip_ref.infolist():
            if member.is_dir():
                continue
            parts = member.filename.split('/')
            relative_path = os.path.join(target_folder, *parts[1:])  # Strip first folder
            os.makedirs(os.path.dirname(relative_path), exist_ok=True)
            with zip_ref.open(member) as source, open(relative_path, 'wb') as target:
                shutil.copyfileobj(source, target)
    print(f"Flattened extraction complete: {zip_path} → {target_folder}/")

# Run download + extraction steps
download_file(train_url, train_zip)
download_file(test_url, test_zip)

os.makedirs("train", exist_ok=True)
os.makedirs("test", exist_ok=True)

extract_zip_flat(train_zip, "train")
extract_zip_flat(test_zip, "test")

# Optional cleanup
# os.remove(train_zip)
# os.remove(test_zip)

print("All done! Datasets are ready in 'train/' and 'test/'.")


