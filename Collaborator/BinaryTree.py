from Fraction import *

symbols = ['+', '-', '×', '÷']  # 运算符字典
precedence = {
    '+': 1,
    '-': 1,
    '×': 2,
    '÷': 2
}  # 优先级字典
expressions_list = []  # 表达式列表
exercises_list = []  # 练习题列表
answers_list = []  # 答案列表
right_answers_list = []  # 正确答案序号列表
wrong_answers_list = []  # 错误答案序号列表


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
    result_str = ""
    if node is None:
        return result_str

    # 为了保持运算符优先级
    if node.left is not None and node.left.value in ['+', '-'] and node.value in ['×', '÷']:
        result_str += "(" + read_tree(node.left) + ")"
    else:
        result_str += read_tree(node.left)

    result_str += node.value

    if node.right is not None and node.right.value in ['+', '-'] and node.value in ['×', '÷']:
        result_str += "(" + read_tree(node.right) + ")"
    else:
        result_str += read_tree(node.right)

    return result_str


# (函数)利用后序遍历树和栈结构计算表达式的值 返回值为字符串类型的结果
def calculate_expression(tree_root):
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


# (函数)把根节点对应的树进行变换 把树中所有加号和乘号的左右子树交换的情况 返回值为所有变体树的根节点生成器 比如(1+2)×3有3种变体(2+1)*3,3*(1+2),3*(2+1) 在表达式形式上都是顺序问题
def search_variant_tree(node):
    if node is None:
        return []

    # 递归处理左子树和右子树
    left_trees = search_variant_tree(node.left)
    right_trees = search_variant_tree(node.right)

    variants = []

    # 处理加法和乘法节点
    if node.value in ['+', '×']:
        # 生成左右组合
        for left_tree in left_trees:
            for right_tree in right_trees:
                new_tree1 = Node(node.value)
                new_tree1.left = left_tree
                new_tree1.right = right_tree
                variants.append(new_tree1)

                new_tree2 = Node(node.value)
                new_tree2.left = right_tree
                new_tree2.right = left_tree
                variants.append(new_tree2)
    else:
        # 对其他运算符处理
        for left_tree in left_trees:
            new_tree = Node(node.value)
            new_tree.left = left_tree
            new_tree.right = node.right
            variants.append(new_tree)

        for right_tree in right_trees:
            new_tree = Node(node.value)
            new_tree.left = node.left
            new_tree.right = right_tree
            variants.append(new_tree)

    # 当没有子树时，返回当前节点作为变体
    if not variants:
        variants.append(node)

    return variants