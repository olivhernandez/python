class Television:
    MIN_VOLUME = 0
    MAX_VOLUME = 2
    MIN_CHANNEL = 0
    MAX_CHANNEL = 3

    def __init__(self) -> None:
        '''
        Function to declare instance variables.
        :param self: access variables that belong to this class.
        '''
        self.__status = False
        self.__muted = False
        self.__volume = Television.MIN_VOLUME
        self.__channel = Television.MIN_CHANNEL


    def power(self) -> None:
        '''
        function to turn the tv on or off by changing the value of the status variable
        :param self: access variables that belong to this class.
        '''
        self.__status = not self.__status


    def mute(self) -> None:
        '''
        Function to mute and unmute the tv when it's on by changing the value of the status variable.
        '''
        if self.get_status() is True:
            self.__muted = not self.__muted


    def get_status(self) -> bool:
        '''
        Function to get the status of the tv
        :return: true or false based on if the tv is on or off
        '''
        return self.__status


    def get_channel(self) -> int:
        '''
        Function to get the channel of the tv
        :return: the channel number of the tv
        '''
        return self.__channel


    def get_volume(self) -> int:
        '''
        Function to get the volume of the tv
        :return: volume of the tv
        '''
        if self.get_muted() is True:
            return 0
        else:
            return self.__volume


    def get_muted(self) -> bool:
        '''
        Function to get the muted status of the tv
        :return: true or false based on muted status
        '''
        return self.__muted


    def channel_up(self) -> None:
        '''
        Function to turn the channel up
        :return: the channel number of the tv
        '''
        if  self.get_status() is True:
            self.__channel += 1
            if self.__channel > Television.MAX_CHANNEL:
                self.__channel = Television.MIN_CHANNEL


    def channel_down(self) -> None:
        '''
        Function to turn the channel down
        :return: the channel number of the tv
        '''
        if  self.get_status() is True:
            self.__channel -= 1
            if self.__channel < Television.MIN_CHANNEL:
                self.__channel = Television.MAX_CHANNEL


    def volume_up(self) -> None:
        '''
        Function to turn the volume up
        :return: the volume of the tv
        '''
        if self.get_status() is True:
            if self.get_muted() is True:
                self.__muted = False

            if self.__volume == Television.MAX_VOLUME:
                self.__volume = 2
            else:
                self.__volume += 1


    def volume_down(self) -> None:
        '''
        Function to turn the volume down
        :return: the volume of the tv
        '''
        if self.get_status() is True:
            if self.get_muted() is True:
                self.__muted = False

            if self.__volume == self.MIN_VOLUME:
                self.__volume = 0
            else:
                self.__volume -= 1


    def __str__(self) -> str:
        '''
        Function to print the power, channel, and volume status of the tv
        :return: a print statement showing the statuses
        '''
        return f'Power = {self.get_status()}, Channel = {self.get_channel()}, Volume = {self.get_volume()}.'

if __name__ == '__main__':
    Television()
