# %%
import math
import xml.etree.ElementTree as etree
import random
import pprint

# %%
class Point:
    def __init__(self):
        self.x = None
        self.y = None
        self.z = None

        self.id = None

# %%


pp = pprint.PrettyPrinter(indent=4)

def Distance(point1, point2):
    x1, y1 = point1
    x2, y2 = point2

    print("p1:", point1, "p2:", point2)

    dx = x1 - x2
    dy = y1 - y2
    
    return(math.sqrt(dx * dx + dy * dy))

def ClosestPoint(all_points, new_points):
    best_point = None
    best_distance = None

    for current_point in all_points:
        current_distance = Distance(new_points, current_point)
        if best_distance == None or current_distance < best_distance:
            best_distance = current_distance
            best_point = current_point
    
    return best_point

k = 2 
def BuildKdtree(points, depth=0):
    n = len(points)

    if n<= 0:
        return None
    
    axis = depth % k

    sorted_points = sorted(points, key= lambda point: point[axis])
    print(sorted_points[((int)(n / 2))][:k])

    return({
        "point": sorted_points[ (int)(n / 2)][:k],
        "left":  BuildKdtree(sorted_points[:(int)(n/2)], depth+1),
        "right": BuildKdtree(sorted_points[(int)(n/2) + 1:], depth+1),
        "classified": -1
    })

def KdtreeNaiveClosestPoint( root, point, depth=0, best=None):
    if root is None:
        return best
    
    axis = depth % k
 
    next_best = None
    next_branch = None
    if best is None or Distance(point, best) > Distance(point, root["point"]):
        next_best = root["point"]
    else:
        next_best = best
    
    if point[axis] < root["point"][axis]:
        next_branch = root["left"]
    else:
        next_branch = root["right"]
    
    return(KdtreeNaiveClosestPoint(next_branch, point, depth+1, best = next_best))

def CloserDistance( pivot, p1, p2):
    if p1 is None:
        return(p2)
    if p2 is None:
        return(p1)
    
    d1 = Distance(p1, pivot)
    d2 = Distance(p2, pivot)
    
    if d1 < d2:
        #return(p1, d1)
        return(p1)
    else:
        #return(p2, d2)
        return(p2)

def KdtreeClosestPoint( root, point, depth=0):
    if root is None:
        return (None)
    
    axis = depth % k 
    next_branch = None
    opposite_branch = None

    if point[axis] < root["point"][axis]:
        next_branch = root["left"]
        opposite_branch = root["right"]
    else:
        next_branch = root["right"]
        opposite_branch = root["left"]
    
    print("depth:",depth, " p1:", point)
    
    best = CloserDistance(point,
                        KdtreeClosestPoint(next_branch, point, depth + 1),
                        root["point"])

    if Distance(point, best) > abs(point[axis] - root["point"][axis]):
        best = CloserDistance(point,
                                KdtreeClosestPoint(opposite_branch, point, depth+1),
                                best)

    return(best)


def KdtreeRangeSearch( root, point, depth=0, epsilon=1.0):
    if root is None:
        return(None)
    
    
    axis = depth % k
    next_branch = None
    opposite_branch = None
    
    points = []
    
    if root["classified"] == -1 and Distance(point, root["point"]) <= epsilon:
        #print("Member")
        points.append(root["point"])
    
    if point[axis] < root["point"][axis]:
        next_branch = root["left"]
        opposite_branch = root["right"]
    else:
        next_branch = root["right"]
        opposite_branch = root["left"]


    #print("Depth>>", depth)
    #if root["right"] is not None:
    ##    print("right>>", root["right"]["point"])
    #if root["left"] is not None:
    #    print("left>>", root["left"]["point"])
    #if next_branch is not None:
    #    print("Next>>", next_branch["point"])


    
    # 近い側のブランチの探索
    #print("Near Branch")
    new_points = KdtreeRangeSearch( next_branch, point, depth + 1, epsilon)
    if new_points is not None:
        points.extend(new_points)
    
    # 遠い側のブランチの探索
    #print("Opposite Branch")
    if opposite_branch is not None:
        #print(opposite_branch["point"])
        #print(point[axis] - opposite_branch["point"][axis])
        if math.fabs(point[axis] - root["point"][axis]) <= epsilon:
            new_points = KdtreeRangeSearch( opposite_branch, point, depth + 1, epsilon)
            if new_points is not None:
                points.extend(new_points)
    

    return(points)
    


