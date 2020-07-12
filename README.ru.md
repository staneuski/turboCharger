# О turboCharger
![GitHub release (latest by date)](https://img.shields.io/github/v/release/StasF1/turboCharger)
![GitHub All Releases](https://img.shields.io/github/downloads/StasF1/turboCharger/total)
**[[English 🇬🇧](https://github.com/StasF1/turboCharger/blob/master/README.md)]**

Программа для 0D-моделирования турбокомпрессора поршневого двигателя

После успешного моделирования создаются отчеты (на языке Markdown) с оразмерными картинками (см. пример ниже)

![inTurbineWheel](https://github.com/StasF1/turboCharger/wiki/images/inTurbineWheel.png)

Программа писалась для чтения отчётов в Markdown-редакторе
[Typora](https://typora.io). Желательно использовать его для правильного
отображения Latex-формул в Markdown-файлах (автоматическая генерация LaTeX .pdf
в разработке).

#### Примеры отчётов
| Тип моделирования | Настройки |
| -------: | -------- |
| [Радиально-осовой компрессор](https://github.com/StasF1/turboCharger/releases/download/v1-beta/compressorReport.pdf) | По умолчанию |
| [Радиально-осовая турбина](https://github.com/StasF1/turboCharger/releases/download/v1-beta/radialTurbineReport.pdf) | По умолчанию |
| [Осевая турбина](https://github.com/StasF1/turboCharger/releases/download/v1-beta/axialTurbineReport.pdf) | Не по умолчанию |


# Требования
1. [Python 3](https://www.python.org/downloads/) с пакетом _pillow_
1. Markdown-редактор ([Typora](https://typora.io/#download), желательно)


# Использование программы
## Установка
### Windows
1. Установка менеджера пакетов для Windows [Chocolatey](https://chocolatey.org/)
(если не установлен). Скопировать в окно PowerShell запущенную от имени
Администратора и запустить:
    ```PowerShell
    Set-ExecutionPolicy Bypass -Scope Process -Force; [System.Net.ServicePointManager]::SecurityProtocol = [System.Net.ServicePointManager]::SecurityProtocol -bor 3072; iex ((New-Object System.Net.WebClient).DownloadString('https://chocolatey.org/install.ps1'))
    ```
1. Установка Python 3 вместе с необходимыми пакетами и Markdown-редактора
(также использую PowerShell от имени Администратора)
    ```PowerShell
    choco install -y python3 typora
    python3 -m pip install pillow
    ```
1. Скачивание самой программы turboCharger:
    ```PowerShell
    curl "https://github.com/StasF1/turboCharger/archive/v2.3-beta.zip" -o $HOME/Downloads/turboCharger
    ```

### macOS
1. Установка менеджера пакетов для macOS [Homebrew](https://brew.sh/)
(if not installed). Скопировать в окно Терминала и запустить:
    ```bash
    /bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install.sh)"
    ```
1. Установка Python 3 вместе с необходимыми пакетами и Markdown-редактора
    ```bash
    brew install python3 typora
    python3 -m pip install pillow
    ```
1. Скачивание самой программы turboCharger:
    ```bash
    curl "https://github.com/StasF1/turboCharger/archive/v2.3-beta.zip" -o $HOME/Downloads/turboCharger
    ```

### Linux
1. Установка необходимых пакетов Python 3
    ```bash
    python3 -m pip install pillow
    ```
1. Скачивание самой программы turboCharger:
    ```bash
    curl "https://github.com/StasF1/turboCharger/archive/v2.3-beta.zip" -o $HOME/Downloads/turboCharger
    ```

## Запуск
```bash
cd $HOME/Downloads/turboCharger
python3 turbocharger.py
```
⚠ Подробное руководство доступно в [**Wiki**](https://github.com/StasF1/turboCharger/wiki)


# Структура
```gitignore
turboCharger-2.2-beta
├── compressor
│   ├── post
│   └── pre
├── etc                 # шрифты, бланки картинок и проч.
│   ├── compressor
│   └── turbine
│       ├── axial
│       └── radial
├── results*            # результаты расчётов и копии словарей (*config.py-файлов)
│   ├── compressor
│   └── turbine
│       ├── axial
│       └── radial
└── turbine
    ├── post
    └── pre
# *создаётся при проведённом расчёте
```
---
Отдельная благодарность **Алексею Быкову** за проведённое тестирование кода и поиск ошибок.