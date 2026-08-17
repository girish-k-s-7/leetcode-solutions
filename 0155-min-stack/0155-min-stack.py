class MinStack:
    def __init__(self):
        self.st = []
        self.mini = None

    def push(self, value):
        if not self.st:
            # if stack is empty updating min value as value
            self.mini = value

            self.st.append(value)
            return

        # if the value is greater than the minimum
        if value > self.mini:
            self.st.append(value)
        else:
            self.st.append(2 * value - self.mini)
            self.mini = value

    def pop(self):
        if not self.st:
            return
        x = self.st.pop()

        # if the modified value is added to stack
        if x < self.mini:
            self.mini = 2 * self.mini - x

    def top(self):
        if not self.st:
            return -1

        # get the top
        x = self.st[-1]

        # return top if the mini is less than the top
        if self.mini < x:
            return x

        return self.mini

    def getMin(self):
        return self.mini