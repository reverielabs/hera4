"""This example showcases the hello world example of Hera"""
from hera4 import Task, Workflow


def hello():
    print("Hello, Hera!")


# assumes you used `hera4.set_global_token` and `hera4.set_global_host` so that the workflow can be submitted
with Workflow("hello-hera4") as w:
    Task("t", hello)

w.create()
