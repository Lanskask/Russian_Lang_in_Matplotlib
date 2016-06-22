# #!/usr/bin/env pytnon
# # vim: set fileencoding=utf-8 ts=4 sw=4 expandtab:

# # Cyrillic letters in Matplotlib,
# # thanks to Alexey for solution, see http://koldunov.net/?p=290#comments
# from matplotlib import rc
# rc('font',**{'family':'serif'})
# rc('text', usetex=True)
# rc('text.latex',unicode=True)
# rc('text.latex',preamble='\usepackage[utf8]{inputenc}')
# rc('text.latex',preamble='\usepackage[russian]{babel}')

# from pylab import *

# def figsize(wcm,hcm): figure(figsize=(wcm/2.54,hcm/2.54))
# figsize(13,9)

# x = linspace(0,2*pi,100)
# y = sin(x)
# plot(x,y,'-')
# xlabel(r"ось абсцисс")
# ylabel(r"ось ординат")
# title(r"Две беды в России — синусы и косинусы!")
# savefig('rus-mpl.pdf')

#!/usr/bin/python
# -*- coding: UTF-8 -*-

import numpy
import pylab
from matplotlib import rcParams
# rcParams['font.family'] = 'sans-serif'
# rcParams['font.family'] = 'verdana'
rcParams['font.sans-serif'] = ['Tahoma']
# rcParams['font.sans-serif'] = ['verdana']

if __name__ == "__main__":
    xvals = numpy.arange (-10.0, 10.1, 0.1)
    yvals = numpy.sinc (xvals)

    pylab.plot (xvals, yvals)
    # pylab.rc('font',**{'family':'verdana'})

    pylab.text (0.1, 1.1, u"Какая-то фигня: Надпись на русском языке", family="verdana")
    pylab.xlabel(u"Ось абсцисс")
    pylab.ylabel(u"Ось ординат")
    pylab.show()