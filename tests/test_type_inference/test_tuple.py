import astroid
import nose
from hypothesis import given, settings, HealthCheck
import tests.custom_hypothesis_support as cs
from typing import Tuple
settings.load_profile("pyta")


@given(cs.tuple_node())
@settings(suppress_health_check=[HealthCheck.too_slow])
def test_tuple(t_tuple):
    """ Test Tuple nodes representing a tuple of various types."""
    module, _ = cs._parse_text(t_tuple)
    for t_node in module.nodes_of_class(astroid.Tuple):
        elt_types = tuple(elt.type_constraints.type for elt in t_node.elts)
        assert t_node.type_constraints.type == Tuple[elt_types]


if __name__ == '__main__':
    nose.main()