import unittest
from FileUtil import FileUtil
from BinaryTree import  *


def remove_denominator_one(fraction_str):
    if '/' in fraction_str:
        try:
            numerator, denominator = map(int, fraction_str.split('/'))

            # 处理分母为1的情况
            if denominator == 1:
                return str(numerator)

                # 处理假分数转换为带分数的情况
            if numerator >= denominator:
                whole_part = numerator // denominator
                new_numerator = numerator % denominator

                # 如果余数为0，则只需返回整数部分
                if new_numerator == 0:
                    return str(whole_part)
                else:
                    # 否则，返回带分数形式
                    return f"{whole_part}'{new_numerator}/{denominator}"

                    # 如果不是假分数，则直接返回原始分数字符串
            else:
                return fraction_str
        except ValueError:
            # 如果无法将分割后的字符串转换为整数，则返回错误信息
            return "Invalid fraction format"

            # 如果输入不是分数字符串，则直接返回原字符串（或根据需要处理）
    return fraction_str

class TestCollaborator(unittest.TestCase):

    def test_fraction_operations(self):
        # 测试分数的加减乘除和化简，执行十次
        for _ in range(10):
            # 随机生成两个分数
            a = Fraction()
            b = Fraction()
            a_str = a.to_string_simplified()
            b_str = b.to_string_simplified()

            # 测试加法
            add_result = Fraction().add(a_str, b_str)

            # 测试减法
            sub_result = Fraction().sub(b_str, a_str)

            # 测试乘法
            mul_result = Fraction().mul(a_str, b_str)

            # 测试除法
            div_result = Fraction().div(b_str, a_str)

            # 将分数字符串转换为 Fraction 对象进行比较
            add_expected = Fraction().from_string(add_result).to_string_simplified()
            if sub_result != 'fail' :
                sub_expected = Fraction().from_string(sub_result).to_string_simplified()
            else :sub_expected = 'fail'
            mul_expected = Fraction().from_string(mul_result).to_string_simplified()
            div_expected = Fraction().from_string(div_result).to_string_simplified()

            add_result = remove_denominator_one(add_result)
            sub_result = remove_denominator_one(sub_result)
            mul_result= remove_denominator_one(mul_result)
            div_result= remove_denominator_one(div_result)

            self.assertEqual(add_result, add_expected)
            self.assertEqual(sub_result, sub_expected)
            self.assertEqual(mul_result, mul_expected)
            self.assertEqual(div_result, div_expected)

    def test_transform_tree_and_calculate(self):
        # 测试表达式转换和计算，执行十次
        for _ in range(10):
            # 随机生成一个表达式
            a = Fraction()
            b = Fraction()
            expression = f"{a.to_string_simplified()}+{b.to_string_simplified()}"
            tree_root = transform_tree(expression)
            result = calculate_expression(tree_root)
            result_str = Fraction().from_string(result).to_string_simplified()


            # 计算预期结果
            expected_result = Fraction().add(a.to_string_simplified(), b.to_string_simplified())
            expected_result = remove_denominator_one(expected_result)
            self.assertEqual(result_str, expected_result)

    def test_read_tree(self):
        # 测试树结构读取为表达式字符串，执行十次
        for _ in range(10):
            a = Fraction()
            b = Fraction()
            expression = f"{a.to_string_simplified()}+{b.to_string_simplified()}"
            tree_root = transform_tree(expression)
            read_expr = read_tree(tree_root)
            self.assertEqual(read_expr, expression)

    def test_file_util(self):
        # 测试文件操作
        file_util = FileUtil()
        file_util.clear_file()  # 清空文件
        test_exercise = "3/4+1/2"
        test_answer = "5/4"
        file_util.write_exercises(test_exercise)
        file_util.write_answers(test_answer)

        exercises = []
        answers = []
        file_util.read_exercises()
        file_util.read_answers()

        exercises = exercises_list
        answers = answers_list

        self.assertEqual(exercises[0], test_exercise.strip())
        self.assertEqual(answers[0], test_answer.strip())

if __name__ == '__main__':
    unittest.main()
