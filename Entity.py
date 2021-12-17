class Entity:
    def _init_(self, starting_position, velocity):
        self.velocity = velocity
        self.location = []
        self.location[0] = starting_position

    def _disired_location(self,x, y):
        self._disired_location = (x, y)

    def _movement(self):

        if self.disired_location[0] > self.x:
            self.x += 1
        else:
            self.x -= 1
        if self.disired_location[1] > self.y:
            self.y += 1
        else:
            self.y -= 1