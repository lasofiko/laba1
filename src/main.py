import sys

#проверка числа, является ли он целым

def zeloe(a):
    return a.is_integer()

# проверка на скобkи, правильно ли они расставлены

def skob(s):
    st=[]
    for i in s:
        if i=='(': # добавляем открывающую в стек 
            st.append(i)
        elif i==')': 
            if not st: #  если закрывающей есть пара открывающая, то все хорошо, идем дальше 
                return False # иначе ошибка
            st.pop()
    return len(st)==0

# убирает скобки из выражения, если они правильно расставлены

def del_skob(s):
    if skob(s):
        return ''.join(i if i not in '()' else ' ' for i in s).strip()
    return None

# проверет можно ли перевести строкув число для выполнения действий

def chislo(s):
    try:
        float(s)
        return True
    except ValueError:
        return False
        
# ведет подсчет выражения в обратной польской записи

def obr_polsk(s):
    st=[]
    for i in s:
        if chislo(i)==True:
            # добавляем число в виде float в стек
            st.append(float(i))
        elif i=='~' or i=='$':
            a=st.pop()
            if i=='~':
                st.append(a*(-1)) # унарный минус
            if i=='$':
                st.append(a) # унарный плюс

        elif i in['+','-','//','/','%','**','*']:
            if len(st)<2:
                raise IndexError
            a=st.pop()
            b=st.pop()
            r=0
# в обратной польской записи сначала идет b, потом а!!!
            #  выполняем встреченную операцию
            match i:
                case '+':
                    r = b + a
                case '-':
                    r=b-a
                case '*':
                    r=b*a
                case '**':
                    r=b**a
                case '//':
                    #  необходимы целые числа 
                    if zeloe(a)==True and zeloe(b)==True and a!=0:
                        r=b//a
                    elif a==0:
                        raise  ZeroDivisionError
                    else:
                        raise ValueError
                case '/':
                    if a!=0:
                        r=b/a
                    else:
                        raise  ZeroDivisionError
                case '%':
                    # необходимы целые числа 
                    if zeloe(a)==True and zeloe(b)==True and a!=0:
                        r=b%a
                    elif a==0:
                        raise  ZeroDivisionError
                    else:
                        raise ValueError
             st.append(r) # убираем в стек полученный результа 
        else:
            raise ValueError    
# В конце всех действий должен остаться только один результат 
    rez=st.pop()
    if not st:
        print(rez)
    else:
        raise IndexError('Error')
    
from sys import stdin  

# основная функция которая ведет подсчет выражений из ввода 

def code():
    for i in stdin:
        try:
            # есть ли скобки в выражении
            if '(' in i or ')' in i:
                if skob(i):
                    n=del_skob(i)
                    obr_polsk(n.strip().split())
                else:
                    raise SyntaxError        
            else:
                # подсчет выражения без скобок 
                obr_polsk(i.strip().split())
# если случается ошибка, идет обработка 
        except ZeroDivisionError:
            print("Error,zero")
        except ValueError:
            print('Error, value')
        except SyntaxError:
            print('Error,syn')
        except IndexError as syn:
            print("Error,index")


if __name__ == "__main__":
    code()
