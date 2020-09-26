# this script is designed to help you pick rooms optimally

# input room preference weightings as a 2d array
# [
#   [{weight for room 0}, {weight for room 1}] # room preferences for person 0
#   [{weight for room 0}, {weight for room 1}] # room preferences for person 1
# ]

def createAssignments(choices): # choices is a set of room #s you can pick from
  if not choices:
    return [[]]

  # index = person, value = room
  res = []
  # so we can freely remove/add from/to set
  choicesList = [ choice for choice in choices ]

  for choice in choicesList:
    choices.remove(choice)
    prev = createAssignments(choices)
    res.extend([ p + [choice] for p in prev])
    choices.add(choice)
  
  # print(res)
  return res


def pickRooms(weights, assignments): # 2d array of weights, and possible assingments
  maxWeight = 0
  weighted = {}

  for assignment in assignments:
    weight = sum([ weights[person][room] for person, room in enumerate(assignment) ])
    if weight in weighted:
      weighted[weight].append(assignment)
    else:
      weighted[weight] = [assignment]
    maxWeight = max(maxWeight, weight)

  #print(weighted)
  return weighted[maxWeight]


# some examples

print("\nBoth people want rooms equally")
roomWeights = [
  [2,1],
  [2,1]
]

print(pickRooms(roomWeights, createAssignments(set([0,1]))))


print("\nPerson 0 preferes room 1, person 1 prefers room 0")
roomWeights = [
  [1,2],
  [2,1]
]

print(pickRooms(roomWeights, createAssignments(set([0,1]))))


print("\nPeople 1 and 2 prefer room 0, person 0 prefers room 1")
roomWeights = [
  [1,2,1],
  [2,1,1],
  [2,1,1]
]

print(pickRooms(roomWeights, createAssignments(set([0,1,2]))))
