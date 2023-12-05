class Character:
    def __init__(self, file, speed):
        self.file = file
        self.speed = speed

    def moving(self, destination):
        pass

    def death(self):
        pass

    def get_pos(self):
        x, y = (0, 0)
        return (x, y)


class Ghost(Character):
    def __init__(self, file, speed):
        super.__init__(file, speed)
        super().__init__(file, speed)


class Pacman(Character):
    def __init__(self, file, speed):
        super.__init__(file, speed)
        super().__init__(file, speed)

    def moving(self, destination):
        x, y = self.get_pos()[0], self.get_pos()[1]
        match destination:
            case 'up':
                y -= self.speed
            case 'down':
                y += self.speed
            case 'right':
                x -= self.speed
            case 'left':
                x += self.speed





