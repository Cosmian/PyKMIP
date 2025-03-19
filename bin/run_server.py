#!/usr/bin/env python
import os
from multiprocessing import Lock, Process

# Copyright (c) 2016 The Johns Hopkins University/Applied Physics Laboratory
# All Rights Reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License"); you may
# not use this file except in compliance with the License. You may obtain
# a copy of the License at
#
#    http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
# WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
# License for the specific language governing permissions and limitations
# under the License.

from kmip.services.server import KmipServer


def start_server(lock):


    # acquire the lock
    with lock:
        print(f"Current working directory: {os.getcwd()}")
        # block for a moment
        server = KmipServer(
            config_path='./bin/pykmip_server/server.conf',
            log_path='./bin/pykmip_server/server.log',
        )
        server.start()
        server.serve()
        # server.stop()

def run_server():
    # change start method
    # set_start_method('fork')
    # create a shared lock
    lock = Lock()
    # create a process that uses the lock
    process = Process(target=start_server, args=(lock,))
    # start the process
    process.start()
    # wait for the process to finish
    process.join()



if __name__ == '__main__':
    # server.main()
    run_server()
