# -*- coding: utf-8 -*-

"""
calculatormharis

This file was automatically generated by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""

from calculatormharis.decorators import lazy_property
from calculatormharis.configuration import Configuration
from calculatormharis.configuration import Environment
from calculatormharis.controllers.simple_calculator_controller\
    import SimpleCalculatorController


class CalculatormharisClient(object):

    @lazy_property
    def simple_calculator(self):
        return SimpleCalculatorController(self.config)

    def __init__(self, http_client_instance=None,
                 override_http_client_configuration=False, http_call_back=None,
                 timeout=60, max_retries=0, backoff_factor=2,
                 retry_statuses=[408, 413, 429, 500, 502, 503, 504, 521, 522, 524],
                 retry_methods=['GET', 'PUT'],
                 environment=Environment.PRODUCTION, config=None):
        if config is None:
            self.config = Configuration(
                                         http_client_instance=http_client_instance,
                                         override_http_client_configuration=override_http_client_configuration,
                                         http_call_back=http_call_back,
                                         timeout=timeout,
                                         max_retries=max_retries,
                                         backoff_factor=backoff_factor,
                                         retry_statuses=retry_statuses,
                                         retry_methods=retry_methods,
                                         environment=environment)
        else:
            self.config = config


