import unittest


class ValidaCPF:
    def __init__(self, num_cpf):
        self.num_cpf = num_cpf

    def retira_formatacao(self):
        cleaned_cpf = ''
        for num in self.num_cpf:
            if num.isalnum():
                cleaned_cpf += num
        return cleaned_cpf

    # This method check if the number has equals characters. If is all equals return True.
    def check_characters(self):
        num_cpf = self.retira_formatacao()
        for character in num_cpf:
            if character != num_cpf[0]:
                return False
        return True

    @staticmethod
    def valida_cpf_logic(cpf):
        # Getting numbers until -
        str_result = str(cpf)[0:9]
        numbers = [10, 9, 8, 7, 6, 5, 4, 3, 2]
        result = 0

        # This for multiply and sum the number for me.
        for index, number in enumerate(numbers):
            result += int(str_result[index]) * number
        print('Resultado da soma {}'.format(result))

        # Getting the first digit
        if (result * 10 % 11) != 10:
            first_digit = (result * 10) % 11
        else:
            first_digit = 0

        print('Resultado da divisão por 11 é: {}'.format(first_digit))

        # Adding the first digit to the sequence.
        plus_digit = str_result + str(first_digit)
        print('')

        # Adding eleven to the sequence numbers
        numbers.insert(0, 11)
        result = 0

        # Meking same for to get the second digit
        for index, number in enumerate(numbers):
            result += int(plus_digit[index]) * number

        # Getting second digit
        if (result * 10) % 11 != 10:
            second_digit = (result * 10) % 11
        else:
            second_digit = 0

        # Sum the too digit got.
        full_digit = str(first_digit) + str(second_digit)
        print(full_digit)

        # Cheking if the number is a valid cpf
        if full_digit == str(cpf)[9:11]:
            return True
        else:
            return False

    def valida_cpf(self):
        if self.check_characters():
            return False
        else:
            bool_value = self.valida_cpf_logic(self.retira_formatacao())
        return bool_value


class Test_valida(unittest.TestCase):
    def setUp(self):
        self.cpf_1 = ValidaCPF('464.946.958-92')
        self.cpf_2 = ValidaCPF('12345678988')
        self.cpf_3 = ValidaCPF('212548465481')
        self.cpf_4 = ValidaCPF('111.111.111-11')
        self.cpf_5 = ValidaCPF('1.1.1.1.1.1.789-01')

    def test_retira_formatacao(self):
        self.assertEqual(self.cpf_1.retira_formatacao(), '46494695892')

        self.assertEqual(self.cpf_5.retira_formatacao(), '11111178901')

    def test_check_character(self):
        # Testing if the first object has all same characters
        self.assertEqual(self.cpf_1.check_characters(), False)

        self.assertEqual(self.cpf_4.check_characters(), True)

    def test_valida_cpf(self):
        # Testing if the object cpf_1 in setUp is really a valid cpf.
        self.assertEqual(self.cpf_1.valida_cpf(), True)

        # Testing the format returned by method valida_cpf
        self.assertEqual(self.cpf_2.valida_cpf(), False)

        # Testing if method valida_cpf return False when the number is more than 11.
        self.assertEqual(self.cpf_3.valida_cpf(), False)

        # Checking if 111.111.111-11 is invalid
        self.assertEqual(self.cpf_4.valida_cpf(), False)


if __name__ == '__main__':
    unittest.main()
