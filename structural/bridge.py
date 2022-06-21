from abc import ABC, abstractmethod


class Device(ABC):
    def __init__(self):
        self.on = False

    def enable(self):
        self.on = True

    def disable(self):
        self.on = False

    @abstractmethod
    def status(self): ...


class Radio(Device):
    def status(self):
        print(f"I'm radio and I'm {'on' if self.on else 'off'}")


class TV(Device):
    def status(self):
        print(f"I'm TV and I'm {'on' if self.on else 'off'}")


class Remote(ABC):
    def __init__(self, device: Device):
        self.device = device

    @abstractmethod
    def power(self): ...


class BasicRemote(Remote):
    def power(self):
        self.device.disable() if self.device.on else self.device.enable()


class EnableRemote(Remote):
    def power(self):
        self.device.enable()


def click_power(remote: Remote):
    remote.power()
    remote.power()
    remote.device.status()


if __name__ == '__main__':
    radio = Radio()
    basic_remote = BasicRemote(radio)

    tv = TV()
    enable_remote = EnableRemote(tv)
    click_power(basic_remote)
    click_power(enable_remote)

