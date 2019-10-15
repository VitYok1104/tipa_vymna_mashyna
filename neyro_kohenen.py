from pprint import pprint as pp
import numpy as np

my_name = [[1, 0, 1, 0, 0, 0, 1, 0, 0, 0],             #прізвище
                      [0, 0, 1, 0, 0, 0, 1, 0, 0, 0],
                      [1, 0, 1, 0, 0, 0, 1, 0, 0, 1],
           
                      [0, 1, 0, 1, 0, 1, 0, 0, 0, 0],             #ім'я
                      [0, 1, 0, 1, 1, 1, 0, 0, 0, 0],
                      [0, 1, 0, 1, 0, 1, 0, 1, 0, 0],
           
                      [0, 1, 0, 1, 0, 0, 1, 0, 1, 0],             #по батькові
                      [0, 1, 0, 1, 0, 0, 1, 0, 1, 1],
                      [1, 0, 0, 1, 0, 0, 1, 0, 0, 0]]


#масив коефіцієнтів з рандомних значень
neyron = [[0.9581062142733822, 0.3489763065508322, 0.4861339389305236, 0.038858390613092264, 0.28943999827414746,
                  0.003739403433724031, 0.4452020156476416, 0.11185214125768916, 0.5132172836881244, 0.09752244538893506],
                 [0.19149769311835918, 0.11555468815624004, 0.7466823084056669, 0.3066504139772205, 0.3264060399411265,
                  0.5198651743029984, 0.14097212081536648, 0.19313596216026252, 0.33420425032420153, 0.01886831034501213],
                 [0.7043886237424511, 0.7542972014289009, 0.3370813283093872, 0.2517623402629279, 0.3913933237672338,
                  0.20859276103647006, 0.13240265701072507, 0.7180910370641022, 0.38834990732283536, 0.7119371399746277]]
#pp(coefficient)   #вивід менш більш нормальним списком

#новий масив коеіцієнтів
new_neyron = [[0 for element in range(10)] for column in range(3)]

#масив для довжин 
len_mas = [[0 for element in range(3)] for column in range(9)]

#
mas_sub = [[0 for element in range(10)] for column in range(3)]

#масив переможців
winner = [0 for element in range(9)]

n = .7
k = .5
    
#функція пошуку довжин
def serch_lens():
    pos = 0
    i = 0
    nomber_len = 0
    for line_names in range(9):
        '''по 9 векторам масиву ПІБ'''
        nomber = 0
        for nomber_neyron in range(3):
            '''по 3 рази для кожного нейрона'''
            j = 0
            for element in range(10):
                '''виконуєм по формулі додавання квадратної різниці коефіцієнта від ПІБ'''
                len_mas[i][nomber] += (neyron[nomber][j] - my_name[i][j])**2
                j += 1
            nomber += 1
            nomber_len += 1
        i += 1
        
#пошук найкращого значення
def find_min_len():
    step_n = 0
    for elemtnt in range(9):
        '''шукаєм індекс найменшого елемента'''
        winner[step_n] = len_mas[step_n][:].index(min(len_mas[step_n][:]))
        step_n += 1
        

def update(n):
    print(neyron)
    i = 0
    element = 0 
    for element in range(9):
        j = 0
        w = winner[element]
        for element in range(10):
            if w == 0:
                new_neyron[0][j] = neyron[0][j] + n*(my_name[i][j] - neyron[0][j])
            elif w == 1:
                new_neyron[1][j] = neyron[1][j] + n*(my_name[i][j] - neyron[1][j])
            elif w == 2:
                new_neyron[2][j] = neyron[2][j] + n*(my_name[i][j] - neyron[2][j])
            j += 1
        i += 1
    return neyron

def loop(new_neyron):
    serch_lens()
    find_min_len()

    pp(winner)
    update(n)
    print(str(new_neyron) + ' +1')
    subtraction()
    print(mas_sub)
    neyron = new_neyron
    update(n)
    print(str(new_neyron) + ' +1')

##    for o in range(6):
##        if comp >= 0:
##            n = n * k
##            neyron = new_neyron
##            update(k, n)
##            subtraction()
##            comparison()
##            comp = comparison()
##            print(comp)
            
            


#перевірка різниці 2 мсивів(нового і старого) на наявність умови
def comparison():
    i = 0
    comp = 0
    for line_names in range(3):
        j = 0
        for nomber in range(9):
            if mas_sub[i][j] <= 0.005:
                comp += 0
            else:
                comp += 1
            j += 1
        i += 1
    return comp

#створення масиву різниць між старим і новим
def subtraction():
    i = 0
    for line_names in range(3):
            j = 0
            for nomber in range(9):
                mas_sub[i][j] = neyron[i][j] - new_neyron[i][j]
                j += 1
            i += 1



loop(new_neyron)


