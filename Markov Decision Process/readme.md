# Markov Decision Process (MDP)
- It is a mathematical framework used in AI.
- It is used for reinforcement learning model. 
- `The Future is depends on the current state`, not full history.

## Components of MDP
1. **States** `(S)` - possible actions (start, middle, goal)
2. **Actions** `(A)` - Choices to the agent
3. **Transition Probability** `(P or T)` - Probability of moving to the next state.
4. **Reward** `(R)` - recieved after taing an action
5. **Discount Factor** `(γ)` - A value between 0 and 1 that determines the importance of future rewards compared to immediate rewards.
6. **Policy** `(\(\pi \))` strategy tells to the AI angentwhich action to take in each state.

## Applications
- Robotics
- Self-driving Cars
- Recomendation systems

## Advantages
- Handles uncertainity
- Sequential decisions

## Limitations
- Large State space

## Sample code to understand Markov Decision Process
```python
states = ["start", "middle", "goal"]
transition = {
    "start": { "move": "middle"},
    "middle": {"move": "goal"},
    "goal": {}
}

reward = {
    "start": 0,
    "middle": 5,
    "goal": 10
}

total_reward = 0
current_state = "start"

while current_state != "goal":
    print("Current State: ", current_state)
    
    # Process
    action = "move"
    next_state = transition[current_state][action]
    rewarded = reward[next_state]
    total_reward = total_reward + rewarded
    current_state = next_state

    # For Viewing the process
    print("Action: ", action)
    print("Next State: ", next_state)
    print("rewarded: ", rewarded)
    print("------------------")

print("Total reward: ", total_reward)
print("Current State: ", current_state)
print("\n\nReached Goal..!")
    
```