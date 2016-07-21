# Visvalingam-and-evaluation
Implement the Visvalingam algorithm for line simplification with a little variation. And give evaluation programs based on the 1987 paper by McMaster. 

### How to Use Overpass API to Get OSM Data
OpenStreetMap has an Overpass API which is very convenient to use. 
The following scripts are the queries I made to get data of highways and nodes:

```
way(area:3,600,000,000+area relation id);
way._["highway"~"motorway|motorway-link"];  
node(w);  
out;
```
The above gives all the nodes that make up all the highways. The ~ indicates a key-value pair in a tag of a way. 

````
way(area:3,600,000,000+area relation id);  
way._["highway"~"motorway|motorway-link"];  
out;
```
This gives only the ways without nodes. 

```
way(area:3,600,000,000+area relation id);  
way._["highway"~"motorway|motorway-link"];  
rel(bw);  
out;
```
This gives all the relations about the ways.  

### Evaluation part
I think with the vector class, the exterior angle of each point can be calculated, and this will become a measure of angularity. 
The other is the number of coordinates per unit length of the curve. 
Still need to implement...
