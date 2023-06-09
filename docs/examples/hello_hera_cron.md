# Hello Hera Cron

This example showcases the cron hello world example of Hera

```python
from hera4 import CronWorkflow, Task


def hello():
    print("Hello, Hera!")


# assumes you used `hera4.set_global_token` and `hera4.set_global_host` so that the workflow can be submitted
with CronWorkflow("hello-hera4-cron", "5 4 * * *", timezone="UTC") as cw:
    Task("t", hello)

cw.create()

# Delete the cron workflow:
# cw.delete()

# Update the cron workflow after redefining it, but keeping the same name:
# cw.update()
```