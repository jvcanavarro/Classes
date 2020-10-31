
def reflection():
    if -1 < m < 1:
        x, y = y, x
        switch_xy = True

    if x1 > x2:
        x1 = -x1
        x2 = -x2
        switch_x = True

    if y1 > y2:
        y1 = -y1
        y2 = -y2
        switch_y = True


def inv_reflecion():
    if switch_y:
        for point in points:
            point[1] = -points[1]

    if switch_x:
        for point in points:
            point[0] = -point[0]

    if switch_xy:
        for point in points:
            point = point[::-1]

def bresenham(p1, p2):
    # reflection (p1, p2)

    x1 = p1[0]
    y1 = p1[1]
    x2 = p2[0]
    y2 = p2[1]

    dx = p2[0] - p1[0]
    dy = p2[1] - p1[1]

    m = dy / dx
    e = (m - 1) /  2

    # draw (x1, y1)

    while x1 <= x2:
        if e >= 0:
            y1 += 1
            e -= 1
        x1 += 1
        e += m
        # draw (x1, y1)

    # inv_reflection()
