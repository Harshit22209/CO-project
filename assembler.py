registers = {
    "R0":["000",0],"R1":["001",0],"R2":["010",0],
    "R3":["011",0],"R4":["100",0],"R5":["101",0],
    "R6":["110",0],"FLAGS":["111",0],
}  
# Type A:Harshit 
def A(op,R1,R2,R3):#op-5 u-2 r1-3,r2-3,r3-3
    print(op+"00"+R1+R2+R3)

def checkA(s):
    if(len(s)!=4):
        raise Exception("Syntax Error")
    if(len(s[1])==len(s[2])==len[s(3)]==4):
        pass
    else:
        raise Exception("Invalid reg name")
    if(s[1][-1] not in "1234" or s[2][-1] not in "1234" or s[3][-1] not in 1234):
        raise Exception("Invalid reg name")
def add(s):
    checkA(s)
    registers[s[1]][1]=registers[s[1]][2]+registers[s[1]][3]
def sub(s):
    checkA(s)
    k=registers[s[1]][2]-registers[s[1]][3]
    registers[s[1]][1]=k if k>0 else 0
def mul(s):
    checkA(s)
    registers[s[1]][1]=registers[s[1]][2]*registers[s[1]][3]
def xor(s):
    checkA(s)
    registers[s[1]][1]=registers[s[1]][2]^registers[s[1]][3]
def Or(s):
    checkA(s)
    registers[s[1]][1]=registers[s[1]][2]|registers[s[1]][3]
def And(s):
    checkA(s)
    registers[s[1]][1]=registers[s[1]][2]&registers[s[1]][3]
#Type B:Abhay
def movB(s):
    pass
def rs(s):
    pass
def ls(s):
    pass
#type C:Dev Utkarsh
def div(s):
    pass
def movC(s):
    pass
def Not(s):
    pass
def cmp(s):
    pass
#type D:Dev Utkarsh
def ld(s):
    pass
def st(s):
    pass
#type E:Arpan
def jmp(s):
    pass
def jlt(s):
    pass
def jgt(s):
    pass
def je(s):
    pass
#type-f Arpan:
def hlt(s):
    pass

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
        s=input().strip()
    s=s.split()
    