# %%
class RayCasting:
    def __init__(self, range_min_th, range_max_th, range_resolution, angle_min, angle_max, angle_resolution):

                         
        self.__lookuptable  =   None
        self.ray_line_num     =   None
        self.single_ray_point_num     = None

        self.__range_max_th = None
        self.__range_min_th = None
        self.__range_res    = None

        self.__angle_max    = None
        self.__angle_min    = None
        self.__angle_res    = None
        
        self.ChangeRangeParam( range_min_th, range_max_th, range_resolution)
        self.ChangeAngleParam( angle_min, angle_max, angle_resolution)
        
        self.CreateLookUpTable()
        

    def ChangeRangeParam(self, range_min_th, range_max_th, range_resolution):
        self.__range_min_th = range_min_th
        self.__range_max_th = range_max_th
        self.__range_res    = range_resolution

        print("Range Param")
        print(self.__range_min_th, self.__range_max_th, self.__range_res)
        
    def ChangeAngleParam(self, angle_min, angle_max, angle_resolution):
        deg2rad = 1.0
        if angle_min > 1.57 or angle_max > 1.57:
            deg2rad = math.pi / 180.0

        self.__angle_min    = deg2rad * angle_min
        self.__angle_max    = deg2rad * angle_max
        self.__angle_res    = deg2rad * angle_resolution
        print("Angle Param")
        print(self.__angle_min, self.__angle_max, self.__angle_res)
        
        
    def CreateLookUpTable(self):
        print("Angle Param")
        print(self.__angle_min, self.__angle_max, self.__angle_res)
        print("Range Param")
        print(self.__range_min_th, self.__range_max_th, self.__range_res)
        
        self.ray_line_num            = (int) ( (self.__angle_max - self.__angle_min) / self.__angle_res )
        self.single_ray_point_num    = (int) ( (self.__range_max_th - self.__range_min_th) / self.__range_res)

        #line = [[ 0.0, 0.0, 0.0] for i in range(self.single_ray_point_num)]
        point_range = self.__range_min_th
        p = [ 0.0, 0.0, 0.0]
        
        range_list = []
        self.single_ray_point_num = 0
        while point_range < self.__range_max_th:
            #p[0] = point_range 
            #p[2] = point_range * math.tan(self.__angle_res * 0.5)
            range_list.append([point_range, point_range * math.tan(self.__angle_res * 0.5)])
            point_range += point_range * math.tan( self.__angle_res)
            self.single_ray_point_num += 1
        
        #for i in range(self.single_ray_point_num):
        #    point_range = self.__range_min_th + self.__range_res * i
        #    line[i][2] = point_range * math.tan(self.__angle_res * 0.5)

        #self.__lookuptable = [line for i in range(self.ray_line_num)]


        point_range = None
        self.__lookuptable = []
        for i in range(self.ray_line_num):
            ang = self.__angle_min + self.__angle_res * i
            line = []
            #for j in range(self.single_ray_point_num):
            for j in range(len(range_list)):
                #point_range = self.__range_min_th + self.__range_res * j
                #point_range = l[j][0]
                #l[j][0] = point_range * math.cos(ang)
                #l[j][1] = point_range * math.sin(ang)
                p = []
                x = range_list[j][0] * math.cos(ang)
                y = range_list[j][0] * math.sin(ang)
                p = [ x, y, range_list[j][1]]
                line.append( p )
                #self.__lookuptable[i][j][0] = point_range * math.cos(ang)
                #self.__lookuptable[i][j][1] = point_range * math.sin(ang)
                #self.__lookuptable[i][j][2] = point_range * math.tan(self.__angle_res * 0.5)
                #print( point_range, ":", self.__lookuptable[i][j][2])
            self.__lookuptable.append(line)

        #for i in range(self.ray_line_num):
        #    for j in range(len(self.__lookuptable[i])):
        #        print(self.__lookuptable[i][j])
        
    def Run( self, kdtree):
        nearest_points = []
        for i in range(self.ray_line_num):
            p = None
            for j in range(self.single_ray_point_num):
                p = KdtreeClosestPoint( kdtree,  self.__lookuptable[i][j][:2], 0)
                dist = Distance( self.__lookuptable[i][j][:2], p)
                #print(i,",",j,",",self.__lookuptable[i][j], ":::: dist=",dist)
                
                if dist < self.__lookuptable[i][j][2]:
                    nearest_points.append(p)
            if p == None:
                nearest_points.append(self.__lookuptable[i][self.range_ray_point_num - 1][:2])
        return(nearest_points)

# %%


points = [[random.uniform(0,100), random.uniform(-50,50), i] for i in range(100)]

print(points)

#points[5][0] = points[6][0]
#points[7][1] = points[8][1]


# %%
kdtree = BuildKdtree(points, 0)

# %%

# %%
ray_cast = RayCasting( 5, 100, 1, -90, 90, 0.5)

# %%
#nn_points = ray_cast.Run(kdtree)

# %%

# %%
#nn_points

# %%
import time

# %%
#pp.pprint(kdtree)
p = [ 25, 25]
#nearest = kdtree_naive_closest_point(kdtree, p)

#nearest = KdTreeClosestPoint(kdtree, p)
#nearest
epsilon = 10
t1 = time.time()
cluster_points = KdtreeRangeSearch(kdtree, p, 0, epsilon=epsilon)
t2 = time.time()
print(t2-t1)

# %%
len(cluster_points)

# %%
import matplotlib.pyplot as plt
import matplotlib.patches as patches

# %%
fig = plt.figure()
ax = plt.axes()

for point in points:
    ax.scatter(point[0], point[1], c= "blue", s=2)

#for point in nn_points:
#    ax.scatter(point[0], point[1], c="red", s=3)


# %%

# %%
nearest = KdtreeClosestPoint(kdtree, p)
nearest

fig = plt.figure()
ax = plt.axes()
ax.set_aspect("equal")
for point in points:
    ax.scatter(point[0], point[1], c="green", s=2)
ax.scatter(p[0], p[1], c="red")
ax.scatter(nearest[0], nearest[1], c="blue", s=2)

for member in cluster_points:
    ax.scatter(member[0],member[1], c="red", s=2)
    #circle = patches.Ellipse(xy=(member[0], member[1]), width=5, height=5, ec="blue", fill=False)
    #ax.add_patch(circle)

eps = patches.Ellipse(xy=(p[0], p[1]), width = 2*epsilon, height=2*epsilon, ec="red", fill=False, linewidth=1)
ax.add_patch(eps)


# %%
fig

# %%
plt.show()

# %%

start = 150000
result = start
def ri( start, riri):
    return(start * (1 + riri))

for i in range(10):
    result = ri(result, 0.0005)
result

# %%
math.pi / 180

# %%
ang = 0.1 * math.pi / 180 

# %%
60 * math.tan(ang)

# %%



