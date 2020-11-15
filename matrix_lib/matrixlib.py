# To add a new cell, type '# %%'
# To add a new markdown cell, type '# %% [markdown]'
# %%
import math
import copy
class Matrix:
    def __init__(self, row, col):
        self.row = row
        self.col = col
        self.data = [ 0 for i in range(row * col)]
        self.error = False

    def ResetMatrix(self, row, col):
        self.row = row
        self.col = col
        self.error = False

    def InitializeWithIdentity(self):
        for row in range(self.row):
            for col in range(self.col):
                if row == col:
                    self.data[row * self.col + col] = 1
                else:
                    self.data[row * self.col + col] = 0

    def CheckScalar(self, other):
        scalar = False
        if type(other) is float or type(other) is int:
            scalar = True
        return(scalar)

    def Add(self, other):
        scalar = self.CheckScalar(other)
        ans = Matrix(self.row, self.col)

        if scalar==False:
            if self.row != other.row or self.col != other.col:
                ans.error = True
                return(ans)

            for row in range(self.row):
                for col in range(self.col):
                    ans[row, col] = self[row, col] + other[row, col]

        else:
            for row in range(self.row):
                for col in range(self.col):
                    ans[row, col] = self[ row, col] + other
        return(ans)

    def __add__(self, other):
        return(self.Add(other))


    def Sub(self, other):
        scalar = self.CheckScalar(other)
        ans = Matrix(self.row, self.col)

        if scalar==False:
            if self.row != other.row or self.col != other.col:
                ans.error = True
                return(ans)

            for row in range(self.row):
                for col in range(self.col):
                    ans[row, col] = self[row,col] - other[row, col]
        else:
            for row in range(self.row):
                for col in range(self.col):
                    ans[row, col] = self[row,col] - other
        return(ans)

    def __sub__(self, other):
        return(self.Sub(other))

    def __mul__(self, other):
        scalar = self.CheckScalar(other)

        if scalar == False and self.col != other.row:
            ans.error = True
            return(ans)

        if scalar==False:
            ans = Matrix(self.row, other.col)
            for row in range(self.row):
                for col in range(other.col):
                    for other_row in range(other.row):
                        ans[row,col] += self[row,other_row] * other[other_row,col]
        else:
            ans = Matrix(self.row, self.col)
            for row in range(self.row):
                for col in range(self.col):
                    ans[row, col] = self[row,col] * other

        return(ans)

    def __str__(self):
        if self.error == True:
            return("No Matrix")

        s = ""
        for row in range(self.row):
            s += "|"
            for col in range(self.col):
                s += "\t" + "{:.3f}".format(self[row,col])
            s += "\t|\n"
        return(s)

    def __setitem__(self, key, value):
        if len(key) == 2:
            row = key[0]
            col = key[1]
        elif len(key) == 1:
            row = 0
            col = key[0]
        else:
            return(None)
        if row>=self.row or row < 0 or col >= self.col or col < 0:
            return(None)

        self.data[ row * self.col + col ] = value


    def __getitem__(self, key):
        if len(key) == 2:
            row = key[0]
            col = key[1]
        elif len(key) == 1:
            row = 0
            col = key[0]
        else:
            return(None)
        if row>=self.row or row < 0 or col >= self.col or col < 0:
            return(None)

        #print("row:",row," col:",col)
        return(self.data[ row * self.col + col])

    def Inverse(self, inv_type="GaussJordan"):

        if inv_type == "GaussJordan":
              return(self.GaussJordanInverse())


    def GaussJordanInverse(self):
        det     = self.Det()
        ans     = Matrix(self.row, self.col)
        temp    = copy.deepcopy(self)
        ans.InitializeWithIdentity()
        if self.row != self.col or det == 0:
            ans.error = False
            return(ans)

        for i in range(self.row):
            buf = 1.0 / self[i,i]
            for j in range(self.row):
                self[i,j] = self[i,j] * buf
                ans[i,j] = ans[i,j] * buf

            for j in range(self.row):
                if i != j:
                    buf = self[j,i]
                    for k in range(self.row):
                        self[j,k] = self[j,k] - self[i,k] * buf
                        ans[j,k] = ans[j,k] - ans[i,k] * buf

        self = copy.deepcopy(temp)

        return(ans)

    def Det(self):
        temp = copy.deepcopy(self)
        det = 1.0
        for i in range(self.row):
            if self[i,i] == 0:
                for j in range(i,self.row):
                    for k in range(self.row):
                        buf = self[i,k]
                        self[i,k] = self[j,k]
                        self[j,k] = buf
                    det *= -1.0
                    break


        for i in range(self.row):
            for j in range(self.row):
                if i < j:
                    buf = self[j,i] / self[i,i]
                    for k in range(self.row):
                        self[j,k] = self[j,k] - self[i,k] * buf

        for i in range(self.row):
            det *= self[i,i]
        self = copy.deepcopy(temp)
        return(det)


'''

# %%

a = Matrix(3,3)
b = Matrix(3,3)


# %%
a.data = [1,2,3,4,5,6,7,8,9]
b.data = [1,2,3,4,5,6,0,0,0]
print("a=\n",a)
print("b=\n",b)
ans = a+b
print("ans=\n",ans)


# %%
c = Matrix(4,4)
c.data = [2,-2,4,2, 2,-1,6,3, 3,-2,12,12, -1,3,-4,4]
print(a.Det())


# %%
print(a)


# %%
c = Matrix(2,2)
c[0,0] = 1
c[1,0] = 0
c[0,1] = 0
c[1,1] = 2


# %%
c.Det()


# %%
print(c.Inverse())


# %%
d = Matrix(4,4)
d.data = [1,2,0,-1, -1,1,2,0, 2,0,1,1, 1,-2,-1,1]


# %%
print(d.Inverse())


# %%

'''

