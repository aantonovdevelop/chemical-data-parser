import unittest
import chemical

x = [-7.5, -7.4, -7.300000000000001, -7.200000000000001, -7.100000000000001, -7.000000000000002, -6.900000000000002,
     -6.8000000000000025, -6.700000000000003, -6.600000000000003, -6.5000000000000036, -6.400000000000004,
     -6.300000000000004, -6.200000000000005, -6.100000000000005, -6.000000000000005, -5.900000000000006,
     -5.800000000000006, -5.700000000000006, -5.600000000000007, -5.500000000000007, -5.4000000000000075,
     -5.300000000000008, -5.200000000000008, -5.1000000000000085, -5.000000000000009, -4.900000000000009,
     -4.80000000000001, -4.70000000000001, -4.60000000000001, -4.500000000000011, -4.400000000000011,
     -4.300000000000011, -4.200000000000012, -4.100000000000012, -4.000000000000012, -3.900000000000013,
     -3.800000000000013, -3.7000000000000135, -3.600000000000014, -3.500000000000014, -3.4000000000000146,
     -3.300000000000015, -3.2000000000000153, -3.1000000000000156, -3.000000000000016, -2.9000000000000163,
     -2.8000000000000167, -2.700000000000017, -2.6000000000000174, -2.5000000000000178, -2.400000000000018,
     -2.3000000000000185, -2.200000000000019, -2.100000000000019, -2.0000000000000195, -1.90000000000002,
     -1.8000000000000203, -1.7000000000000206, -1.600000000000021, -1.5000000000000213, -1.4000000000000217,
     -1.300000000000022, -1.2000000000000224, -1.1000000000000227, -1.000000000000023, -0.9000000000000234,
     -0.8000000000000238, -0.7000000000000242, -0.6000000000000245, -0.5000000000000249, -0.4000000000000252,
     -0.3000000000000256, -0.20000000000002593, -0.10000000000002629, -2.6645352591003757e-14, 0.099999999999973,
     0.19999999999997264, 0.2999999999999723, 0.39999999999997193, 0.4999999999999716, 0.5999999999999712,
     0.6999999999999709, 0.7999999999999705, 0.8999999999999702, 0.9999999999999698, 1.0999999999999694,
     1.199999999999969, 1.2999999999999687, 1.3999999999999684, 1.499999999999968, 1.5999999999999677,
     1.6999999999999673, 1.799999999999967, 1.8999999999999666, 1.9999999999999662, 2.099999999999966,
     2.1999999999999655, 2.299999999999965, 2.399999999999965, 2.4999999999999645, 2.599999999999964,
     2.6999999999999638, 2.7999999999999634, 2.899999999999963, 2.9999999999999627, 3.0999999999999623,
     3.199999999999962, 3.2999999999999616, 3.3999999999999613, 3.499999999999961, 3.5999999999999606, 3.69999999999996,
     3.79999999999996, 3.8999999999999595, 3.999999999999959, 4.099999999999959, 4.199999999999958, 4.299999999999958,
     4.399999999999958, 4.499999999999957, 4.599999999999957, 4.699999999999957, 4.799999999999956, 4.899999999999956,
     4.999999999999956, 5.099999999999955, 5.199999999999955, 5.2999999999999545, 5.399999999999954, 5.499999999999954,
     5.5999999999999535, 5.699999999999953, 5.799999999999953, 5.899999999999952, 5.999999999999952, 6.099999999999952,
     6.199999999999951, 6.299999999999951, 6.399999999999951, 6.49999999999995, 6.59999999999995, 6.6999999999999496,
     6.799999999999949, 6.899999999999949, 6.9999999999999485, 7.099999999999948, 7.199999999999948, 7.299999999999947,
     7.399999999999947]
