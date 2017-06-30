# BRO

<p align="center">
<img align="center" src="https://raw.githubusercontent.com/Utkarsh0901/Bro-intrusion_detection_system/master/BRO_logo.png" alt="osquery logo" width="500"/>


__Why Choose Bro?__ Bro is a powerful network analysis framework that is much different from the typical IDS you may know. 

|Features  | Info |
|---|---|
 **Adaptable** | Bro's domain-specific scripting language enables site-specific monitoring policies. 
 **Efficient** | Bro targets high-performance networks and is used operationally at a variety of large sites.
 **Flexible** | Bro is not restricted to any particular detection approach and does not rely on traditional signatures.
 **Forensics** | Bro comprehensively logs what it sees and provides a high-level archive of a network's activity.
 **In-depth_Analysis** | Bro comes with analyzers for many protocols, enabling high-level semantic analysis at the application layer.
 **Highly_Stateful** |Bro keeps extensive application-layer state about the network it monitors.
 **Open_Interfaces** | Bro interfaces with other applications for real-time exchange of information.
 **Open_Source**    | Bro comes with a BSD license, allowing for free use with virtually no restrictions.

While focusing on network security monitoring, Bro provides a comprehensive platform for more general network traffic analysis as well. Well grounded in more than 15 years of research, Bro has successfully bridged the traditional gap between academia and operations since its inception. Today, it is relied upon operationally in particular by many scientific environments for securing their cyberinfrastructure. Bro's user community includes major universities, research labs, supercomputing centers, and open-science communities. 
# Platform : Ubuntu 16.04 -

## Downloads 

See the [bro downloads page](https://www.bro.org/download/index.html) for currently supported/targeted platforms for binary releases or you can use following commands!

```bash
$ wget https://www.bro.org/downloads/bro-2.5.1.tar.gz
$ tar -xvf bro-2.5.1.tar.gz
$ cd bro-2.5.1/
```
## Required Dependencies
Bro requires the following libraries and tools to be installed before you begin:
- Libpcap (http://www.tcpdump.org)
- OpenSSL libraries (http://www.openssl.org)
- BIND8 library
- Libz
- Bash (for BroControl)
- Python 2.6 or greater (for BroControl)

To build Bro from source, the following additional dependencies are required:
- CMake 2.8 or greater (http://www.cmake.org)
- Make
- C/C++ compiler with C++11 support (GCC 4.8+ or Clang 3.3+)
- SWIG (http://www.swig.org)
- Bison (GNU Parser Generator)
- Flex (Fast Lexical Analyzer)
- Libpcap headers (http://www.tcpdump.org)
- OpenSSL headers (http://www.openssl.org)
- zlib headers
- Python

To install the required dependencies, you can use:
```bash
sudo apt-get install cmake make gcc g++ flex bison libpcap-dev libssl-dev python-dev swig zlib1g-dev
```
## Building from source

The typical way to build and install from source is (for more options, run __./configure --help__):

```bash
$ cd bro-2.5.1/
$ ./configure
$ make 
$ sudo make install
$ sudo make install-aux
$ sudo /usr/local/bro/bin/bro --help
```
- You can use ./configure --prefix /path/of/installation/ to provide other than default path of installation. 
## Configure the Run-Time Environment
- You may want to adjust your PATH environment variable according to the platform/shell/package you’re using
```
$ export PATH=/usr/local/bro/bin:$PATH
$ bro --help
```
## Bro IDS
An Intrusion Detection System (IDS) allows you to detect suspicious activities happening on your network as a result of a past or active attack. Because of its programming capabilities, Bro can easily be configured to behave like traditional IDSs and detect common attacks with well known patterns, or you can create your own scripts to detect conditions specific to your particular case.

- Bro have it's own scripts to detect such attacks, one of them is to detect FTP Brute-forcing. 

### Detecting FTP Brute-force Attack :
- You can pass a pcap file as a input by using __-r file_name.pcap__ option.
- you can pass script to execute by __$BROPATH /path/to/script/script_name.bro__
```
$ mkdir logs
$ cd logs/
$ sudo /usr/local/bro/bin/bro -r /path_to_source/bro-2.5.1/testing/btest/Traces/ftp/bruteforce.pcap $BROPATH /path_to_source/bro-2.5.1/scripts/policy/protocols/ftp/detect-bruteforcing.bro
```
- Similarly, you can use other scripts. You can also run all existing scripts all together.

### Sending logs to remote server
- checkout __us_threading.py__, It's a daemon python file which can send json format logs from __notice.log__ which is produced when we run FTP Brute-force Attacking scripts.
- Change the destination address to the server address where you want to send the logs.
## Load multiple scripts through bro
- checkout _bro-2.5.1/scripts/test-all-policy.bro_ and _bro-2.5.1/scripts/policy/_ ,you can add scripts in the later and add them in test-all-policy.bro .
- The base/ scripts are all loaded by default and not included here. example :
```bash
bro-2.5.1/scripts/test-all-policy.bro
...
@load detect_something.bro
...

$ cd bro-2.5.1/scripts/policy/
$ ls
... detect_something.bro ...
```
- Command to run all scripts:
```bash
$ mkdir logs
$ cd logs/
$ sudo /usr/local/bro/bin/bro -r /path_to_source/bro-2.5.1/testing/btest/Traces/ftp/bruteforce.pcap $BROPATH /path_to_source/bro-2.5.1/scripts/test-all-policy.bro 
$ ls
... multiple_files_for_different_scripts.log ...
```
- You can test these scripts on other trace files in __bro-2.5.1/testing/btest/Traces/__ .