 # Define the instruction set in a dictionary as follows
#  The instructions are mapped as key = instruction and value = instruction number in hexadecimal  format
instructions = {
    "halt": 0x00,
    "nop": 0x01,
    "li": 0x02,
    "lw": 0x03,
    "sw": 0x04,
    "add": 0x05,
    "sub": 0x06,
    "mult": 0x07,
    "div": 0x08,
    "j": 0x09,
    "jr": 0x0A,
    "beq": 0x0B,
    "bne": 0x0C,
    "inc": 0x0D,
    "dec": 0x0E

}

# The assembly code is in code.txt file
# Read the text assembly program using the following code
with open('code.txt') as f:
    program = f.readlines()

# get the number of instructions and comments in the program
# file which is code.txt
size = len(program)

# creating a string to hold the result which can be used to run the function to assemble the code
d= "" 

# Loop through the file to get it contents line by line
i = 0
while(i < size):
    # print(program[i])

    # Set a string for every line in the assembly code file
    line = program[i]

    # Now split each line obtained to get individual words ( Contents of a line)
    a = program[i].split()
     
    # Get the size of each token or lexeme in each instructions
    size3 = len(a)

    # Loop through each string of each instrution to check if it has the assembler commands like li, sw etc...
    j = 0
    while(j < size3):
        if(a[j] == "halt" or a[j] == "nop" or a[j] == "li" or a[j] == "lw" or a[j] == "sw" or a[j] == "add" or a[j] == "mult" or a[j] == "sub" or a[j] == "div" or a[j] == "j" or a[j] == "jr" or a[j] == "beq" or a[j] == "bne" or a[j] == "inc" or a[j] == "dec"):

            # assign each encoded line of code to a string variable a.
            # the code goes ahead to get the value which is the instruction number from the instructions dict above
            # the register and immediate value are then gotten from the text program

            # if there are more than three words in program line print the instruction number followed by the other contents of instruction
            if(size3>3):
                b = (hex(instructions[a[j]]) + "" + a[j+1] +""+ a[j+2] +""+ a[j+3])

            # if there are more than 2 words in program line  print the instruction number followed by the other contents of instruction
            elif(size3>2):
                b = (hex(instructions[a[j]]) + "" + a[j+1] +""+ a[j+2])
            
            # if there are more than 1 word in program line  print the instruction number followed by the other contents of instruction
            elif(size3>1):
                b = (hex(instructions[a[j]]) + "" + a[j+1])
            
            # if there are is 1 word in program line  print the instruction number 
            elif(size3>0):
                b = (hex(instructions[a[j]]))

            # convert the other contents of instruction to encoded format as explained below
            # R1 assigned hex value of 100
            # R2 assigned hex value of 200
            # R3 assigned hex value of 300
            # loop assigned hex value of 400

            # replace every appearance of above values with their hex values
            c = b.replace("R1", hex(100))
            c = c.replace("R2", hex(200))
            c = c.replace("R3", hex(300))
            c = c.replace("loop", hex(400))

            # String d will be used in the function to assemble as a parameter
            # Here we add every new line to variable d using the following code
            d += c+"\n"

            # Print to standard output the encoded program (in hexadecimal format)
            print(c)   

        # # Code to assume comments by doing nothing when it encounters one
        # else:
        #     pass

        j+=1 

    i+=1




# print(hex(500))
# Define register mappings
REGISTERS = {
    0x64: 'R1',
    0xc8: 'R2',
    0x12c: 'R3'

}
''' There are additional registers PC and COND not included in above 
    dict because they are not used to store operands, in this case the
    dict above is referenced for this purpose only'''

# define the loop start as the PC 
LOOP_START = 0x0000CFFF

def assemble(program):
    # Initialize registers
    registers = {'R' + str(i): 0 for i in range(3)}

    # initialize memory
    memory = [0] * (LOOP_START + 1)

    # use the code below to load program into memory
    # loading starts from address 0
    for i, instructions in enumerate(program):
        memory[i] = instructions

        
    # Initialize program counter using the following code
    pc = 0

    # Execute program using the while loop below
    while instructions:
        # Fetch next instruction from memory
        instructions = memory[pc]

        # print(memory[pc])

        # if the instructio is 0x0 for halt end execution
        if isinstance(instructions, int):
            # instructions = 0x0
            # print(instructions)
            break

        # else split the instruction line to its individual contents
        else:
            instructions = instructions.split('0x')[1:]

            # Splitted contents are still in string format convert them to integer, they can be accessed by program as hex
            instructions = [int(hex_num, 16) for hex_num in instructions]

            # print(len(instructions))
            # Decode instruction

            # print(instructions)

            # opcode will always be the first element of instruction line
            opcode = (instructions[0])

            # check subsequent contents of instruction line to see if they point to a given register
            i = 0
            while(i < len(instructions)):
                if instructions[i] in REGISTERS:
                    r = instructions[i]
                elif len(instructions) >2:
                    operand = instructions[2]
                i+=1

            # Execute the instruction using the following series of if statements
            if opcode == 0x0: #for halt
                print(registers)
                break

            elif opcode == 0x01:  #for nop
                pass

            elif opcode == 0x2:  #for li
                registers[REGISTERS[r]] = int(operand)
                print(registers)

            elif opcode == 0x4:  #for sw
                memory[registers[REGISTERS[r]]] = registers[REGISTERS[r]]
                print(registers)

            elif opcode == 0x0E:  #for dec
                registers[REGISTERS[r]] -= 1
                print(registers)

            elif opcode == 0xc:  #for bne

                if registers[REGISTERS[r]] != registers[REGISTERS[r]]:
                    pc = operand
                    print(registers)
                    continue

            elif opcode == 0xd:  #for inc
                registers[REGISTERS[r]] += 1
                print(registers)

            else: #incase the execution fails
                print("Sorry an error occurred pleas re-check")

            # Increment program counter
            pc += 1


# split string d to get its contents line by line
d=d.split()

# call the function
assemble(d)




