import src.app.utils.mymath.addition as addition


class TestMath:
    def test_normal_scenario_1(self):
        assert addition.Math.add(1, 2) == 3
