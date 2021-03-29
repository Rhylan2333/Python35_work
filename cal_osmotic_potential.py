def cal_ψ_C():
    C = eval(input('C = '))
    R = 0.0083  # MPa·L·mol^-1·K^-1
    i = 2.6  # for CaCl2
    T = eval(input('t =')) + 273
    ψ_C = -i*C*R*T
    return ψ_C



def cal_ψ_M():
    M = eval(input('M = '))
    R = 0.0083  # MPa·L·mol^-1·K^-1
    T = eval(input('t = ')) + 273
    ψ_M = -M*R*T*pow(10,-3)
    return ψ_M



def show_osmotic_potential(ψ):
    print("Osmotic Potential: {:.2f} MPa".format(ψ))



def main():
    flag = input('Input "c" to calculate ψ_C, Input "m" to calculate ψ_M: ')
    while flag:
        if flag == 'm':
            show_osmotic_potential(cal_ψ_M())
        elif flag == 'c':
            show_osmotic_potential(cal_ψ_C())
        else:
            print('Error, you can only input "m" or "c".')



main()
