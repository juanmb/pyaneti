#!/usr/bin/env python

#-----------------------------------------------------------
#                         pyaneti.py
#                     Main pyaneti file
#                   Barragan O, March 2016
#-----------------------------------------------------------

#Load libraries
import os
import sys
import pyaneti as pti #FORTRAN module

#-------------------------------------------------------------
#                   INITIALIZATION
#-------------------------------------------------------------

#Load the input file
#You have to run the program as ./pyaneti star_name
star = str(sys.argv[1])

#Create path to the input_fit.py file
INF_NAME = 'inpy/%s/input_fit.py' % star

#Did you create an input_fit.py file?
if not os.path.isfile(INF_NAME):
    print('You have not created', INF_NAME)
    sys.exit()

#Read the file with all the python functions
exec(compile(open('src/todo-py.py', "rb").read(), 'src/todo-py.py', 'exec'))

#Read the file with the default values
exec(compile(open('src/default.py', "rb").read(), 'src/default.py', 'exec'))

#Read input file
exec(compile(open(INF_NAME, "rb").read(), INF_NAME, 'exec'))

#Prepare data
exec(compile(open('src/prepare_data.py', "rb").read(), 'src/prepare_data.py', 'exec'))

#Create ouput directory
outdir = outdir + star + '_out'
if not os.path.exists(outdir):
    os.makedirs(outdir)

#Obtain smart priors based on iput data
if is_smart_priors:
    smart_priors()

print_init()

#-------------------------------------------------------------
#                   FITTING ROUTINES
#-------------------------------------------------------------

joint_fit()

#-------------------------------------------------------------
#             	PRINT AND PLOT ROUTINES
#-------------------------------------------------------------

exec(compile(open('src/output.py', "rb").read(), 'src/output.py', 'exec'))

#-------------------------------------------------------------
#             	 END pyaneti.py FILE
#-------------------------------------------------------------
