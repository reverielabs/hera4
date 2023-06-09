from hera4 import Task, TemplateRef, Workflow

# The name of the DAG template is either the name of WorkflowTemplate (default), or the `dag_name`
with Workflow("workflow-with-template-ref") as w:
    Task("coin-flip", template_ref=TemplateRef(name="hera4-workflow-templates", template="coin-flip"))

w.create()
