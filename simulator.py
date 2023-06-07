#FINAL CODE
outpt=[]
PC=[]

reg={
    "000":"0","001":"0","010":"0","011":"0","100":"0","101":"0","110":"0","111":"0"
}
addr_variables={}
addr_labels={}
mem_addr={}
# def checkl(lst,l):
#     # print(lst)
#     if(len(lst)!=l):
#         # print(s)
#         raise Exception("Syntax Error")
#     if(lst[1] not in registers or lst[2] not in registers):
#         raise Exception("Invalid reg name")
# # Type A:Harshit 

def A(s):#op-5 u-2 r1-3,r2-3,r3-3
    if(s[:2]!="00"):
        raise Exception("For Type A Unused Bits should be 00")
    r1=s[2:5]
    r2=s[5:8]
    r3=s[8:]
    if('111' in [r1,r2,r3]):
        raise Exception("Can not use Flag register ")
    if((r1 not in reg) or (r2 not in reg) or (r3 not in reg)):
        raise Exception("Invalide Register Address")
    return (r1,r2,r3)


def add(s):
    r1,r2,r3=A(s)
    sum=bin(int(reg[r2],2) + int(reg[r3],2))
    reg[r1]=sum[2:]

def sub(s):
    r1,r2,r3=A(s)
    reg[r1]=bin(int(reg[r2],2)-int(reg[r3],2))[2:]

def mul(s):
    # print("mul")
    r1,r2,r3=A(s)
    reg[r1]=bin(int(reg[r2],2)*int(reg[r3],2))[2:]


def xor(s):
    # print(s[0])
    r1,r2,r3=A(s)
    reg[r1]=bin(int(reg[r2],2)^int(reg[r3],2))[2:]


def Or(s):
    # print(s[0])
    r1,r2,r3=A(s)
    reg[r1]=bin(int(reg[r2],2)|int(reg[r3],2))[2:]


def And(s):
    # print(s[0])
    r1,r2,r3=A(s)
    reg[r1]=bin(int(reg[r2],2)&int(reg[r3],2))[2:]

#Type B

def B(s):
    if(s[0] != '0'):
        raise Exception("For type B Unused bit should be 0")
    r=s[1:4]
    if(r=='111'):
        raise Exception("Can not use FLAG REGISTER")
    if r not in reg:
        raise Exception("Invalid Register Address")
    Imm=s[4:]
    return r,int(Imm,2)

def movB(s):
  r,Imm=B(s)
  reg[r]=bin(Imm)[2:]
    # printb(s)

def rs(s):
    r,Imm=B(s) 
    reg[r]=bin(reg[r]>>Imm)[2:] 
    
def ls(s):
   r,Imm=B(s)
   reg[r]=bin(int(reg[r],2)<<Imm)[2:]

#Type C
def C(s):
    if(s[:5]!="00000"):
        raise Exception("For Type C Unused Bits should be 00000")
    r1=s[5:8]
    r2=s[8:]
    if('111' in [r1,r2]):
        raise Exception("Can not use Flag register ")

    if((r1 not in reg) or (r2 not in reg) ):
        raise Exception("Invalide Register Address")
    return (r1,r2)

def C1(s):   # Using this for move register function psecially, some imp!!!
    if(s[:5]!="00000"):
        raise Exception("For Type C Unused Bits should be 00000")
    r1=s[5:8]
    r2=s[8:]
    if((r1 not in reg) or (r2 not in reg) ):
        raise Exception("Invalide Register Address")
    return (r1,r2)


def div(s):
    r1,r2=C(s)
    r3=int(reg[r1],2)
    r4=int(reg[r2],2)
    if(r4==0):
        reg["111"]=bin(8)[2:]
        reg["000"]=bin(0)[2:]
        reg["001"]=bin(0)[2:]
        return   
    reg["000"]=bin(r3/r4)[2:]
    reg["001"]=bin(r3%r4)[2:]

def movC(s):
    r1,r2=C1(s)
    reg[r1]=reg[r2]
    reg["111"]="0"

def Not(s):
    r1,r2=C(s)
    reg[r1]=-1*int(reg[r2],2)

def cmp(s):
    r1,r2=C(s)
    r1=reg[r1]
    r2=reg[r2]
    if(int(r1)>int(r2)):
        reg['111']="10"
    if(int(r1)==int(r2)):
        reg['111']="1"
    if(int(r1)<int(r2)):
        reg['111']="100"
    
    
