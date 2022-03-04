<!-- SHIELDS -->
![Platform](https://img.shields.io/badge/Platform-Linux%20%7C%20macOS%20%7C%20Windows-informational)
[![Python](https://img.shields.io/badge/Python-3.7%20%7C%203.8%20%7C%203.9%20%7C%203.10-informational)](https://www.python.org/)
[![Qiskit](https://img.shields.io/badge/Qiskit-%E2%89%A5%200.34.1-6133BD)](https://github.com/Qiskit/qiskit)
[![Qiskit Machine Learning](https://img.shields.io/badge/Qiskit%20Machine%20Learning-%E2%89%A5%200.3.0-6133BD)](https://github.com/Qiskit/qiskit-machine-learning)
[![License](https://img.shields.io/github/license/IBM-Quantum-prototypes/quantum-kernel-training?label=License)](https://github.com/IBM-Quantum-prototypes/quantum-kernel-training/blob/main/LICENSE.txt)
[![Tests](https://github.com/IBM-Quantum-prototypes/quantum-kernel-training/actions/workflows/makefile.yml/badge.svg)](https://github.com/IBM-Quantum-prototypes/quantum-kernel-training/actions/workflows/makefile.yml)



<!-- PROJECT LOGO -->
<br />
<p align="center">
  <a href="https://github.com/IBM-Quantum-prototypes/quantum-kernel-training#readme">
    <img src="docs/images/qkt_image.png" alt="Logo" width="350">
  </a>
  <h2 align="center">Quantum Kernel Training Toolkit</h2>

  <p align="center">
   <a href="https://mybinder.org/v2/gh/IBM-Quantum-prototypes/quantum-kernel-training/HEAD?labpath=docs%2Ftutorials%2Fkernel_optimization_using_qkt.ipynb">
     <img src="https://img.shields.io/badge/launch-demo-579ACA.svg?style=for-the-badge&logo=data:image/png;base64,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" alt="Launch Demo" hspace="10" vspace="10">
   </a>
   <a href="https://www.youtube.com/playlist?list=PLOFEBzvs-VvqEaBUQ-Doi9XM94N0Oagnq">
     <img src="https://img.shields.io/badge/watch-video-FF0000.svg?style=for-the-badge&logo=youtube" alt="Watch Video" hspace="10" vspace="10">
   </a>
  </p>
</p>



<!-- TABLE OF CONTENTS -->
### Table of Contents
* [Installation](INSTALL.md)
* [Tutorials](docs/tutorials/)
* [How-Tos](docs/how_tos/)
* [Background](docs/background/)
* [How to Give Feedback](#how-to-give-feedback)
* [Contribution Guidelines](#contribution-guidelines)
* [Acknowledgements](#acknowledgements)
* [About Prototypes](#about-prototypes)
* [References](#references)
* [License](#license)


----------------------------------------------------------------------------------------------------

<!-- ABOUT THIS PROJECT -->
### About This Project

The quantum kernel training (QKT) toolkit is designed to enable users to leverage quantum kernels for machine learning tasks; in particular, researchers who are interested in investigating quantum kernel training algorithms in their own research, as well as practitioners looking to explore and apply these algorithms to their machine learning applications. 

We've designed this python-based toolkit around new components in Qiskit Machine Learning that provide extensible kernel training capabilities, documentation to guide users, as well as datasets and utilities for exploring and testing concepts.

This project evolved out of research at IBM Quantum on ["Covariant Quantum Kernels for Data with Group Structure"](https://arxiv.org/abs/2105.03406) [[1]](#references).


***Problem Statement***

Given a labeled dataset, optimize a parametrized quantum kernel, according to a given loss function, for a machine learning task. For example, use quantum kernel alignment (QKA) as a loss function to iteratively adapt a quantum kernel to a classification dataset while converging to the maximum SVM margin.


***Why Does It Matter?***

Kernel methods are widespread in machine learning applications. A kernel is a similarity measure between data encoded in a high-dimensional feature space and can be utilized, for instance, in classification tasks with support vector machines. It is known that quantum computers can be used to replace classical feature spaces by encoding data in a quantum-enhanced feature space. Using an algorithm called the quantum kernel estimator (QKE), one can compute quantum kernels with data provided classically [[2]](#references). A key observation of this work was that a necessary condition for a computational advantage requires quantum circuits for the kernel that are hard to estimate classically. More recently, researchers proved that a quantum kernel can offer superpolynomial speedups over any classical learner on a particular learning problem based on the hardness of the discrete logarithm problem [[3]](#references). Furthermore, this particular kernel is contained in a kernel family, called covariant quantum kernels, that can be used for data with a group structure [[1]](#references). These results indicate that quantum kernels are an increasingly promising approach in machine learning problems. 

However, finding a good quantum kernel for any given dataset can be a challenging problem in practice. Sometimes, structure in the data can inform this selection, other times a kernel is chosen in an ad hoc manner. Quantum Kernel Alignment (QKA) is one approach to learning a quantum kernel on a dataset. This technique iteratively adapts a parametrized quantum kernel to have high similarity to a target kernel informed from the underlying data distribution, while converging to the maximum SVM margin [[1,4-6]](#references). Such an approach has connections to the performance of the machine learning model; that is, QKA finds a quantum kernel, from a family of kernels, that yields the smallest upper bound to the generalization error. For data with an underlying group structure, covariant quantum kernels can be designed to exploit that structure. In this case, QKA provides a way to optimize the fiducial state of the quantum feature map on such a dataset. This toolkit provides examples of datasets with group structure and corresponding covariant quantum kernels. More information can be found in the [background material](docs/background/qkernels_and_data_w_group_structure.ipynb) and in Ref. [[1]](#references).

To enable future research on quantum kernel training algorithms, this toolkit is extensible to methods beyond QKA. More information about the design is provided in the next section.


***Overall Architecture***

The structure of the QKT Toolkit is illustrated in the diagram below. New components and features were integrated into Qiskit Machine Learning to enable training of quantum kernels. The QKT Tookit is built on top of these integrations and includes local components such as datasets, feature maps, and documentation&mdash;all maintained with style, unit, and notebook tests.

<br />

<p align="center">
  <img src="docs/images/qkt_toolkit_arch.png" width="550">
</p>

***New Integrations into Qiskit Machine Learning***

* `QuantumKernelTrainer`: (New) Class to manage quantum kernel training for a given loss function and optimizer.
* `QuantumKernel`: Option to handle quantum kernels with trainable parameters.
* `KernelLoss`: (New) Base class to calculate loss of quantum kernel functions over trainable parameters and input data.
* `SVCLoss(KernelLoss)`: (New) Class to compute loss corresponding to QKA for classification tasks.

This framework is extensible to other loss functions and optimizers and is compatible with Qiskit's existing kernel-based model interfaces (e.g., classification with `QSVC` and regression with `QSVR`).

***Datasets and Feature Maps***

The QKT toolkit includes datasets useful for illustrating how to train quantum kernels. Two [datasets with a particular underlying group structure](data) are provided for 7 and 10 qubits. These datasets can be used with a [covariant quantum kernel](qkt/feature_maps/covariant_feature_map.py) to test and explore kernel training algorithms. More information about the datasets and kernel can be found in the [background material](docs/background/qkernels_and_data_w_group_structure.ipynb).

***Documentation***

The QKT Toolkit includes documentation split into
- [Tutorials](docs/tutorials): longer examples of end-to-end usage
- [How-to guides](docs/how_tos): targeted answers to common questions
- [Background material](docs/background): in-depth information about quantum kernels and algorithms


----------------------------------------------------------------------------------------------------

<!-- HOW TO GIVE FEEDBACK -->
### How to Give Feedback

We encourage your feedback! You can share your thoughts with us by:
- [Opening an issue](https://github.com/IBM-Quantum-prototypes/quantum-kernel-training/issues) in the repository
- [Starting a conversation on GitHub Discussions](https://github.com/IBM-Quantum-prototypes/quantum-kernel-training/discussions)
- Filling out our [survey](https://airtable.com/shrFxJXYzjxf5tFvx)


----------------------------------------------------------------------------------------------------

<!-- CONTRIBUTION GUIDELINES -->
### Contribution Guidelines

For information on how to contribute to this project, please take a look at our [contribution guidelines](CONTRIBUTING.md).


----------------------------------------------------------------------------------------------------

<!-- ACKNOWLEDGEMENTS -->
### Acknowledgements

This toolkit is based on the research described in [[1]](#references).

The initial codebase was written by Jennifer R. Glick and Tanvi P. Gujarati.


----------------------------------------------------------------------------------------------------

<!-- ABOUT PROTOTYPES -->
### About Prototypes

Prototypes is a collaboration between developers and researchers that will give users access to prototypes from cutting-edge research in areas like quantum simulation and machine learning. These software packages are built on top of, and may eventually be integrated into the Qiskit SDK. They are a contribution as part of the Qiskit community.

Check out our [blog post](https://medium.com/qiskit/try-out-the-latest-advances-in-quantum-computing-with-ibm-quantum-prototypes-11f51124cb61) for more information!


----------------------------------------------------------------------------------------------------

<!-- REFERENCES -->
### References
[1] Jennifer R. Glick, Tanvi P. Gujarati, Antonio D. Córcoles, Youngseok Kim, Abhinav Kandala, Jay M. Gambetta, and Kristan Temme. Covariant quantum kernels for data with group structure. [link](https://arxiv.org/abs/2105.03406)<br>

[2] Havlíček et al. Supervised learning with quantum-enhanced feature spaces. _Nature_ **567**, 209 (2019) [link](https://www.nature.com/articles/s41586-019-0980-2)<br>

[3] Liu et al. A rigorous and robust quantum speed-up in supervised machine learning. _Nature Physics_ **17**, 1013 (2021) [link](https://www.nature.com/articles/s41567-021-01287-z)<br>

[4] B. E. Boser et al. Proceedings of the Fifth Annual Workshop on Computational Learning Theory. COLT ’92, 144-152 [link](https://doi.org/10.1145/130385.130401)<br>

[5] V. Vapnik. The Nature of Statistical Learning Theory. Information Science and Statistics (Springer New York, 2013) [link](https://books.google.com/books?id=EqgACAAAQBAJ)<br>

[6] N. Cristianini et al. Advances in Neural Information Processing Systems 14 (2001) [link](https://proceedings.neurips.cc/paper/2001/file/1f71e393b3809197ed66df836fe833e5-Paper.pdf)<br>

Qiskit Global Summer School on Quantum Machine Learning (in particular, lectures [6.1](https://learn.qiskit.org/summer-school/2021/lec6-1-from-variational-classifiers-linear-classifiers), [6.2](https://learn.qiskit.org/summer-school/2021/lec6-2-quantum-feature-spaces-kernels), and [6.3](https://learn.qiskit.org/summer-school/2021/lec7-1-quantum-kernels-practice))


----------------------------------------------------------------------------------------------------

<!-- LICENSE -->
### License
[Apache License 2.0](LICENSE.txt)
