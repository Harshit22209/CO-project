registers = {
    "R0":["000",0],"R1":["001",0],"R2":["010",0],
    "R3":["011",0],"R4":["100",0],"R5":["101",0],
    "R6":["110",0],"FLAGS":["111",0],
}  
addr_variables={}
# Type A:Harshit 
def A(op,R1,R2,R3):#op-5 u-2 r1-3,r2-3,r3-3
    print(op+"00"+R1+R2+R3)

def checkA(s):
    if(len(s)!=4):
        print(s)
        raise Exception("Syntax Error")
   
    if(s[1] not in registers or s[2] not in registers or s[3] not in registers):
        raise Exception("Invalid reg name")
def add(s):
    checkA(s)
    print("Add")
    registers[s[1]][1]=registers[s[2]][1]+registers[s[3]][1]
def sub(s):
    checkA(s)
    print("Sub")
    k=registers[s[2]][1]-registers[s[3]][1]
    registers[s[1]][1]=k if k>0 else 0
def mul(s):
    print("mul")
    checkA(s)
    registers[s[1]][1]=registers[s[2]][1]*registers[s[3]][1]
def xor(s):
    print(s[0])
    checkA(s)
    registers[s[1]][1]=registers[s[2]][1]^registers[s[3]][1]
def Or(s):
    print(s[0])
    checkA(s)
    registers[s[1]][1]=registers[s[2]][1]|registers[s[3]][1]
def And(s):
    print(s[0])
    checkA(s)
    registers[s[1]][1]=registers[s[2]][1]&registers[s[3]][1]
#Type B:Abhay
def movB(s):

    print(s[0])
def rs(s):
    print(s[0])
def ls(s):
    print(s[0])
#type C:Dev Utkarsh
def div(s):
    print(s[0])
def movC(s):
    print(s[0])
def Not(s):
    print(s[0])
def cmp(s):
    print(s[0])
#type D:Dev Utkarsh
def ld(s):
    print(s[0])
def st(s):
    print(s[0])
#type E:Arpan
def jmp(s):
    print(s[0])
def jlt(s):
    print(s[0])
def jgt(s):
    print(s[0])
def je(s):
    print(s[0])
#type-f Arpan:
def hlt(s):
    print("hlt")
#mov ->calls mov for type B and type C i.e movB and movC
def mov(s):
    pass
#to check is it a valid syntax for declaring a var
def checkIsVar(s):
    if(len(s)!=2):
        raise Exception("Invalid Syntax")
    
opcodes = {
    "add":[add,"00000"],"sub":[sub,"00001"],"mov":[mov,"00010","00011"],#move register
    "ld":[ld,"00100"],"st":[st,"00101"],"mul":[mul,"00110"],"div":[div,"00111"],"rs":[rs,"01000"],
    "ls":[ls,"01001"],"xor":[xor,"01010"],"or":[Or,"01011"],"and":[And,"01100"],"not":[Not,"01101"],
    "cmp":[cmp,"01110"],"jmp":[jmp,"01111"],"jlt":[jlt,"11100"],"jgt":[jgt,"11101"],"je":[je,"11111"],
    "hlt":[hlt,"11010"],
}
file=open("input.txt",'r')
lines=file.read().split('\n')
cnt=0
final_code=[]
variables=[]
labels={}
f=0
for line in lines:
    s=line.strip()
    if(s=='' or s=='\n'):
        continue
    s=s.split()
    if(s[0]=='var'):
        if(len(final_code)!=0):
            raise Exception("var should be declare at top")
        checkIsVar(s)
        variables.append(s[1])
        continue
    elif(s[0] not in opcodes):
        if(s[0][-1]==':' and len(s[0])>1):
            if(s[0] in labels):
                raise Exception("label"+s[0]+"is already declared")
            labels[s[0][:-1]]=len(final_code)
        else:
            raise Exception("Syntax Error")

    
    final_code.append(s)
    if(s[0]=='hlt'):
        f=1
        break
    if(len(s)==128):
     break
# if(f==0):
#     raise Exception("hlt statement not used")
print(final_code)
print(variables)
print(labels)
#assign address to variables using dictionary addr_variables declared at top

for i in range(len(final_code)):
    inst=final_code[i][0]
    cmds=final_code[i]
    if inst in opcodes:
        opcodes[inst][0](cmds)
    elif inst[:-1] in labels:
        continue
    else:
        # print()
        raise Exception("Invalid Syntax")

    

#providing addr to hlt and var

# for i in range(128):
#     s=input().strip()
#     while s=='' or s=='\n':
#         s=input().strip()
#     s=s.split()
    