#type D:Dev Utkarsh
# def checkD(lst,l):
#     # print(lst)
#     if(len(lst)!=l):
#         # print(s)
#         raise Exception("Syntax Error")
#     if(lst[1] not in registers or lst[2] not in addr_variables):
#         raise Exception("Invalid reg name or variable name")
def D(s):
    if(s[0] != '0'):
        raise Exception("For type B Unused bit should be 0")
    r=s[1:4]
    if(r=='111'):
        raise Exception("Can not use FLAG REGISTER")
    if r not in reg:
        raise Exception("Invalid Register Address")
    addr=s[4:]
    return r,addr

def ld(s):
    r1,addr=D(s)
    reg[r1]=mem_addr[addr]
    
    

def st(s):
    r1,addr=D(s)
    mem_addr[addr]=reg[r1]


def check_jump(s):
    if(s[0:4]!="0000"):
        raise Exception("4 unused bits need to be there")

#type E:Arpan
def jmp(s):
    check_jump(s)
    global is_branch_taken
    is_branch_taken=s[4:]
    reg["111"]="0"

        
def jlt(s):
    check_jump(s)
    if(reg["111"]=="100"):
        global is_branch_taken
        is_branch_taken=s[4:]
    reg["111"]="0"

def jgt(s):
    check_jump(s)
    if(reg["111"]=="10"):
        global is_branch_taken
        is_branch_taken=s[4:]
    reg["111"]="0"



def je(s):
    check_jump(s)
    if(reg["111"]=="1"):
        global is_branch_taken
        is_branch_taken=s[4:]
    reg["111"]="0"


#type-f Arpan:
def hlt(s):
    pass

    
def addf(s):
    print()
def subf(s):
    print()
def mulf(s):
    print()
def divf(s):
    print()
def mod(s):
    print()

# Added extra OPCODES for extra functions like addf subf mod divf etc...

opcodes = {
    "00000":add,"00001":sub,"00010":movB,"00011":movC,#move register
    "00100":ld,"00101":st,"00110":mul,"00111":div,"01000":rs,
    "01001":ls,"01010":xor,"01011":Or,"01100":And,"01101":Not,
    "01110":cmp,"01111":jmp,"11100":jlt,"11101":jgt,"11111":je,
    "11010":hlt,"10000":addf,"10001":subf,"10010":mulf,"110011":divf,"110100":mod
}


file=open("C:/msys64/mingw64/bin/2022105/Lab_4/SimpleSimulator/input.txt",'r')
lines=file.readlines()

cnt=0
final_code=[]
variables=[]
labels={}
f=0
instruction_address=[]
variable_idx=[]
return_address=0


for i in range(len(lines)):
    if(lines[i][-1]=='\n'):
        lines[i]=lines[i][:-1]


#Decode


def checkop(opc):
    if opc not in opcodes:
        raise Exception("Invalid Opcode")


# def printing_regfile(str):
#     # print((("0"*(16-len(bin(reg[str])[2:]))) + bin(reg[str])[2:]+" "), end="")
#     print((("0"*(16-len(reg[str]))) + (reg[str])+" "), end="")

i=0
j=0
pc=0
actual_length=0
flag_cmp=0
is_branch_taken=0

while(True): 
    opcode=lines[pc][:5]
    checkop(opcode)
    if(opcode=="11010"):# Exit out of this loop just after halt is executed!
        if(is_branch_taken!=0):
            if(is_branch_taken!=("0"*(7-len(bin(pc)[2:]))) + bin(pc)[2:]):
                raise Exception("The Branch address is of an instruction Ahead of Halt")
            
        PC.append(("0"*(7-len(bin(pc)[2:]))) + bin(pc)[2:])
        final_code.append([])
        final_code[actual_length].append(PC[actual_length]+"        ")
        for j in reg:
            final_code[actual_length].append((("0"*(16-len(reg[j]))) + (reg[j])+" "))
        break

    if (is_branch_taken!=0):
        if(is_branch_taken!=("0"*(7-len(bin(pc)[2:]))) + bin(pc)[2:]):
            pc+=1
            continue
    is_branch_taken=0

    opcodes[opcode](lines[pc][5:])
    PC.append(("0"*(7-len(bin(pc)[2:]))) + bin(pc)[2:])
    
    if(opcode=="01110"):
        flag_cmp=1
    if(opcode=="01110" or opcode=="01111" or opcode== "11101" or opcode =="11111" or opcode=="11010" or opcode=="00011"):
        pass
    else:
        flag_cmp=0
        reg["111"]="0"
    final_code.append([])
    final_code[actual_length].append(PC[actual_length]+"        ")
    
    for j in reg:
        final_code[actual_length].append((("0"*(16-len(reg[j]))) + (reg[j])+" "))

    actual_length+=1
    pc+=1

i=0
j=0
for i in final_code:
    for j in i:
        print(j,end="")
    print()