# Medical Diagnosis using Knowledge Base

## AI Course – II AIML/REC

### Category 8 – Knowledge Base

### Task 1 – Medical Diagnosis

---

## Aim

To implement a **Medical Diagnosis system using a Knowledge Base** containing:

* Facts
* Rules
* Forward Chaining
* Backward Chaining

---

# Knowledge Base

A Knowledge Base contains information represented as **facts and rules**.

### Facts

Facts are known information.

Example:

```text
fever
cough
body_pain
```

### Rules

Rules are used to derive new information from existing facts.

Example:

```text
IF fever AND cough
THEN flu
```

---

# Forward Chaining

Forward Chaining is a **data-driven reasoning technique**.

It starts with known facts and applies rules to derive new facts.

### Example

```text
Facts:
fever
cough

Rule:
fever AND cough → flu

Result:
flu
```

The process continues until no new facts can be derived.

---

# Backward Chaining

Backward Chaining is a **goal-driven reasoning technique**.

It starts with a goal and works backward to check whether the required facts are available.

### Example

Goal:

```text
flu
```

Rule:

```text
fever AND cough → flu
```

The system checks:

```text
Is fever available? → Yes
Is cough available? → Yes
```

Therefore:

```text
flu → True
```

---

# Program Working

The program:

1. Stores patient symptoms as facts.
2. Stores medical knowledge as rules.
3. Uses Forward Chaining to derive possible diagnoses.
4. Uses Backward Chaining to verify a selected diagnosis.
5. Displays the result.

---

# Example

### Initial Facts

```text
fever
cough
body_pain
```

### Rules

```text
fever + cough → flu
fever + body_pain → viral_infection
cough + body_pain → infection
```

### Result

```text
Forward Chaining:
flu
viral_infection
infection

Backward Chaining:
Diagnosis: flu
```

---

# Difference Between Forward and Backward Chaining

| Forward Chaining           | Backward Chaining              |
| -------------------------- | ------------------------------ |
| Starts with facts          | Starts with a goal             |
| Data-driven                | Goal-driven                    |
| Derives new facts          | Checks required facts          |
| Continues until conclusion | Works backward from conclusion |

---

# Conclusion

The Medical Diagnosis system was implemented using a Knowledge Base containing facts and rules.

Both **Forward Chaining** and **Backward Chaining** were implemented to demonstrate reasoning in Artificial Intelligence.

**Note:** This program is an educational AI demonstration and is not intended for real medical diagnosis.
