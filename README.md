# snippet_logger_progressbar

## Snippet z loggerem i progressbarem


## **Przed uruchomieniem:** 

Przed uruchomieniem należy utworzyć plik "settings.ini" i uzupełnić poniższe dane:

```ini
[main_config]
debug = False

```


## **Użycie:** 

```python
from config_cls import Config
import logging

CONF = Config()
CONF.logger()
logging.info(f"Products: {len(products)}")
total = len(products)
progress = 0
for product in products:
    progress += 1
    CONF.progress_bar(progress, total)

CONF.reset_progress_color()
```