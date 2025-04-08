# ¬‿¬ smoly ★

A command-line utility built in Python (`pycups`) to send files directly to your USB printer on Linux — tested on **Fedora 41** with the **Epson L3250** (my personal printer and OS, btw), but with cross-platform dreams.

The project was born out of personal frustration: even after installing the correct drivers, communicating with my printer and actually sending print jobs was more painful than it should be. Printing documents became a bottleneck in my workflow. So I decided to build something fast, simple, and intuitive (and customizable!) to solve it once and for all — and thus, **smoly** was born.

Besides just working (hopefully), it also:
- 💅 Uses `rich` to make your terminal a beautiful place.
- 🔍 Displays detailed technical info about the print job (format, color, size, status, etc.).
- 🧠 Features custom error messages and feedback with colorful **ASCII-style emojis** to make the experience fun and friendly.
- 💡 Fully hackable and extensible — feel free to play with the visuals or extend the logic.

<br>

## REQUIREMENTS

To run **smoly** smoothly on your system, you'll need the following:

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


So, after checking all these details and installing the necessary dependencies, clone this repository:


```shell
git clone https://github.com/mvghasty/smoly.git
```


After you have cloned the repository, you can now access smoly and run it inside the application folder:


```shell
cd smoly/src
python main.py
```


or you can turn it into a binary inside your bin folder:


```shell
chmod +x smoly
sudo mv smoly /usr/local/bin/
smoly
```
