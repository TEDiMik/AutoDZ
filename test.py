import unittest
import codewars

class TestCalc(unittest.TestCase):


    def test_codewars_stringEdit(self):

        result = codewars.to_camel_case("the_stealth_warrior")

        self.assertEqual(result,"theStealthWarrior","to_camel_case('the_stealth_warrior') did not return correct value")


    def test_codewars_stringEdit_2(self):

        result = codewars.to_camel_case("The-Stealth-Warrior")

        self.assertEqual(result,"TheStealthWarrior","to_camel_case('The-Stealth-Warrior') did not return correct value")


    def test_codewars_stringEdit_3(self):
        result = codewars.to_camel_case("a-Cat_Is-evil")
        self.assertEqual(result,"aCatIsEvil")

    

    


    def test_codewars(self):
        
        result = codewars.camel_case("test case")

        self.assertEqual(result,"TestCase")

    #Что такое self ??? Надо узнать









    

if __name__ == '__main__':
    unittest.main()


