##########################################################################################
#                                                                                        #
#    Script to compile Fortran module from Python using f2py                             #
#                                                                                        #
#                                                                                        #
#    Copyright (C) 2018  David Topping : david.topping@manchester.ac.uk                  #
#                                      : davetopp80@gmail.com                            #
#    Personal website: davetoppingsci.com                                                #
#    This file is part of PyBox.                                                         #
#                                                                                        #
#    PyBox is free software: you can redistribute it and/or modify it under              #
#    the terms of the GNU General Public License as published by the Free Software       #
#    Foundation, either version 3 of the License, or (at your option) any later          #
#    version.                                                                            #
#                                                                                        #
#    PyBox is distributed in the hope that it will be useful, but WITHOUT                #
#    ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS       #
#    FOR A PARTICULAR PURPOSE.  See the GNU General Public License for more              #
#    details.                                                                            #
#                                                                                        #
#    You should have received a copy of the GNU General Public License along with        #
#    PyBox.  If not, see <http://www.gnu.org/licenses/>.                                 #
#                                                                                        #
##########################################################################################
# Developed using the Anaconda Python 3 distribution and with the Assimulo ODE solver    # 
# suite: http://www.jmodelica.org/assimulo                                               #
# In the import statements, all files developed specifically for this project            #
# as marked [•]                                                                          #
##########################################################################################

from numpy.distutils.core import Extension
ext = Extension (name = "rate_coeff_f2py",
                 sources = ["Rate_coefficients.f90"], 
                 extra_compile_args=["-O3",
                                     "-ffast-math",
                                     "-fopenmp"],
                 extra_link_args=["-lgomp",
                                  "-llapack",
                                  "-lblas"])
if __name__ == '__main__':
    from numpy.distutils.core import setup 
    setup (name = "rate_coeff_f2py" ,
           ext_modules = [ext])

    