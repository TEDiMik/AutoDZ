import unittest
import codewars

class TestCalc(unittest.TestCase):



    def test_codewars_countBits_0_0(self):

        result = codewars.countBits(0)

        self.assertEqual(result,0)



    def test_codewars_countBits_4_1(self):

        result = codewars.countBits(4)

        self.assertEqual(result,1)


#make_readable

    def test_codewars_make_readable_86399_23_59_59(self):

        result = codewars.make_readable(86399)

        self.assertEqual(result,"23:59:59")


    def test_codewars_make_readable_70_00_01_10(self):

        result = codewars.make_readable(70)

        self.assertEqual(result,"00:01:10")

    def test_codewars_make_readable_60_00_01_00(self):

        result = codewars.make_readable(60)

        self.assertEqual(result,"00:01:00")


    def test_codewars_make_readable_0_00_00_00(self):

        result = codewars.make_readable(0)

        self.assertEqual(result,"00:00:00")


    def test_codewars_make_readable_5_00_00_05(self):

        result = codewars.make_readable(5)

        self.assertEqual(result,"00:00:05")

    def test_codewars_format_duration_86399_23_59_59(self):

        result = codewars.format_duration(86399)

        self.assertEqual(result,"23:59:59")
    


        



    
    def test_codewars_countBits_7_3(self):

        result = codewars.countBits(7)

        self.assertEqual(result,3)


        

    def test_codewars_stringEdit(self):

        result = codewars.to_camel_case("the_stealth_warrior")

        self.assertEqual(result,"theStealthWarrior","to_camel_case('the_stealth_warrior') did not return correct value")


    def test_codewars_stringEdit_2(self):

        result = codewars.to_camel_case("The-Stealth-Warrior")

        self.assertEqual(result,"TheStealthWarrior","to_camel_case('The-Stealth-Warrior') did not return correct value")


    def test_codewars_stringEdit_3(self):
        result = codewars.to_camel_case("a-Cat_Is-evil")
        self.assertEqual(result,"aCatIsEvil")


    def test_codewars_BounceBall(self):
        result = codewars.bouncingBall(3, 0.66, 1.5)
        self.assertEqual(result,3)

    

    


    def test_codewars(self):
        
        result = codewars.camel_case("test case")

        self.assertEqual(result,"TestCase")

    #Что такое self ??? Надо узнать









    

if __name__ == '__main__':
    unittest.main()


