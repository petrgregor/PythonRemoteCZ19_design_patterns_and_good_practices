class Image:
    def show(self):
        pass


class RemoteImage(Image):
    def load_from_source(self):
        pass

    def is_loaded(self):
        pass


class DiskImage(RemoteImage):
    def load_from_source(self):
        pass

    def is_loaded(self):
        pass

    def show(self):
        print("Show disk image.")


class InternetImage(RemoteImage):
    def load_from_source(self):
        pass

    def is_loaded(self):
        pass

    def show(self):
        print("Show internet image")


class ImageProxy(Image):
    def __init__(self, remote_image):
        self._remote_image = remote_image

    def show(self):
        if not self._remote_image.is_loaded():
            self._remote_image.load_from_source()
        return self._remote_image.show()


def main():
    disk_image_proxy = ImageProxy(DiskImage())
    internet_image_proxy = ImageProxy(InternetImage())

    disk_image_proxy.show()
    internet_image_proxy.show()

    disk_image = DiskImage()
    disk_image.show()


if __name__ == '__main__':
    main()
