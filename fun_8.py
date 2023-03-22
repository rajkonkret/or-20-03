#  / - odziela argumenty pozycyjne od takich po nazwie
# w tym przykładzie a i b nie moga byc podane po nazwie.
# liczy sie tylko pozycja(kolejnosc argumentow)
def allparams(a, b, /, c=42, *args, d=256, **kwargs):
    print('a, b', a, b)
    print('c, d', c, d)
    print('args', args)
    print('kwargs', kwargs)


allparams(1, 2)
allparams(1, 2, 3)
# a, b 1 2
# c, d 3 256
# args ()
# kwargs {}
allparams(1, 4, c=7)  # tak moge, ale nie moge allparams(b=1,a=7,c=9)
allparams(1, 2, 3, 4, 5, 6, 7, 8, 9, d=0)  # po tupli musimy d podac jawnie czyli d=0
allparams(1, 2, 3, 4, 5, 6, 7, 8, 9, d=0, k=10, l=19, m=46, zenek="/home")
# a, b 1 2
# c, d 3 0
# args (4, 5, 6, 7, 8, 9)
# kwargs {'k': 10, 'l': 19, 'm': 46, 'zenek': '/home'}
