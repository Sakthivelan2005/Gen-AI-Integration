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
    