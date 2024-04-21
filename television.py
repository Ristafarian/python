

class Television:
    """
    This is a class whose methods reflect the basic operations of a TV.
    """
    MIN_VOLUME = 0
    MAX_VOLUME = 2
    MIN_CHANNEL = 0
    MAX_CHANNEL = 3

    def __init__(self) -> None:
        """
        This is the initialization function, setting the base values for variables for use throughout.
        """
        self.__status = False
        self.__muted = False
        self.__volume = Television.MIN_VOLUME
        self.__channel = Television.MIN_CHANNEL

    def power(self) -> None:
        """
        This is the power button on the remote, will switch the TV power status when called.
        """
        self.__status = not self.__status

    def mute(self) -> None:
        """
        This is the mute button on the remote, will switch the mute status when called.
        Button only functions if TV power is On.
        NOTE: While typically the mute function actually changes volume status, it will not here.
         Volume status switching to 0 reflected in __str__ function.
        """
        if self.__status:
            self.__muted = not self.__muted

    def channel_up(self) -> None:
        """
        This is the channel + button on the remote, will increase the channel by 1.
        If the channel is the highest (max) channel, will roll over to lowest (min) channel.
        Button only functions if TV power is On.
        """
        if self.__status:
            if self.__channel < Television.MAX_CHANNEL:
                self.__channel += 1
            else:
                self.__channel = Television.MIN_CHANNEL

    def channel_down(self) -> None:
        """
        This is the channel - button on the remote, will decrease the channel by 1.
        If the channel is the lowest (min) channel, will roll over to highest (max) channel.
        Button only functions if TV power is On.
        """
        if self.__status:
            if self.__channel > Television.MIN_CHANNEL:
                self.__channel -= 1
            else:
                self.__channel = Television.MAX_CHANNEL

    def volume_up(self) -> None:
        """
        This is the volume + button on the remote, will increase the volume by 1 unless already max.
        Button only functions if TV power is On.
        Button will cancel mute status -- or always set it to False -- prior to adjusting volume.
        """
        if self.__status:
            self.__muted = False
            if self.__volume < Television.MAX_VOLUME:
                self.__volume += 1

    def volume_down(self) -> None:
        """
        This is the volume - button on the remote, will decrease the volume by 1 unless already min.
        Button only functions if TV power is On.
        Button will cancel mute status -- or always set it to False -- prior to adjusting volume.
        """
        if self.__status:
            self.__muted = False
            if self.__volume > Television.MIN_VOLUME:
                self.__volume -= 1

    def __str__(self) -> str:
        """
        This is the string method function for Television class.
        It modifies the strings returned to reflect TV status for Power, Channel, and Volume.
        NOTE: While typically the mute function actually changes volume status, it does note.
         Mute status reflected here in return without actually changing self.__volume in code above.
         This is done by utilizing the Television.MIN_VOLUME variable is mute status is True.

        :return: Current Power/Channel/Volume status
        """
        if self.__muted:
            return f'Power = {self.__status}, Channel = {self.__channel}, Volume = {Television.MIN_VOLUME}'
        else:
            return f'Power = {self.__status}, Channel = {self.__channel}, Volume = {self.__volume}'
