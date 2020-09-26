from picker import createAssignments, pickRooms

def test_equal():
  print("\nBoth people want rooms equally")
  roomWeights = [
    [2,1],
    [2,1]
  ]

  assert pickRooms(roomWeights, createAssignments(set([0,1]))) == [[1,0],[0,1]]

def test_2():
  print("\nPerson 0 preferes room 1, person 1 prefers room 0")
  roomWeights = [
    [1,2],
    [2,1]
  ]

  assert pickRooms(roomWeights, createAssignments(set([0,1]))) == [[1,0]]

def test_3():
  print("\nPeople 1 and 2 prefer room 0, person 0 prefers room 1")
  roomWeights = [
    [1,2,1],
    [2,1,1],
    [2,1,1]
  ]

  assert pickRooms(roomWeights, createAssignments(set([0,1,2]))) == [[1,2,0],[1,0,2]]
