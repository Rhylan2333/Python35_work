# coding=gbk
# ֲ��ѧB�漰����ֲ��ķֿƼ�����
# Identification Key of Spermatophyte by Family in Botany B
# Use Python 3.8.3 (tags/v3.8.3:6f8c832, May 13 2020, 22:37:02) [MSC v.1924 64 bit (AMD64)] on win32
message_title = "\t\t\t\t\tֲ��ѧB���漰����ֲ��ļ�����"
message_title += "\n\t\t�ش�������������������������Ӧ������ʾ���룬�����˳�����"
message_title += "���ǡ���y���񡪡�n��\n"
print(message_title)

# ����������
head = "���������ǣ�"
case_1 = input("��Ҷһö������ö���������֡�һ����������?\n")
if case_1 == 'һ' :
    print("���ꡢ�������������ſ飿")
    case_2 = input("�����롰y�� ��n����\n")
    if case_2 == 'y' :
        print(head + "����")
    elif case_2 == 'n' :
        print("ӱ����")
        case_3 = input("�����롰y�� ��n����\n")
        if case_3 == 'y' :
            print(head + "�̱���")
        elif case_3 == 'n' :
            print("1.�����⡢ʵ�ġ��޽�\n"
                    + "2.��λ�ӷ�������6ö\n"
                    + "3.��λ�ӷ�������6ö")
            case_4 = str(input("�������Ӧ����ţ��硰1������\n"))
            if case_4 == '1' :
                print(head + "ɯ�ݿ�")
            elif case_4 == '2' :
                print(head + "�ٺϿ�")
            elif case_4 == '3' :
                print(head + "�β��")
            else :
                print("Thanks for your use1 ")
        else :
            print("Thanks for your use! ")
    else :
        print("Thanks for your use! ")
elif case_1 == '��' :
    print("������")
    case_5 = input("�����롰�ޡ� ���С���\n")
    if case_5 == '��' :
        print(head + "������")
    elif case_5 == '��' :
        print("��ꣿ")
        case_6 = input("�����롰���֡��򡰷֡���\n")
        if case_6 == '����' :
            print(head + "ľ����")
        elif case_6 == '��' :
            print("���ڣ�")
            case_7 = input("�����롰�������򡰺�������\n")
            if case_7 == '����' :
                print("1.˫����;ɡ�λ�ɡ�λ���\n"
                        + "2.�Թ�\n"
                        + "3.������")
                case_8 = str(input("�������Ӧ����ţ��硰1������\n"))
                if case_8 == '1' :
                    print(head + "ɡ�ο�")
                elif case_8 == '2' :
                    print(head + "����")
                    print("1.���λ���\n"
                            + "2.�ٵ��λ���\n"
                            + "3.����Գƻ���")
                    case_9 = str(input("�������Ӧ����ţ��硰1������\n"))
                    if case_9 == '1' :
                        print(head + "���λ��ǿ�")
                    elif case_9 == '2' :
                        print(head + "��ʵ�ǿ�")
                    elif case_9 == '3' :
                        print(head + "���߲��ǿ�")
                    else :
                        print("Thanks for your use! ")
                elif case_8 == '3' :
                    print("1.ʮ�ֻ���;��ǿ����;�ǹ�\n"
                            + "2.�и���;��������\n"
                            + "3.�о�\n"
                            + "4.�����;�����ǻ��������\n"
                            + "5.��5����;�������")
                    case_10 = str(input("�������Ӧ����ţ��硰1������\n"))
                    if case_10 == '1' :
                        print(head + "ʮ�ֻ���")
                    elif case_10 == '2' :
                        print(head + "������")
                    elif case_10 == '3' :
                        print(head + "���˿�")
                    elif case_10 == '4' :
                        print(head + "ʯ���")
                    elif case_10 == '5' :
                        print(head + "Ǿޱ��")
                        print("1.�ӷ���λ�����\n"
                                + "2.�ӷ���λ")
                        case_11 =  str(input("�������Ӧ����ţ��硰1������\n"))
                        if case_11 == '1' :
                            print(head + "ƻ���ǿ�")
                        elif case_11 == '2' :
                            print("1.�˹�\n"
                                    + "2.��Ƥ����\n"
                                    + "3.��Ƥ5")
                            case_12 = str(input("�����Ӧ����ţ��硰1����\n"))
                            if case_12 == '1' :
                                print(head + "���ǿ�")
                            elif case_12 == '2' :
                                print(head + "Ǿޱ�ǿ�")
                            elif case_12 == '3' :
                                print(head + "���߾��ǿ�")
                            else :
                                print("Thanks for your use! ")
                    else :
                        print("Thanks for your use!")
                else :
                    print("Thanks for your use! ")
            elif case_7 == '����' :
                print("1.��ҩ����;�����޴�;�����򽬹�\n"
                        + "2.©��״����;������;����\n"
                        + "3.���λ���;��ǿ���������2��;�ӷ�������;��С���\n"
                        + "4.���λ��ڣ���ǿ���2��Ƥ����Ϊ2�ң�����\n"
                        + "5.����4�ѣ�����2ö\n"
                        + "6.�ӷ���λ�������뻨��ͬ������\n"
                        + "7.ͷ״�������ܰ�����ҩ����ݹ�")
                case_13 = str(input("�������Ӧ����ţ��硰1������\n"))
                if case_13 == '1' :
                    print(head + "�ѿ�")
                elif case_13 == '2' :
                    print(head + "������")
                elif case_13 == '3' :
                    print(head + "���ο�")
                elif case_13 == '4' :
                    print(head + "���ο�")
                elif case_13 == '5' :
                    print(head + "ľϬ��")
                elif case_13 == '6' :
                    print(head + "�̶���")
                elif case_13 == '7' :
                    print(head + "�տ�")
                    print("1ͷ״������ȫΪ��״��������֭\n"
                            + "2.ͷ״������Ϊ��״��")
                    case_14 = str(input("�������Ӧ����ţ��硰1������\n"))
                    if case_14 == '1' :
                        print(head + "��״���ǿ�")
                    elif case_14 == '2' :
                        print(head + "��״���ǿ�")
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
