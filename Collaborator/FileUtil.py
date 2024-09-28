from BinaryTree import *


# (类)包含五种文件读写函数和一种清空文件函数 主要负责文件的处理层
class FileUtil():
    def clear_file(self):
        with open("exercises.txt", 'r+') as file:
            file.truncate(0)
        with open("answers.txt", 'r+') as file:
            file.truncate(0)

    def clear_grade(self):
        with open("grade.txt", 'r+') as file:
            file.truncate(0)

    def read_exercises(self):
        with open('exercises.txt', 'r', encoding="utf-8") as f:
            for line in f:
                exercises_list.append(line.strip().replace("=", ""))

    def read_answers(self):
        with open('answers.txt', 'r', encoding="utf-8") as f:
            for line in f:
                answers_list.append(line.strip())

    def write_exercises(self, str):
        with open('exercises.txt', 'a', encoding="utf-8") as f:
            f.write(str + "\n")

    def write_answers(self, str):
        with open('answers.txt', 'a', encoding="utf-8") as f:
            f.write(str + "\n")

    def write_grade(self):
        with open('grade.txt', 'a', encoding="utf-8") as f:
            f.write(
                f"Right:{len(right_answers_list)}{right_answers_list}\nWrong:{len(wrong_answers_list)}{wrong_answers_list}\n")

