# motor-test
Python test scripts for the EPICS motor record &amp; various drivers

To run any of the scripts:

<code>./script_name.py motor_record_PV_name</code>

for example:

<code>./moves.py BL99:Mot:Axis1</code>

The run_tests.py script runs the scripts listed in run_tests.txt in sequence.

Some of the scripts may require external records to control driver parameters, or require multiple motors (eg. for testing deferred moves) but the following scripts will work with any standalone motor record:
* moves.py
* moves_small.py
* moves_reverse.py
* moves_delay.py


