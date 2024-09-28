import unittest
from FileUtil import FileUtil
from BinaryTree import Node, transform_tree, read_tree, calculate_expression, exercises_list, answers_list, \
    search_variant_tree
from Fraction import Fraction


class TestCollaborator(unittest.TestCase):

    def test_fraction_operations(self):
        a = Fraction().from_string("2/3")  # 2/3的字符串表示
        b = Fraction().from_string("1/3")  # 1/3的字符串表示
        a_str = a.to_string_simplified()
        b_str = b.to_string_simplified()

        # 测试加法
        add_result = Fraction().add(a_str, b_str)
        expected_add = "1/1"
        self.assertEqual(add_result, expected_add, f"加法结果错误: {a_str} + {b_str} = {add_result}")

        # 测试减法
        sub_result = Fraction().sub(b_str, a_str)
        expected_sub = "1/3"
        self.assertEqual(sub_result, expected_sub, f"减法结果错误: {a_str} - {b_str} = {sub_result}")

        # 测试乘法
        mul_result = Fraction().mul(a_str, b_str)
        expected_mul = "2/9"
        self.assertEqual(mul_result, expected_mul, f"乘法结果错误: {a_str} * {b_str} = {mul_result}")

        # 测试除法
        if int(b.numerator) != 0:  # 确保不除以零
            div_result = Fraction().div(b_str, a_str)
            expected_div = "2/1"
            self.assertEqual(div_result, expected_div, f"除法结果错误: {a_str} / {b_str} = {div_result}")
        else:
            self.assertEqual(Fraction().div(a_str, b_str), "fail", f"如果除数为零，应返回 'fail'")

    def test_gcd(self):
        self.assertEqual(Fraction.gcd(10, 5), 5, "gcd 方法错误")
        self.assertEqual(Fraction.gcd(17, 5), 1, "gcd 方法错误")

    def test_to_string_simplified(self):
        # 测试分数转字符串的功能
        fraction = Fraction()
        fraction.numerator = 5
        fraction.denominator = 10
        self.assertEqual(fraction.to_string_simplified(), "1/2", "to_string_simplified 方法错误")

        fraction.numerator = 7
        fraction.denominator = 1
        self.assertEqual(fraction.to_string_simplified(), "7", "to_string_simplified 方法错误")

        fraction.numerator = 0
        fraction.denominator = 1
        self.assertEqual(fraction.to_string_simplified(), "0", "to_string_simplified 方法错误")

        fraction.numerator = 8
        fraction.denominator = 7
        self.assertEqual(fraction.to_string_simplified(), "1'1/7", "to_string_simplified 方法错误")

    def test_from_string(self):
        fraction = Fraction()
        fraction.from_string("2'3/4")
        self.assertEqual(fraction.numerator, 11)
        self.assertEqual(fraction.denominator, 4, "from_string 方法错误")

        fraction.from_string("3/5")
        self.assertEqual(fraction.numerator, 3)
        self.assertEqual(fraction.denominator, 5, "from_string 方法错误")

        fraction.from_string("6")
        self.assertEqual(fraction.numerator, 0)
        self.assertEqual(fraction.denominator, 1, "from_string 方法错误")

    def test_transform_tree_and_calculate(self):
        # 测试表达式转换和计算
        a = Fraction().from_string("1/3")
        b = Fraction().from_string("1/2")
        expression = f"{a.to_string_simplified()}+{b.to_string_simplified()}"
        tree_root = transform_tree(expression)
        result = calculate_expression(tree_root)
        result_str = Fraction().from_string(result).to_string_simplified()

        # 计算预期结果
        expected_result = Fraction().add(a.to_string_simplified(), b.to_string_simplified())
        self.assertEqual(result_str, expected_result)

    def test_read_tree(self):
        # 测试树结构读取为表达式字符串
        for _ in range(10):
            a = Fraction()
            b = Fraction()
            expression = f"{a.to_string_simplified()}+{b.to_string_simplified()}"
            tree_root = transform_tree(expression)
            read_expr = read_tree(tree_root)
            self.assertEqual(read_expr, expression)

    def test_search_variant_tree_strict(self):
        # 构建树: (1 + 2) × 3
        root = Node('×')
        root.left = Node('+')
        root.left.left = Node('1')
        root.left.right = Node('2')
        root.right = Node('3')

        # 生成所有变体
        variants = search_variant_tree(root)

        # 打印生成的变体
        generated_expressions = [read_tree(variant) for variant in variants]
        print(f"Generated Variants: {generated_expressions}")

        # 生成预期的变体
        expected_variants = [
            '(1+2)×3',
            '(2+1)×3',
            '3×(1+2)',
            '3×(2+1)'
        ]

        # 确保每个预期变体都可以被确认
        for expected in expected_variants:
            self.assertIn(expected, generated_expressions, f"未检测到变体: {expected}")

        print("所有变体均已检测到!")

    def test_calculate_expression(self):
        root = Node('+')
        root.left = Node('1')
        root.right = Node('1/2')
        self.assertEqual(calculate_expression(root), '3/2', "计算表达式值错误")

    def test_transform_tree(self):
        expression = "1/2 + 1/2"
        tree_root = transform_tree(expression)
        self.assertIsNotNone(tree_root, "转换表达式为树失败，树根节点为None")

    def test_file_util(self):
        # 测试文件操作
        file_util = FileUtil()
        file_util.clear_file()  # 清空文件
        test_exercise = "3/4+1/2"
        test_answer = "5/4"
        file_util.write_exercises(test_exercise)
        file_util.write_answers(test_answer)

        file_util.read_exercises()
        file_util.read_answers()

        exercises = exercises_list
        answers = answers_list

        self.assertEqual(exercises[0], test_exercise.strip())
        self.assertEqual(answers[0], test_answer.strip())


if __name__ == '__main__':
    unittest.main()
