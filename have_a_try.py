# coding=gbk
# 植物学B涉及种子植物的分科检索表
# Identification Key of Spermatophyte by Family in Botany B
# Use Python 3.8.3 (tags/v3.8.3:6f8c832, May 13 2020, 22:37:02) [MSC v.1924 64 bit (AMD64)] on win32
message_title = "\t\t\t\t\t植物学B所涉及种子植物的检索表"
message_title += "\n\t\t回答问题以与你所检索的特征对应。按提示输入，否则退出程序。"
message_title += "（是——y；否——n）\n"
print(message_title)

# 进入主程序
head = "您检索的是："
case_1 = input("子叶一枚还是两枚（输入文字“一”或“两”）?\n")
if case_1 == '一' :
    print("唇瓣、和蕊柱、花粉团块？")
    case_2 = input("（输入“y” 或“n”）\n")
    if case_2 == 'y' :
        print(head + "兰科")
    elif case_2 == 'n' :
        print("颖果？")
        case_3 = input("（输入“y” 或“n”）\n")
        if case_3 == 'y' :
            print(head + "禾本科")
        elif case_3 == 'n' :
            print("1.秆三棱、实心、无节\n"
                    + "2.上位子房、雄蕊6枚\n"
                    + "3.下位子房、雄蕊6枚")
            case_4 = str(input("（输入对应的序号（如“1”））\n"))
            if case_4 == '1' :
                print(head + "莎草科")
            elif case_4 == '2' :
                print(head + "百合科")
            elif case_4 == '3' :
                print(head + "鸢尾科")
            else :
                print("Thanks for your use1 ")
        else :
            print("Thanks for your use! ")
    else :
        print("Thanks for your use! ")
elif case_1 == '两' :
    print("花被？")
    case_5 = input("（输入“无” 或“有”）\n")
    if case_5 == '无' :
        print(head + "杨柳科")
    elif case_5 == '有' :
        print("萼瓣？")
        case_6 = input("（输入“不分”或“分”）\n")
        if case_6 == '不分' :
            print(head + "木兰科")
        elif case_6 == '分' :
            print("花冠？")
            case_7 = input("（输入“离生”或“合生”）\n")
            if case_7 == '离生' :
                print("1.双悬果;伞形或复伞形花序\n"
                        + "2.荚果\n"
                        + "3.非上述")
                case_8 = str(input("（输入对应的序号（如“1”））\n"))
                if case_8 == '1' :
                    print(head + "伞形科")
                elif case_8 == '2' :
                    print(head + "豆科")
                    print("1.蝶形花冠\n"
                            + "2.假蝶形花冠\n"
                            + "3.辐射对称花冠")
                    case_9 = str(input("（输入对应的序号（如“1”））\n"))
                    if case_9 == '1' :
                        print(head + "蝶形花亚科")
                    elif case_9 == '2' :
                        print(head + "云实亚科")
                    elif case_9 == '3' :
                        print(head + "含羞草亚科")
                    else :
                        print("Thanks for your use! ")
                elif case_8 == '3' :
                    print("1.十字花冠;四强雄蕊;角果\n"
                            + "2.有副萼;单体雄蕊\n"
                            + "3.有距\n"
                            + "4.节膨大;雄蕊是花瓣的两倍\n"
                            + "5.花5基数;雄蕊多数")
                    case_10 = str(input("（输入对应的序号（如“1”））\n"))
                    if case_10 == '1' :
                        print(head + "十字花科")
                    elif case_10 == '2' :
                        print(head + "锦葵科")
                    elif case_10 == '3' :
                        print(head + "堇菜科")
                    elif case_10 == '4' :
                        print(head + "石竹科")
                    elif case_10 == '5' :
                        print(head + "蔷薇科")
                        print("1.子房下位；梨果\n"
                                + "2.子房上位")
                        case_11 =  str(input("（输入对应的序号（如“1”））\n"))
                        if case_11 == '1' :
                            print(head + "苹果亚科")
                        elif case_11 == '2' :
                            print("1.核果\n"
                                    + "2.心皮多数\n"
                                    + "3.心皮5")
                            case_12 = str(input("输入对应的序号（如“1”）\n"))
                            if case_12 == '1' :
                                print(head + "李亚科")
                            elif case_12 == '2' :
                                print(head + "蔷薇亚科")
                            elif case_12 == '3' :
                                print(head + "绣线菊亚科")
                            else :
                                print("Thanks for your use! ")
                    else :
                        print("Thanks for your use!")
                else :
                    print("Thanks for your use! ")
            elif case_7 == '合生' :
                print("1.花药孔裂;花萼宿存;蒴果或浆果\n"
                        + "2.漏斗状花冠;茎缠绕;蒴果\n"
                        + "3.唇形花冠;二强雄蕊或雄蕊2个;子房深四裂;四小坚果\n"
                        + "4.唇形花冠；二强雄蕊；2心皮合生为2室；蒴果\n"
                        + "5.花被4裂；雄蕊2枚\n"
                        + "6.子房下位；雄蕊与花被同数互生\n"
                        + "7.头状花序；有总苞；聚药雄蕊；瘦果")
                case_13 = str(input("（输入对应的序号（如“1”））\n"))
                if case_13 == '1' :
                    print(head + "茄科")
                elif case_13 == '2' :
                    print(head + "旋花科")
                elif case_13 == '3' :
                    print(head + "唇形科")
                elif case_13 == '4' :
                    print(head + "玄参科")
                elif case_13 == '5' :
                    print(head + "木犀科")
                elif case_13 == '6' :
                    print(head + "忍冬科")
                elif case_13 == '7' :
                    print(head + "菊科")
                    print("1头状花序且全为舌状花；有乳汁\n"
                            + "2.头状花序大多为管状花")
                    case_14 = str(input("（输入对应的序号（如“1”））\n"))
                    if case_14 == '1' :
                        print(head + "舌状花亚科")
                    elif case_14 == '2' :
                        print(head + "管状花亚科")
                    else :
                        print("Thanks for your use!")
                else :
                    print("Thanks for your use!")
            else :
                print("hanks for your use! ")
        else :
            print("Thanks for your use! ")
    else :
        print("Thanks for your use! ")
else :
    print("Thanks for your use! ")
