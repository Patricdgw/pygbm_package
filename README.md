# pygbm

A Python package to simulate Geometric Brownian Motion.

## Installation

```sh
pip install -e .


## to run the package, do  either of:


pygbm simulate --y0 1.0 --mu 0.05 --sigma 0.2 --t 1.0 --n 100 --output gbm_plot.png

python -m pygbm.GBM.launch_script

