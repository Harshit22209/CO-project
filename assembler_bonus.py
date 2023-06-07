
import sys
outpt=[]
def write(s):
    # while(s[-1]=='\n'):
    #     s=s[:-1]
    print(s)
    
    # print(s)

registers = {
    "R0":["000",0],"R1":["001",0],"R2":["010",0],
    "R3":["011",0],"R4":["100",0],"R5":["101",0],
    "R6":["110",0],"FLAGS":["111",0],
}  
addr_variables={}
addr_labels={}
codes = {
    "add":"00000",
    "sub":"00001",
    "mov":["00010","00011"],#move register
    "ld":"00100",
    "st":"00101",
    "mul":"00110",
    "div":"00111",
    "rs":"01000",
    "ls":"01001",
    "xor":"01010",
    "or":"01011",
    "and":"01100",
    "not":"01101",
    "cmp":"01110",
    "jmp":"01111",
    "jlt":"11100",
    "jgt":"11101",
    "je":"11111",
    "hlt":"11010",
}
def checkl(lst,l):
    # print(lst)
    if(len(lst)!=l):
        # print(s)
        raise Exception("Syntax Error")
    if(lst[1] not in registers or lst[2] not in registers):
        raise Exception("Invalid reg name")
# Type A:Harshit 
def A(op,R1,R2,R3):#op-5 u-2 r1-3,r2-3,r3-3
    write(op+"00"+R1+R2+R3)

def checkA(s):
    
    if(len(s)!=4):
        # print(s)
        raise Exception("Syntax Error")
   
    if(s[1] not in registers or s[2] not in registers or s[3] not in registers or s[1]=="FLAGS" or s[2]=="FLAGS" or s[3]=="FLAGS"):
        raise Exception("Invalid reg name")
def add(s):
    checkA(s)
    # print("Add")
    registers[s[1]][1]=registers[s[2]][1]+registers[s[3]][1]
    A(codes[s[0]],registers[s[1]][0],registers[s[2]][0],registers[s[3]][0])
def sub(s):
    checkA(s)
    # print("Sub")
    k=registers[s[2]][1]-registers[s[3]][1]
    registers[s[1]][1]=k if k>0 else 0
    A(codes[s[0]],registers[s[1]][0],registers[s[2]][0],registers[s[3]][0])
def mul(s):
    # print("mul")
    checkA(s)
    registers[s[1]][1]=registers[s[2]][1]*registers[s[3]][1]
    A(codes[s[0]],registers[s[1]][0],registers[s[2]][0],registers[s[3]][0])
def xor(s):
    # print(s[0])
    checkA(s)
    registers[s[1]][1]=registers[s[2]][1]^registers[s[3]][1]
    A(codes[s[0]],registers[s[1]][0],registers[s[2]][0],registers[s[3]][0])
def Or(s):
    # print(s[0])
    checkA(s)
    registers[s[1]][1]=registers[s[2]][1]|registers[s[3]][1]
    A(codes[s[0]],registers[s[1]][0],registers[s[2]][0],registers[s[3]][0])
def And(s):
    # print(s[0])
    checkA(s)
    registers[s[1]][1]=registers[s[2]][1]&registers[s[3]][1]
    A(codes[s[0]],registers[s[1]][0],registers[s[2]][0],registers[s[3]][0])

#Type B:Abhay
def checkB(lst):
    # print(lst)
    if(len(lst)!=3):
        # print(s)
        raise Exception("Syntax Error")
    if(lst[1] not in registers ):
        raise Exception("Invalid reg name or variable name")

def printb(s):
   
   a=bin((int(s[2].lstrip("$"))))[2:]
   write(codes[s[0]]+"0"+registers[s[1]][0]+"0"*(7-len(a))+a)
    # printb(s)

def movB(s):
    checkB(s)
    # print(s[0])
    registers[s[1]][1]=int((s[2]).lstrip("$"))
    if(registers[s[1]][1]>128):
        raise Exception("Number should be 7bit Overflow...")
    a=bin((int(s[2].lstrip("$"))))[2:]
    write(codes[s[0]][0]+"0"+registers[s[1]][0]+"0"*(7-len(a))+a)
    # printb(s)

