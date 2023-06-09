from hera4 import Parameter, Task, WorkflowTemplate


def foo(v):
    print(v)


# assumes you used `hera4.set_global_token` and `hera4.set_global_host` so that the workflow can be submitted
with WorkflowTemplate("global-parameters", parameters=[Parameter("v", "42")]) as w:
    Task("t", foo, inputs=[w.get_parameter("v")])

w.create()
