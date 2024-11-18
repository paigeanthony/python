
class Television:
    '''
    This class represents a television remote.
    '''
    MIN_VOLUME = 0
    MAX_VOLUME = 2
    MIN_CHANNEL = 0
    MAX_CHANNEL = 3

    def __init__(self) -> None:
        '''
        Initializes the default values for power, mute, volume, and channel.
        '''
        self.__status = False
        self.__muted = False
        self.__volume = Television.MIN_VOLUME
        self.__channel = Television.MIN_CHANNEL
        
    def power(self) -> None:
        '''
        Sets the power status of the t.v.
        '''
        self.__status = not self.__status

    def mute(self) -> None:
        '''
        Sets the mute status of the t.v.
        Set to the minimum volume when muted.
        Restores to previous value when unmuted.
        '''
        if self.__status:
            self.__muted = not self.__muted
            if self.__muted:
                self.__pre_volume = self.__volume
                self.__volume = Television.MIN_VOLUME
            else:
                self.__volume = self.__pre_volume
                
    def channel_up(self) -> None:
        '''
        Increases channel number by 1.
        Wraps to min channel at max channel.
        '''
        if self.__status:
            if self.__channel < Television.MAX_CHANNEL:
                self.__channel += 1
            else:
                self.__channel = Television.MIN_CHANNEL

    def channel_down(self) -> None:
        '''
        Decreases channel number by 1.
        Wraps to max channel at min channel.
        '''
        if self.__status:
            if self.__channel > Television.MIN_CHANNEL:
                self.__channel -= 1
            else:
                self.__channel = Television.MAX_CHANNEL

    def volume_up(self) -> None:
        '''
        Increases the volume by 1.
        Unmutes if muted.
        Volume doesn't exceed max volume.
        '''
        if self.__status:
            if self.__muted:
                self.__muted = False
                self.__volume = self.__pre_volume
            if self.__volume < Television.MAX_VOLUME:
                self.__volume += 1

    def volume_down(self) -> None:
        '''
        Decreases the volume by 1.
        Unmutes if muted.
        Volume doesn't fall below min volume.
        '''
        if self.__status:
            if self.__muted:
                self.__muted = False
                self.__volume = self.__pre_volume
            if self.__volume > Television.MIN_VOLUME:
                self.__volume -= 1

    def __str__(self) -> str:
        '''
        Returns string representing the status of the television.
        '''
        current_volume = self.__volume if not self.__muted else Television.MIN_VOLUME
        return f'Power = {self.__status}, Channel = {self.__channel}, Volume = {current_volume}'

