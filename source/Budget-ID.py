#%%
import argparse

parser = argparse.ArgumentParser(description = "Budgeted Purchase Problem Iterative Deepening Solver")
    
parser.add_argument('--file_path', 
                    type = str, 
                    default = '../data/1.txt',
                    help = 'Path to the input file')

args = parser.parse_args()

#%%
# Read txt file and parse output
def ParseInput(path):
    with open(path, 'r') as file:
        lines = file.readlines()

    T, B, Flag = lines[0].strip().split()

    Objects = [(line.split()[0], 
                int(line.split()[1]), 
                int(line.split()[2])) for line in lines[1:]]

    return int(T), int(B), Flag, Objects

# Main iterative deepening implementation
def ID(T, B, Objects, Flag):
    for Depth in range(1, len(Objects) + 1):
        if Flag == 'V': print(f'Depth = {Depth}')

        # Parameter Initialization
        DummyTuple = [([], 0, 0, 0)]  
        Addition = False

        while DummyTuple:
            # Pop most recent value
            Order, Value, Cost, Index = DummyTuple.pop()

            if Cost <= B:
                if Flag == 'V' and Addition: 
                    print(f'{Order}. Value = {Value}. Cost = {Cost}.')
                    Addition = False

                # Cost less than B and Value geq than T, goal state
                if Value >= T:
                    return Order, Value, Cost
                
            # If can add a new object to the basket given current depth
            if Index < len(Objects) and len(Order) < Depth:
                DummyTuple.append((Order, Value, Cost, Index + 1))

                obj, obj_value, obj_cost = Objects[Index]
                if Cost + obj_cost <= B:
                    Addition = True
                    DummyTuple.append((Order + [obj], 
                                       Value + obj_value, 
                                       Cost + obj_cost, 
                                       Index + 1))
        if Flag == 'V': print()
                    
    return None

# Helper function to determine output given Flag and search result
def Output(DummyTuple, Flag):
    if DummyTuple is None:
        print("No Solution")

    else:
        Order, Value, Cost = DummyTuple

        if Flag == 'C':
            print(' '.join(Order))

        else:
            print(f"Found solution {Order}. Value = {Value}. Cost = {Cost}.")

#%%
# Main
if __name__ == '__main__': 
    T, B, Flag, Objects = ParseInput(args.file_path)
    Result = ID(T, B, Objects, Flag)
    Output(Result, Flag)