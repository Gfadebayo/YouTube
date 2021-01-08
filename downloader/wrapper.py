import pytube
from pytube.streams import Stream

class YouTubeWrapper(pytube.YouTube):


    def duration(self):
        duration = []
        length = int(self.length)
        print(f"Length is {length}")

        if(length >= 3600):
            hours = length // 3600
            length = length - (hours * 3600)

            duration.append(f"{hours} hours ")


        if(length >= 60):
            minutes = length // 60
            length = length - (minutes * 60)

            duration.append(f"{minutes} minutes ")


        duration.append(f"{length} seconds")
        print(f"Duration is {duration}")
        return ''.join(duration)

    def streams(self):
        stream_objects = list(super().streams)
        return map(lambda stream: StreamTemplate(stream), stream_objects)




class StreamTemplate():

    def __init__(self, stream: Stream):

        self.size = self.resolve_size(stream.filesize)

        self.stream = stream

    def resolve_size(self, size):
        sizes = ('KB', 'MB', 'GB')
        current = 0

        while True:
            size = size / 1000
            if size < 1000:
                return "{:.2f} {}".format(size, sizes[current])

            current = current+1