y = [-0.9379999767747389, -0.8987080958116269, -0.8504366206285648, -0.7936678638491537, -0.7289690401258772,
     -0.6569865987187904, -0.5784397643882017, -0.4941133511386105, -0.40484992061660074, -0.3115413635133812,
     -0.215119988087819, -0.11654920485049718, -0.016813900484354154, 0.08308940281749197, 0.18216250427209066,
     0.27941549819892075, 0.3738766648302311, 0.46460217941375187, 0.5506855425976325, 0.6312666378723161,
     0.7055403255703868, 0.7727644875559826, 0.8322674422238968, 0.8834546557201495, 0.9258146823277291,
     0.9589242746631359, 0.9824526126243308, 0.9961646088358398, 0.999923257564101, 0.9936910036334656,
     0.9775301176650993, 0.9516020738895193, 0.9161659367494596, 0.8715757724135939, 0.8182771110644175,
     0.7568024953079364, 0.6877661591839831, 0.6118578909427295, 0.5298361409085046, 0.4425204432948648,
     0.35078322768963316, 0.2555411020268454, 0.15774569414326312, 0.05837414342759516, -0.04158066243327496,
     -0.1411200080598514, -0.23924932921396647, -0.3349881501558892, -0.4273798802338145, -0.5155013718214493,
     -0.5984721441039422, -0.6754631805511375, -0.7457052121767078, -0.8084964038195791, -0.863209366648864,
     -0.9092974268256736, -0.946300087687408, -0.9738476308781906, -0.9916648104524659, -0.9995736030415046,
     -0.9974949866040559, -0.9854497299884639, -0.9635581854171988, -0.9320390859672345, -0.8912073600614456,
     -0.8414709848079089, -0.783326909627498, -0.7173560908995393, -0.6442176872377096, -0.5646424733950556,
     -0.4794255386042248, -0.3894183423086737, -0.295520206661364, -0.19866933079508664, -0.09983341664685431,
     -2.6645352591003757e-14, 0.09983341664680129, 0.1986693307950344, 0.2955202066613131, 0.38941834230862465,
     0.4794255386041781, 0.5646424733950116, 0.6442176872376688, 0.7173560908995023, 0.7833269096274649,
     0.8414709848078802, 0.8912073600614214, 0.9320390859672152, 0.9635581854171846, 0.9854497299884548,
     0.9974949866040521, 0.9995736030415061, 0.9916648104524728, 0.9738476308782027, 0.9463000876874252,
     0.9092974268256957, 0.863209366648891, 0.8084964038196104, 0.7457052121767433, 0.6754631805511768,
     0.598472144103985, 0.515501371821495, 0.4273798802338627, 0.3349881501559394, 0.2392493292140182,
     0.14112000805990416, 0.041580662433328204, -0.05837414342754196, -0.1577456941432105, -0.25554110202679386,
     -0.35078322768958325, -0.44252044329481705, -0.5298361409084594, -0.6118578909426873, -0.6877661591839445,
     -0.7568024953079016, -0.8182771110643868, -0.8715757724135677, -0.9161659367494381, -0.9516020738895029,
     -0.977530117665088, -0.9936910036334596, -0.9999232575641004, -0.9961646088358445, -0.9824526126243407,
     -0.9589242746631511, -0.9258146823277492, -0.8834546557201745, -0.8322674422239263, -0.7727644875560165,
     -0.7055403255704247, -0.6312666378723574, -0.5506855425976769, -0.46460217941379905, -0.37387666483028054,
     -0.27941549819897193, -0.18216250427214306, -0.08308940281754508, 0.01681390048430087, 0.11654920485044425,
     0.21511998808776694, 0.31154136351333056, 0.404849920616552, 0.49411335113856414, 0.5784397643881581,
     0.6569865987187502, 0.7289690401258406, 0.7936678638491212, 0.8504366206285369, 0.8987080958116035]


class ChemicalTest(unittest.TestCase):
    def test_instantiate_data_parser(self):
        parser = chemical.ChemicalDataParser(list(zip(x, y)))

        self.assertEqual(parser.difference, 1)