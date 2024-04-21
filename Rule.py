from Literal import Literal


class Rule:
    count = 1

    def __init__(self, premisses, conclusions, is_defeasible):
        self.premisses = premisses
        self.conclusions = conclusions
        self.is_defeasible = is_defeasible
        self.reference = "r"+str(Rule.count)
        Rule.count += 1

    def __str__(self):
        premises_str = ', '.join(map(str, self.premisses))
        if self.is_defeasible:
            return f"{self.reference}: {premises_str} => {self.conclusions}"
        return f"{self.reference}: {premises_str} -> {self.conclusions}"

    def __eq__(self, other):
        if not isinstance(other, Rule):
            return False
        return (self.premisses == other.premisses and
                self.conclusions == other.conclusions and
                self.is_defeasible == other.is_defeasible and
                self.reference == other.reference)


    def contraposition(self):
        LR=[]
        if(self.is_defeasible):
            return LR
        premises = self.premisses
        if len(premises) == 0:
            return LR
        elif len(premises) == 1:
            Rule.count +=1
            if premises[0].is_negative==True:
                LR.append(Rule([Literal(f"¬{self.conclusions}")], Literal(f" {premises[0]}"), False))
            else:
                LR.append(Rule([Literal(f"¬{self.conclusions}")], Literal(f"¬{premises[0]}"), False))
            return LR
        else:
            for i, premisse in enumerate(premises):
                remaining_premisses = [Literal(f"¬{self.conclusions}")] + premises[:i] + premises[i + 1:]
                LR.append(Rule(remaining_premisses,Literal(f"¬{premisse}"),False))
                Rule.count += 1 
            return LR



# rule1 = Rule([Literal("a"), Literal("¬b"), Literal("c")], Literal("e"), False)
# print(rule1)

# rule2 = Rule([], Literal("¬a"), False)
# print(rule2)

# rule3 = Rule([Literal("a")], Literal("e"), False)
# print(rule1 == rule2)

# rules=rule1.contraposition()
# for rule in rules:
#     print(rule)
