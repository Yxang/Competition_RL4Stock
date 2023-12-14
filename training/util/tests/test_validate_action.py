import unittest

from training.util.validate_action import validate_action


class UtilTestCase(unittest.TestCase):
    def test_validate_action(self):
        state = [{
            'observation': {
                'serverTime': 93004818.0,
                'eventTime': 93004880.0,
                'code': 2.0,
                'signal0': 0.06040532250349382,
                'signal1': -1.7849400355777338,
                'signal2': -3.4662585069980576,
                'ap0': 4606.900000000001,
                'bp0': 4606.049,
                'av0': 5.0,
                'bv0': 15.0,
                'ap1': 4607.912,
                'bp1': 4605.911,
                'av1': 1.0,
                'bv1': 1.0,
                'ap2': 4609.2,
                'bp2': 4599.816,
                'av2': 10.0,
                'bv2': 5.0,
                'ap3': 4611.5,
                'bp3': 4599.793000000001,
                'av3': 8.0,
                'bv3': 12.0,
                'ap4': 4613.57,
                'bp4': 4599.655000000001,
                'av4': 1.0,
                'bv4': 9.0,
                'code_net_position': 0,
                'ap0_t0': 4599.908
            },
            'new_game': False
        }]

        side = [0, 0, 1]
        vol = [1]
        price = [4583.164]

        (side, vol, price), is_invalid = validate_action(state, (side, vol, price))
        self.assertEqual(side, [0, 1, 0])
        self.assertEqual(vol, [0])
        self.assertEqual(price, [0])
        self.assertTrue(is_invalid)


if __name__ == '__main__':
    unittest.main()
