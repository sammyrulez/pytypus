from pytypus.either import right, left


def test_map():

    ok_val = right("Hello")
    hello_world = ok_val.map(lambda v: v + " world")
    assert hello_world.right != None
    assert hello_world.right == "Hello world"

    ko_val = left("x")
    ko_val.map(lambda v: v + " world")
    assert hello_world.right == None
