#coding=gbk
# ����һ���ļ���һ���ַ���ͳ�Ƹ��ַ����ļ��г��ֵĴ���

def countstr(filename, str0) :
    f = open(filename, "rt", encoding='UTF-8')  #��UTF-8��ʽ����
    count = 0  # ����ַ�һ��Ҳûͳ�ƣ�����Ĭ��=0
    for line in f :  # ����row
        for c in line :  #����column
            if c == str0 :# �����row����column���ڡ��������str0���������
                count += 1
    print('��{}���ַ��ڡ�{}���г�����{:^3}�Ρ�'.format(str0,filename,count))
    f.close()

def main() :
    filename = input("����ó���Ŀ¼�е��ļ�����")
    str0 = input("��������Ҫͳ�Ƶ��ַ���")
    countstr(filename, str0)



main()
