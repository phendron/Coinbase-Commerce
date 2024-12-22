#!/bin/python3

import os
import sys
import string
import math


class Endpoints:

    def __init__(self):
        self.endpoint_models = {
            "headers": {
                "X-CC-Api-Key": {
                    "type": "string",
                    "default": "123456789",
                    "required": True
                },
                "Content-Type": {
                    "type": "string",
                    "default": "application/json",
                    "required": True
                },
                "Accept": {
                    "type": "string",
                    "default": "application/json",
                    "required": True
                }
            },
            "charge": {
                "headers": {
                    "inherit_parent": True,
                    "X-CC-Api-Key": {
                        "type": "string",
                        "default": "123456789",
                        "required": True
                    },
                    "Content-Type": {
                        "type": "string",
                        "default": "application/json",
                        "required": True
                    },
                    "Accept": {
                        "type": "string",
                        "default": "application/json",
                        "required": True
                    }
                },
                "create": {
                    "method": "POST",
                    "headers": {
                        "inherit_parent": True
                    },
                    "body": {
                        "buyer_local": {
                            "type": "string",
                            "required": False
                        },
                        "cancel_url": {
                            "type": "uri",
                            "required": False
                        },
                        "checkout_id": {
                            "type": "string",
                            "required": False
                        },
                        "local_price": {
                            "type": "object",
                            "object": {
                                "amount": "string",
                                "currency": "string"
                             },
                            "required": True
                        },
                        "metadata": {
                            "type": "object",
                            "object": {
                                "custom_field": {
                                    "type": "string",
                                    "limit": "infinity"
                                }
                            },
                            "required": False
                        },
                        "pricing_type": {
                            "type": "array.string",
                            "array": ["fixed_price", "no_price"],
                            "required": True
                        },
                        "redirect_uri": {
                            "type": "uri",
                            "required": False
                        }
                    },
                    "responses": {
                        "200": {
                      "brand_color": "string",
                      "brand_logo_url": "string",
                      "charge_kind": "string",
                      "checkout": {
                        "id": "string"
                      },
                      "code": "string",
                      "confirmed_at": "string",
                      "created_at": "string",
                      "description": "string",
                      "expires_at": "string",
                      "hosted_url": "string",
                      "id": "string",
                      "name": "string",
                      "organization_name": "string",
                      "pricing": {
                        "local": {
                          "amount": "string",
                          "currency": "string"
                        },
                        "settlement": {
                          "amount": "string",
                          "currency": "string"
                        }
                      },
                      "pricing_type": "string",
                      "redirects": {
                        "cancel_url": "string",
                        "success_url": "string",
                        "will_redirect_after_success": "boolean"
                      },
                      "support_email": "string",
                      "third_party_provider": "string",
                      "timeline": [
                        {
                          "status": "string",
                          "time": "string"
                        }
                      ],
                      "web3_data": {
                        "failure_events": [
                          {
                            "input_token_address": "string",
                            "network_fee_paid": "string",
                            "reason": "string",
                            "sender": "string",
                            "timestamp": "string",
                            "tx_hsh": "string"
                          }
                        ],
                        "success_events": [
                          {
                            "finalized": "boolean",
                            "input_token_address": "string",
                            "input_token_amount": "string",
                            "network_fee_paid": "string",
                            "recipient": "string",
                            "sender": "string",
                            "timestamp": "string",
                            "tx_hsh": "string"
                          }
                        ],
                        "transfer_intent": {
                          "call_data": {
                            "deadline": "string",
                            "fee_amount": "string",
                            "id": "string",
                            "operator": "string",
                            "prefix": "string",
                            "recipient": "string",
                            "recipient_amount": "string",
                            "recipient_currency": "string",
                            "refund_destination": "string",
                            "signature": "string"
                          },
                          "metadata": {
                            "chain_id": "number",
                            "contract_address": "string",
                            "sender": "string"
                          }
                        },
                        "contract_address": "string",
                        "contract_addresses": None
                      }
                    },
                        "401": {
                      "error": {
                        "type": "authentication_error",
                        "message": "No such API key.",
                        "code": "no_such_api_key"
                      }
                    }
                    },
                    "description": "Creates a charge"
                },
                "all": {
                    "method": "GET",
                    "headers": {
                        "inherit_parent": True
                    },
                    "body": None,
                    "responses": {
                        "201": {
                          "brand_color": "string",
                          "brand_logo_url": "string",
                          "charge_kind": "string",
                          "checkout": {
                            "id": "string"
                          },
                          "code": "string",
                          "confirmed_at": "string",
                          "created_at": "string",
                          "description": "string",
                          "expires_at": "string",
                          "hosted_url": "string",
                          "id": "string",
                          "name": "string",
                          "organization_name": "string",
                          "pricing": {
                            "local": {
                              "amount": "string",
                              "currency": "string"
                            },
                            "settlement": {
                              "amount": "string",
                              "currency": "string"
                            }
                          },
                          "pricing_type": "string",
                          "redirects": {
                            "cancel_url": "string",
                            "success_url": "string",
                            "will_redirect_after_success": "boolean"
                          },
                          "support_email": "string",
                          "third_party_provider": "string",
                          "timeline": [
                            {
                              "status": "string",
                              "time": "string"
                            }
                          ],
                          "web3_data": {
                            "failure_events": [
                              {
                                "input_token_address": "string",
                                "network_fee_paid": "string",
                                "reason": "string",
                                "sender": "string",
                                "timestamp": "string",
                                "tx_hsh": "string"
                              }
                            ],
                            "success_events": [
                              {
                                "finalized": "boolean",
                                "input_token_address": "string",
                                "input_token_amount": "string",
                                "network_fee_paid": "string",
                                "recipient": "string",
                                "sender": "string",
                                "timestamp": "string",
                                "tx_hsh": "string"
                              }
                            ],
                            "transfer_intent": {
                              "call_data": {
                                "deadline": "string",
                                "fee_amount": "string",
                                "id": "string",
                                "operator": "string",
                                "prefix": "string",
                                "recipient": "string",
                                "recipient_amount": "string",
                                "recipient_currency": "string",
                                "refund_destination": "string",
                                "signature": "string"
                              },
                              "metadata": {
                                "chain_id": "number",
                                "contract_address": "string",
                                "sender": "string"
                              }
                            },
                            "contract_address": "string",
                            "contract_addresses": None
                          }
                        },
                        "401": {
                          "error": {
                            "type": "authentication_error",
                            "message": "No such API key.",
                            "code": "no_such_api_key"
                          }
                        },
                        "404": {
                          "description": "Not Found"
                        }
                    },
                    "description": "Returns all charges"
                },
                "get": {
                    "method": "get",
                    "headers": {
                        "inherit_parent": True
                    },
                    "body": None,
                    "responses": {
                        "201": {
                            "brand_color": "string",
                            "brand_logo_url": "string",
                            "charge_kind": "string",
                            "checkout": {
                            "id": "string"
                            },
                            "code": "string",
                            "confirmed_at": "string",
                            "created_at": "string",
                            "description": "string",
                            "expires_at": "string",
                            "hosted_url": "string",
                            "id": "string",
                            "name": "string",
                            "organization_name": "string",
                            "pricing": {
                            "local": {
                            "amount": "string",
                            "currency": "string"
                            },
                            "settlement": {
                            "amount": "string",
                            "currency": "string"
                            }
                            },
                            "pricing_type": "string",
                            "redirects": {
                            "cancel_url": "string",
                            "success_url": "string",
                            "will_redirect_after_success": "boolean"
                            },
                            "support_email": "string",
                            "third_party_provider": "string",
                            "timeline": [
                            {
                            "status": "string",
                            "time": "string"
                            }
                            ],
                            "web3_data": {
                            "failure_events": [
                            {
                            "input_token_address": "string",
                            "network_fee_paid": "string",
                            "reason": "string",
                            "sender": "string",
                            "timestamp": "string",
                            "tx_hsh": "string"
                            }
                            ],
                            "success_events": [
                            {
                            "finalized": "boolean",
                            "input_token_address": "string",
                            "input_token_amount": "string",
                            "network_fee_paid": "string",
                            "recipient": "string",
                            "sender": "string",
                            "timestamp": "string",
                            "tx_hsh": "string"
                            }
                            ],
                            "transfer_intent": {
                            "call_data": {
                            "deadline": "string",
                            "fee_amount": "string",
                            "id": "string",
                            "operator": "string",
                            "prefix": "string",
                            "recipient": "string",
                            "recipient_amount": "string",
                            "recipient_currency": "string",
                            "refund_destination": "string",
                            "signature": "string"
                            },
                            "metadata": {
                            "chain_id": "number",
                            "contract_address": "string",
                            "sender": "string"
                            }
                            },
                            "contract_address": "string",
                            "contract_addresses": None
                            }
                            },
                        "401": {
                            "error": {
                            "type": "authentication_error",
                            "message": "No such API key.",
                            "code": "no_such_api_key"
                            }
                            },
                        "404": {
                            "description": "Not Found"
                            }
                    },
                    "description": "Returns the charge with the order code"
                }
            }
        }

        self.endpoint_responses = {
            "charges": {
                "confirmed": {
                    "attempt_number": 1,
                    "event": {
                    "api_version": "2018-03-22",
                    "created_at": "2023-08-30T19:29:20Z",
                    "data": {
                    "id": "2aee9dd1-67b8-43ef-8dfe-977959850f27",
                    "code": "XA6G6ZFR",
                    "pricing": {
                    "local": {
                      "amount": "1.00",
                      "currency": "USD"
                    },
                    "settlement": {
                      "amount": "1",
                      "currency": "USDC"
                    }
                    },
                    "metadata": {
                    "name": "Bobby Axlerod",
                    "email": "bobby@axecapital.com"
                    },
                    "timeline": [
                    {
                      "time": "2023-08-30T18:55:51Z",
                      "status": "NEW"
                    },
                    {
                      "time": "2023-08-30T19:24:27Z",
                      "status": "SIGNED"
                    },
                    {
                      "time": "2023-08-30T19:24:45Z",
                      "status": "PENDING"
                    },
                    {
                      "time": "2023-08-30T19:29:20Z",
                      "status": "COMPLETED"
                    }
                    ],
                    "redirects": {
                    "cancel_url": "",
                    "success_url": "",
                    "will_redirect_after_success": False
                    },
                    "web3_data": {
                    "failure_events": [],
                    "success_events": [
                      {
                        "sender": "0xb6d00d83158fee6695c72ff9c5e915478a479224",
                        "tx_hsh": "0xc0a731f82af615d7a5f6ba691ba07e083d5403d812adaa8659ed5892c9d3320d",
                        "finalized": False,
                        "recipient": "0x293a08a589f44a6188d65e92fbcd2a27e93d49e3",
                        "timestamp": "2023-08-30T19:24:37Z",
                        "network_fee_paid": "17215600576946625",
                        "input_token_amount": "1000000",
                        "input_token_address": "0x2791bca1f2de4661ed88a30c99a7a9449aa84174"
                      },
                      {
                        "sender": "0xb6d00d83158fee6695c72ff9c5e915478a479224",
                        "tx_hsh": "0xc0a731f82af615d7a5f6ba691ba07e083d5403d812adaa8659ed5892c9d3320d",
                        "finalized": True,
                        "recipient": "0x293a08a589f44a6188d65e92fbcd2a27e93d49e3",
                        "timestamp": "2023-08-30T19:24:37Z",
                        "network_fee_paid": "17215600576946625",
                        "input_token_amount": "1000000",
                        "input_token_address": "0x2791bca1f2de4661ed88a30c99a7a9449aa84174"
                      }
                    ],
                    "transfer_intent": {
                      "metadata": {
                        "sender": "0xB6d00D83158feE6695C72ff9c5E915478A479224",
                        "chain_id": 137,
                        "contract_address": "0xeF0D482Daa16fa86776Bc582Aff3dFce8d9b8396"
                      },
                      "call_data": {
                        "id": "0x58e8e1e895274125a3dcc7e398daa6c0",
                        "prefix": "0x4b3220496e666f726d6174696f6e616c204d6573736167653a20333220",
                        "deadline": "2023-09-01T18:55:51Z",
                        "operator": "0x8fccc78dae0a8f93b0fe6799de888d4c57e273db",
                        "recipient": "0x293a08a589f44a6188d65e92fbcd2a27e93d49e3",
                        "signature": "0xc9b4b26d20ef9e953d145214a335e61495e9d4a559329885952a1b98c72611601e4deb30556b457bdcc1c66ce93976bed9b261447ce7eb770fce70f5216b3a481b",
                        "fee_amount": "10000",
                        "recipient_amount": "990000",
                        "recipient_currency": "0x2791Bca1f2de4661ED88A30C99A7a9449Aa84174",
                        "refund_destination": "0xB6d00D83158feE6695C72ff9c5E915478A479225"
                      }
                    },
                    "contract_addresses": {
                      "1": "0x71b3ba7607abd0cd35eb398c2a38313f10aa3fdb",
                      "137": "0xeF0D482Daa16fa86776Bc582Aff3dFce8d9b8396"
                    }
                    },
                    "created_at": "2023-08-30T18:55:51Z",
                    "expires_at": "2023-09-01T18:55:51Z",
                    "hosted_url": "https://commerce.coinbase.com/pay/2aee9dd1-67b8-43ef-8dfe-977959850f27",
                    "brand_color": "#000000",
                    "charge_kind": "WEB3",
                    "confirmed_at": "2023-08-30T19:29:20Z",
                    "pricing_type": "fixed_price",
                    "support_email": "",
                    "brand_logo_url": "https://res.cloudinary.com/commerce/image/upload/v1653516296/dlwoolpero6qgsffxmpz.jpg",
                    "organization_name": "Fine Art"
                    },
                    "id": "053b96aa-868f-4d8f-8ac6-6b96644da340",
                    "resource": "event",
                    "type": "charge:confirmed"
                    },
                    "id": "5306c113-7ece-4b8b-9452-49abf442bbe4",
                    "scheduled_for": "2023-08-30T19:29:20Z"
                }
            }
        }

    def getEndpointResponses(self):
        return self.endpoint_responses