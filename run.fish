#!/usr/local/bin/fish

echo
if not argparse --min-args 1 'n/name' -- $argv
    exit 1
end

echo
echo -e "\033[32mpython $1.py:\033[39m"
if test -e $argv.py
    python $argv.py
else
    echo "The $argv.py file does not exist"
end


echo
echo -e "\033[35mjulia $1.jl\033[39m"
if test -e $argv.jl
    julia $argv.jl
else
    echo "The $argv.jl file does not exist"
end
# [ -f "$1.jl" ] && julia $1.jl || echo "The file does not exist"


echo

echo
echo -e "\033[34mgo build $1.go\033[39m"
go clean

if test -e $argv.go
    go run $argv.go
else
    echo "The $argv.go file does not exist"
end
## [ -f "$1.go" ] && go build $1.go || echo "The file does not exist"


echo

echo
echo -e "\033[33mclang++ $1.cpp\033[39m"
# clear old compiled file
/bin/rm a.out 2> /dev/null

if test -e $argv.cpp
    xcrun clang++ -std=c++11 -stdlib=libc++ $argv.cpp
    if test -e ./a.out
        echo "a.out compiled ok"
        echo
    else
        "No compiled file"
    end
else
    echo "The $argv.cpp file does not exist"
end
##[ -f "$1.cpp" ] && xcrun clang++ -std=c++11 -stdlib=libc++ -Weverything $1.cpp || echo "The file does not exist"
echo
