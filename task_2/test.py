import unittest
from json_converter import Converter
from json_converter_raw import ConverterRaw

class TestConverter(unittest.TestCase):
    def test_default(self):
        json_imp = Converter(['id,name,birth,salary,dep\n', '1,Ivan,1980,150000,1\n', '2,Alex,1960,200000,5\n', '3,Ivan,,130000,8'])
        self.assertEqual(json_imp.to_json(), """[
    {
        "id": "1",
        "name": "Ivan",
        "birth": "1980",
        "salary": "150000",
        "dep": "1"
    },
    {
        "id": "2",
        "name": "Alex",
        "birth": "1960",
        "salary": "200000",
        "dep": "5"
    },
    {
        "id": "3",
        "name": "Ivan",
        "birth": "",
        "salary": "130000",
        "dep": "8"
    }
]""")

    def test_default_raw(self):
        json_man = ConverterRaw(['id,name,birth,salary,dep\n', '1,Ivan,1980,150000,1\n', '2,Alex,1960,200000,5\n', '3,Ivan,,130000,8'])
        self.assertEqual(json_man.to_json(), '[{ "id": "1","name": "Ivan","birth": "1980","salary": "150000","dep": "1" '
                                             '},{ "id": "2","name": "Alex","birth": "1960","salary": "200000","dep": "5" '
                                             '},{ "id": "3","name": "Ivan","birth": "","salary": "130000","dep": "8" ''}]') 

    def test_empty_file(self):
        json_imp = Converter(['id,name,birth,salary,dep'])
        self.assertEqual(json_imp.to_json(), '[]')

    def test_empty_file_raw(self):
        json_man = ConverterRaw(['id,name,birth,salary,dep'])
        self.assertEqual(json_man.to_json(), '[]')

    def test_title_another_line(self):
        json_imp = Converter(['1,Ivan,1980,150,1\n', 'id,name,birth,salary,dep\n', '2,Alex,1960,200,5\n', '3,Ivan,2000,130,8'], title=1)
        self.assertEqual(json_imp.to_json(), """[
    {
        "id": "1",
        "name": "Ivan",
        "birth": "1980",
        "salary": "150",
        "dep": "1"
    },
    {
        "id": "2",
        "name": "Alex",
        "birth": "1960",
        "salary": "200",
        "dep": "5"
    },
    {
        "id": "3",
        "name": "Ivan",
        "birth": "2000",
        "salary": "130",
        "dep": "8"
    }
]""")

    def test_title_another_line_raw(self):
        json_man = ConverterRaw(['1,Ivan,1980,150,1\n', 'id,name,birth,salary,dep\n', '2,Alex,1960,200,5\n', '3,Ivan,2000,130,8'], title=1)
        self.assertEqual(json_man.to_json(), '[{ "id": "1","name": "Ivan","birth": "1980","salary": "150","dep": "1" '
                                             '},{ "id": "2","name": "Alex","birth": "1960","salary": "200",'
                                             '"dep": "5" },{ "id": "3","name": "Ivan","birth": "2000",'
                                             '"salary": "130","dep": "8" }]')

    def test_other_delimiter(self):
        json_imp = Converter(['id.name.birth.salary.dep\n', '1.Ivan.1980.150000.1\n', '2.Alex.1960.200000.5\n', '3.Ivan..130000.8'], delimiter='.')
        self.assertEqual(json_imp.to_json(), """[
    {
        "id": "1",
        "name": "Ivan",
        "birth": "1980",
        "salary": "150000",
        "dep": "1"
    },
    {
        "id": "2",
        "name": "Alex",
        "birth": "1960",
        "salary": "200000",
        "dep": "5"
    },
    {
        "id": "3",
        "name": "Ivan",
        "birth": "",
        "salary": "130000",
        "dep": "8"
    }
]""")

    def test_other_delimiter_raw(self):
        json_man = ConverterRaw(['id.name.birth.salary.dep\n', '1.Ivan.1980.150000.1\n', '2.Alex.1960.200000.5\n', '3.Ivan..130000.8'], delimiter='.')
        self.assertEqual(json_man.to_json(), '[{ "id": "1","name": "Ivan","birth": "1980","salary": "150000","dep": "1" '
                                             '},{ "id": "2","name": "Alex","birth": "1960","salary": "200000","dep": "5" '
                                             '},{ "id": "3","name": "Ivan","birth": "","salary": "130000","dep": "8" ''}]') 

if __name__ == "__main__":
    unittest.main()