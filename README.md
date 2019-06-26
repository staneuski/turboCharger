# Описание
Программа производит 0D расчёт турбокомпрессора. Написана на языке **_Python 2_**.

По результатам расчёта генерируется отчёт  _compressorReport.md_, _axialTurbineReport.md_  или _radialTurbineReport.md_ на языке **Markdown**. И сохраняются рисунки с уже выставленными _размерами_ на них. Всё это располагается в папке _results/_, создаваемой автоматически. 

![alt text](https://github.com/StasF1/READMEPictures/blob/master/turboCharger/inTurbineWheel.png)

Больше примеров рисунков можно найти [тут](https://github.com/StasF1/turboCharger/wiki/Примеры-получаемых-рисунков)

Программа писалась для чтения отчётов  Markdown-редакторе [Typora](https://typora.io). Желательно использовать его для правильного отображения Latex-формул в файлах формата _.md_.

Если программа выводит ошибку `Error XX: `, то её номер - соответсвующий пункт в методичке, в котором присутствуют некоторые ограничения и результат расчёта не удовлетворяет им.

# История версий
* [Version 4](https://github.com/StasF1/turboCharger/archive/v4.1.zip) - текущая стабильная версия (проверена на WindowsOS, macOS и Linux). Добавлена возможность расчёта лопаточного диффузора компрессора
* [Version 3](https://github.com/StasF1/turboCharger/archive/2f434710fcaaf7b3490b27ce547eeb675d5640c9.zip) - добавлен расчёт осевой турбины
* [Version 2](https://github.com/StasF1/turboCharger/archive/b662077078b15b35b4018b8175d48d35511bdbf9.zip) - добавлена возможность выставления значений с рисунков 2.2 и 3.7 автоматически с помощью весовых коэффициентов
* [Version 1](https://github.com/StasF1/turboCharger/archive/6426ec34df5ef5c2d30bfc3fbf852d39bd998852.zip) - все значения коэффициентов задаются вручную

# Требования
1. [Python 2](https://www.python.org)
2. Pillow - Python-модуль для редактирования изображений ([о том как его скачать](https://github.com/StasF1/turboCharger/issues/2))
3. Markdown-редактор ([Typora](https://typora.io), желательно)

# Порядок работы с программой -> [Wiki](https://github.com/StasF1/turboCharger/wiki)

---
# DEBUGGING
**[Типичные проблемы](https://github.com/StasF1/turboCharger/issues?utf8=✓&q=is%3Aissue+is%3Aclosed+label%3A%22good+first+issue%22+)** при первом запуске:

- [Pillow](https://github.com/StasF1/turboCharger/issues/2)
- [Make Python2 executable](https://github.com/StasF1/turboCharger/issues/3)

Также, в случае, если у вас **что-то не работет** и решения нет – не стесняйтесь нажимать на [`New Issue`](https://github.com/StasF1/turboCharger/issues?utf8=✓&q=) и создавать сообщение о возникшей проблеме.

---
Отдельная благодарность **Алексею Быкову** за проведённое тестирование кода и поиск ошибок.

