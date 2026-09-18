# Logical Agent in AI
- A Logical Agent represent knowledge using logic and reasons to make decisions.
- It uses first order logic or propositional knowledge to represent knowlege.

## Charateristics
- `Knowledge-based` - Stores facts and rules.
- `Uses inference Engine` - Derives new facts using logical reasoning.
- `Rational decision making` - **Example:** If Rain -> WetRoad
- `Explains conslusions`

## Applications
- Robotics
- Medical Diagnosis
- NLP

## Advantages
- Explainable
- Consistent
- Supports complex reasoning

## Limitations
- Knowledge acquisition is difficult
- computationally expensive


## Example code: `Relationship amoug Family`
```python
class family1:
    def __init__(self):
        self.parents = []
    
    def add_parent(self,p,c):
        self.parents.append((p,c))
    
    # Checking Grandparent
    def is_grandparent(self):
        for p1, c1 in self.parents:
            for p2, c2 in self.parents:
                if c1 == p2:
                    print(c2, " is Grandparent of ", p1)

    # Checking Sibblings
    def is_sibblings(self):
        for p1, c1 in self.parents:
            for p2, c2 in self.parents:
                if p1 == p2 and c1 < c2:
                    print(c1, " is Sibblings of ", c2)


obj = family1()
obj.add_parent("Sita", "Rama")
obj.add_parent("Rama", "Lavan")
obj.add_parent("Rama", "kusan")
obj.is_grandparent()
obj.is_sibblings()

```