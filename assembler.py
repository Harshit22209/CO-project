def A(op,R1,R2,R2):#op-5 u-2 r1-3,r2-3,r3-3
    pass
def add(s):
    if(len(s)!=4):
        raise Exception("Syntax Error")
    if(len(s[1])==len(s[2])==len[s(3)]==4):
        pass
    else
        raise Exception("Invalid reg name")
    if(s[1][-1] not in "1234" || s[2][-1] not in "1234")
opcodes = {
    "add":{add,"00000"},"sub":{sub,"00001"},"mov":{mov,"00010","00011"},#move register
    "ld":{ld,"00100"},"st":{st,"00101"},"mul":{mul,"00110"},"div":{div,"00111"},"rs":{rs,"01000"},
    "ls":{ls,"01001"},"xor":{xor,"01010"},"or":{Or,"01011"},"and":{And,"01100"},"not":{Not,"01101"},
    "cmp":{cmp,"01110"},"jmp":{jmp,"01111"},"jlt":{jlt,"11100"},"jgt":{jgt,"11101"},"je":{je,"11111"},
    "hlt":{hlt,"11010"},
}
for i in range(128):
    s=input().strip()
    while s=='' or s=='\n':
        s=input().strip();
    s=s.split()
    
