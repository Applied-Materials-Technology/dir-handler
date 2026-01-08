import pytest
import dirhandler as dh

def test_set_definition_default():

    my_definitions = {"x":"3", "y":"2"}
    default_definitions = dh.set_definitions()
    assert my_definitions == default_definitions

def test_set_definition_custom():

    my_definitions = {"x":"30", "y":"20"}
    set_definitions = dh.set_definitions(my_definitions)
    assert my_definitions == set_definitions

def test_set_single_definition():
    
    my_definitions = {"x":"3", "y":"2"}
    set_definition = dh.set_definitions(my_definitions)
    dh.set_value(set_definition, "x", "30")
    expected_definitions = {"x":"30", "y":"2"}
    assert set_definition == expected_definitions