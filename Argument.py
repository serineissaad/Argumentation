from Literal import Literal
from Rule import Rule


class Argument:
    count = 1

    def __init__(self, top_rule, sub_arguments):
        self.top_rule = top_rule #rule
        self.sub_arguments = sub_arguments #argument
        self.name = "A"+str(Argument.count)
        Argument.count += 1

        #for each top rule, if conc(rule of any_argument)== conc(the current rule's premises) 
        #then replace this premise by the currrent argument 

    def __str__(self):
        # return f"Argument {self.name}:  Top rule: {self.top_rule}, Direct sub-arguments: {self.sub_arguments}"
        # for premise, sub in self.top_rule.premisses, self.sub_arguments:
        return f"{self.name}: {self.sub_arguments} => {self.top_rule.conclusions}"

        # return f"Argument {self.name}:  Top rule: {self.top_rule}, Direct sub-arguments: {self.sub_arguments}"

    def __eq__(self, other):
        if not isinstance(other, Argument):
            return False
        return (self.top_rule == other.top_rule and
                self.sub_arguments == other.sub_arguments and
                self.name == other.name)

LR=[
    Rule([], Literal("a"), False),
    Rule([Literal("b"), Literal("d")], Literal("c"), False),
    Rule([Literal("¬c")], Literal("d"), False),
    Rule([Literal("a")], Literal("¬d"), True),
    Rule([], Literal("b"), True),
    Rule([], Literal("¬c"), True),
    Rule([], Literal("d"), True),
    Rule([Literal("c")], Literal("e"), True),
    Rule([Literal("¬c")], Literal("¬r2"), True)
]

contrap_rules = [] 

for rule in LR:
    LRC = rule.contraposition() 
    if LRC:
        contrap_rules.extend(LRC)
LR.extend(contrap_rules)

for rule in LR:
    print(rule)

print("________ARGUMENTS________\n")

Arguments=[]
LRCopy=LR[:]

# Iterate over the list backwards using reversed range
for i in range(len(LR) - 1, -1, -1):
    rule=LRCopy[i] 
    if len(rule.premisses)==0:
        arg=Argument(rule,[])
        Arguments.append(arg)
        del LRCopy[i]

new_arg_added = True
while len(LRCopy) > 0 and new_arg_added:
    new_arg_added = False
    i = len(LRCopy) - 1
    while i >= 0:
        rule = LRCopy[i]
        # Initialize a list for possible new arguments with full sub-arguments
        possible_new_args = []

        # Assess each premise of the rule
        for premise in rule.premisses:
            prem_eq_args = [argument.name for argument in Arguments if (premise == argument.top_rule.conclusions) or (f"¬¬{premise}"==argument.top_rule.conclusions)]
            if not prem_eq_args:  # No matching arguments for the premise
                Argument.count-=1
                break  # This rule cannot form a valid argument at this time
            else:
                # If this is the first premise we are evaluating for this rule
                if not possible_new_args:
                    possible_new_args = [Argument(rule, [sub_arg]) for sub_arg in prem_eq_args]
                else:
                    # Extend each existing argument in possible_new_args with new sub-arguments
                    new_combinations = []
                    for existing_arg in possible_new_args:
                        new_combinations.extend([Argument(rule, existing_arg.sub_arguments + [new_sub_arg]) for new_sub_arg in prem_eq_args])
                    possible_new_args = new_combinations

        # Only append to Arguments if the rule could form complete new arguments
        if possible_new_args:
            Arguments.extend(possible_new_args)
            del LRCopy[i]  # Remove the rule as it's been processed
            new_arg_added = True
        i -= 1


for argument in Arguments:
    print(f"{argument}, rule: {argument.top_rule}")


# TO CORRECT: WE'RE NOT MODIFYING LITERALS IN CONTRAPOSITION