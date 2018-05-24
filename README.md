# modern-ci
implements a ci for a simple python factorial

To test
`python -m pytest -v test/`

`pip install -r requirements.txt`

To activate the virtual env you must have virtualenv installed
`source venv/bin/activate`

Build and run with docker
`docker build -t factorial .`
`docker run -p 5000:5000 --rm -it factorial`

# source

Following the tutorial
https://medium.com/bettercode/how-to-build-a-modern-ci-cd-pipeline-5faa01891a5b

checkin coding quality with https://bettercodehub.com
running CI with travis https://travis-ci.org/
