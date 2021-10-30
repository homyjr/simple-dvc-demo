import pytest

class NotInRange(Exception):
    def __init__(self, input_, message="value not in range"):
        self.input_ = input_
        self.message = message
        super().__init__(self.message)




def test_generic():
    a = 5
    with pytest.raises(NotInRange):
        if a not in range(10, 20):
            raise NotInRange
    