def rs(s):
    checkB(s,3)
    # print(s[0])
    registers[s[1]][1]=registers[s[1]][1]>>(int(s[2].lstrip("$")))
    printb(s)
    
def ls(s):
    checkB(s,3)
    # print(s[0])
    registers[s[1]][1]=registers[s[1]][1]<<(int(s[2].lstrip("$")))
    printb(s)
#type C:Dev Utkarsh
#type C:Dev Utkarsh
def printc(s):
    write(codes[s[0]]+"00000"+registers[s[1]][0]+registers[s[2]][0])

def div(s):
    checkl(s,3)
    # print(s[0])
    registers["R0"]=registers[s[1]][1]/registers[s[2]][1]
    printc(s)

def movC(s):
    # print(s)
    checkl(s,3)
    # print(s[0])
    registers[s[1]][1]=registers[s[2]][1]
    write(codes[s[0]][1]+"00000"+registers[s[1]][0]+registers[s[2]][0])


def Not(s):
    checkl(s,3)
    # print(s[0])
    registers[s[1]][1]=(-1)*(registers[s[2]][1]+1)
    printc(s)

def cmp(s):
    checkl(s,3)
    # print(s[0])
    if(registers[s[1]][1]>registers[s[2]][1]):
        registers["FLAGS"][1]=10
    if(registers[s[1]][1]==registers[s[2]][1]):
        registers["FLAGS"][1]=1
    if(registers[s[1]][1]<registers[s[2]][1]):
        registers["FLAGS"][1]=100
    printc(s)
    
#type D:Dev Utkarsh
def checkD(lst,l):
    # print(lst)
    if(len(lst)!=l):
        # print(s)
        raise Exception("Syntax Error")
    if(lst[1] not in registers or lst[2] not in addr_variables):
        raise Exception("Invalid reg name or variable name")
def printd(s):
    write(codes[s[0]]+"0"+registers[s[1]][0]+("0"*(7-len(addr_variables[s[2]][0])))+addr_variables[s[2]][0])

def ld(s):
    checkD(s,3)
    # print(s[0])
    registers[s[1]][1]=addr_variables[s[2]][1]
    printd(s)

def st(s):
    checkD(s,3)
    # print(s[0])
    registers[s[1]][1]=addr_variables[s[2]][1]
    printd(s)
# def PC(start_idx):

# checker function for all jump function-E:-

def print_jump():
    print(opcodes[cmds][0]+"")

def check_jump(s):
    if(len(s)<2):
        # print(s)
        raise Exception("Syntax Error, less operands")
    elif(len(s)>2):
        # print(s)
        raise Exception("Syntax Error, more operands")
    flag=0
    for i in range(len(lines)):
        label_name=[]
        label_name=lines[i].split()
        if(label_name[0]==(s[1]+':')):
            flag=1
        if(flag==1):
            return
    if(flag==0):
        raise Exception("No such Label Found in the whole Assembly code")


#type E:Arpan
def jmp(s):
    check_jump(s)
    temp=0
    if (len(memory_for_labels[s[1]])<7):
        temp=7-len(memory_for_labels[s[1]])
    write("01111"+"0000"+"0"*temp + memory_for_labels[s[1]])
    for i in range(len(lines)):
        if(lines[i][0]==s[1]):
            # print(s[0])
            return i

def jlt(s):
    check_jump(s)
    #PRINTING
    temp=0
    if (len(memory_for_labels[s[1]])<7):
        temp=7-len(memory_for_labels[s[1]])
    write("11100"+"0000"+"0"*temp + memory_for_labels[s[1]])
    
    if(registers["FLAGS"][1]==100):
        for i in range(len(lines)):
            if(lines[i][0]==s[1]):
                print(s[0])
                return i
        # print(s[0])
    else:
        return cnt

