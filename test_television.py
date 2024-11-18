from television import *

class Test:
    def setup_method(self):
        self.tvi = Television()

    def teardown_method(self):
        del self.tvi

    def test_init(self):
        assert self.tvi.__str__() == 'Power = False, Channel = 0, Volume = 0'

    def test_power(self):
        self.tvi.power()
        assert self.tvi.__str__() == 'Power = True, Channel = 0, Volume = 0'

        self.tvi.power()
        assert self.tvi.__str__() == 'Power = False, Channel = 0, Volume = 0'

    def test_mute(self):
        self.tvi.mute()
        assert self.tvi.__str__() == 'Power = False, Channel = 0, Volume = 0'

        self.tvi.power()
        self.tvi.volume_up()
        self.tvi.mute()
        assert self.tvi.__str__() == 'Power = True, Channel = 0, Volume = 0'

        self.tvi.mute()
        assert self.tvi.__str__() == 'Power = True, Channel = 0, Volume = 1'

    def test_channel_up(self):
        self.tvi.channel_up()
        assert self.tvi.__str__() == 'Power = False, Channel = 0, Volume = 0'

        self.tvi.power()
        self.tvi.channel_up()
        assert self.tvi.__str__() == 'Power = True, Channel = 1, Volume = 0'

        self.tvi.channel_up()
        self.tvi.channel_up()
        self.tvi.channel_up()
        assert self.tvi.__str__() == 'Power = True, Channel = 0, Volume = 0'

    def test_channel_down(self):
        self.tvi.channel_down()
        assert self.tvi.__str__() == 'Power = False, Channel = 0, Volume = 0'

        self.tvi.power()
        self.tvi.channel_down()
        assert self.tvi.__str__() == 'Power = True, Channel = 3, Volume = 0'

        self.tvi.channel_down()
        assert self.tvi.__str__() == 'Power = True, Channel = 2, Volume = 0'

        self.tvi.channel_down()
        assert self.tvi.__str__() == 'Power = True, Channel = 1, Volume = 0'

        self.tvi.channel_down()
        assert self.tvi.__str__() == 'Power = True, Channel = 0, Volume = 0'

    def test_volume_up(self):
        self.tvi.volume_up()
        assert self.tvi.__str__() == 'Power = False, Channel = 0, Volume = 0'

        self.tvi.power()
        self.tvi.volume_up()
        assert self.tvi.__str__() == 'Power = True, Channel = 0, Volume = 1'

        self.tvi.volume_up()
        assert self.tvi.__str__() == 'Power = True, Channel = 0, Volume = 2'
        self.tvi.volume_up()
        assert self.tvi.__str__() == 'Power = True, Channel = 0, Volume = 2'

    def test_volume_down(self):
        self.tvi.volume_down()
        assert self.tvi.__str__() == 'Power = False, Channel = 0, Volume = 0'

        self.tvi.power()
        self.tvi.volume_up()
        self.tvi.volume_up()
        self.tvi.volume_down()
        assert self.tvi.__str__() == 'Power = True, Channel = 0, Volume = 1'

        self.tvi.volume_down()
        assert self.tvi.__str__() == 'Power = True, Channel = 0, Volume = 0'

        self.tvi.volume_down()
        assert self.tvi.__str__() == 'Power = True, Channel = 0, Volume = 0'

  

