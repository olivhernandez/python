class Television:
    MIN_VOLUME = 0
    MAX_VOLUME = 2
    MIN_CHANNEL = 0
    MAX_CHANNEL = 3

    def __init__(self):

        self.__status = False
        self.__muted = False
        self.__volume = Television.MIN_VOLUME
        self.__channel = Television.MIN_CHANNEL

    def power(self):
        self.__status = not self.__status

    def mute(self):
        if self.get_status() is True:
            self.__muted = not self.__muted

    def get_status(self):
        return self.__status

    def get_channel(self):
        return self.__channel

    def get_volume(self):
        if self.get_muted() is True:
            return 0
        else:
            return self.__volume

    def get_muted(self):
        return self.__muted

    def channel_up(self):
        if  self.get_status() is True:
            self.__channel += 1
            if self.__channel > Television.MAX_CHANNEL:
                self.__channel = Television.MIN_CHANNEL

    def channel_down(self):
        if  self.get_status() is True:
            self.__channel -= 1
            if self.__channel < Television.MIN_CHANNEL:
                self.__channel = Television.MAX_CHANNEL

    def volume_up(self):
        if self.get_status() is True:
            if self.get_muted() is True:
                self.__muted = False

            if self.__volume == Television.MAX_VOLUME:
                self.__volume = 2
            else:
                self.__volume += 1

    def volume_down(self):
        if self.get_status() is True:
            if self.get_muted() is True:
                self.__muted = False

            if self.__volume == self.MIN_VOLUME:
                self.__volume = 0
            else:
                self.__volume -= 1

    def __str__(self):
        return f'Power = {self.get_status()}, Channel = {self.get_channel()}, Volume = {self.get_volume()}.'

if __name__ == '__main__':
    Television()
