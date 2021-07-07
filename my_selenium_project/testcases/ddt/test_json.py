import pytest
import json


def get_data():
    with open('test.json') as f:
        lst = []
        data = json.load(f)
        lst.extend(data['keys'])
        return lst


@pytest.mark.parametrize('name', get_data())
def test01(name):
    print(name)


if __name__ == '__main__':
    # print(get_data())
    pytest.main(['-sv', 'test_json.py'])
