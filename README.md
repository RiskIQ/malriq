# README

## malriq, Maltego RiskIQ transforms

Make RiskIQ API calls to generate new nodes.

Tested with Maltego v3.5.0 and v3.5.3, and canari 1.1.

## Installation

#### Install dependencies

````bash
sudo python setup.py install
./generate_mtz.sh
# It may ask to regenerate configs in ~/.canari . If so, make sure you put back
# your riskiq API token and private key inside ~/.canari/malriq.conf
````

#### Set up credentials
* Open ~/.canari/malriq.conf
* Input token and private key from creds from RiskIQ API token/key generated through web UI

#### Install transforms
* Open Maltego
* Click main icon at top left, with 3 circles
* Go to Import->Import Configuration
* Select malriq.mtz (within the same directory as this README)
* Click Next
* Select Transforms + Transform Sets
* Click Next, then Finish

#### Try it
* Right click any Domain, IP or URL
* Select Run Transform->RiskIQ-> Any available imported transform
* If no results are generated, no results found in API response

### Problems

If there are issues and error messages pop up, check the debug console.

It may be that the credentials are not inside ~/.canari/malriq.conf or
~/.canari/canari.conf does not specify a link to malriq.conf:

````
[default]
configs = malriq.conf
````

Another problem may be due to a misconfiguration in maltego. It may be best to
click Manage and Manage Transforms and delete every Malriq/RiskIQ transform,
pip uninstall canari, riskiq and malriq, and start from scratch.

If all else fails and you do not have any personal configurations in maltego
that you'd like to save, the easiest solution may be to completely uninstall
maltego and wipe out its configuration directories (located in 
~/Library/Application\ Support/maltego/{your maltego version}/etc on Mac), and
then start the canari and malriq installation procedures again from scratch.
