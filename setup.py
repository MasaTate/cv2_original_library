from setuptools import setup, find_packages

install_requires = ["cv2", "PIL", "numpy"]

packages = ["cv2utils"]
setup(
    name="cv2utils", version="1.0", packages=packages, install_requires=install_requires
)
