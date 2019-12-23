from pytypus import option


def test_map():

    e = option.empty()
    mapped_e = e.map(lambda k: str(k))
    assert mapped_e.is_empty()
    f = option.some("string")
    mapped_f = f.map(lambda s: len(s))
    assert mapped_f.or_value(5) == 6


def test_obj_protocols():
    counter = 0
    e = option.empty()
    assert str(e) == "EmptyOption"
    for x in e:
        counter = counter + 1
    assert counter == 0
    f = option.some("string")
    assert str(f) == "string"
    for x in f:
        counter = counter + 1
    assert counter > 0
