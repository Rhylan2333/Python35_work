# 程序计时
import time
def core_Loop() :
    limit = 10**8  # 10^8逐次减1直到0，运算10^8次
    while limit > 0 :
        limit -= 1



def other_Loop1() :
    """休息0.2秒"""
    time.sleep(0.2)



def other_Loop2() :
    """休息0.4秒"""
    time.sleep(0.4)



def main() :
    start_Time = time.localtime()
    print("程序开始时间：", time.strftime('%Y-%m-%d %a %H:%M:%S', start_Time))
    
    start_Perf_Counter = time.perf_counter()
    
    other_Loop1()
    other_Loop1_Perf_Counter = time.perf_counter()  # 返回一个CPU级别的精确时间计数值，单位为秒。
    other_Loop1_Perf = other_Loop1_Perf_Counter - start_Perf_Counter  # 接perf_counter()后运行，即t1-t0

    core_Loop()  # 执行核心程序
    core_Loop_Perf_Counter = time.perf_counter()
    core_Loop_Perf = core_Loop_Perf_Counter - other_Loop1_Perf_Counter  # 接other_Loop1()后运行，t即t2-t1

    other_Loop2()
    other_Loop2_Perf_Counter = time.perf_counter()
    other_Loop2_Perf = other_Loop2_Perf_Counter - core_Loop_Perf_Counter  # 接core_Loop()后运行，t即t3-t2

    end_Perf_Counter = time.perf_counter()
    total_Perf = end_Perf_Counter - start_Perf_Counter  # 即t4-t0
    
    end_Time = time.localtime()

    print("模块1运行时间是：{:.2f} 秒".format(other_Loop1_Perf))
    print("核心模块运行时间是：{:.2f} 秒".format(core_Loop_Perf))
    print("模块2运行时间是：{:.2f} 秒".format(other_Loop2_Perf))
    print("程序运行总时间是：{:.2f} 秒".format(total_Perf))
    print("程序结束时间：", time.strftime('%Y-%m-%d %a %H:%M:%S', end_Time))



main()
