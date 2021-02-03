# 编写一个程序，生成一个10x10的随机矩阵并保存为文件（空格分隔行向量、换行分隔列向量），
# 再写程序将刚才保存的矩阵文件另存为CSV格式，用Excel或文本编辑器打开看看结果对不对
import random

def main() :
    Create_TXT_file()
    TXT_to_CSV()



def Create_TXT_file() :
    file = open("chapter_g_c_result.txt", "w")
    matrix = Create_matrix()
    file.write(matrix)
    file.close()
    print("10x10的随机矩阵已保存为“chapter_g_c_result.txt”。")
    return None



def TXT_to_CSV() :
    txt_file = open("chapter_g_c_result.txt", "rt")
    csv_file = open("chapter_g_c_result.csv", "w")
    for line in txt_file :
        processed = line.replace(" ",",")
        csv_file.write(processed)
    txt_file.close()
    txt_file.close()
    print("“chapter_g_c_result.txt”被另存为“chapter_g_c_result.csv”，用WPS检查一下。")
    return None



# 生成矩阵
def Create_matrix() :
    matrix = ""
    for i in range(10) :
        line = ""
        for j in range(10) :
            line += "{} ".format(random.randint(0,9))
        if i != 9 :
            matrix +="{}".format(line).rstrip() + "\n"  # 剔除末尾空格再换行
        else :
            matrix +="{}".format(line).rstrip()
    return matrix



main()

