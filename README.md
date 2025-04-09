# P R I N T E R G E I S T ★ 
[![Licence](https://img.shields.io/github/license/Ileriayo/markdown-badges?style=for-the-badge)](./LICENSE) ![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54) ![Linux](https://img.shields.io/badge/Linux-FCC624?style=for-the-badge&logo=linux&logoColor=black) 

A command-line utility built in Python (`pycups`) to send files directly to your USB printer on Linux — tested on **Fedora 41** with the **Epson L3250** (my personal printer and OS, btw), but with cross-platform dreams.

The project was born out of personal frustration: even after installing the correct drivers, communicating with my printer and actually sending print jobs was more painful than it should be. Printing documents became a bottleneck in my workflow. So I decided to build something fast, simple, and intuitive (and customizable!) to solve it once and for all — and thus, **printergeist** was born.

Besides just working (hopefully), it also:
- 💅 Uses `rich` to make your terminal a beautiful place.
- 🔍 Displays detailed technical info about the print job (format, color, size, status, etc.).
- 🧠 Features custom error messages and feedback with colorful **ASCII-style emojis** to make the experience fun and friendly.
- 💡 Fully hackable and extensible — feel free to play with the visuals or extend the logic.


### Printergeist Software Officially Supported Models (PSOSM - Official List)
<br>

![Epson](https://img.shields.io/badge/Epson-ECOTANK/WORKFORCE/EXPRESSION-003d99?style=for-the-badge&logo=epson&logoColor=white) ![Canon](https://img.shields.io/badge/Canon-Pixma/imageCLASS/SELPHY-ffffff?style=for-the-badge&logo=canon&logoColor=red) ![DELL](https://img.shields.io/badge/dell-COLOR/C—Series/B—Series-007DB8?style=for-the-badge&logo=dell&logoColor=white) ![Samsung](https://img.shields.io/badge/samsung-Xpress/ProXpress/CLP—Series-1428A0?style=for-the-badge&logo=Samsung&logoColor=white) ![Xerox](https://img.shields.io/badge/Xerox-VersaLink/Phaser/WorkCentre-d51631?style=for-the-badge&logo=xerox&logoColor=white) ![Brother](https://img.shields.io/badge/Brother-MFC—Series/DCP—Series-1535a3?style=for-the-badge&logo=Brother&logoColor=white) ![Kyocera](https://img.shields.io/badge/Kyocera-ECOSYS/TASKalfa-e42136?style=for-the-badge&logo=kyocera&logoColor=white) ![Ricoh](https://img.shields.io/badge/Ricoh-P—Series/SP—Series-727375?style=for-the-badge&logo=lexmark&logoColor=white) ![HP](https://img.shields.io/badge/hp-OfficeJet-0096D6?style=for-the-badge&logo=hp&logoColor=white) ![Lexmark](https://img.shields.io/badge/Lexmark-M—Series-08c62c?style=for-the-badge&logo=lexmark&logoColor=white) 

<br>

The list above highlights a selection of representative printer models from each major brand that offer official Linux driver support. As of the latest update (2025-04-08), these models are known to be compatible with printergeist or are expected to function correctly when configured via CUPS.

This list is curated for reference and user convenience only. As a Free and Open Source Software (FOSS) project licensed under the GPLv2 License, printergeist operates independently and is not affiliated with, endorsed by, or sponsored by any of the manufacturers mentioned.

Compatibility may vary depending on the Linux distribution, driver version, and CUPS configuration. Users are encouraged to consult the official documentation of each vendor to ensure full support for advanced printing features (e.g., duplex, color modes, resolution control).

## REQUIREMENTS

To run **printergeist** smoothly on your system, you'll need the following:

- Python 3.9 or newer  
- Python dependencies:

  ```bash
  pip install pycups rich
  ```

<br>

## USAGE AND INSTALLATION

Before running the project, make sure CUPS is installed:

| Distribution         | Package Manager        | Installation Command                     | Enable & Start Service                                      |
|----------------------|------------------------|------------------------------------------|-------------------------------------------------------------|
| **Ubuntu/Debian**    | `apt`                  | `sudo apt install cups`                 | `sudo systemctl enable --now cups`                          |
| **Fedora/RHEL/CentOS** | `dnf` or `dnf5`      | `sudo dnf install cups`                 | `sudo systemctl enable --now cups`                          |
| **Arch/Manjaro**     | `pacman`               | `sudo pacman -S cups`                   | `sudo systemctl enable --now cups`                          |
| **openSUSE**         | `zypper`               | `sudo zypper install cups`              | `sudo systemctl enable --now cups`                          |
| **Alpine Linux**     | `apk`                  | `sudo apk add cups cups-daemon`         | `sudo rc-update add cupsd default && sudo service cupsd start` |
| **Gentoo**           | `emerge`               | `sudo emerge --ask net-print/cups`      | `sudo rc-update add cupsd default && sudo /etc/init.d/cupsd start` |
| **NixOS**            | `nixos-rebuild`        | `services.printing.enable = true;`      | `sudo nixos-rebuild switch` | 


Also make sure you have your printer drivers installed on your computer. If not, check if your printer brand is on the list below and download the available drivers for it:


| Brand     | Linux Support | Driver Download Page |
|-----------|----------------|-----------------------|
| **HP**    | ✅ Fully supported via **HPLIP** (HP Linux Imaging and Printing) | [developers.hp.com](https://developers.hp.com/hp-linux-imaging-and-printing) |
| **Epson** | ✅ Wide support with official `.deb`/`.rpm` packages | [download.ebz.epson.net](https://download.ebz.epson.net/dsc/search/01/search/?OSC=LX) |
| **Brother** | ✅ Supports many models via **Driver Install Tool** | [support.brother.com](https://support.brother.com/g/b/faqend.aspx?c=us&faqid=faq00100556_000&lang=en) |
| **Canon** | ⚠️ Limited support; only select models | [usa.canon.com](https://www.usa.canon.com/support/software-and-drivers) |
| **Lexmark** | ✅ Offers a **Universal Print Driver** for Linux | [support.lexmark.com](https://support.lexmark.com/en_us/drivers-downloads.html) |
| **Samsung** | ⚠️ Legacy support via Unified Linux Driver | [samsungsetup.com](https://www.samsungsetup.com/ts/client/en/install.html) |
| **Xerox** | ✅ Provides Linux-compatible drivers and PPDs | [support.xerox.com](https://www.support.xerox.com/en-ca/content/111461) |
| **Ricoh** | ✅ Universal drivers for many models | [support.ricoh.com](https://support.ricoh.com/bb/html/dr_ut_e/rc3/model/p_i/p_i.htm?lang=en) |
| **Kyocera** | ✅ Good Linux support with documentation | [kyoceradocumentsolutions.us](https://www.kyoceradocumentsolutions.us/en/support/downloads.html) |
| **Dell** | ⚠️ Basic support for some legacy printers | [dell.com](https://www.dell.com/support/home/en-us?app=drivers) |


After reviewing the project requirements and ensuring all dependencies are properly installed, you can proceed by cloning this repository:


```shell
git clone https://github.com/mvghasty/printergeist.git
```


Once the repository is cloned, navigate to the application directory and run the main script:


```shell
cd printergeist/src
python main.py
```


Alternatively, you can create a binary-like executable using the ``pgeist`` bash script located in the ``src/`` directory. This allows you to run the program from anywhere as a CLI tool.

### Creating the CLI Executable

  **1.** Open the ``pgeist`` file in your preferred text editor:

  ```shell
  emacs pgeist  # or use nano, vim, code, etc.
  ```

  **2.** Locate the following line:

  ```shell
  MAIN_PATH="path/to/main.py"
  ```

  **3.** Replace ``"path/to/main.py"`` with the absolute or relative path to the main.py file inside the ``printergeist/src`` directory.

  **4.** Save the file and execute it. The script will automatically handle the installation and move the executable to the ``/usr/local/bin`` directory, making it accessible system-wide as ``pgeist``.

The source code is thoroughly documented. If you have any questions about implementation details or internal logic, please refer to the inline comments within the codebase.
