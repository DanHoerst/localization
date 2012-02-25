# list of probabilities
p = [0.2, 0.2, 0.2, 0.2, 0.2]
# course/track by color
world = ['green', 'red', 'red', 'green', 'green']
# correct square 
measurements = ['red', 'green']
# how many squares to move
motions = [1,1]
# probability of hit/miss
pHit = 0.6
pMiss = 0.2
# probability of exact hit, overshoot, undershoot
pExact = 0.8
pOvershoot = 0.1
pUndershoot = 0.1

def sense(p, Z):
    q = []
    for i in range(len(p)):
        # hit if Z = world course color
        hit = (Z == world[i])
        # equals pHit if hit is true, pMiss if false
        q.append(p[i] * (hit * pHit + (1-hit) * pMiss))
    s = sum(q)
    # finds true probability by dividing each by sum
    for i in range(len(q)):
        q[i] = q[i] / s
    return q

def move(p, U):
    q = []
    # adds all possibilities of outcomes for each probability square
    for i in range(len(p)):
        s = pExact * p[(i-U) % len(p)]
        s += pOvershoot * p[(i-U-1) % len(p)]
        s += pUndershoot * p[(i-U+1) % len(p)]
        q.append(s)
    return q

for k in range(len(measurements)):
    p = sense(p, measurements[k])
    p = move(p, motions[k])
print p

