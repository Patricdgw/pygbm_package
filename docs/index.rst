.. notebook_test documentation master file, created by
   sphinx-quickstart on Sat Jul 25 11:56:56 2020.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

.. .. figure:: logo.jpg
..    :alt: Course Logo
..    :align: left
..    :width: 200px

Geometric Brownian Motion Package
===============================================================================




.. image:: https://readthedocs.org/projects/pygbm_package/badge/?version=latest
   :target: https://pygbm_package.readthedocs.io/en/latest/?badge=latest
   :alt: Documentation Status

.. image:: https://colab.research.google.com/assets/colab-badge.svg
   :target: https://colab.research.google.com/github/Patricdgwme/pygbm_package/blob/master/notebooks/index.ipynb
   :alt: Open In Colab

| *Author*: Patric de Gentile-Williams


.. note::
    Test Package for the 
   `MPhil in Data Intensive Science <https://mphildis.bigdata.cam.ac.uk>`_ and the 
 


.. _Geometric_Brownian_Motion_Package:

The **Geometric Brownian Motion Package** is a Python package designed to generate geometric Brownian motion paths.

Features
--------

- **Base `pygbm` class**: Core attributes and methods.

Installation
------------

Ensure you have Python 3.6 or higher. Install the package and its dependencies with:

.. code-block:: bash

    pip install -e .

Usage
-----

Here's a quick example of how to use the package:

Run either of these command line instructions:

pygbm simulate --y0 1.0 --mu 0.05 --sigma 0.2 --t 1.0 --n 100 --output gbm_plot.png

python -m pygbm.GBM.launch_script




Documentation
-------------

Visit our `documentation page https://geometric-brownian-motion-package-test.readthedocs.io/en/latest/.

Contributing
------------

Contributions are welcome! Fork our repository and submit a pull request.

License
-------

This project is licensed under the MIT License - see the `LICENSE` file for details.



API Reference
-------------------------------------------------------------------------------


.. automodule:: pygbm.base
    :members:
    :undoc-members:

.. automodule:: pygbm.cli 
    :members:
    :undoc-members:

.. automodule:: pygbm.GBM 
    :members:
    :undoc-members:






Useful Resources and further reading
----------------------------------------

- `Wikipedia <https://en.wikipedia.org/wiki/Pandas_(software)>`_


