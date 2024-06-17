from setuptools import find_packages,setup


setup(
    name="mcqgenerator",
    version="0.0.1",
    author='Yug2801',
    author_email='yug284@gmail.com',
    packages=find_packages(),
    install_requires=[
        "openai","langchain","streamlit","python-dotenv","PyPDF2","langchain_community","langchain-openai"
    ]
)