import pytest

from hera4 import WorkflowStatus


def test_workflow_status_instantiates_as_expected():
    argo_status = "Running"
    hera4_status = WorkflowStatus.from_argo_status(argo_status)

    assert isinstance(hera4_status, WorkflowStatus)
    assert hera4_status == WorkflowStatus.Running


def test_workflow_status_raises_key_error_on_unrecognized_status():
    argo_status = "Unknown"

    with pytest.raises(KeyError) as e:
        WorkflowStatus.from_argo_status(argo_status)

    assert f"Unrecognized status {argo_status}" in str(e.value)
