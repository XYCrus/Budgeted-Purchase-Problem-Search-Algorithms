#%%
import argparse
import random

parser = argparse.ArgumentParser(description = "Budgeted Purchase Problem Hill Climbing Solver")

parser.add_argument('--file_path', 
                    type = str, 
                    default = '../data/5.txt', 
                    help = "The path to the input file.")

args = parser.parse_args()

#%%
# Read txt file and parse output
def ParseInput(file_path):
    with open(file_path, 'r') as file:
        lines = file.readlines()
    T, B, Flag, Restarts = map(str, lines[0].strip().split())

    Objects = [tuple(line.strip().split()) for line in lines[1:]]

    Objects = [(obj[0], 
                int(obj[1]), 
                int(obj[2])) for obj in Objects]  
    
    return int(T), int(B), Flag, int(Restarts), Objects

# Calcuate error function value along with cost and value of a given state
def ErrorFunction(S, Objects, B, T):
    Cost = sum(Objects[obj][1] for obj in S)
    Value = sum(Objects[obj][0] for obj in S)

    return max(Cost - B, 0) + max(T - Value, 0), Cost, Value

# Find all possible successors given a state
def FindNeighbors(State, Objects):
    Neighbors = []
    for obj in Objects.keys():
        DummyState = State.copy()

        if obj in State: DummyState.remove(obj)
        else: DummyState.add(obj)

        Neighbors.append(DummyState)

    return Neighbors

# Determine best neighbor using error function
def FindBestNeighbor(Neighbors, Objects, B, T):
    BestError = 1e9
    BestNeighbor = None

    for neighbor in Neighbors:
        Error, _, _ = ErrorFunction(neighbor, Objects, B, T)

        if Error < BestError:
            BestError = Error
            BestNeighbor = neighbor

    
    Value = sum(Objects[obj][0] for obj in BestNeighbor)
    Cost = sum(Objects[obj][1] for obj in BestNeighbor)

    return BestNeighbor, BestError, Value, Cost

# Helper function to print given flag == 'V'
def PrintNeighbors(Neighbors, Objects, B, T):
    print("Neighbors:")

    for State in Neighbors:
        Error, Cost, Value = ErrorFunction(State, Objects, B, T)

        print(f"{State}. Value = {Value}. Cost = {Cost}. Error = {Error}.")

        if Error == 0:
            break

# Main hill climbing implementation
def HC(T, B, Objects, Restarts, Flag):
    # Parameter initialization
    Objects = {obj[0]: (obj[1], obj[2]) for obj in Objects}
    BestGlobalError = 1e9
    BestGlobalState = None

    for restart in range(Restarts):
        # Random restart with 0.5 probability for each object
        DummyState = set(random.choice([obj[0], None]) for obj in Objects if random.random() < 0.5)
        DummyState.discard(None)

        Error, Cost, Value = ErrorFunction(DummyState, Objects, B, T)

        print("Randomly chosen starting state: ")
        print(f"{DummyState}. Value = {Value}. Cost = {Cost}. Error = {Error}.")

        while True:
            # Find neighbors and then determine how to proceed based on error function value
            Neighbors = FindNeighbors(DummyState, Objects)
            BestNeighbor, BestError, NeighborValue, NeighborCost = FindBestNeighbor(Neighbors, Objects, B, T)
            
            if Flag == 'V': PrintNeighbors(Neighbors, Objects, B, T)

            if BestError == 0: break

            if BestError < Error:
                if Flag == 'V':
                    print()
                    print(f"Move to {BestNeighbor}. Value = {NeighborValue}. Cost = {NeighborCost}. Error = {BestError}.")

                DummyState, Error = BestNeighbor, BestError

            else:
                if Flag == 'V': 
                    print("Search failed.")
                    print()
                break
            
            if Error < BestGlobalError:
                BestGlobalError = Error
                BestGlobalState = DummyState

    # Output after search loop 
    if BestGlobalState is not None:
        print(f"Found solution: {BestGlobalState}. Error = {BestGlobalError}.")

    else:
        print("No solution.")

#%%
# Main
if __name__ == '__main__':
    T, B, Flag, Restarts, Objects = ParseInput(args.file_path)
    HC(T, B, Objects, Restarts, Flag)
