from sys import stdin

# проверка числа, является ли он целым
def zeloe(a):
    return a.is_integer()


# проверка на скобки, правильно ли они расставлены
def skob(s):
    st = []
    for i in s:
        if i == '(':
            st.append(i)
        elif i == ')':
            if not st:
                return False
            st.pop()
    return len(st) == 0


# убирает скобки из выражения, если они правильно расставлены
def del_skob(s):
    if skob(s):
        return ''.join(c if c not in '()' else ' ' for c in s).strip()
    return None


# можно ли перевести строку в число для выполнения действий
def chislo(s):
    try:
        float(s)
        return True
    except ValueError:
        return False


def obr_polsk(s):
    st = []
    for i in s:
        if chislo(i):
            st.append(float(i))
        elif i == '~' or i == '$':
            a = st.pop()
            if i == '~':
                st.append(a * (-1))
            if i == '$':
                st.append(a)

        elif i in ['+', '-', '//', '/', '%', '**', '*']:
            if len(st) < 2:
                raise IndexError
            a = st.pop()
            b = st.pop()
            r = 0

            match i:
                case '+':
                    r = b + a
                case '-':
                    r = b - a
                case '*':
                    r = b * a
                case '**':
                    r = b ** a
                case '//':
                    if zeloe(a) and zeloe(b) and a != 0:
                        r = b // a
                    elif a == 0:
                        raise ZeroDivisionError
                    else:
                        raise ValueError
                case '/':
                    if a != 0:
                        r = b / a
                    else:
                        raise ZeroDivisionError
                case '%':
                    if zeloe(a) and zeloe(b) and a != 0:
                        r = b % a
                    elif a == 0:
                        raise ZeroDivisionError
                    else:
                        raise ValueError
            st.append(r)
        else:
            raise ValueError

    rez = st.pop()
    if not st:
        print(rez)
    else:
        raise IndexError('Error')


def code():
    for i in stdin:
        try:
            if '(' in i or ')' in i:
                if skob(i):
                    n = del_skob(i)
                    obr_polsk(n.strip().split())
                else:
                    raise SyntaxError
            else:
                print(1, *i.strip().split())
                obr_polsk(i.strip().split())

        except ZeroDivisionError:
            print("Error, zero")
        except ValueError:
            print('Error, value')
        except SyntaxError:
            print('Error, syn')
        except IndexError as syn:
            print("Error, index")


if __name__ == "__main__":
    code()





























# # import sys
# # #проверка числа, является ли он целым
# # def zeloe(a):
# #     return a.is_integer()

# # # проверка на скобkи, правильно ли они расставлены
# # def skob(s):
# #     st=[]
# #     for i in s:
# #         if i=='(':
# #             st.append(i)
# #         elif i==')':
# #             if not st:
# #                 return False
# #             st.pop()
# #     return len(st)==0

# # # убирает скобки из выражения, если они правильно расставлены
# # def del_skob(s):
# #     if skob(s):
# #         return ''.join(c if c not in '()' else ' ' for c in s).strip()
# #     return None

# # #можно ли перевести строкув число для выполнения действий
# # def chislo(s):
# #     try:
# #         float(s)
# #         return True
# #     except ValueError:
# #         return False

# # def obr_polsk(s):
# #     st=[]
# #     for i in s:
# #         if chislo(i)==True:
# #             st.append(float(i))
# #         elif i=='~' or i=='$':
# #             a=st.pop()
# #             if i=='~':
# #                 st.append(a*(-1))
# #             if i=='$':
# #                 st.append(a)

# #         elif i in['+','-','//','/','%','**','*']:
# #             if len(st)<2:
# #                 raise IndexError
# #             a=st.pop()
# #             b=st.pop()
# #             r=0

