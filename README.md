

# FoodLensApp

![Platform](https://img.shields.io/badge/platform-Linux%20%7C%20Windows%20%7C%20macOS-blue)
![License](https://img.shields.io/badge/license-MIT-green)
![PyQt6](https://img.shields.io/badge/GUI-PyQt6-ff69b4)
![Build](https://img.shields.io/badge/build-Nuitka%20%7C%20C-nativebrightgreen)


**FoodLensApp** is a fast and responsive cross-platform desktop application for searching and extracting data from Excel files. Built using Python with PyQt6 and compiled to native code using Nuitka, it offers a lightweight and efficient experience across Linux, Windows, and macOS.

---

## ✨ Features

- 🔍 **Instant Search**: Quickly search for items across Excel sheets.
- 📄 **Excel Support**: Parses `.xlsx` files for structured item lookup.
- 🖥️ **Cross-Platform**: Runs natively on Linux, Windows, and macOS.
- ⚡ **High Performance**: Compiled to C for speed and responsiveness.
- 🎨 **Simple UI**: Clean, intuitive interface with PyQt6.
- 📦 **Standalone Executable**: No Python runtime required.

---

## 📦 Installation

### Linux

1. Extract the compiled archive:
   ```bash
   tar -xzf FoodLensApp_Linux.tar.gz
````

2. (Optional) Move to a system path:

   ```bash
   sudo cp -r FoodLensApp /usr/local/bin/FoodLensApp
   sudo cp -r _internal /usr/local/bin/_internal
   ```

3. Add desktop entry (for App Finder):

   * Copy `food-lens.desktop` to `/usr/share/applications/`
   * Set a valid `.png` icon path in the `Icon=` line

### Windows & macOS

Executables should be compiled on those platforms using Nuitka. Cross-compilation is not fully supported at this time.

---

## 🛠️ Build Instructions (Developer)

```bash
# Create and activate a virtual environment
python -m venv .venv
source .venv/bin/activate

# Install dependencies
pip install -r requirements.txt
pip install nuitka

# Build the application
nuitka --standalone \
       --enable-plugin=pyqt6 \
       --output-dir=build_nuitka \
       --follow-imports \
       widget.py
```

Output binaries and the `_internal` folder will be placed in `dist/`.

---

## 📁 Project Structure

```
food_lens2/
├── widget.py             # Main application
├── form_ui.py            # UI logic
├── form.ui               # Qt Designer file
├── requirements.txt      # Python dependencies
├── FoodLensApp.spec      # (Optional) spec file
├── dist/                 # Final executable and runtime files
├── _internal/            # Required for Nuitka standalone mode
└── food-lens.desktop     # Desktop entry for Linux
```

---

## 📜 License

**MIT License** – see [LICENSE](LICENSE) for full text.

---

Made for chefs, analysts, and inventory managers.

```


