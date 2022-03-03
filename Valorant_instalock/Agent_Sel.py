
def agentSel():
    slotInput = input("Select agent: ")
    if slotInput.strip().isdigit():
        slotInput = int(slotInput)
    else:
        print("Not a number")
        quit()

    while 1 < slotInput > 18:
        print("Ivalid number, has to be between 1-18")
        slotInput = int(input("Select agent: "))
        

    global agent_X
    agent_X = 626

    global agent_Y
    agent_Y = 925

    if slotInput == 1:
        agent_X = agent_X
    elif slotInput > 1 and slotInput < 10:
        agent_X = agent_X+84*(slotInput-1)
    elif slotInput > 9 and slotInput < 19:
        agent_X = agent_X+84*(slotInput-10)
        agent_Y = agent_Y + 84
    else:
        print("Not in range, try again")

def main():
    agentSel()
    print(agent_X)
    print(agent_Y)

main()