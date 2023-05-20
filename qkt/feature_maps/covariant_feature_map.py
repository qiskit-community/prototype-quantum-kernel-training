# This code is part of Qiskit.
#
# (C) Copyright IBM 2021.
#
# This code is licensed under the Apache License, Version 2.0. You may
# obtain a copy of this license in the LICENSE.txt file in the root directory
# of this source tree or at http://www.apache.org/licenses/LICENSE-2.0.
#
# Any modifications or derivative works of this code must retain this
# copyright notice, and modified files need to carry a notice indicating
# that they have been altered from the originals.

"""Create a new Covariant Feature Map circuit."""

import copy
from typing import Callable, Optional, Union, List, Dict, Any

import numpy as np

from qiskit import QuantumCircuit
from qiskit.circuit import ParameterVector


class CovariantFeatureMap(QuantumCircuit):
    """The Covariant Feature Map circuit.

    On 3 qubits and a linear entanglement,  the circuit is represented by:

    .. parsed-literal::


         ┌──────────────┐       ░ ┌─────────────────┐┌─────────────────┐
    q_0: ┤ Ry(θ_par[0]) ├─■─────░─┤ Rz(-2*x_par[1]) ├┤ Rx(-2*x_par[0]) ├
         ├──────────────┤ │     ░ ├─────────────────┤├─────────────────┤
    q_1: ┤ Ry(θ_par[1]) ├─■──■──░─┤ Rz(-2*x_par[3]) ├┤ Rx(-2*x_par[2]) ├
         ├──────────────┤    │  ░ ├─────────────────┤├─────────────────┤
    q_2: ┤ Ry(θ_par[2]) ├────■──░─┤ Rz(-2*x_par[5]) ├┤ Rx(-2*x_par[4]) ├
         └──────────────┘       ░ └─────────────────┘└─────────────────┘

    where θ_par is a vector of trainable feature map parameters and x_par is a
    vector of data-bound feature map parameters.
    """

    def __init__(
        self,
        feature_dimension: int,
        entanglement: Union[str, List[List[int]], Callable[[int], List[int]]] = None,
        single_training_parameter: bool = False,
        name: str = "CovariantFeatureMap",
    ) -> None:
        """Create a new Covariant Feature Map circuit.

        Args:
            feature_dimension: The number of features
            insert_barriers: If True, barriers are inserted around the entanglement layer

        """
        if (feature_dimension % 2) != 0:
            raise ValueError(
                """
            Covariant feature map requires an even number of input features.
                """
            )
        self.feature_dimension = feature_dimension
        self.entanglement = entanglement
        self.single_training_parameter = single_training_parameter
        self.training_parameters = None
        self.input_parameters = None

        num_qubits = feature_dimension / 2
        super().__init__(
            num_qubits,
            name=name,
        )

        self._generate_feature_map()

    @property
    def settings(self) -> Dict[str, Any]:
        training_parameters_list = [param for param in self.training_parameters]
        input_parameters_list = [param for param in self.input_parameters]
        return {
            "feature_dimension": self.feature_dimension,
            "entanglement": self.entanglement,
            "single_training_parameter": self.single_training_parameter,
            "training_parameters": training_parameters_list,
            "input_parameters": input_parameters_list,
        }

    def _generate_feature_map(self):
        # If no entanglement scheme specified, use linear entanglement
        if self.entanglement is None:
            self.entanglement = [[i, i + 1] for i in range(self.num_qubits - 1)]

        # Vector of data parameters
        input_params = ParameterVector("x_par", self.feature_dimension)

        # Use a single parameter to rotate each qubit if sharing is desired
        if self.single_training_parameter:
            training_params = ParameterVector("\u03B8_par", 1)
            # Create an initial rotation layer using a single Parameter
            for i in range(self.num_qubits):
                self.ry(training_params[0], self.qubits[i])

        # Train each qubit's initial rotation individually
        else:
            training_params = ParameterVector("\u03B8_par", self.num_qubits)
            # Create an initial rotation layer of trainable parameters
            for i in range(self.num_qubits):
                self.ry(training_params[i], self.qubits[i])

        self.training_parameters = training_params
        self.input_parameters = input_params

        # Create the entanglement layer
        for source, target in self.entanglement:
            self.cz(self.qubits[source], self.qubits[target])

        self.barrier()

        # Create a circuit representation of the data group
        for i in range(self.num_qubits):
            self.rz(-2 * input_params[2 * i + 1], self.qubits[i])
            self.rx(-2 * input_params[2 * i], self.qubits[i])
