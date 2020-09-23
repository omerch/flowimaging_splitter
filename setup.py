from setuptools import setup

setup(name = 'flowimagingsplitter',
      version = '0.0.1',
      description = 'Splitting of Flow Imaging Microscopes (FlowCam & FlowCam Nano) collage images   \
                     into single images for in-depth data analysis and deep learning purposes',
      packages = ['flowimagingsplitter'],
      author = 'Muhammad Umar',
      author_email = 'omerch35@yahoo.com',
      url = 'https://github.com/omerch/flowimaging_splitter',
      packages = setuptools.find_packages(),
      zip_safe = False )