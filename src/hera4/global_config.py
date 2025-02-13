from __future__ import annotations

from collections.abc import Callable
from typing import TYPE_CHECKING, Optional, Tuple, Union

from typing_extensions import Protocol

if TYPE_CHECKING:
    from hera4.task import Task
    from hera4.workflow import Workflow


# usage of `pragma: no cover` since coverage will complain that protocols are not tested. These are indeed tested
# but protocols encourage nominal typing, so any function definition that implements a protocol will not be "noticed"
# by coverage. See `test_global_config` for test coverage
class TaskHook(Protocol):  # pragma: no cover
    def __call__(self, t: Task) -> None:
        ...


# usage of `pragma: no cover` since coverage will complain that protocols are not tested. These are indeed tested
# but protocols encourage nominal typing, so any function definition that implements a protocol will not be "noticed"
# by coverage. See `test_global_config` for test coverage
class WorkflowHook(Protocol):  # pragma: no cover
    def __call__(self, w: Workflow) -> None:
        ...


class _GlobalConfig:
    """Hera global configuration holds any user configuration such as global tokens, hooks, etc.

    Notes
    -----
    This should not be instantiated directly by the user. There is an instance of the `_GlobalConfig` in this module,
    which is what should be used. Access as either `hera4.GlobalConfig` or `hera4.global_config.GlobalConfig/Config`.
    """

    # protected attributes are ones that are computed/go through some light processing upon setting or
    # are processed upon accessing. The rest, which use primitive types, such as `str`, can remain public
    _image: Union[str, Callable[[], str]] = "python:3.7"
    _token: Union[Optional[str], Callable[[], Optional[str]]] = None

    host: Optional[str] = None
    verify_ssl: bool = True
    api_version: str = "argoproj.io/v1alpha1"
    namespace: str = "default"
    service_account_name: Optional[str] = None
    task_post_init_hooks: Tuple[TaskHook, ...] = ()
    workflow_post_init_hooks: Tuple[WorkflowHook, ...] = ()

    def reset(self) -> None:
        """Resets the global config container to its initial state"""
        self.__dict__.clear()  # Wipe instance values to fallback to the class defaults

    @property
    def image(self) -> str:
        """Return the default image to use for Tasks"""
        if isinstance(self._image, str):
            return self._image
        return self._image()

    @image.setter
    def image(self, image: Union[str, Callable[[], str]]) -> None:
        """Set the default image to use for Tasks"""
        self._image = image

    @property
    def token(self) -> Optional[str]:
        """Returns an Argo Workflows global token"""
        if self._token is None or isinstance(self._token, str):
            return self._token
        return self._token()

    @token.setter
    def token(self, t: Union[Optional[str], Callable[[], Optional[str]]]) -> None:
        """Sets the Argo Workflows token at a global level so services can use it"""
        self._token = t


GlobalConfig = _GlobalConfig()
