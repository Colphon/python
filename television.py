class Television:
    MIN_VOLUME = 0
    MAX_VOLUME = 2
    MIN_CHANNEL = 0
    MAX_CHANNEL = 3
    def __init__(self, status: bool = False, muted: bool = False, volume: int = MIN_VOLUME, channel: int = MIN_CHANNEL) -> None:
        '''
        Method to set default values of television object.
        :param status: The state of the tv (True = on, False = off).
        :param muted: Whether the tv is muted (True = muted, False = unmuted)
        :param volume: The volume of the tv.
        :param channel: The channel the tv is on
        '''
        self.__status = status
        self.__muted = muted
        self.__volume = volume
        self.__channel = channel

    def power(self) -> None:
        '''
        Method to modify the status of the tv
        '''
        if self.__status == True:
            self.__status = False
        else:
            self.__status = True
    def mute(self) -> None:
        '''
        Method to modify whether the tv is muted
        '''
        if self.__status == True:
            if self.__muted == True:
                self.__muted = False
            else:
                self.__muted = True
    def channel_up(self) -> None:
        '''
        Method to increase the channel.
        '''
        if self.__status == True:
            if self.__channel == Television.MAX_CHANNEL:
                self.__channel = Television.MIN_CHANNEL
            else:
                self.__channel += 1
    def channel_down(self) -> None:
        '''
        Method to decrease the channel.
        '''
        if self.__status == True:
            if self.__channel == Television.MIN_CHANNEL:
                self.__channel = Television.MAX_CHANNEL
            else:
                self.__channel -= 1
    def volume_up(self) -> None:
        '''
        Method to increase the volume.
        '''
        if self.__status == True:
            self.__muted = False
            if self.__volume == Television.MAX_VOLUME:
                pass
            else:
                self.__volume += 1
    def volume_down(self) -> None:
        '''
        Method to decrease the volume.
        '''
        if self.__status == True:
            self.__muted = False
            if self.__volume == Television.MIN_VOLUME:
                pass
            else:
                self.__volume -= 1

    def __str__(self) -> str:
        '''
        Method to return a string of certain characteristics of the tv
        :return: The state of the tv (on/off), the channel and the volume.
        '''
        if self.__muted == False:
            return f'Power = {self.__status}, Channel = {self.__channel}, Volume = {self.__volume}'
        else:
            return f'Power = {self.__status}, Channel = {self.__channel}, Volume = {self.__volume - self.__volume}'


