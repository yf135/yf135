from FileUtil import *
import argparse
random_max=10# 默认值


# （函数）通过递归生成表达式 返回值为字符串类型的表达式
def produce_expression():
    init = random.randint(1, 3)
    tree_root = create_tree(init)
    calculate_expression(tree_root)# 这是一步验算
    if tree_root.error==0 and read_tree(tree_root) not in expressions_list:
        viariant_trees=search_variant_tree(tree_root)
        for viariant_tree in viariant_trees:  # 迭代生成器
            expressions_list.append(read_tree(viariant_tree))  # 处理并添加生成的表达式
        return read_tree(tree_root)
    else:
        produce_expression()

# (函数)用于检查答案正确性
def check_answer(expressions_list,answers_list):
    for i in range(len(expressions_list)):
        if answers_list[i] == Fraction().from_string(calculate_expression(transform_tree(expressions_list[i]))).to_string_simplified():
            right_answers_list.append(i+1)
        else:
            wrong_answers_list.append(i+1)
# (函数)命令行参数解析
def command_line_parser():
    global random_max
    parser = argparse.ArgumentParser(description='Fraction arithmetic calculator')
    parser.add_argument('-n', '--number', type=int, default=0, help='number of exercises')
    parser.add_argument('-e','--exercise_path', type=str, default=None, help='exercise file path')
    parser.add_argument('-a','--answer_path', type=str, default=None, help='answer file path')
    parser.add_argument('-s', '--random_max', type=int, default=None, help='random maximum value')
    args = parser.parse_args()
    if args.exercise_path !=  None and args.answer_path != None:
        FileUtil().clear_grade()
        FileUtil().read_exercises()
        FileUtil().read_answers()
        check_answer(exercises_list,answers_list)
        FileUtil().write_grade()
    elif args.exercise_path != None or args.answer_path != None:
        print("exercise_path and answer_path must be both specified or both not specified")
    if args.random_max != None :
        if args.random_max>0:
            random_max = args.random_max-1
        else:
            print("random seed must be a positive integer")
    if args.number>0:
        run(args.number)
# (函数)生成表达式和对应答案到对应文件中
def run(n):
    FileUtil().clear_file()
    while n>0:
        test_str=produce_expression()
        if test_str != None:
            FileUtil().write_exercises(test_str+"=")
            root=transform_tree(test_str)
            result=calculate_expression(root)
            result=Fraction().from_string(result).to_string_simplified()
            FileUtil().write_answers(result)
            n-=1

# 运行部分
command_line_parser()
