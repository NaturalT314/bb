$imageName = "bb"

docker build -t $imageName .\bb\

docker run -d -p 8000:8000 $imageName