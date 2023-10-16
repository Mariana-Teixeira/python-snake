from observer import Observer

class Publisher():
    def __init__(self):
        self.observers = []

    def add_observer(self, obs: Observer):
        self.observers.append(obs)

    # TODO
    def remove_observer(self):
        pass

    def notify(self, position):
        for obs in self.observers:
            obs.on_notify(position)