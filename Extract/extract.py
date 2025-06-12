import zipfile
import os
import ijson
import json

def extract_json_files(zip_path):
    # Create folders: trilogy/network and trilogy/provider
    os.makedirs('trilogy/network', exist_ok=True)
    os.makedirs('trilogy/provider', exist_ok=True)
    
    # Open the ZIP file
    try:
        with zipfile.ZipFile(zip_path, 'r') as zip_ref:
            zip_ref.extractall('temp')  # Unpack to a temporary folder
            
            # Look for files in the temporary folder
            for root, _, files in os.walk('temp'):
                for file in files:
                    if file == 'network.json':
                        # Read network.json using ijson
                        with open(os.path.join(root, file), 'rb') as f:
                            data = list(ijson.items(f, ''))[0]  # Get JSON data
                        # Save to trilogy/network/network.json
                        with open('trilogy/network/network.json', 'w') as f:
                            json.dump(data, f)
                        print("Saved network.json")
                    elif file == 'provider.json':
                        # Read provider.json using ijson
                        with open(os.path.join(root, file), 'rb') as f:
                            data = list(ijson.items(f, ''))[0]  # Get JSON data
                        # Save to trilogy/provider/provider.json
                        with open('trilogy/provider/provider.json', 'w') as f:
                            json.dump(data, f)
                        print("Saved provider.json")
            
            # Delete temporary folder
            for root, dirs, files in os.walk('temp', topdown=False):
                for file in files:
                    os.remove(os.path.join(root, file))
                for dir in dirs:
                    os.rmdir(os.path.join(root, dir))
            os.rmdir('temp')
    
    except:
        print("Problem with trilogy.zip! Check if it exists or is valid.")
        return None
    
    return 'trilogy'

# Run the function
extract_json_files('trilogy.zip')