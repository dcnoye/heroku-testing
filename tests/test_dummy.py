import pytest

#TODO Can be removed later once we have a real test.
@pytest.mark.parametrize("input", [("A"), ("B"),])
def test_dummy(input):
    print("hello test" + input)
    assert True
