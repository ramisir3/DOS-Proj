# DOS-Proj
The Distributed Operating Systems Course Project which is a Multi-tier Online Book Store called Bazar.com
## How to run
- You need a Docker Client to run this program,[Docker](https://www.docker.com/get-started)
- Navigate to the project home directory using the terminal
- The docker client has Docker Compose included so using the terminal run the command
`docker-compose up`
- The three services should be running
- The frontend can be accessed on [localhost:8080](http://localhost:8080)
- The catalog can be accessed on [localhost:8081](http://localhost:8081)
- The orders can be accessed on [localhost:8082](http://localhost:8082)

## Orders Server Endpoints 
- To purchase a book use : `purchase/<item_Number>` using GET methods

## Catalog Server Endpoints
- To get all items in the catalog : `search` using GET methods
- To get an item in the catalog : `info/<item_number>` using GET methods
- To get all items of a topic : `search/<category>` using GET methods
- To decrease an item quantity by 1 : `update/<item_number>` using PUT methods

  # How it works
We wrote the code in Python using FLASK
  
The design implemented consists of three separate components one on the frontend and two on the backend,
namely the frontend, Orders and Catalog servers. The main server is the Catalog which has the data on products,the orders server has the orders info and connects to the catalog to read and modify an item's info when an order comes.
We wrote a docker file which builds a docker image for each server to work separately independently, then we connected the images/dockerfile with a docker compose file that connects the containers.

  # Considerations and Possible Improvements
A GUI can be used with FrontEnd server

