import unittest

from Chapter_3 import module_3_4


class TestModule36(unittest.TestCase):
    def setUp(self):
        self.root_word = "course"
        self.words = ["discourse", "source", "purse", "recourse", "horse"]
        self.expected_output = ["discourse", "source", "recourse"]
        self.non_string_values = [1, 2.4, None, True, [], {}]

    def test_single_root_words(self):
        result = module_3_4.single_root_words(self.root_word, *self.words)
        self.assertEqual(result, self.expected_output)

    def test_empty_input_parameters(self):
        result = module_3_4.single_root_words("", "")
        self.assertEqual(result, [])

    def test_with_non_string_values(self):
        for i in self.non_string_values:
            with self.assertRaises(TypeError):
                module_3_4.single_root_words(i, *self.words)
            with self.assertRaises(TypeError):
                module_3_4.single_root_words(self.root_word, i)

    def test_root_word_in_self(self):
        words = ["course", "free"]
        self.assertEqual(module_3_4.single_root_words(self.root_word, *words), ["course"])


if __name__ == "__main__":
    unittest.main()
