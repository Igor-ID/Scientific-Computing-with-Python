import copy
import random
# Consider using the modules imported above.

class Hat:
    def __init__(self, **kwargs):
        self.contents = [key for key, val in kwargs.items() for num in range(val)]

    def draw(self, balls_num):
        if balls_num >= len(self.contents):
            return self.contents
        else:
            indices = random.sample(range(len(self.contents)), balls_num)
            chosen = [self.contents[i] for i in indices]
            new_contents = [elem for count, elem in enumerate(self.contents) if count not in indices]
            self.contents = new_contents
            return chosen


def experiment(hat, expected_balls, num_balls_drawn, num_experiments):
    num_successes = 0

    for _ in range(num_experiments):
        balls_drawn = copy.deepcopy(hat).draw(num_balls_drawn)
        balls_expected = [expected_balls[key] for key in expected_balls]

        balls_occurred = [balls_drawn.count(key) for key in expected_balls]

        if balls_occurred >= balls_expected:
            num_successes += 1

    return num_successes / num_experiments
