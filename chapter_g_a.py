#coding=gbk
# ����һ���ļ���һ���ַ���ͳ�Ƹ��ַ����ļ��г��ֵĴ���

def countstr(filename, str0) :
    f = open(filename, "rt", encoding='UTF-8')
    count = 0  # ����ַ�һ��Ҳûͳ�ƣ�����Ĭ��=0
    for line in f :  # ����row
        for i in line :  #����column
            if i == str0 :# �����row����column���ڡ��������str1���������
                count += 1
    print('��{}���ַ��ڡ�{}���г���{}�Ρ�'.format(str0,filename,count))
    f.close()

def main() :
    filename = input("����ó���Ŀ¼�е��ļ�����")
    str0 = input("��������Ҫͳ�Ƶ��ַ���")
    countstr(filename, str0)



main()
