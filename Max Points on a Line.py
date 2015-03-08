# Definition for a point
# class Point:
#     def __init__(self, a=0, b=0):
#         self.x = a
#         self.y = b


class Solution:
    def gcd(self, a, b):
        if b != 0:
            return self.gcd(b, a % b)
        else:
            return a

    def reduce(self, p):
        if (p.x ** 2 + p.y ** 2) == 0:
            return '0 0'
        m = self.gcd(p.x, p.y)
        #print(str(p) + "," + str(m))
        return str(p.x / m) + ',' + str(p.y / m)

    # @param points, a list of Points
    # @return an integer
    def maxPoints(self, points):
        """Given n points on a 2D plane, \
find the maximum number of points that lie on the same straight line."""
        count = len(points)
        if count < 3:
            return count
        res = 0
        for p in points:
            slopes = [self.reduce(Point(p1.x - p.x, p1.y - p.y)) for p1 in points]
            lines = {}
            for slope in slopes:
                if lines.get(slope) is None:
                        lines[slope] = 1
                else:
                    lines[slope] = lines.pop(slope) + 1
            for line in lines:
                tmp = lines[line]
                if line != '0 0':
                    tmp += lines['0 0']
                if tmp > res:
                    res = tmp
        return res

    # @param points, a list of Points
    # @return an integer
    def maxPointsTLE(self, points):
        """Given n points on a 2D plane, \
find the maximum number of points that lie on the same straight line."""
        count = len(points)
        if count < 3:
            return count
        res = 2
        for i in range(0, count - 1):
            if count - i <= res:
                break
            for j in range(i + 1, count):
                tmp = 2
                for k in range(0, count):
                    if k == i or k == j:
                        continue
                    inline = self.pointInLine(points[i], points[j], points[k])
                    if inline:
                        if k < j:
                            break
                        else:
                            tmp += 1
                if tmp > res:
                    res = tmp
        return res

    def vectorInLine(self, v1, v2):
        return v1.x * v2.y == v2.x * v1.y

    def pointInLine(self, p1, p2, p3):
        v1 = Point(p2.x - p1.x, p2.y - p1.y)
        v2 = Point(p3.x - p1.x, p3.y - p1.y)
        return self.vectorInLine(v1, v2)


class Point:
    def __init__(self, a=0, b=0):
        self.x = a
        self.y = b

    def __str__(self):
        return str(self.x) + " " + str(self.y)


lin = [(0, 0), (1, 1), (1, -1)]
lin1 = [(560,248),(0,16),(30,250),(950,187),(630,277),(950,187),(-212,-268),(-287,-222),(53,37),(-280,-100),(-1,-14),(-5,4),(-35,-387),(-95,11),(-70,-13),(-700,-274),(-95,11),(-2,-33),(3,62),(-4,-47),(106,98),(-7,-65),(-8,-71),(-8,-147),(5,5),(-5,-90),(-420,-158),(-420,-158),(-350,-129),(-475,-53),(-4,-47),(-380,-37),(0,-24),(35,299),(-8,-71),(-2,-6),(8,25),(6,13),(-106,-146),(53,37),(-7,-128),(-5,-1),(-318,-390),(-15,-191),(-665,-85),(318,342),(7,138),(-570,-69),(-9,-4),(0,-9),(1,-7),(-51,23),(4,1),(-7,5),(-280,-100),(700,306),(0,-23),(-7,-4),(-246,-184),(350,161),(-424,-512),(35,299),(0,-24),(-140,-42),(-760,-101),(-9,-9),(140,74),(-285,-21),(-350,-129),(-6,9),(-630,-245),(700,306),(1,-17),(0,16),(-70,-13),(1,24),(-328,-260),(-34,26),(7,-5),(-371,-451),(-570,-69),(0,27),(-7,-65),(-9,-166),(-475,-53),(-68,20),(210,103),(700,306),(7,-6),(-3,-52),(-106,-146),(560,248),(10,6),(6,119),(0,2),(-41,6),(7,19),(30,250)]
lin2 = [(1, 1), (1, 1), (1, 1)]
lin3 = [(1, 1), (1, 1), (2, 2), (2, 2)]
lins = [lin, lin1, lin2, lin3]

for lint in lins:
    points = []
    for kv in lint:
        #print(kv)
        points.append(Point(kv[0], kv[1]))
    #print(points)
    ss = Solution()
    print(len(lint), lint)
    print(ss.maxPoints(points))
    print()