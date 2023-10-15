# pydub-demo
## prerequisite
* Install `ffmpeg`, or
* Install `docker`

## How to build
```
docker build -t mypydub .
docker run -it --rm --entrypoint bash -v $(pwd)/wav:/app/code/wav mypydub
```

Or, 
```
docker run -it --rm --entrypoint "/app/code/init.sh" -v $(pwd)/wav:/app/code/wav mypydub
```

## How to run
```
python3 hello.py --path wav/718786886.373270.wav
```

