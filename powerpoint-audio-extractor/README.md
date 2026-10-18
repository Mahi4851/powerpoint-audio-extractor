# PowerPoint audio extractor

A small Python desktop utility that extracts embedded MP3, WAV and M4A files from a PowerPoint `.pptx` presentation.

## Requirements

- Python 3 with Tkinter support
- A desktop environment (the script opens a file chooser)

No third-party Python packages are required.

## Run

```powershell
python extract_audio_from_pptx.py
```

Choose a `.pptx` file in the dialog. Extracted audio is saved to:

```text
Desktop/VO_FROM_PPT/<presentation_name>_audio/
```

## Notes

- Only embedded audio files with `.mp3`, `.wav`, or `.m4a` extensions are extracted.
- File output names are taken from the embedded media filenames, not slide titles.
- This tool does not extract narration that is not stored as one of the supported embedded audio file types.
