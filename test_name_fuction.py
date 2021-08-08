import unittest

from name_function import get_formatted_name

class NamesTestCase(unittest.TestCase):
      """ tests for name_fuction.py """

      def test_first_last_name(self):
          """ Do names 'janis joplin work"""
          formatted_name = get_formatted_name('chinmaya', 'das')
          self.assertEqual(formatted_name, 'Chinmaya Das')


      def test_first_last_middle(self):
            """ Do names like chinmaya lenka das """
            formatted_name = get_formatted_name('chinmaya', 'das', 'lenka')
            self.assertEqual(formatted_name, 'Chinmaya Lenka Das')
            

if __name__== '__main__':
    unittest.main()
