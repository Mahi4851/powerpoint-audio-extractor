import zipfile
import os
from tkinter import Tk, filedialog

# Step 1: Ask user to select a .pptx file
Tk().withdraw()  # Hide the root window
pptx_path = filedialog.askopenfilename(
    title="Select PowerPoint File",
    filetypes=[("PowerPoint files", "*.pptx")]
)

if not pptx_path:
    print("No file selected.")
    exit()

# Step 2: Get file name (without extension)
file_name = os.path.splitext(os.path.basename(pptx_path))[0]

# Step 3: Create output folder on Desktop
desktop_path = os.path.join(os.path.expanduser("~"), "Desktop/VO_FROM_PPT")
output_folder = os.path.join(desktop_path, file_name + "_audio")
os.makedirs(output_folder, exist_ok=True)

# Step 4: Extract audio files from pptx (which is a zip file)
with zipfile.ZipFile(pptx_path, 'r') as zip_ref:
    media_files = [f for f in zip_ref.namelist() if f.startswith("ppt/media/") and (f.endswith(".mp3") or f.endswith(".wav") or f.endswith(".m4a"))]
    
    if not media_files:
        print("No audio files found in this presentation.")
    else:
        for file in media_files:
            audio_data = zip_ref.read(file)
            output_path = os.path.join(output_folder, os.path.basename(file))
            with open(output_path, "wb") as out_file:
                out_file.write(audio_data)

        print(f"✅ Extracted {len(media_files)} audio file(s) to: {output_folder}")
