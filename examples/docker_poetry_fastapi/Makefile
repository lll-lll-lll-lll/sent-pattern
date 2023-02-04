build-run:
	docker build . -t sent && docker run --name sentcontainer -p 80:80  -it sent 

start:
	docker start sentcontainer

remove:
	docker rm sentcontainer && docker rmi sent

stop:
	docker stop sentcontainer