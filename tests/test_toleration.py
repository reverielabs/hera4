from hera4 import Toleration


def test_toleration_translates():
    hera4_t = Toleration(key="a", effect="NoSchedule", operator="Equal", value="value123")
    argo_t = hera4_t.build()
    assert hasattr(argo_t, "key")
    assert hera4_t.key == getattr(argo_t, "key")
    assert hasattr(argo_t, "effect")
    assert hera4_t.effect == getattr(argo_t, "effect")
    assert hasattr(argo_t, "operator")
    assert hera4_t.operator == getattr(argo_t, "operator")
    assert hasattr(argo_t, "value")
    assert hera4_t.value == getattr(argo_t, "value")
