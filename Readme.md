# 🗂️ Automated File Organizer

A lightweight, automated Python utility that cleans up cluttered directories (such as Downloads or Desktop) by sorting files into categorized folders based on their file extensions using Python's built-in `os` and `shutil` modules.

---

## 🌟 Features

* **Zero External Dependencies:** Built entirely with standard Python libraries (`os`, `shutil`, `pathlib`).
* **Customizable Categories:** Easily add or edit file mappings (e.g., Documents, Images, Videos, Audio, Archives, Code).
* **Safe File Handling:** Prevents accidental overwrites by automatically handling duplicate file names.
* **Recursive or Flat Sorting:** Organizes loose files within target directories while ignoring existing category folders.
* **Lightweight & Fast:** Executes in seconds, even across directories containing thousands of files.

---

## 📂 Category Mappings

| Folder Name | Supported Extensions |
| :--- | :--- |
| **Images** | `.jpg`, `.jpeg`, `.png`, `.gif`, `.bmp`, `.svg`, `.webp` |
| **Documents** | `.pdf`, `.docx`, `.doc`, `.txt`, `.xlsx`, `.pptx`, `.csv` |
| **Videos** | `.mp4`, `.mkv`, `.mov`, `.avi`, `.flv`, `.wmv` |
| **Audio** | `.mp3`, `.wav`, `.aac`, `.flac`, `.ogg` |
| **Archives** | `.zip`, `.rar`, `.tar`, `.gz`, `.7z` |
| **Code & Scripts** | `.py`, `.js`, `.html`, `.css`, `.cpp`, `.java`, `.json` |
| **Installers / Executables** | `.exe`, `.msi`, `.dmg`, `.deb`, `.pkg` |
| **Others** | Any unmatched extensions |

---

## 📂 Project Structure

```text
file-organizer/
├── organizer.py        # Main execution script
├── README.md           # Documentation
└── sample_files/       # Optional test directory