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
- To decrease an item quantity by 1 : `update/<item_number>` using GET methods in frontEnd but PUT from order to catalog

  # How it works
We wrote the code in Python using FLASK
  
The design implemented consists of three separate components one on the frontend and two on the backend,
namely the frontend, Orders and Catalog servers. The main server is the Catalog which has the data on products,the orders server has the orders info and connects to the catalog to read and modify an item's info when an order comes.
We wrote a docker file which builds a docker image for each server to work separately independently, then we connected the images/dockerfile with a docker compose file that connects the containers.

  # Considerations and Possible Improvements
 A GUI can be used with FrontEnd server

  # Output Screenshots
  screenshots showing the output of each operation on the frontEnd server using Postman
  /search
  ![image](https://user-images.githubusercontent.com/54281674/161630311-fa1469f6-b9f8-44bb-830b-345c4d7ea9ba.png)
  
  /search/<category>
  ![image](https://user-images.githubusercontent.com/54281674/161630424-87233093-3776-4b6d-bde8-274c92ad58ba.png)
  ![image](https://user-images.githubusercontent.com/54281674/161630482-66516e3f-4240-4a84-a4c0-451c94aea0e5.png)

  /info/<item_number>
  ![image](https://user-images.githubusercontent.com/54281674/161630580-9211b34b-73cd-4c6d-86f5-21dbf15bc2bc.png)
  ![image](https://user-images.githubusercontent.com/54281674/161630631-3823a179-e1fd-4af4-a807-c8009ce82e16.png)
  
  /purchase/<item_number>
  ![image](https://user-images.githubusercontent.com/54281674/161630699-8ed5d22e-5c4b-4783-a5d5-2f0587a9e23e.png)
  ![image](https://user-images.githubusercontent.com/54281674/161630747-d0b32b3e-5576-4c39-9d8c-dfa144b1805c.png)
