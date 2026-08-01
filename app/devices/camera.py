from dataclasses import dataclass, field
from datetime import datetime
from random import randint


@dataclass
class CameraDevice:

    manufacturer: str = "Sentinel Technologies"
    model: str = "SentinelCam SC-4200"
    firmware: str = "3.1.7"
    serial_number: str = "SC4200-2026-0001"
    mac_address: str = "94:8A:3D:12:56:A8"
    ip_address: str = "192.168.0.104"
    resolution: str = "1920×1080"

    start_time: datetime = field(default_factory=datetime.now)

    def get_device_info(self):

        return {
            "manufacturer": self.manufacturer,
            "model": self.model,
            "firmware": self.firmware,
            "serial_number": self.serial_number,
            "mac_address": self.mac_address,
            "ip_address": self.ip_address,
            "resolution": self.resolution,
            "uptime": self.get_uptime()
        }

    def get_status(self):

        return {
            "cpu": randint(8, 20),
            "memory": randint(30, 55),
            "temperature": randint(36, 43),
            "online": True
        }

    def get_uptime(self):

        delta = datetime.now() - self.start_time

        days = delta.days

        hours = delta.seconds // 3600

        minutes = (delta.seconds % 3600) // 60

        return f"{days} Days {hours} Hours {minutes} Minutes"


camera = CameraDevice()