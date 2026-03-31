from pathlib import Path


class Timeline:

    def __init__(self, scene, audio_path, labels_path):

        self.scene = scene
        self.audio = audio_path

        self.events = {}
        self.intervals = {}

        with open(labels_path, encoding="utf-8") as f:
            for line in f:
                start, end, label = line.strip().split("\t")

                start = float(start)
                end = float(end)

                self.events[label] = start
                self.intervals[label] = (start, end)

        scene.add_sound(self.audio)

        self.start = scene.renderer.time

        # tiempo final del score
        self.end_time = max(end for (_, end) in self.intervals.values())

    def now(self):
        return self.scene.renderer.time - self.start

    def wait_until(self, label):

        target = self.events[label]
        dt = target - self.now()

        if dt > 0:
            self.scene.wait(dt)

    def wait_for(self, label):

        start, end = self.intervals[label]
        dt = end - self.now()

        if dt > 0:
            self.scene.wait(dt)

    def play_at(self, label, animation):

        self.wait_until(label)
        self.scene.play(animation)

    def play_between(self, label, animation):

        start, end = self.intervals[label]

        self.wait_until(label)

        duration = end - start

        self.scene.play(animation, run_time=duration)

    def wait_until_end(self):

        dt = self.end_time - self.now()

        if dt > 0:
            self.scene.wait(dt)

    def play_sync(self, label, animation, lead=0.7):

        start, end = self.intervals[label]

        self.wait_until(label)

        duration = end - start

        run_time = duration * lead

        self.scene.play(animation, run_time=run_time)

        remaining = duration - run_time

        if remaining > 0:
            self.scene.wait(remaining)