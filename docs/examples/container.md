# Container

This example showcases how to run a container, rather than a Python, function, as the payload of a task in Hera

```python
from hera4 import Task, Workflow

# assumes you used `hera4.set_global_token` and `hera4.set_global_host` so that the workflow can be submitted
with Workflow("container") as w:
    Task("cowsay", image="docker/whalesay", command=["cowsay", "foo"])

w.create()
```