# #             match i:
# #                 case '+':
# #                     r = b + a
# #                 case '-':
# #                     r=b-a
# #                 case '*':
# #                     r=b*a
# #                 case '**':
# #                     r=b**a
# #                 case '//':
# #                     if zeloe(a)==True and zeloe(b)==True and a!=0:
# #                         r=b//a
# #                     elif a==0:
# #                         raise  ZeroDivisionError
# #                     else:
# #                         raise ValueError
# #                 case '/':
# #                     if a!=0:
# #                         r=b/a
# #                     else:
# #                         raise  ZeroDivisionError
# #                 case '%':
# #                     if zeloe(a)==True and zeloe(b)==True and a!=0:
# #                         r=b%a
# #                     elif a==0:
# #                         raise  ZeroDivisionError
# #                     else:
# #                         raise ValueError
# #             st.append(r)
# #         else:
# #             raise ValueError    

# #     rez=st.pop()
# #     if not st:
# #         print(rez)
# #     else:
# #         raise IndexError('Error')
    
# # from sys import stdin   

# # def code():
# #     for i in stdin:
# #         try:
# #             if '(' in i or ')' in i:
# #                 if skob(i):
# #                     n=del_skob(i)
# #                     obr_polsk(n.strip().split())
# #                 else:
# #                     raise SyntaxError
# #             else:
# #                 obr_polsk(i.strip().split())

# #         except ZeroDivisionError:
# #             print("Error,zero")
# #         except ValueError:
# #             print('Error, value')
# #         except SyntaxError:
# #             print('Error,syn')
# #         except IndexError as syn:
# #             print("Error,index")


# # if __name__ == "__main__":
# #     code()



# from sys import stdin

# # проверка числа, является ли он целым
# def zeloe(a):
#     return a.is_integer()


# # проверка на скобки, правильно ли они расставлены
# def skob(s):
#     st = []
#     for i in s:
#         if i == '(':
#             st.append(i)
#         elif i == ')':
#             if not st:
#                 return False
#             st.pop()
#     return len(st) == 0


# # убирает скобки из выражения, если они правильно расставлены
# def del_skob(s):
#     if skob(s):
#         return ''.join(c if c not in '()' else ' ' for c in s).strip()
#     return None


# # можно ли перевести строку в число для выполнения действий
# def chislo(s):
#     try:
#         float(s)
#         return True
#     except ValueError:
#         return False


# def obr_polsk(s):
#     st = []
#     for i in s:
#         if chislo(i):
#             st.append(float(i))
#         elif i == '~' or i == '$':
#             a = st.pop()
#             if i == '~':
#                 st.append(a * (-1))
#             if i == '$':
#                 st.append(a)

#         elif i in ['+', '-', '//', '/', '%', '**', '*']:
#             if len(st) < 2:
#                 raise IndexError
#             a = st.pop()
#             b = st.pop()
#             r = 0

#             match i:
#                 case '+':
#                     r = b + a
#                 case '-':
#                     r = b - a
#                 case '*':
#                     r = b * a
#                 case '**':
#                     r = b ** a
#                 case '//':
#                     if zeloe(a) and zeloe(b) and a != 0:
#                         r = b // a
#                     elif a == 0:
#                         raise ZeroDivisionError
#                     else:
#                         raise ValueError
#                 case '/':
#                     if a != 0:
#                         r = b / a
#                     else:
#                         raise ZeroDivisionError
#                 case '%':
#                     if zeloe(a) and zeloe(b) and a != 0:
#                         r = b % a
#                     elif a == 0:
#                         raise ZeroDivisionError
#                     else:
#                         raise ValueError
#             st.append(r)
#         else:
#             raise ValueError

#     rez = st.pop()
#     if not st:
#         print(rez)
#     else:
#         raise IndexError('Error, more operand')


# def code():
#     print("stars code")
#     for i in stdin:
#         try:
#             if '(' in i or ')' in i:
#                 if skob(i):
#                     n = del_skob(i)
#                     obr_polsk(n.strip().split())
#                 else:
#                     raise SyntaxError
#             else:
#                 print(1, *i.strip().split())
#                 obr_polsk(i.strip().split())

#         except ZeroDivisionError:
#             print("Error, zero")
#         except ValueError:
#             print('Error, value')
#         except SyntaxError:
#             print('Error, syn')
#         except IndexError as syn:
#             print("Error, index")


# if __name__ == "__main__":
#     print("start")
