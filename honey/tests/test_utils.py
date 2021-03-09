from honey import utils


class TestParseList:
    def test_empty(self):
        assert utils.parse_list('') == []

    def test_if_string(self):
        value = utils.parse_list("\n1, 2, 3   ")

        assert value == [1, 2, 3]

    def test_if_list(self):
        value = utils.parse_list(["1", None, 2, 3, None])

        assert value == [1, 2, 3]

    def test_if_string_and_is_numeric_is_false(self):
        value = utils.parse_list("\n1, 2, 3  ", is_numeric=False)

        assert value == ["1", "2", "3"]

    def test_if_list_and_is_numeric_is_false(self):
        value = utils.parse_list(["1", None, 2, 3, None], is_numeric=False)

        assert value == ["1", 2, 3]


class TestParseText:
    def test_ip_num_str(self):
        assert utils.parse_text("wrong format\nIP=1.2.3.4\nNUM=-12\nFLOAT=1.1\nFREQ=50Hz\nNAME=name") == dict(
            IP="1.2.3.4", NUM=-12, FLOAT=1.1, FREQ=50, NAME="name"
        )

    def test_delimiter(self):
        assert utils.parse_text("DNS: 1.2.3.4\n MODEL: iPhone X", delimiter=":") == dict(
            DNS="1.2.3.4", MODEL="iPhone X"
        )


def test_convert_value_float():
    val = utils.convert_value("1.7")
    assert val == 1.7
    assert isinstance(val, float)


def test_convert_value_integer():
    val = utils.convert_value("2")
    assert val == 2
    assert isinstance(val, int)


def test_convert_value_string():
    assert utils.convert_value("ab") == "ab"


def test_remove_emoji():
    text = "😎😃Remove emoji 😍"
    after_strip = utils.remove_emoji(text=text, repl="")
    assert after_strip == "Remove emoji"
