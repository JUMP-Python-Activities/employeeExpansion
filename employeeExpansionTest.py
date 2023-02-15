import unittest 
from unittest.mock import patch
from io import StringIO
import datetime

from employeeExpansion import employee
class TesteEmployeeExpansion(unittest.TestCase):

    @patch('sys.stdin', StringIO('3\nSpongebob Squarepants\n34\nPatrick Star\n32\nSquidward Tentacles\n38'))
    def test_dict_contents(self):
        #Run the function
        results = employee()

        #Save what we are expecting
        expected= [{'First Name':'Spongebob','Last Name': 'Squarepants','Birth Year': (datetime.date.today().year - 34),'Email':'Spongebob.Squarepants@company.com' },
                   {'First Name':'Patrick','Last Name': 'Star','Birth Year': (datetime.date.today().year - 32),'Email':'Patrick.Star@company.com' },
                   {'First Name':'Squidward','Last Name': 'Tentacles','Birth Year': (datetime.date.today().year - 38),'Email':'Squidward.Tentacles@company.com' }]

        #Check values
        self.assertEqual(results, expected)

    @patch('sys.stdin', StringIO('1\nSpongebob Squarepants\nb\ns\n32'))
    def test_age_error(self):
        try:
            employee()
        except:
            self.fail('The program should check if users input a number and allow them to reenter the age until it is a number')

    @patch('sys.stdin', StringIO('b\nx\n1\nSpongebob Squarepants\n32'))
    def test_number_of_employees_error(self):
        try:
            employee()
        except:
            self.fail('The program should check if users input a number and allow them to reenter the number of employees until it is a number')

    
if __name__ == '__main__':
    unittest.main()