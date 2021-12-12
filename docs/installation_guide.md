## Installation

To get started running the Quantum Kernel Training (QKT) Toolkit demos and tutorials, users should first clone the repository and install the required dependencies.

### Clone the Repository
Navigate to your workspace and clone the repository using the HTTPS address.

`cd path/to/your/workspace`

`git clone https://github.com/IBM-Quantum-Prototypes/quantum-kernel-training.git`

[This Github tutorial](https://docs.github.com/en/authentication/connecting-to-github-with-ssh) provides more information on cloning git repositories using ssh keys.

### Create a Fresh Python Development Environment
To avoid dependency conflicts, it is recommended to first start a new Python development environment. We use [conda](https://docs.anaconda.com/anaconda/install/index.html) in this example:

`conda create -n qkt-tookit python=3.9`

`conda activate qkt-tookit`



### Install Dependencies
Once a fresh environment has been created, installing the dependencies should be straightforward. Navigate to the
top level of the repository and:

`pip install -r requirements.txt`



### Test Your Environment
To make sure the notebooks will run on your local machine, you may test the QKT Toolkit locally. From the top directory:

`pip install -r requirements-dev.txt`

`make test`

### Play Around
After the dependencies have installed, users may run the [tutorials](tutorials) and [guides](how_tos) on their local machines.
