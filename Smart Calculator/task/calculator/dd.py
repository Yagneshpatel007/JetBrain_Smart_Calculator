from string import *
import operator

def dmf(ad):
    ri = False
    df = list(ad)
    for i in df:
        if i in digits:
            ri = True
            return ri
        else:
            pass
    return ri


def dmfd(ad):
    ri = False
    df = list(ad)
    for i in df:
        if i in digits:
            pass
        elif ad in ff:

            return ri
        else:
            ri = True
            return ri
    return ri

def mining(dec):
    der = list(dec)
    ddd = ''
    fff = []
    for i in der:
        if i != '+' and i != '-':
            ddd += ''.join(i)
        else:
            fff.append(ddd)
            fff.append(i)
            ddd = ''
    fff.append(ddd)
    return fff



exits = True
ff = dict()
while exits:
    dd = input()
    if not dd:
        pass
    elif dd.startswith('/'):
        if dd == '/exit':
            print('Bye!')
            exits = False
        elif dd == '/help':
            print('The program calculates the sum of numbers')
        else:
            print('Unknown command')
    elif '=' not in dd:
        if dd in ff:
            print(ff.get(dd))
        else:
            try:

                mm = dd.replace(' ', '')
                frt = mining(mm)
                gg = []
                for i in frt:
                    if i in ff:
                        gg.append(ff.get(i))
                    else:
                        gg.append(i)
                bb = ''
                for f in gg:
                    bb += ''.join(f)
                print(eval(bb))
            except:
                print('Unknown variable')

    else:
        rr = dd.replace(' ', '')
        try:
            m, n = rr.split('=')
            if dmf(m):
                print('Invalid identifier')
            elif dmfd(n):
                print('Invalid assignment')
            elif n in ff:
                n = ff.get(n)
                ff[m] = n
            else:
                ff[m] = n
        except:
            print('Invalid assignment')



