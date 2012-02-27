colors = [['red', 'green', 'green', 'red' , 'red'],
          ['red', 'red', 'green', 'red', 'red'],
          ['red', 'red', 'green', 'green', 'red'],
          ['red', 'red', 'red', 'red', 'red']]

measurements = ['green', 'green', 'green' ,'green', 'green']
motions = [[0,0],[0,1],[1,0],[1,0],[0,1]]
sensor_right = 0.7
sensor_wrong = (1-sensor_right)
p_move = 0.8
# sets p to empty, then values() giving it an equal distribution of probability
p = []
p = values(p)

# prints the array
def show(p):
    for i in range(len(p)):
        print p[i]

# gives values to each cell in the array as a probability. these values will sum to 1.
def values(n):
    p = []
    sum = 0
    for i in range(len(colors)):
        sum = sum + len(colors[i])
    cell_val = (1.0/sum)
    for x in range(len(colors)):
        m = []
        for y in range(len(colors[x])):
            m.append(cell_val) 
        p.append(m)
    return p

# senses the array
def sense(p, Z):
    q = []
    sum = 0
    for i in range(len(p)):
        m = []
        for y in range(len(p[i])):
            # hit if Z = color
            hit = (Z == colors[i][y])
            # equals sensor_right if hit is true, sensor_wrong if false
            sum += (p[i][y] * (hit * sensor_right + (1-hit) * sensor_wrong))
            m.append(p[i][y] * (hit * sensor_right + (1-hit) * sensor_wrong))
        q.append(m)
    # finds true probability by dividing each by sum
    for i in range(len(q)):
        for y in range(len(q[i])):
            q[i][y] = q[i][y] / sum
    return q
    
def move(p, args):
    q = []
    # takes first argument or array, up and down index
    first = args[0]
    # takes second argument of array, left and right index
    second = args[1]
    sum = 0 
    # adds all possibilities of outcomes for each probability square
    for i in range(len(p)):
        m = []
        # calculates the probability of a move given the p_move variable
        for y in range(len(p[i])):
            if first == 0:
                s = p_move * p[i][(y-second) % len(p[i])]
                s += (1-p_move) * p[i][y]
                sum += s
                m.append(s)
            else:
                s = p_move * p[(i-first) % len(p)][y]
                s += (1-p_move) * p[i][y]
                sum += s
                m.append(s)
        q.append(m)
    # finds true probability by dividing each by sum
    for i in range(len(q)):
        for y in range(len(q[i])):
            q[i][y] = q[i][y] / sum
    return q

# loops through each measurement, moves, then senses
for k in range(len(measurements)):
    p = move(p, motions[k])
    p = sense(p, measurements[k])

show(p)

