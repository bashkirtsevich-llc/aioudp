from setuptools import setup, find_packages

with open("README.md") as f:
    long_description = f.read()

setup(
    name="aio-udp-server",
    version="0.0.2",
    description="Asyncio UDP server with traffic throttling",
    long_description=long_description,
    long_description_content_type="text/markdown",
    classifiers=["Programming Language :: Python"],
    keywords="UDP asyncio UDPserver throttling throttler",
    author="D.Bashkirtsevich",
    author_email="bashkirtsevich@gmail.com",
    url="https://github.com/bashkirtsevich-llc/aioudp",
    license="GPL3 License",
    include_package_data=True,
    zip_safe=True,
    packages=find_packages("src"),
    package_dir={"": "src"},
    python_requires=">=3.6.*"
)
