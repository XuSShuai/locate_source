# locate_source

## About

Locating source based on sparesly placed observers and utilizes the correlated information between network structure 
(shortest path) and diffusion dynamic(time sequence of infection) on complex network. Paper `Locating the epidemic source in complex networks`

## Version

Implemented by python3.

## Introduction

 - Main
   - type:
      ```python
      python locate_source.py 
      ```
      to run source locating algorithm on artifical network("ba" or "er") and have a look the on the output.

   - `base_expriment_code.py` test the average accuracy of algorithm under different percentage of observers on "BA" network and "ER" network, respectively.

 - how_to_select_observers
   - `how_to_select_observers.py` test the performance of algorithm under different observers selection strategy, the strategies include not limited to set nodes who with the bigger degree/closeness/betweeness or the smaller ones as observers. All the results of experiment save to "plot/..".
   
- empirical_network
  - test the performance of algorithm on four empirical networks
  
- plot
  - save and visualize the result of the algorithm.
  
  
## Some results
  
  
![different correlation method](https://github.com/XuSShuai/locate_source/blob/master/plot/correlation/soogif.gif)
