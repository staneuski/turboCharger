# About turboCharger
![GitHub release (latest by date)](https://img.shields.io/github/v/release/StasF1/turboCharger)
![GitHub All Releases](https://img.shields.io/github/downloads/StasF1/turboCharger/total)
**[[Русский 🇷🇺](https://github.com/StasF1/turboCharger/blob/master/README.ru.md)]**

Piston engine turbocharger 0D simulation tool

After the successfull simulation the reports are created (in the Markdown
language, in Russian for now only) with dimesioned pictures (see example below)

![inTurbineWheel](https://github.com/StasF1/turboCharger/wiki/images/inTurbineWheel.png)

The program was written to open reports in the Markdown editor
[Typora](https://typora.io). It is advisable to use it to display LaTeX formulas
correctly in Markdown files (automatic .pdf LaTeX generation in develop).

#### Report examples
| Run type | Settings |
| -------: | -------- |
| [Radial Compressor](https://github.com/StasF1/turboCharger/releases/download/v1-beta/compressorReport.pdf) | Default |
| [Radial Turbine](https://github.com/StasF1/turboCharger/releases/download/v1-beta/radialTurbineReport.pdf) | Default |
| [Axial Turbine](https://github.com/StasF1/turboCharger/releases/download/v1-beta/axialTurbineReport.pdf) | Not default |


# Requirements
1. [Python 3](https://www.python.org/downloads/) with _pillow_ package
1. Markdown editor ([Typora](https://typora.io/#download), preferably)


# Usage
## Installation
### Windows
1. Install a package managemer for Windows [Chocolatey](https://chocolatey.org/)
(if not installed). Copy in the PowerShell elevated prompt and run:
    ```PowerShell
    Set-ExecutionPolicy Bypass -Scope Process -Force; [System.Net.ServicePointManager]::SecurityProtocol = [System.Net.ServicePointManager]::SecurityProtocol -bor 3072; iex ((New-Object System.Net.WebClient).DownloadString('https://chocolatey.org/install.ps1'))
    ```
1. Install Python 3 with required packages and Markdown editor (also using the PowerShell elevated prompt)
    ```PowerShell
    choco install -y python3 typora
    python3 -m pip install pillow
    ```
1. Download turboCharger repository:
    ```PowerShell
    curl "https://github.com/StasF1/turboCharger/archive/v2.3-beta.zip" -o $HOME/Downloads/turboCharger
    ```

### macOS
1. Install a package managemer for macOS [Homebrew](https://brew.sh/)
(if not installed). Copy into the Terminal and run:
    ```bash
    /bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install.sh)"
    ```
1. Install Python 3 with required packages and Markdown editor
    ```bash
    brew install python3 typora
    python3 -m pip install pillow
    ```
1. Download turboCharger repository:
    ```bash
    curl "https://github.com/StasF1/turboCharger/archive/v2.3-beta.zip" -o $HOME/Downloads/turboCharger
    ```

### Linux
1. Install Python required packages
    ```bash
    python3 -m pip install pillow
    ```
1. Download turboCharger repository:
    ```bash
    curl "https://github.com/StasF1/turboCharger/archive/v2.3-beta.zip" -o $HOME/Downloads/turboCharger
    ```

## Run
```bash
cd $HOME/Downloads/turboCharger
python3 turbocharger.py
```
⚠ A detailed guide is available on [**Wiki**](https://github.com/StasF1/turboCharger/wiki)


# Structure
```gitignore
turboCharger-2.2-beta
├── compressor
│   ├── post
│   └── pre
├── etc
│   ├── compressor
│   └── turbine
│       ├── axial
│       └── radial
├── results*            # reports and dictionary copies (*Config.py-files)
│   ├── compressor
│   └── turbine
│       ├── axial
│       └── radial
└── turbine
    ├── post
    └── pre
#* created during the calculation
```