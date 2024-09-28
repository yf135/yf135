from Fraction import *


symbols = ['+', '-', '×', '÷']  # 运算符字典
precedence = {
        '+': 1,
        '-': 1,
        '×': 2,
        '÷': 2
    }# 优先级字典
expressions_list = []  # 表达式列表
exercises_list = []  # 练习题列表
answers_list = []  # 答案列表
right_answers_list = [] # 正确答案序号列表
wrong_answers_list = [] # 错误答案序号列表

# （类）这个是节点的格式类
class Node:


    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
        self.error = 0  # 异常标志位：0表示正常，1表示异常 包括负数异常、除数为0异常


# (函数)针对四种树型进行随机选择生成 返回值为节点类型的根节点
def create_tree(symbols_num):
    random_one = random.choice(symbols)
    root = Node(random_one)  # 创建新的节点
    root.left = Node(Fraction().to_string_simplified())  # 递归创建左子树
    root.right = Node(Fraction().to_string_simplified())  # 递归创建右子树
    if symbols_num > 1:
        random_two = random.choice(symbols)
        root2 = Node(random_two)  # 创建新的节点
        root.left = root2  # 递归创建左子树
        root2.left = Node(Fraction().to_string_simplified())  # 递归创建左子树
        root2.right = Node(Fraction().to_string_simplified())  # 递归创建右子树
    if symbols_num > 2:
        random_three = random.choice(symbols)
        root3 = Node(random_three)  # 创建新的节点
        choice = random.randint(1, 2)
        if choice == 1:
            root2.left = root3  # 递归创建左子树
            root3.left = Node(Fraction().to_string_simplified())  # 递归创建左子树
            root3.right = Node(Fraction().to_string_simplified())  # 递归创建右子树
        if choice == 2:
            root.right = root3  # 递归创建右子树
            root3.left = Node(Fraction().to_string_simplified())  # 递归创建左子树
            root3.right = Node(Fraction().to_string_simplified())  # 递归创建右子树
    return root  # 返回根节点


# （函数）中序遍历树实现读取表达式 返回值为字符串类型的表达式
def read_tree(node):
    str = ""
    if node is None:
        return str  # 如果节点为空，则返回
    if node.left is not None and node.left.value in ['+', '-'] and node.value in ['×', '÷']:
        str += "("
        str += read_tree(node.left)
        str += ")"
    else:
        str += read_tree(node.left)

    str += node.value

    if node.right is not None and node.right.value in ['+', '-'] and node.value in ['×', '÷']:
        str += "("
        str += read_tree(node.left)
        str += ")"
    else:
        str += read_tree(node.right)

    return str


# (函数)利用后序遍历树和栈结构计算表达式的值 返回值为字符串类型的结果
def calculate(tree_root):
    # 栈压入的是字符串
    stack = []

    def dfs(node):
        if node is None:
            return
        dfs(node.left)
        dfs(node.right)
        stack.append(node.value)
        if stack[-1] == '+':
            stack.pop()
            str = Fraction().add(stack.pop(), stack.pop())
            stack.append(str)
        if stack[-1] == '-':
            stack.pop()
            str = Fraction().sub(stack.pop(), stack.pop())
            if 'fail' in str:
                tree_root.error = 1
                stack.append("-1")
                # print("出现了负数异常 ")
                return
            stack.append(str)
        if stack[-1] == '×':
            stack.pop()
            str = Fraction().mul(stack.pop(), stack.pop())
            stack.append(str)
        if stack[-1] == '÷':
            stack.pop()
            str = Fraction().div(stack.pop(), stack.pop())
            if 'fail' in str:
                tree_root.error = 1
                stack.append("-1")
                # print("出现了除数为0异常")
                return
            stack.append(str)

    dfs(tree_root)
    return stack.pop()


# (函数)把表达式转化为树 返回值为树的根节点
def transform_tree(expression):
    # 去除等于号字符
    expression = expression.replace("=", "")
    optr_stack = []  # 运算符栈
    expt_stack = []  # 表达式树的根节点栈
    current_number = ''
    for char in expression:
        if char.isdigit() or char == '\'' or char == '/':  # 处理数字或分数
            current_number += char
        else:
            if current_number:
                expt_stack.append(Node(current_number))  # 创建数字节点并入栈
                current_number = ''

            if char in symbols:  # 如果是运算符
                while (optr_stack and optr_stack[-1] != '(' and
                       precedence[char] <= precedence[optr_stack[-1]]):
                    # 弹出运算符，构造树
                    top_op = optr_stack.pop()
                    right_node = expt_stack.pop()
                    left_node = expt_stack.pop()
                    operator_node = Node(top_op)
                    operator_node.left = left_node
                    operator_node.right = right_node
                    expt_stack.append(operator_node)  # 重新将构造的树根节点压入expt栈

                optr_stack.append(char)  # 将当前运算符压入运算符栈

            elif char == '(':
                optr_stack.append(char)  # 左括号直接入运算符栈

            elif char == ')':
                while optr_stack and optr_stack[-1] != '(':
                    # 弹出运算符，构造树
                    top_op = optr_stack.pop()
                    right_node = expt_stack.pop()
                    left_node = expt_stack.pop()
                    operator_node = Node(top_op)
                    operator_node.left = left_node
                    operator_node.right = right_node
                    expt_stack.append(operator_node)  # 重新将构造的树根节点压入expt栈

                optr_stack.pop()  # 弹出左括号

    if current_number:  # 处理最后一个数字
        expt_stack.append(Node(current_number))

    # 处理栈中剩余的内容
    while optr_stack:
        top_op = optr_stack.pop()
        right_node = expt_stack.pop()
        left_node = expt_stack.pop()
        operator_node = Node(top_op)
        operator_node.left = left_node
        operator_node.right = right_node
        expt_stack.append(operator_node)  # 将新形成的子树放回栈

    return expt_stack[0] if expt_stack else None  # 返回根节点

