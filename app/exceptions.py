class DeviceNotFound(Exception):
    def __init__(self, device_id):
        self.device_id = device_id
        super().__init__(f"Device with ID {device_id} not found")
