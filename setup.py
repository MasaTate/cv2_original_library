from setuptools import setup, find_packages

install_requires = ["cv2", "PIL", "numpy"]

packages = ["transform", "video"]
setup(name="cv2_utils", version="1.0", packages=find_packages())
