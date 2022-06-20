from abc import ABC, abstractmethod


class Charger(ABC):
    @abstractmethod
    def charge(self): ...


class EuroCharger(Charger):
    def charge(self):
        print("I'm charging in EU.")


class USCharger:
    def specific_charge(self):
        print("I'm charging in US.")


class USChargerAdapter(Charger, USCharger):
    def charge(self):
        self.specific_charge()


def charge(charger: Charger):
    charger.charge()


if __name__ == '__main__':
    eu_charger = EuroCharger()
    us_charger = USChargerAdapter()
    charge(eu_charger)
    charge(us_charger)
