# Medical Diagnosis using Knowledge Base
# Facts, Rules, Forward Chaining and Backward Chaining


# -----------------------------
# FACTS
# -----------------------------

facts = {
    "fever",
    "cough",
    "body_pain"
}


# -----------------------------
# RULES
# -----------------------------

rules = [
    (["fever", "cough"], "flu"),
    (["fever", "body_pain"], "viral_infection"),
    (["cough", "body_pain"], "infection"),
    (["fever", "cough", "body_pain"], "flu")
]


# -----------------------------
# FORWARD CHAINING
# -----------------------------

def forward_chaining(facts):

    known = set(facts)

    changed = True

    while changed:

        changed = False

        for conditions, conclusion in rules:

            if all(condition in known for condition in conditions):

                if conclusion not in known:

                    known.add(conclusion)
                    changed = True

    return known


# -----------------------------
# BACKWARD CHAINING
# -----------------------------

def backward_chaining(goal, facts):

    if goal in facts:
        return True

    for conditions, conclusion in rules:

        if conclusion == goal:

            result = True

            for condition in conditions:

                if not backward_chaining(condition, facts):
                    result = False
                    break

            if result:
                return True

    return False


# -----------------------------
# MAIN PROGRAM
# -----------------------------

print("================================")
print("     Medical Diagnosis System")
print("================================")

print("\nInitial Facts:")

for fact in facts:
    print("-", fact)


# Forward Chaining
print("\nForward Chaining:")

new_facts = forward_chaining(facts)

for fact in new_facts:
    print("-", fact)


# Backward Chaining
print("\nBackward Chaining:")

goal = "flu"

if backward_chaining(goal, facts):
    print("Diagnosis:", goal)
else:
    print("Diagnosis cannot be determined.")






*OUTPUT*

================================
     Medical Diagnosis System
================================

Initial Facts:
- fever
- cough
- body_pain

Forward Chaining:
- fever
- cough
- body_pain
- flu
- viral_infection
- infection

Backward Chaining:
Diagnosis: flu