def jgt(s):
    check_jump(s)
    temp=0
    if (len(memory_for_labels[s[1]])<7):
        temp=7-len(memory_for_labels[s[1]])
    write("11101"+"0000"+"0"*temp + memory_for_labels[s[1]])
    

    if(registers["FLAGS"][1]==10):
        for i in range(len(lines)):
            if(lines[i][0]==s[1]):
                # print(s[0])
                return i
        # print(s[0])
    else:
        return cnt

def je(s):
    check_jump(s)

    temp=0
    if (len(memory_for_labels[s[1]])<7):
        temp=7-len(memory_for_labels[s[1]])
    write("11111"+"0000"+"0"*temp + memory_for_labels[s[1]])


    if(registers["FLAGS"][1]==1):
        for i in range(len(lines)):
            if(lines[i][0]==s[1]):
                # print(s[0])
                return i
        # print(s[0])
    else:
        return cnt

# def check_halt():


#type-f Arpan:
def hlt(s):
    # printing
    write("11010"+"00000000000")
    sys.exit()
    # print()


#mov ->calls mov for type B and type C i.e movB and movC
def mov(s):
    if '$' in s[2]:
        movB(s)
    else:
        movC(s)


#to check is it a valid syntax for declaring a var
def checkIsVar(s):
    if(len(s)!=2):
        raise Exception("Invalid Syntax")
    
def checklen(s):
    if(len(s)!=3):
        raise Exception("Invalid Syntax")
    if(s[1] not in registers):
        raise Exception("Invalid reg name or variable name")

def addf(s):
    checkl(s,4)
    write(opcodes[s[0]][1]+"00"+registers[s[1]][0]+registers[s[2]][0]+registers[s[3]][0])

def subf(s):
    checkl(s,4)
    # if(registers[s[3]]>registers[s[2]]):
    #     raise Exception("reg3 > reg2")

    write(opcodes[s[0]][1]+"00"+registers[s[1]][0]+registers[s[2]][0]+registers[s[3]][0])

def movf(s):
    checklen(s)
    a=bin((int(s[2].lstrip("$"))))[2:]
    if(len(a)>8):
        raise Exception("immediate value greater than 8 bits")
    write(opcodes[s[0]][1]+"0"+registers[s[1]][0]+"0"*(7-len(a))+a)
    
def addi(s):
    checklen(s)
    a=bin((int(s[2].lstrip("$"))))[2:]
    print(opcodes[s[0]][1]+"0"+registers[s[1]][0]+"0"*(7-len(a))+a)
def subi(s):
    checklen(s)
    a=bin((int(s[2].lstrip("$"))))[2:]
    print(opcodes[s[0]][1]+"0"+registers[s[1]][0]+"0"*(7-len(a))+a)
def muli(s):
    checklen(s)
    a=bin((int(s[2].lstrip("$"))))[2:]
    print(opcodes[s[0]][1]+"0"+registers[s[1]][0]+"0"*(7-len(a))+a)
def divi(s):
    checklen(s)
    a=bin((int(s[2].lstrip("$"))))[2:]
    print(opcodes[s[0]][1]+"0"+registers[s[1]][0]+"0"*(7-len(a))+a)
def pow(s):
    checklen(s)
    a=bin((int(s[2].lstrip("$"))))[2:]
    print(opcodes[s[0]][1]+"0"+registers[s[1]][0]+"0"*(7-len(a))+a)
    
opcodes = {
    "add":[add,"00000"],"sub":[sub,"00001"],"mov":[mov,"00010","00011"],#move register
    "ld":[ld,"00100"],"st":[st,"00101"],"mul":[mul,"00110"],"div":[div,"00111"],"rs":[rs,"01000"],
    "ls":[ls,"01001"],"xor":[xor,"01010"],"or":[Or,"01011"],"and":[And,"01100"],"not":[Not,"01101"],
    "cmp":[cmp,"01110"],"jmp":[jmp,"01111"],"jlt":[jlt,"11100"],"jgt":[jgt,"11101"],"je":[je,"11111"],
    "hlt":[hlt,"11010"],"addf":[addf,"10000"],"subf":[subf,"10001"],"movf":[movf,"10010"],
    "addi":[addi,"10011"],"subi":[subi,"10100"],"muli":[muli,"10101"],"divi":[divi,"10110"],"pow":[pow,"10111"]
}
# file=open("CO_A_P1/Simple-Assembler/input.txt",'r')
# lines=file.readlines()
lines=sys.stdin.readlines()
cnt=0
final_code=[]
variables=[]
labels={}
f=0
instruction_address=[]
variable_idx=[]
return_address=0
# for line in sys.stdin:
#     line=line.rstrip()
#     lines.append(line)
for i in range(len(lines)):
    if(lines[i][-1]=='\n'):
        lines[i]=lines[i][:-1]
