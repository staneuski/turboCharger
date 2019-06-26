# Описание
Программа производит 0D расчёт турбокомпрессора. Написана на языке **_Python 2_**.

По результатам расчёта генерируются отчёты на языке **Markdown** (примеры отчётов представлены ниже), сохраняются рисунки с уже выставленными _размерами_ на них ([примеры рисунков](https://github.com/StasF1/turboCharger/wiki/Примеры-рисунков)). Всё это располагается в папке _results/_, создаваемой автоматически.

![alt text](https://github.com/StasF1/READMEPictures/blob/master/turboCharger/inTurbineWheel.png)

Программа писалась для чтения отчётов  Markdown-редакторе [Typora](https://typora.io). Желательно использовать его для правильного отображения Latex-формул в файлах формата _.md_.

#### Примеры отчётов
|Вариант расчёта         |Настройки        |Отчёт                   |
|-----------------------:|----------------:|:-----------------------|
|     Компрессор         | По умолчанию    |[compressorReport.pdf](https://github.com/StasF1/turboCharger/releases/download/v4.1/compressorReport.pdf)|
|Радиально-осевая турбина| По умолчанию    |[radialTurbineReport.pdf](https://github.com/StasF1/turboCharger/releases/download/v4.1/radialTurbineReport.pdf)|
|Осевая турбина          | Не по умолчанию |[axialTurbineReport.pdf](https://github.com/StasF1/turboCharger/releases/download/v4.1/axialTurbineReport.pdf)|

# Требования
1. [Python 2](https://www.python.org)
2. Pillow - Python-модуль для редактирования изображений ([как его скачать](https://github.com/StasF1/turboCharger/issues/2))
3. Markdown-редактор ([Typora](https://typora.io), желательно)

# История версий

### [Скачать текущую стабильную версию: _v-4.1_](https://github.com/StasF1/turboCharger/archive/v4.1.zip)

|Версия|Скачать|   |
|-----:|------:|:--|
|[4.1](https://github.com/StasF1/turboCharger/releases/tag/v4.1)|[v-4.1](https://github.com/StasF1/turboCharger/archive/v4.1.zip)|**текущая _стабильная_ версия** (проверена на WindowsOS, macOS и Linux). Добавлена возможность расчёта лопаточного диффузора компрессора|
|[3](https://github.com/StasF1/turboCharger/tree/2f434710fcaaf7b3490b27ce547eeb675d5640c9)|[v-3.0](https://github.com/StasF1/turboCharger/archive/2f434710fcaaf7b3490b27ce547eeb675d5640c9.zip)|добавлен расчёт осевой турбины|
|[2](https://github.com/StasF1/turboCharger/tree/b662077078b15b35b4018b8175d48d35511bdbf9)|[v-2.0](https://github.com/StasF1/turboCharger/archive/b662077078b15b35b4018b8175d48d35511bdbf9.zip)|добавлена возможность выставления значений с рисунков 2.2 и 3.7 автоматически с помощью весовых коэффициентов|
|[1, Beta](https://github.com/StasF1/turboCharger/tree/6426ec34df5ef5c2d30bfc3fbf852d39bd998852)|[v-1-beta](https://github.com/StasF1/turboCharger/archive/6426ec34df5ef5c2d30bfc3fbf852d39bd998852.zip)|все значения коэффициентов задаются вручную|

# Порядок работы с программой
Подробное руководство по работе с программой (текущей версии - v-4.1) выложено в [Wiki](https://github.com/StasF1/turboCharger/wiki)

# Структура
```gitignore
turboCharger-4.1
├── compressor
│   └── include        # include-файлы вложенные в compressorMain.py
├── programFiles       # шрифты, бланки картинок и проч.
│   ├── compressor
│   └── turbine
│       ├── axial
│       └── radial
├── results*            # результаты расчётов
└── turbine
    ├── axial
    │   └── include     # include-файлы вложенные в turbineMain.py
    └── radial
        └── include     # include-файлы вложенные в turbineMain.py
 

# *создаётся при проведённом расчёте
```

---
# DEBUGGING
**[Типичные проблемы](https://github.com/StasF1/turboCharger/issues?utf8=✓&q=is%3Aissue+is%3Aclosed+label%3A%22good+first+issue%22+)** при первом запуске:

- [Pillow](https://github.com/StasF1/turboCharger/issues/2)
- [Make Python2 executable](https://github.com/StasF1/turboCharger/issues/3)

Также, в случае, если у вас **что-то не работет** и решения нет – не стесняйтесь нажимать на [`New Issue`](https://github.com/StasF1/turboCharger/issues?utf8=✓&q=) и создавать сообщение о возникшей проблеме.

---
Отдельная благодарность **Алексею Быкову** за проведённое тестирование кода и поиск ошибок.

