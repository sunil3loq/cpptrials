exec=result
codeout=processed.cpp
flag=Wall
files=twoexamp.cpp
debugcode=ndebug
prep:
	cpp -P $(files) > $(codeout)
doit:
	g++ -D $(debugcode) -$(flag) $(files) -o $(exec)
clean:
	rm -rf $(exec)
all:clean doit
