import unittest

from didyoumean3.didyoumean import did_you_mean

mock_meal = ("Aubergines sautées", "sautéed eggplants", 10)


class IntegrationTestCase(unittest.TestCase):
    """ Integration Tests for didyoumean. """
    corrections = [
        ("Aubergine sautee", "Aubergine sautée"),
        ("Pommes de terre sautees", "Pommes de terre sautées"),
        ("steak hache", "steak haché"),
        ("télégrafe", "télégraphe"),
        ("Focacia d'aubergine", "Focaccia d'aubergine")
    ]

    def setUp(self):
        pass

    def test_simple(self):
        for (query, corrected) in self.corrections:
            self.assertEqual(corrected, did_you_mean(query, "fr"),
                             "%s should correct to %s" % (query, corrected))
