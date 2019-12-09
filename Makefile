#-------------------------------------------------------------------------#
#                         Makefile for pyaneti                            #
#                       Oscar Barragán, Oct. 2016                         #
#-------------------------------------------------------------------------#
#    make       -> compiles the code in its sequential configuration      #
#    make para  -> compiles the code in its parallel configuration        #
#    make clean -> removes the pyaneti.so file                            #
#-------------------------------------------------------------------------#

NAME=pyaneti

FP=f2py3
FC=gnu95
CC=unix

FLAGS=-c -m --quiet
FLAGS_OMP=$(FLAGS) --f90flags='-fopenmp'
LGOMP=-L/usr/lib64/ -lgomp

SRC= $(wildcard src/*.f90)


all: $(NAME)

$(NAME): $(SRC)
	${FP} ${FLAGS} $(NAME) $(SRC) --fcompiler=$(FC) --compiler=$(CC)

para: $(NAME)
	${FP} ${FLAGS_OMP} $(NAME) $(SRC) --fcompiler=$(FC) ${LGOMP} --compiler=$(CC)

clean:
	rm -f $(NAME)*.so
