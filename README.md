# app-lifecycle-demo

Ohk so far you can view pull the code and view it yourself , ya i vibe coded some stuff because am lazy to write two lines of get / post request code.  
Hey, but i know how it works though.  
So, i wrote a simple docker file from refering docker official documentation [Dockerfile basics](https://docs.docker.com/get-started/docker-concepts/building-images/writing-a-dockerfile/)

ohk, so i pushed my image to docker hub now you can pull the image and test it out 
### Pull the image  

```bash
docker pull shravanjain/fast-apiwdb:1.0
```
### After pulling the image run the container 
```bash
docker run -d -p 8080:8080 shravanjain/fast-apiwdb:1.0
```
### Then open the FastAPI Swagger UI(you can do this using postman or curl no problem):
```
http://localhost:8080/docs
```
### Now you can use GET and POST method in the swagger ui and it'll reflect it in /notes

if you notice any issue or problem, feel free to raise an issue.
