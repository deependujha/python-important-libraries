# Logging in Python

- Logging is a means of tracking events that happen when some software runs. 
- The software’s developer adds logging calls to their code to indicate that certain events have occurred.

| Level    | When it’s used |
| -------- | ------- |
| DEBUG  | Detailed information, typically of interest only when diagnosing problems.   |
| INFO | Confirmation that things are working as expected.|
| WARNING    | An indication that something unexpected happened, or indicative of some problem in the near future (e.g. ‘disk space low’). The software is still working as expected.    |
| ERROR    | Due to a more serious problem, the software has not been able to perform some function.|
| CRITICAL    | A serious error, indicating that the program itself may be unable to continue running.    |

- The **`default level is WARNING`**, which means that only events of this level and above will be tracked, unless the logging package is configured to do otherwise.

```python
import logging

logger = logging.getLogger(__name__)
logging.basicConfig(
    filename='example.log', 
    encoding='utf-8',
    level=logging.DEBUG,
    format='%(asctime)s %(message)s', 
    datefmt='%m/%d/%Y %I:%M:%S %p'
)


logger.debug('This message should go to the log file')
logger.info('So should this')
logger.warning('And this, too')
logger.error('And non-ASCII stuff, too, like Øresund and Malmö')
```
