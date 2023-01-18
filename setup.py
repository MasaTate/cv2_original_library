from setuptools import setup, find_packages

install_requires = ["opencv-python", "Pillow", "numpy"]

packages = ["cv2utils"]
setup(
    name="cv2utils",
    version="1.1",
    packages=packages,
    install_requires=install_requires,
)
