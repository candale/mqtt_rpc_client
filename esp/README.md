### ESP8266 Micropython MQTTRpc

Classes: `MessageHandlerBase`, `MQTTRouter` and `MQTTRpc`.


## Message handlers (operations)

On the device, one may define message handler (operation) classes that must implement a `process_message` and a `get_spec` method (the same as `MessageHandlerBase`) . 

The `process_message` method of a message handler is called whenever a message is received on a topic on which the operation class was registered.
`process_message` takes a keyword argument `msg` and zero or more positional arguments, depending on the format of the topic. 
For example, for a topic of the form `/this/is/a/+/topic` the method should look like this: `def process_message(self, what_kind_of_topic, msg=None)`.
Currently, only `+` wildcard is supported.

`get_spec` is called whenever the RPC starts running. The method must return a string that represents the specification of the operation in question. 
The format is flexible, but the specification must contain this information: 
    * `op_type`: operation type; `call` for operations that are called to execute some code and `recv` for operations that publish data
    * `topic`: the topic on which the operation can be called (if `op_type` is `call`) or on which data is published (if `opt_type` is `recv`)
    * `op_name`: the name of the operation
    * `op_description`: description of the operation
    * `args`: a list of key-value arguments with the key being the type of the argument and the value, the name of the argument; currently the supported types are `str`, `int` and `bool`

## 