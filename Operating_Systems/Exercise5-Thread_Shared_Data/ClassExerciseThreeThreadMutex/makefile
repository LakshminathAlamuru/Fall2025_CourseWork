# Build all programs in the CIS657_Examples tree
# Output binaries go to the bin folder

.PHONY: clean run

PROGRAMS=mutex_demo 

all: $(PROGRAMS) install

$(PROGRAMS): $(PROGRAM=$(.TARGET))

CC=g++
CFLAGS=-O0 -g 
OBJS= 
LIBS=-lpthread
CPATH=.
VPATH=.:./procap

$(PROGRAM): $(PROGRAM).c $(OBJS)
	$(CC) $(CFLAGS) -o $(.TARGET) $(OBJS) $(LIBS) 

$(PROGRAM).o: $(PROGRAM).c

clean:
	rm -f bin/*

run:
	./$(PROGRAM)

dbg:
	lldb ./$(PROGRAM)
	
install:
	mv $(PROGRAMS) bin