for line in lines:
    cnt+=1
    # print("line->",line)
    # line=line.rstrip()
    # lines.append(line)
    if(line[-1]=='\n'):
        line=line[:-1]
    s=line.strip()
    if(s=='' or s=='\n'):
        continue
    
    s=s.split()
    if(s[0]=='var'):
        variable_idx.append(cnt-1)
        if(len(final_code)!=0):
            raise Exception("var should be declare at top")
        checkIsVar(s)
        variables.append(s[1])
        continue

    # if (s[0]=='jmp'|'jgt'|'je'|'jlt'):
    #     return_address=cnt # after completeing the label call if ret would be found then it would come back to the origina label
    #     i=jmp(s)
    #     if(i!=cnt):
    #         line=lines[i]
    
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
        # break
    if(len(s)==128):
     break

# if(f==0):
#     raise Exception("hlt statement not used")
# print(final_code)
# print(variables)
# print("printing labels!!!!!!!!")
# print(labels)
#assign address to variables using dictionary addr_variables declared at top
# print(lines)
memory_for_instructions=[]
last="0000000"
la=0
for i in range(0,len(final_code)):

    la=0000000+int(bin(i)[2:])
    last=str(la)
    memory_for_instructions.append(last)
# print(memory_for_instructions)

# memory_for_variables=[]
for i in range(0,len(variables)):
    addr_variables[variables[i]]=[str(bin(len(final_code)+i)[2:]),0]

memory_for_labels={}
for i in labels:
    memory_for_labels[i]=memory_for_instructions[int(labels[i])]

# print(memory_for_labels)


# for i in range(len(lines)):
#         label_name=[]
#         label_name=lines[i].split()
#         if(label_name[0]==(s[1]+':')):


# memory_for_labels=[]
# for i in range(0,len(labels)):
#     addr_labels[labels[i]]=[str()]
#     addr_labels[labels[i]]=[str()]

# print("memory")
# print(memory_for_instructions)

# print("-----------------------------------------------------------------------------\n")
# print(labels)
# print("-----------------------------------------------------------------------------\n")
# print(addr_variables)
# for i in variables:
#     printf("")

# print(final_code)
for i in range(len(final_code)):
    
    inst=final_code[i][0]
    # print(inst)
    # print("->",inst)
    # print(inst[0])
    cmds=final_code[i]
    # print(inst[:-1])
    # print(lines)
    # if(lines.index("hlt")<len(lines)-1):
    #     raise Exception("No instructuins after halt")
    if inst in opcodes:
        opcodes[inst][0](cmds)
    elif final_code[i][-1] == "hlt":
        hlt(inst)
    elif ':' in final_code[i][0]:
        opcodes[final_code[i][1]][0](cmds[1:])
        
    elif inst[:-1] in labels:
        continue
    else:
        raise Exception("Invalid Syntax")
  # if final_code[i]
# printf("done")
# f=open("out.txt",'a')
# f.writelines(outpt)
# f.close()
if(f==0):
    raise Exception("hlt statement not used")
print(len(outpt))
# for i in range(len(outpt)-1):
    
#     print(outpt[i])
# print(outpt[-1],end='')
# sys.stdout.writelines(outpt)
# providing addr to hlt and var

# for i in range(128):
#     s=input().strip()
#     while s=='' or s=='\n':
#         s=input().strip()
#     s=s.split()